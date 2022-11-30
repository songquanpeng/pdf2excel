import os
import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QSystemTrayIcon, QFileDialog

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

        self.startBtn.setDisabled(True)
        self.config = Config(config_file)
        if 'access_key' in self.config:
            self.akLineEdit.setText(self.config['access_key'])
        self.akLineEdit.textChanged.connect(lambda v: self.update_config("access_key", v))
        if 'secret_key' in self.config:
            self.skLineEdit.setText(self.config['secret_key'])
        self.skLineEdit.textChanged.connect(lambda v: self.update_config("secret_key", v))
        if 'region' in self.config:
            self.regionLineEdit.setText(self.config['region'])
        self.regionLineEdit.textChanged.connect(lambda v: self.update_config("region", v))

        self.convert_thread = None

    def closeEvent(self, event):
        self.quit()

    def quit(self):
        self.convert_thread = None
        app.quit()

    def update_config(self, key, value):
        self.config[key] = value

    @pyqtSlot()
    def on_chooseBtn_clicked(self):
        path = QFileDialog.getOpenFileName(self, "选择要转换的 PDF 文件", ".", "pdf(*.pdf)")[0]
        if path != "":
            self.fileLineEdit.setText(path)
            self.statusbar.showMessage(f"已选择：{os.path.basename(path)}")
            self.startBtn.setDisabled(False)
        else:
            self.statusbar.showMessage(f"未选择文件")

    @pyqtSlot()
    def on_startBtn_clicked(self):
        if self.convert_thread is None:
            self.startBtn.setText("中止转换")
            self.statusbar.showMessage("正在处理中 ...")
            self.convert_thread = ConvertThread(self, self.debug)
            self.convert_thread.setDaemon(True)
            self.convert_thread.start()
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
