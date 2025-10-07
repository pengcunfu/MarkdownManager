import os
import platform
import re
import subprocess

import markdown
from PySide6.QtCore import QTimer, QUrl
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtGui import QIcon, QDesktopServices
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QMenu, QMessageBox
from PySide6.QtWidgets import QTreeWidget, QTreeWidgetItem
from PySide6.QtWidgets import QWidget, QHBoxLayout, QTabWidget, QTextEdit, QFileDialog
from markdown.extensions.tables import TableExtension
from pubsub import pub

"""
假如说这是一个Markdown Preview组件，则所有的事件在这个组件下进行处理
组件：Markdown Preview
"""


class WebViewEngine(QWebEngineView):
    def __init__(self):
        super(WebViewEngine, self).__init__()
        self.setObjectName("WebEngine")
        self.setStyleSheet("""
            #WebEngine {
                border: none;  /* 去掉边框 */
                padding: 2px;   /* 设置内边距 */
            }
        """)
        self.setContentsMargins(0, 0, 0, 0)  # 去除边距，确保没有额外的空间


class MarkdownEdit(QTextEdit):
    def __init__(self):
        super(MarkdownEdit, self).__init__()
        self.setFrameStyle(QTextEdit.Shape.NoFrame)  # 去掉边框
        self.setViewportMargins(2, 2, 2, 2)


class TreeMenu(QMenu):
    def __init__(self, item: QTreeWidgetItem):
        """ 右键菜单 """
        super().__init__()
        self.item = item

        file_path = self.item.data(0, Qt.ItemDataRole.UserRole)
        if os.path.isdir(file_path):  # 只有目录才有的操作
            action_refresh = QAction("刷新", self)
            action_refresh.triggered.connect(lambda: self.on_refresh_folder())
            self.addAction(action_refresh)

        if os.path.isfile(file_path):
            md_image_handle = QAction("Markdown图像处理", self)
            md_image_handle.triggered.connect(self.on_md_image_handle)
            self.addAction(md_image_handle)

            md_export = QAction("导出", self)
            md_export.triggered.connect(self.on_md_export)
            self.addAction(md_export)

            md_export_pdf = QAction("导出为PDF", self)
            md_export_pdf.triggered.connect(self.on_md_export_pdf)
            self.addAction(md_export_pdf)

        action_open = QAction("打开", self)
        action_open.triggered.connect(lambda: self.on_open_item())
        self.addAction(action_open)

        open_in_explore = QAction("在资源管理器打开", self)
        open_in_explore.triggered.connect(self.on_open_in_explore)
        self.addAction(open_in_explore)

        action_delete = QAction("删除", self)
        action_delete.triggered.connect(self.on_delete_item)
        self.addAction(action_delete)

        self.file_path = self.item.data(0, Qt.ItemDataRole.UserRole)
        if not file_path or not isinstance(file_path, str) or not os.path.isfile(file_path):
            return

        if not os.path.isfile(file_path):
            return

    def on_md_export_pdf(self):
        try:

            md_file_name = os.path.basename(self.file_path).split(".")[0]

            save_path, _ = QFileDialog.getSaveFileName(
                self,
                "导出文件",
                md_file_name,
                "PDF 文件 (*.pdf)",
            )

            if not save_path:  # 用户没有选择文件
                return

            from app.utils.md import md_to_pdf
            md_to_pdf(self.file_path, save_path)
            QMessageBox.information(self, "提示", "导出PDF成功", QMessageBox.StandardButton.Yes)
        except Exception as e:
            QMessageBox.critical(self, "错误", str(e))

    def on_md_export(self):
        try:

            md_file_name = os.path.basename(self.file_path)

            save_path, _ = QFileDialog.getSaveFileName(
                self,
                "导出文件",
                md_file_name,
                "Markdown 文件 (*.md)",
            )
            if not save_path:  # 用户没有选择文件
                return

            from app.utils.md import md_export
            md_export(self.file_path, save_path)
            print(f"文件已保存: {save_path}")
        except Exception as e:
            QMessageBox.critical(self, "错误", str(e))

    def on_md_image_handle(self):
        from app.pages.win_image_handle import ImageHandleDialog
        md_dlg = ImageHandleDialog(md_file_path=self.file_path)
        md_dlg.exec()

    def on_open_in_explore(self):
        file_path = self.file_path
        system = platform.system()
        if system == "Windows":  # 在资源管理器中打开
            file_path = file_path.replace("/", "\\")
            subprocess.Popen(f'explorer /select,"{file_path}"')
        elif system == "Darwin":  # macOS
            subprocess.Popen(["open", "-R", file_path])
        else:  # Linux
            folder_path = os.path.dirname(file_path)
            subprocess.Popen(["xdg-open", folder_path])

    def on_open_item(self):
        file_path = self.item.data(0, Qt.ItemDataRole.UserRole)

        if not file_path:
            return

        QDesktopServices.openUrl(QUrl.fromLocalFile(file_path))

    def on_delete_item(self):
        file_path = self.item.data(0, Qt.ItemDataRole.UserRole)

        if not file_path:
            return

        from app.utils.config_file import config_get_list, config_set_list
        data = config_get_list("file_list")
        # if data.__contains__(file_path):
        if file_path in data:
            data.remove(file_path)
            config_set_list("file_list", data)
            pub.sendMessage(FileBrowseTree.TOPIC_REMOVE_ITEM, item=self.item)

    def on_refresh_folder(self):
        pass


