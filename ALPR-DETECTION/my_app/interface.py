import uci as uci
from PyQt5 import QtCore, QtGui, QtWidgets, uic


class MyWindow(QtWidgets.QMainWindow):
    def__init__(self):

    super(MyWindow,self).__init__()
    uci.loadUi('interface.ui',self)


if __name__=='__main__':
    import sys
    app=QtWidgets.QApplication(sys.argv)
    Window=MyWindow()
    Window.show()
    sys.exit(app.exec_())