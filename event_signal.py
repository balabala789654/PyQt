import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLCDNumber, QSlider, QVBoxLayout
from PyQt5.QtCore import Qt

class win(QWidget):
    def __init__(self):
        super().__init__()
        self.initui()

    def initui(self):
        self.setWindowTitle("my_window")
        self.resize(640,640)

        vbox = QVBoxLayout() #创建垂直分布布局盒子
        bt1 = QPushButton("button1", self)
        bt1.clicked.connect(self.clickevent) #将点击事件与clickevent函数连接
        lcd = QLCDNumber() #创建lcd数字组件
        sld = QSlider(Qt.Horizontal, self) #创建滑块组件
        sld.valueChanged.connect(lcd.display) #将滑块拖动事件与lcd数字大小显示连接
        
        vbox.addWidget(bt1) #将按钮加入垂直分布盒子
        vbox.addWidget(lcd) #将lcd数字加入垂直分布盒子
        vbox.addWidget(sld) #将滑块加入垂直分布盒子

        self.setLayout(vbox)

        self.show()

    def clickevent(self):
        QMessageBox.information(self, "message", "button clicked")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = win()
    sys.exit(app.exec_())