class MarkdownOutlineTree(QTreeWidget):
    TOPIC_LOAD_OUTLINE = "TOPIC_LOAD_OUTLINE"

    def __init__(self):
        super().__init__()
        self.setHeaderHidden(True)  # 隐藏表头
        self.itemClicked.connect(self.on_tree_item_clicked)
        pub.subscribe(self.load_markdown, self.TOPIC_LOAD_OUTLINE)
        self.setStyleSheet("""
            QTreeWidget {
                border: none;  /* 设置边框颜色 */
                border-radius: 0px;         /* 圆角 */
                padding: 0px;               /* 内边距 */
            }
        """)

    def on_tree_item_clicked(self, item: QTreeWidgetItem):
        """树形框项点击事件"""
        print(item.text(0))
        print("树形框点击")

    def load_markdown(self, md_text: str):
        """解析 Markdown 并生成大纲树"""
        self.clear()  # 清空旧数据
        outline = self.extract_outline(md_text)

        root_items = []  # 记录各级标题的父节点

        for level, title in outline:
            item = QTreeWidgetItem([title])
            if level == 1:
                self.addTopLevelItem(item)
                root_items = [item]  # 重新记录根节点
            else:
                # 确保当前级别有父节点，否则降级到最近的可用级别
                while len(root_items) < level:
                    root_items.append(root_items[-1])

                parent = root_items[level - 2]  # 找到对应的父节点
                parent.addChild(item)
                root_items[level - 1:] = [item]  # 更新该级别的最新节点

    @staticmethod
    def extract_outline(md_text: str) -> list[tuple[int, str]]:
        """正则解析 Markdown 标题"""
        outline = []
        for line in md_text.split("\n"):
            match = re.match(r"^(#{1,6})\s+(.*)", line)
            if match:
                level = len(match.group(1))  # 计算 # 数量，确定标题层级
                title = match.group(2).strip()
                outline.append((level, str(title)))
        return outline


