'''
Types of Windows

1)The Qmain window class provides a main application window
a main window provides a framework for building an
application's user interface. PyQt has QMainWindow and its
related classes for main window management. QMainWindow has
its own layout to which you can add QToolbars, QDockWidgets,
a QMenuBar, and a QStatusBar
'''

'''
2)The QDialog class is the basic class of dialog window
and a dialog window is a top-level window mostly used for
short-term tasks and brief communications with the user.
QDialog may be modal or modeless
'''

'''
3)The QWidget class is the basic class of all user interface
objects, The widget is the important point of the user interfaces:
it receives mouse, keyboard and other events from the window
system, and paints a representation of itself on the screen.
'''

from PyQt6.QtWidgets import QApplication,QMainWindow,QWidget, QDialog

import sys

app=QApplication(sys.argv)
mainWindow=QMainWindow()
mainWindow.statusBar().showMessage("welcome ispd")
mainWindow.menuBar().addMenu("file1")
mainWindow.menuBar().addMenu("file2")
mainWindow.addToolBar("toolbar")
mainWindow.show()

Dialog=QDialog()
Dialog.show()
sys.exit(app.exec())