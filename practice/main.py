import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
import pykorbit

form_class = uic.loadUiType("ui_test1.ui")[0]
timer = QTimer()

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__();
        self.setupUi(self);

        self.setWindowTitle("Binance Trading Bot");
        self.setWindowIcon(QIcon("icon1.png"));

        self.pushButton_1.clicked.connect(self.btn_clicked1)
        self.pushButton_2.clicked.connect(self.btn_clicked2)

        
        timer.timeout.connect(self.timeout)
        timer.start(1000)
        
        '''
        self.setGeometry(200,200,400,300);
        self.setWindowTitle("Binance Trading Bot");
        self.setWindowIcon(QIcon("icon1.png"));
        
        btn = QPushButton("버튼1", self)
        btn.move(10, 10)

        btn2 = QPushButton("버튼2", self)
        btn2.move(10, 40)
        
        btn.clicked.connect(self.btn_clicked)
        '''
        
    def btn_clicked1(self):
        price = pykorbit.get_current_price("BTC")
        self.lineEdit_1.setText(str(price))
        print(price)
        
    def btn_clicked2(self):
        price = pykorbit.get_current_price("XRP")
        self.lineEdit_2.setText(str(price))
        print(price)

    def timeout(self):
        cur_time = QTime.currentTime()
        str_time = cur_time.toString("hh:mm:ss")
        print(str_time)
        self.statusBar().showMessage(str_time)

        price = pykorbit.get_current_price("BTC")
        self.lineEdit_1.setText(str(price))
        price = pykorbit.get_current_price("XRP")
        self.lineEdit_2.setText(str(price))
        
     
        

app = QApplication(sys.argv);
window = MyWindow();
window.show();

app.exec_();

timer.stop()
