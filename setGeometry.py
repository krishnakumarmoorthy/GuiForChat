# -*-coding: utf-8 -*-
import sys
from PyQt4.QtGui import *

def window():
   app = QApplication(sys.argv)
   w = QWidget()
	
   b = QPushButton(w)
   b.setText("Hello World!")
   b.move(50,20)

   #w.setGeometry(10,10,300,200)
   w.setGeometry(10,10,300,200)
   w.setWindowTitle("PyQt")
   w.show()
   sys.exit(app.exec_())
if __name__ == '__main__':
   window()
