#DESCRIPTION: Runs the application and loads the main window
#Loads and displays the main GUI windows, starts the event loop
#AUTHOR: Md Faizan Ashrafi


import sys
from PyQt5.QtWidgets import QApplication
from ui.main_window import MainWindow

def main():
    app=QApplication(sys.argv)
    app.setApplicationName("Auto Machine Learning Platform")

    window=MainWindow()
    window.show()

    sys.exit(app.exec_())

if __name__=="__main__":
    main()
