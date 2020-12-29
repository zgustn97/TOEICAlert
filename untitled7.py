import sys
sys.path.append("C:/Users/ADMIN/Desktop/ch_selenium")
import untitled8

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic


number_list = []

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("C:/Users/ADMIN/Desktop/ch_selenium/untitled.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.input_name.textChanged.connect(self.save_name)
        self.push_name.clicked.connect(self.push_search)
        self.list_name.itemDoubleClicked.connect(self.chkItemDoubleClicked)
        self.dial_input.valueChanged.connect(self.showDialValue)
        
        3
    def setDial(self) :
        #Dial의 최대/최솟값과 PageStep/SingleStep값을 변경합니다.
        self.dial_input.setMaximum(10)
        self.dial_input.setMinimum(1)
        self.dial_input.setPageStep(1)
        self.dial_input.setSingleStep(1)
        
    def showDialValue(self) :
        #Dial의 시그널 이용 - Dial의 값이 변경되면 Label에 값을 표시
        self.lbl_dial.setText(str(self.dial_input.value()))    
        in_number = 0
        in_number = self.dial_input.value
        
    def chkItemDoubleClicked(self):
        number_ck = 0
        number_ck =int(self.list_name.currentRow())
        self.list_name.clear()
        number_list.append(number_ck)
        ckck = len(number_list)
        if ckck == 1:
            whe = untitled8.noser(number_list[0])
            for cnt in whe:
                self.list_name.addItem(cnt)
        elif ckck == 2:
            whe = untitled8.noser(number_list[1])
            for cnt in whe:
                self.list_name.addItem(cnt)
        elif ckck == 3:
            whe = untitled8.noser(number_list[2])
            for cnt in whe:
                self.list_name.addItem(cnt)
    def save_name(self):
        global finded_name
        finded_name = self.input_name.text()
    def push_search(self):
        untitled8.noser(finded_name)
        global date, name, many
        date, name, many = untitled8.noser(finded_name)
        self.push_name.addItem()
        
        
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()