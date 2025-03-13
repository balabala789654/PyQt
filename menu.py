import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QMessageBox, QMenu, QAction
from PyQt5.QtGui import QIcon

class win(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initui()
    def initui(self):
        self.statusBar().showMessage("ready...") #状态栏
        self.resize(640,640)
        self.setWindowTitle("statusbar")

        menubar = self.menuBar()
        filemenu = menubar.addMenu("file")
        impmenu = menubar.addMenu("image")

        file1 = QMenu('Import', self)
        impAct = QAction('Import mail', self)
        file1.addAction(impAct)

        self.show()

if __name__ == "__main__":

    try:
        app = QApplication(sys.argv)
        window = win()
        sys.exit(app.exec_())
    except KeyboardInterrupt:
        print("exit...")