class FileBrowseTree(QTreeWidget):
    TOPIC_ADD_FILE = "FileBrowseTree.TOPIC_ADD_FILE"
    TOPIC_ADD_FOLDER = "FileBrowseTree.TOPIC_ADD_FOLDER"
    TOPIC_REMOVE_ITEM = "FileBrowseTree.TOPIC_REMOVE_ITEM"

    def __init__(self, parent=None):
        super(FileBrowseTree, self).__init__(parent)
        # self.setColumnCount(1)
        self.setHeaderHidden(True)  # 隐藏表头
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)  # 允许自定义右键菜单
        self.customContextMenuRequested.connect(self.__show_context_menu)
        # self.setHeaderLabel("文件目录")

        self.itemClicked.connect(self.on_tree_item_clicked)
        self.setStyleSheet("""
            QTreeWidget {
                border: none;  /* 设置边框颜色 */
                border-radius: 0px;         /* 圆角 */
                padding: 0px;               /* 内边距 */
            }
        """)
        self.setAcceptDrops(True)  # 启用拖拽接受

        pub.subscribe(self.add_file_item, self.TOPIC_ADD_FILE)
        pub.subscribe(self.add_folder_item, self.TOPIC_ADD_FOLDER)
        pub.subscribe(self.remove_item, self.TOPIC_REMOVE_ITEM)

    def remove_item(self, item: QTreeWidgetItem):
        parent = item.parent()
        if parent:
            parent.removeChild(item)  # 如果有父节点，从父节点移除
        else:
            index = self.indexOfTopLevelItem(item)
            self.takeTopLevelItem(index)  # 如果是顶级节点，直接删除

    def dragEnterEvent(self, event):
        """ 处理拖拽进入事件 """
        if event.mimeData().hasUrls():  # 如果拖入的是文件
            urls = event.mimeData().urls()
            for url in urls:
                file_path = url.toLocalFile()
                if file_path.endswith(".md"):  # 只接受.md文件
                    event.accept()  # 接受拖拽
                    return
            event.ignore()  # 忽略不符合条件的文件类型
        else:
            event.ignore()  # 忽略非文件类型

    def dropEvent(self, event):
        """ 处理拖拽释放事件 """
        urls = event.mimeData().urls()  # 获取拖入的文件列表
        if urls:
            file_path = urls[0].toLocalFile()  # 获取文件路径
            if file_path.endswith(".md"):  # 只处理 .md 文件
                print(f"已拖入Markdown文件: {file_path}")
                self.add_file_item(file_path)  # 添加文件到树形控件
            else:
                print(f"忽略非Markdown文件: {file_path}")

    def on_tree_item_clicked(self, item: QTreeWidgetItem):
        """树形框项点击事件"""
        file_path = os.path.normpath(item.data(0, Qt.ItemDataRole.UserRole))

        if not file_path:
            return

        if not os.path.isfile(file_path):
            return

        # 设置HTML
        pub.sendMessage(MarkdownPreviewWrapper.TOPIC_SET_FILE, file_path=file_path)

    def __add_item_to_tree(self, parent_item, path, is_folder):
        """ 添加文件或文件夹到树中 """
        item = QTreeWidgetItem(parent_item)
        item.setText(0, os.path.basename(path))  # 设置名称
        item.setData(0, Qt.ItemDataRole.UserRole, path)
        if is_folder:
            item.setIcon(0, QIcon("./resources/icons/folder.png"))  # 文件夹图标
        else:
            item.setIcon(0, QIcon("./resources/icons/file.png"))  # 文件图标

    def add_file_item(self, file_path: str):
        """ 添加单个文件到树 """
        if not os.path.exists(file_path):
            return

        if not os.path.isfile(file_path):
            return

        if not file_path.endswith(".md"):
            return

        root = self.invisibleRootItem()  # 获取根节点
        self.__add_item_to_tree(root, file_path, is_folder=False)

    def add_folder_item(self, folder_path):
        """ 递归添加文件夹及其内容到树 """

        if not os.path.exists(folder_path):
            return

        if not os.path.isdir(folder_path):
            return

        root = self.invisibleRootItem()  # 获取根节点

        folder_item = QTreeWidgetItem(root)
        folder_item.setText(0, os.path.basename(folder_path))
        folder_item.setData(0, Qt.ItemDataRole.UserRole, folder_path)
        folder_item.setIcon(0, QIcon("./resources/icons/folder.png"))

        # 遍历文件夹内容
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            if os.path.isdir(item_path):  # 是目录，直接添加
                self.__add_item_to_tree(folder_item, item_path, is_folder=True)
            else:
                if not item_path.endswith(".md"):
                    continue
                self.__add_item_to_tree(folder_item, item_path, is_folder=False)

    def __show_context_menu(self, position):
        """ 右键菜单 """
        item = self.itemAt(position)  # 获取当前点击的项目
        if item is None:
            return

        menu = TreeMenu(item)
        menu.exec(self.viewport().mapToGlobal(position))


class TreeWidgetWrapper(QTabWidget):
    def __init__(self):
        super().__init__()
        self.addTab(FileBrowseTree(), "列表视图")
        self.addTab(MarkdownOutlineTree(), "大纲视图")
        self.setMinimumWidth(200)
        self.setMaximumWidth(400)
        self.setStyleSheet("""
            QTabWidget::pane {
                border: 1px solid #3498db;  /* 选项卡内容区域 */
                padding: 2px;
                background-color: white;
            }
            QTabBar::tab {
                border: 1px solid #3498db;  /* 选项卡按钮 */
                padding: 5px;
                background: #ecf0f1;
            }
            QTabBar::tab:selected {
                background: #3498db;
                color: white;
            }
        """)


