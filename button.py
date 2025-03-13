import sys
from PyQt5.QtWidgets import QWidget, QToolBar, QPushButton, QApplication, QToolTip, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication

class win(QWidget):
    def __init__(self):
        super().__init__()
        # self.initfont()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont("SansSerif", 10)) #10px的SansSerif 字体。
        button = QPushButton("button", self)
        button.setToolTip("this is a button") #提示词
        button.resize(button.sizeHint()) #sizeHint() 方法提供了一个默认的按钮大小。
        button.clicked.connect(self.clickevent)

        button_quit = QPushButton("quit", self)
        button_quit.clicked.connect(QCoreApplication.instance().quit) #连接一个点击事件。使窗口关闭
        button_quit.resize(button_quit.sizeHint())#sizeHint() 方法提供了一个默认的按钮大小。
        button_quit.move(0,50)#移动button
        self.resize(640,640)
        self.setWindowTitle("my_win")
        self.show()

    def initfont(self):
        QToolTip.setFont(QFont("SansSerif", 10))
        self.setToolTip('This is a <b>QWidget</b> widget')

    def closeEvent(self, event):
        #第一个字符串显示在消息框的标题栏，第二个字符串显示在对话框，第三个参数是消息框的俩按钮，最后一个参数是默认按钮，这个按钮是默认选中的
        reply = QMessageBox.question(self, 'Message', "are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def clickevent(self):
        QMessageBox.information(self, "message", "button clicked...") #消息盒子
        print("button clicked...")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window1 = win()
    sys.exit(app.exec_())