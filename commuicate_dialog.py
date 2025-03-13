import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit, QInputDialog, QVBoxLayout, QColorDialog, QFrame, QFontDialog, QFileDialog, QTextEdit
from PyQt5.QtGui import QColor

class win(QWidget):
    def __init__(self):
        super().__init__()
        self.initui()
    def initui(self):
        self.setWindowTitle("my_window")
        self.resize(640,640)

        # self.textedit = QTextEdit()
        self.col = QColor()
        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }" 
            % self.col.name())

        self.btn = QPushButton("input word", self) #创建按钮组件
        self.btn1 = QPushButton("select color", self)
        self.btn2 = QPushButton("select font", self)
        self.btn3 = QPushButton("select file", self)
        self.btn.resize(self.btn.sizeHint())

        self.btn.clicked.connect(self.showDialog) #与showdialog函数连接
        self.btn1.clicked.connect(self.showcolor)
        self.btn2.clicked.connect(self.showfont)
        self.btn3.clicked.connect(self.showfile)

        self.le = QLineEdit(self) #创建文本框组件
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.btn)
        self.vbox.addWidget(self.btn1)
        self.vbox.addWidget(self.btn2)
        self.vbox.addWidget(self.btn3)
        self.vbox.addWidget(self.le)
        self.setLayout(self.vbox)

        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, "input dialog", "enter your names") #第二个参数是标题，第三个参数是内容

        if ok:
            self.le.setText(str(text)) #如果为真，则给文本框输入所输的字符
    def showcolor(self):
        self.col = QColorDialog.getColor()
        if self.col.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s }"
                % self.col.name())

    def showfont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.le.setFont(font)
            self.btn.setFont(font)
            self.btn1.setFont(font)
            self.btn2.setFont(font)
            self.btn3.setFont(font) 
    def showfile(self):
        fname = QFileDialog(self)
        # if fname[0]:
        #     f = open(fname[0], 'r')
        #     with f:
        #         data = f.read()
                
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = win()
    sys.exit(app.exec_())