class MarkdownPreviewWrapper(QTabWidget):
    """
    md文件预览包装
    1、可以编辑
    2、可以预览
    后续优化空间：md文件通过web浏览器渲染编辑框，然后进行编辑
    """
    TOPIC_SET_FILE = "TOPIC_SET_FILE"

    def __init__(self):
        super(MarkdownPreviewWrapper, self).__init__()
        self.style_content = None
        self.web_view = WebViewEngine()
        self.text_edit = MarkdownEdit()

        # 闪烁的解决方案：使用load
        self.web_view.load("https://www.example.com")

        self.addTab(self.text_edit, "文本编辑")
        self.addTab(self.web_view, "渲染效果")
        # self.currentChanged.connect(self.on_tab_changed)
        self.setStyleSheet("""
            QTabWidget::pane {
                border: 1px solid #3498db;  /* 选项卡内容区域 */
                padding: 2px;
                background-color: white;
            }
            QTabBar::tab {
                border: 1px solid #3498db;  /* 选项卡按钮 */
                padding: 5px;
                background: #ecf0f1;
            }
            QTabBar::tab:selected {
                background: #3498db;
                color: white;
            }
        """)

        self.load_styles()

        # 监听 tab 切换
        self.currentChanged.connect(self.handle_tab_change)

        pub.subscribe(self.set_markdown_file, self.TOPIC_SET_FILE)

    def handle_tab_change(self, index):
        if self.widget(index) is self.web_view.parentWidget():
            self.web_view.hide()
            QTimer.singleShot(50, self.web_view.show)  # 延迟 50ms 后再显示，减少闪烁

    def load_styles(self):
        """加载自定义 CSS 样式"""
        file_path1 = "./resources/style/pygments.css"  # 代码高亮 CSS
        file_path2 = "./resources/style/table.css"  # 表格样式 CSS
        css_content = ""

        for file_path in [file_path1, file_path2]:
            if os.path.exists(file_path):
                with open(file_path, "r", encoding="utf-8") as f:
                    css_content += f.read()

        # 加载 highlight.min.js
        self.style_content = f"""
        <style>
        {css_content}
        </style>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github-dark.min.css">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
        <script>hljs.highlightAll();</script>
        """

    def convert_local_images(self, html: str) -> str:
        """ 替换 HTML 中的本地图片路径 """
        from bs4 import BeautifulSoup

        soup = BeautifulSoup(html, "html.parser")
        for img in soup.find_all("img"):
            src = img["src"]
            if not src.startswith("http"):  # 不是网络图片，说明是本地图片
                # abs_path = os.path.abspath(os.path.join(base_path, src))
                abs_path = src
                # print(src)
                win_file_path = abs_path.replace("\\", "/")
                img["src"] = f"file:///{win_file_path}"  # 转换为浏览器可用的路径
                print(img["src"])

        return str(soup)

    def set_markdown_content(self, markdown_text: str):
        html = markdown.markdown(markdown_text, extensions=[
            TableExtension(),
            "fenced_code",  # 支持 ``` 代码块
            "extra"
        ])

        html = self.convert_local_images(html)

        styled_html = f"""
                    <html>
                    <head>{self.style_content}</head>
                    <body>{html}</body>
                    </html>
                    """

        temp_html_path = "./resources/data/render.html"
        with open(temp_html_path, mode="w", encoding="utf-8") as f:
            f.write(styled_html)

        # self.web_view.setHtml(styled_html)
        temp_html_path = os.path.normpath(os.path.realpath(temp_html_path))
        self.web_view.setUrl(QUrl.fromLocalFile(temp_html_path))
        self.text_edit.setText(markdown_text)

    def set_markdown_file(self, file_path: str):
        with open(file_path, "r", encoding="utf-8") as f:
            markdown_text = f.read()
            self.set_markdown_content(markdown_text)


class MarkdownPreviewTree(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout(self)

        self.tree_widget = TreeWidgetWrapper()
        self.tab_widget = MarkdownPreviewWrapper()
        layout.addWidget(self.tree_widget)
        layout.addWidget(self.tab_widget)

        from app.widgets.menubar import MenuBar
        pub.subscribe(self.on_open_file, MenuBar.MARKDOWN_OPEN_FILE)
        pub.subscribe(self.on_open_folder, MenuBar.MENU_OPEN_FOLDER)

    def on_open_folder(self, directory_path: str):
        self.load_directory(directory_path)

    def on_open_file(self, file_path: str):
        """打开 Markdown 文件并渲染"""
        if not os.path.isfile(file_path):
            return

        self.tab_widget.set_markdown_file(file_path)
        pub.sendMessage("tree_widget.add_file_item", file_path=file_path)

        with open(file_path, mode="r", encoding="utf-8") as f:
            content = f.read()
            pub.sendMessage("load_markdown", md_text=content)

    def load_directory(self, dir_path: str):
        """加载当前目录到树形框中"""
        self.tree_widget.clear()
        self.tree_widget.add_folder_item(dir_path)

    def on_tree_item_clicked(self, item: QTreeWidgetItem):
        """树形框项点击事件"""
        file_path = os.path.normpath(item.data(0, Qt.ItemDataRole.UserRole))
        if file_path and os.path.isfile(file_path):
            self.on_open_file(file_path)
