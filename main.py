from PyQt5 import QtWidgets
import sys


if __name__ == "__main__":
    from login_window import Ui_Login_Window
    from connection import Connection
    connection = Connection().connection()

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui1 = Ui_Login_Window(connection)
    ui1.setupUi(MainWindow)

    MainWindow.show()

    sys.exit(app.exec_())