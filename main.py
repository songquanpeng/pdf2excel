import os
import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QSystemTrayIcon

from config import Config
from convert_thread import ConvertThread
from ui import Ui_MainWindow

config_file = "pdf2excel.ini"
is_windows = os.name == "nt"
use_shell = is_windows


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.debug = os.getenv('PA_DEBUG') == "true"
        self.setupUi(self)
        self.setWindowIcon(QIcon(":/icon.png"))
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(QIcon(":/icon.png"))
        self.tray.setVisible(True)

        self.startBtn.setDisabled(True)
        self.config = Config(config_file)
        if 'access_key' in self.config:
            self.akLineEdit.setValue(self.config['access_key'])
        if 'secret_key' in self.config:
            self.skLineEdit.setValue(self.config['secret_key'])
        if 'region' in self.config:
            self.regionLineEdit.setValue(self.config['region'])
        self.convert_thread = None

    def closeEvent(self, event):
        self.quit()

    def quit(self):
        self.convert_thread = None
        app.quit()

    @pyqtSlot()
    def on_startBtn_clicked(self):
        self.restStopBtn.setEnabled(True)
        if self.convert_thread is None:
            self.startBtn.setText("中止转换")
            self.convert_thread = ConvertThread(self, self.debug)
            self.convert_thread.setDaemon(True)
            self.convert_thread.start()
            self.statusbar.showMessage("正在处理中 ...")
        else:
            self.startBtn.setText("开始转换")
            self.convert_thread.stop()
            self.convert_thread = None
            self.statusbar.showMessage("已终止")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Dialog = MainWindow()
    Dialog.show()
    sys.exit(app.exec_())
