import os

from app.pages.win_data_dir import DataDirApp
from app.pages.win_search import SearchDialog
from PySide6.QtWidgets import QMenuBar, QFileDialog, QMenu
from PySide6.QtGui import QAction
from pubsub import pub

from app.pages.win_about import AboutDialog
from app.pages.win_image_handle import ImageHandleDialog
from app.widgets.markdown import MarkdownPreviewWrapper, FileBrowseTree, MarkdownOutlineTree
from app.pages.win_option import OptionDialog


class MenuBar(QMenuBar):
    MARKDOWN_OPEN_FILE = "MARKDOWN_OPEN_FILE"
    MENU_OPEN_FOLDER = "MENU_OPEN_FOLDER"

    def __init__(self):
        super().__init__()
        self.addMenu(self.FileMenu())
        self.addMenu(self.EditMenu())
        self.addMenu(self.ToolMenu())
        self.addMenu(self.AboutMenu())

    class FileMenu(QMenu):
        def __init__(self):
            super().__init__()
            self.setTitle("文件")

            # 创建打开动作
            open_file_action = QAction("打开文件", self)
            open_file_action.triggered.connect(self.on_open_file)
            self.addAction(open_file_action)

            open_files_action = QAction("打开文件夹", self)
            open_files_action.triggered.connect(self.on_open_folder)
            self.addAction(open_files_action)

            save_action = QAction("保存", self)
            save_action.triggered.connect(self.on_save)
            self.addAction(save_action)

            save_as_action = QAction("另存为", self)
            save_as_action.triggered.connect(self.on_save_as)
            self.addAction(save_as_action)

            export_action = QAction("导出", self)
            export_action.triggered.connect(self.on_export)
            self.addAction(export_action)

            # 添加分隔符
            self.addSeparator()

            exit_action = QAction("退出", self)
            exit_action.triggered.connect(self.on_close)
            self.addAction(exit_action)

            from app.widgets.toolbar import ToolBar
            pub.subscribe(self.on_open_file, ToolBar.TOOLBAR_OPEN_FILE)
            pub.subscribe(self.on_save, ToolBar.TOOLBAR_SAVE_FILE)

        def on_export(self):
            file_path, _ = QFileDialog.getSaveFileName(
                self,
                "导出文件",
                "",
                "文本文件 (*.txt);;Markdown 文件 (*.md);;所有文件 (*.*)")

            if not file_path:  # 用户没有选择文件
                return

            with open(file_path, 'w', encoding='utf-8') as file:
                file.write("Hello, PySide6!")  # 示例写入内容

            from app.utils.md import md_export
            md_export(file_path, file_path)

            print(f"文件已保存: {file_path}")

        def on_save_as(self):
            file_path, _ = QFileDialog.getSaveFileName(
                self,
                "保存文件",
                "",
                "文本文件 (*.txt);;Markdown 文件 (*.md);;所有文件 (*.*)")

            if not file_path:  # 用户没有选择文件
                return

            with open(file_path, 'w', encoding='utf-8') as file:
                file.write("Hello, PySide6!")  # 示例写入内容

            print(f"文件已保存: {file_path}")

        def on_open_folder(self):
            directory_path = QFileDialog.getExistingDirectory(self, "选择目录")
            if directory_path:
                # 树形框添加文件
                pub.sendMessage(FileBrowseTree.TOPIC_ADD_FOLDER, folder_path=directory_path)

        def on_open_file(self):
            file_path, _ = QFileDialog.getOpenFileName(
                self, "选择文件", "", "Markdown Files (*.md);;All Files (*.*)"
            )

            if not file_path:
                return

            if not os.path.isfile(file_path):
                return

            from app.utils.config_file import config_get_list, config_set_list
            data = config_get_list("file_list")
            if file_path in data:
                return

            data.append(file_path)
            config_set_list("file_list", data)
            pub.sendMessage(MarkdownPreviewWrapper.TOPIC_SET_FILE, file_path=file_path)
            pub.sendMessage(FileBrowseTree.TOPIC_ADD_FILE, file_path=file_path)
            with open(file_path, mode="r", encoding="utf-8") as f:
                content = f.read()
                pub.sendMessage(MarkdownOutlineTree.TOPIC_LOAD_OUTLINE, md_text=content)

        def on_open_files(self):
            file_paths, _ = QFileDialog.getOpenFileNames(
                self, "选择多个文件", "", "All Files (*);;Text Files (*.txt);;Python Files (*.py)"
            )
            if file_paths:
                print(file_paths)

        def on_save(self):
            file_path, _ = QFileDialog.getSaveFileName(
                self,
                "保存文件",
                "",
                "文本文件 (*.txt);;Markdown 文件 (*.md);;所有文件 (*.*)")

            if not file_path:  # 用户没有选择文件
                return

            with open(file_path, 'w', encoding='utf-8') as file:
                file.write("Hello, PySide6!")  # 示例写入内容

            print(f"文件已保存: {file_path}")

        def on_close(self):
            from app.pages.win_main import MainWindow
            pub.sendMessage(MainWindow.WINDOW_CLOSE)

    class EditMenu(QMenu):
        def __init__(self):
            super().__init__()
            self.setTitle("编辑")

            # 创建剪切动作
            cut_action = QAction("剪切", self)
            cut_action.triggered.connect(self.on_cut)
            self.addAction(cut_action)

            # 创建复制动作
            copy_action = QAction("复制", self)
            copy_action.triggered.connect(self.on_copy)
            self.addAction(copy_action)

            # 创建粘贴动作
            paste_action = QAction("粘贴", self)
            paste_action.triggered.connect(self.on_paste)
            self.addAction(paste_action)

        def on_cut(self):
            print("剪切")

        def on_copy(self):
            print("复制")

        def on_paste(self):
            print("粘贴")

    class ToolMenu(QMenu):
        def __init__(self):
            super().__init__()
            self.setTitle("工具")

            md_upload_action = QAction("Markdown文件上传", self)
            md_upload_action.triggered.connect(self.on_a)
            self.addAction(md_upload_action)

            md_feishu_action = QAction("Markdown上传飞书", self)
            md_feishu_action.triggered.connect(self.on_b)
            self.addAction(md_feishu_action)

            md_image_action = QAction("Markdown图像处理", self)
            md_image_action.triggered.connect(self.on_image_handle)
            self.addAction(md_image_action)

            md_path_handle = QAction("MD路径生成", self)
            md_path_handle.triggered.connect(self.on_path_handle)
            self.addAction(md_path_handle)

            md_search_action = QAction("搜索", self)
            md_search_action.triggered.connect(self.on_search_window)
            self.addAction(md_search_action)

            self.addSeparator()

            option_action = QAction("选项", self)
            option_action.triggered.connect(self.on_option_action)
            self.addAction(option_action)

        def on_path_handle(self):
            dlg = DataDirApp()
            dlg.exec()

        def on_search_window(self):
            dlg = SearchDialog()
            dlg.exec()

        def on_option_action(self):
            dlg = OptionDialog()
            dlg.exec()

        def on_image_handle(self):
            dlg = ImageHandleDialog(r"D:\MyProjects\Tools\MarkdownTools\resources\微信小程序基础.md")
            dlg.exec()

        def on_a(self):
            print("Markdown文件上传")

        def on_b(self):
            print("Markdown上传飞书")

    class AboutMenu(QMenu):
        def __init__(self):
            super().__init__()
            self.setTitle("关于")

            about_menu_action = QAction("关于", self)
            about_menu_action.triggered.connect(self.on_about)
            self.addAction(about_menu_action)

        def on_about(self):
            about_window = AboutDialog()
            about_window.exec()
