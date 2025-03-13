import sys, random, time
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QPainter, QColor, QFont, QPen, QBrush
from PyQt5.QtCore import Qt, QPoint, QTimer

height = 640
width = 640

class win(QWidget):
    def __init__(self):
        super().__init__()
        self.initui()

    def initui(self):
        self.x = 0
        self.y = 0
        self.flag = 0
        self.resize(width,height)
        self.setWindowTitle("my_window")
        print(self.width(), type(self.width()))
        self.initAnimation() #初始化定时器
        self.show() #启动窗口
        

    def initAnimation(self):
        self.timer = QTimer(self) #创建定时器
        self.timer.timeout.connect(self.update_painter) #定时器回调函数与update_painter函数连接
        self.timer.start(1) #启动定时器,参数为定时时长

    def update_painter(self):
        # self.x = random.randint(1, self.height())
        # self.y = random.randint(1, self.height())
        self.x = 340
        if self.flag == 0:
            self.y += 1
            if self.y == self.height():
                self.flag = 1
        else:
            self.y -= 1
            if self.y == 0:
                self.flag = 0
        # print(self.y)
        self.update() #重要！！！ 触发界面重绘

    def paintEvent(self, event):
        self.qp = QPainter(self) #创建绘画
        self.pen = QPen(Qt.red, 2) #创建画笔，颜色为red，2为粗细
        self.qp.setPen(self.pen)
        self.brush = QBrush(Qt.red) #创建填充，填充颜色为红色
        self.qp.setBrush(self.brush) #设置填充
        self.circle_center = QPoint(int(self.height()/2), int(self.width()/2)) #创建点
        self.rand_circle_ceter = QPoint(self.x, self.y) #创建点
        self.qp.drawEllipse(self.circle_center, 5, 5) #画一个圆，水平半径为5，垂直半径为5
        self.qp.drawEllipse(self.rand_circle_ceter, 5, 5) #画一个圆，同上
        self.qp.drawLine(self.circle_center.x(), self.circle_center.y(), self.rand_circle_ceter.x(), self.rand_circle_ceter.y()) #画一条线
        self.qp.end() #重要！！！ 在绘画结束时都需要对其结束

if __name__ =="__main__":
    app = QApplication(sys.argv)
    winodw = win()
    sys.exit(app.exec_())