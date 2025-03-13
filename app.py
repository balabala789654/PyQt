from PyQt5.QtWidgets import QApplication, QWidget
import sys


class window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(640,640)
        self.setWindowTitle("mywindow")
        self.show()   
        
if __name__ == "__main__":

    app = QApplication(sys.argv)

    win = window()
    
    sys.exit(app.exec_())