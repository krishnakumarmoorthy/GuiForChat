import sys
from PyQt4 import QtGui
def window():
	app=QtGui.QApplication(sys.argv)
	scr_res=app.desktop().screenGeometry()
	w=QtGui.QWidget()
	b=QtGui.QLabel(w)
	b.setText("Hello world!")
	width,height=scr_res.width(),scr_res.height()
	w.setGeometry(100,100,200,50)
	b.move(50,20)
	w.setWindowTitle("chat")
	w.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	window()
