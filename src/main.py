import sys
from PyQt5.QtWidgets import QApplication
from gui import GUI

def main():
    '''
    Creates a QApplication instance and starts the GUI. 
    '''
    # Every Qt application must have one instance of QApplication.
    global app # Use global to prevent crashing on exit
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    
    # Start the Qt event loop. (i.e. make it possible to interact with the gui)
    sys.exit(app.exec_())

    # Any code below this point will only be executed after the gui is closed.

if __name__ == '__main__':
    main()
