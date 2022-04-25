import sys

from PyQt5.QtWidgets import QApplication

from pyqt5_reactive_gui import Pyqt5_app

if __name__ == "__main__":

    qApplication = QApplication(sys.argv)

    pyqt5_app = Pyqt5_app()

    sys.exit(qApplication.exec_())
