import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class MainWindow(QMainWindow):
   count = 0
	
   def __init__(self, parent = None):
      super(MainWindow, self).__init__(parent)
      self.mdi = QMdiArea()
      self.setCentralWidget(self.mdi)
      bar = self.menuBar()
		
      file = bar.addMenu("File")
      file.addAction("New")
      file.addAction("cascade")
      file.addAction("Tiled")
      file.triggered[QAction].connect(self.windowaction)
      self.setWindowTitle("MDI demo")
		
   def windowaction(self, q):
      print "triggered"
		
      if q.text() == "New":

       MainWindow.count = MainWindow.count+1
       sub = QMdiSubWindow()
       sub.setWidget(QTextEdit())
       sub.setWindowTitle("subwindow"+str(MainWindow.count))
       self.mdi.addSubWindow(sub)
       sub.show()
		
      if q.text() == "cascade":
        self.mdi.cascadeSubWindows()
		
      if q.text() == "Tiled":
       self.mdi.tileSubWindows()
		
def main():
      app = QApplication(sys.argv)
      ex = MainWindow()
      ex.show()
      sys.exit(app.exec_())
	
if __name__ == '__main__':
      main()
