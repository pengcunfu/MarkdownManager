from PySide6.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem, QWidget, QVBoxLayout

app = QApplication([])

window = QWidget()
layout = QVBoxLayout()

# 创建 TreeWidget
tree = QTreeWidget()
tree.setHeaderLabels(["名称", "描述"])  # 设置表头

# 创建根节点
root = QTreeWidgetItem(tree, ["水果", "所有水果分类"])
tree.addTopLevelItem(root)

# 添加子节点
apple = QTreeWidgetItem(root, ["苹果", "红色"])
banana = QTreeWidgetItem(root, ["香蕉", "黄色"])

# 继续添加子节点（多级）
china_apple = QTreeWidgetItem(apple, ["中国苹果", "甜"])
us_apple = QTreeWidgetItem(apple, ["美国苹果", "酸"])

layout.addWidget(tree)
window.setLayout(layout)
window.show()

app.exec()
