import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import googletrans

form_class = uic.loadUiType('ui/googleUi.ui')[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__() #부모의 초기화자 호출
        self.setupUi(self) #제작해 놓은 googleUi.ui를 연결
        self.setWindowTitle('구글 한줄 번역기') #앱 윈도우 타이틀
        self.setWindowIcon(QIcon('icons/google.png')) #윈도우 아이콘 불러오기
        self.statusBar().showMessage('Google Trans App v 1.0')

        self.pushButton.clicked.connect(self.trans_operation)
        self.pushButton_2.clicked.connect(self.reset_operation)

    def trans_operation(self):
        trans = googletrans.Translator()
        trans_str = self.lineEdit.text()

        trans_eng = trans.translate(trans_str, dest='en')
        trans_jap = trans.translate(trans_str, dest='ja')
        trans_cha = trans.translate(trans_str, dest='zh-cn')

        self.textEdit.append(trans_eng.text)
        self.textEdit_2.append(trans_jap.text)
        self.textEdit_3.append(trans_cha.text)

    def reset_operation(self):
        self.lineEdit.clear()
        self.textEdit.clear()
        self.textEdit_2.clear()
        self.textEdit_3.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWindow()
    ex.show()
    sys.exit(app.exec_())
