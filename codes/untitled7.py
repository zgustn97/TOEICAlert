import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QIcon


class MyApp(QWidget):

  def __init__(self):
      super().__init__()
      self.initUI()

  def initUI(self):
      self.setWindowTitle('Icon')
      self.setWindowIcon(QIcon('C:/Users/ADMIN/Desktop/ch_selenium/img/face.jpg'))
      
      self.setGeometry(300, 300, 300, 200)
      self.show()
  


if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = MyApp()
  sys.exit(app.exec_())
  

