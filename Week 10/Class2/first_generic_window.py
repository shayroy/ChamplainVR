import sys
from PyQt5 import QtCore, QtGui, QtWidgets

def window():

    app = QtWidgets.QApplication(sys.argv) #for this api need to call application object from QtWidgets and
    #assign to app. "sys.argv" is sort of like a null imput, a reference or pointer to the system. So app equals a new
    # application.

    window = QtWidgets.QWidget() #Inside this new application app there will be a window. Window called widget.

    window.setGeometry(50, 50, 1000, 500) #This sets the size of the window in pixels.

    window.setWindowTitle("UI Window") # all windows get titles.

    window.show()

    sys.exc_info(app.exec_()) # This command is kind of like saying make it happen.

window() # this calls the window so something happens



