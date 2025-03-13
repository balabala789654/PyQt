from PyQt5.QtCore import QDate, QTime, QDateTime, Qt

now = QDate.currentDate()
print(now.year(),now.month(),now.day())
print(now.toString(Qt.ISODate))
print(now.toString(Qt.DefaultLocaleLongDate))

datetime = QDateTime.currentDateTime()
print(datetime.toString(Qt.ISODate))