import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QHBoxLayout, QVBoxLayout

class win(QWidget):
    def __init__(self):
        super().__init__()
        self.initui()
    def initui(self):
        self.resize(640,640)
        self.setWindowTitle("my_window")

        button1 = QPushButton("button1")
        button2 = QPushButton("button2")

        hbox = QHBoxLayout() #创建一个水平布局盒子
        vbox = QVBoxLayout() #创建一个垂直布局盒子

        hbox.addStretch(1) #增加一块弹性空间，将按钮挤到右边
        hbox.addWidget(button1) #水平布局盒子中加入按钮1
        hbox.addWidget(button2) #水平布局盒子中加入按钮2

        vbox.addStretch(1) #增加一块弹性空间，将按钮挤到下面去
        vbox.addLayout(hbox) #将水平布局盒子装入到垂直布局盒子中
        self.setLayout(vbox)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = win()
    sys.exit(app.exec_())

