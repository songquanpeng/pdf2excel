import os.path
import time
from threading import Thread, Event

from utils import pdf2images, image2excel, combine_excels


class ConvertThread(Thread):
    def __init__(self, main, debug=False):
        super().__init__()
        self.main = main
        self.working = True
        self.paused = False
        self.count = 0
        self.access_key = self.main.config['access_key']
        self.secret_key = self.main.config['secret_key']
        self.region = self.main.config['region']
        self.pdf_path = self.main.fileLineEdit.text()
        self.start_idx = self.main.startSpinBox.value() - 1
        self.end_idx = self.main.endSpinBox.value()
        if self.end_idx == 0:
            self.end_idx = -1
        self.rotate = int(self.main.rotateComboBox.currentText())
        self._stop_event = Event()
        self._pause_event = Event()

    def convert(self):
        self.main.statusbar.showMessage(f"正在将 PDF 文件转换为图片 ...")
        save_path = "temp"
        images = pdf2images(self.pdf_path, self.rotate, save_path)
        if self.end_idx == -1:
            self.end_idx = len(images) + 1
        images = images[self.start_idx:self.end_idx]
        if self.should_stop():
            return False, ""
        self.main.statusbar.showMessage(f"转换完毕，正在解析图片 ...")
        for i, image in enumerate(images):
            if self.should_stop():
                return False, ""
            self.main.statusbar.showMessage(f"正在解析第 {i + 1} 张图片（共 {self.end_idx - self.start_idx + 1} 张） ...")
            ok, message = image2excel(image, os.path.join(save_path, f"{os.path.basename(image).split('.')[0]}.xlsx"),
                                      self.access_key, self.secret_key, self.region)
            if not ok:
                return False, message
        if self.should_stop():
            return False, ""
        self.main.statusbar.showMessage(f"解析完毕，正在合并 Excel 文件 ...")
        combine_excels(save_path,
                       f"{os.path.basename(self.pdf_path).split('.')[0]}（{self.start_idx + 1}-{self.end_idx}）.xlsx")
        return True, ""

    def run(self):
        start_time = time.time()
        ok, message = self.convert()
        if self.should_stop():
            return
        end_time = time.time()
        if ok:
            self.main.statusbar.showMessage(f"文件处理完毕，耗时 {end_time - start_time:.0f} 秒")
        else:
            self.main.statusbar.showMessage(f"文件处理失败：{message}")
        self.main.startBtn.setText("开始转换")
        self.main.convert_thread = None

    def stop(self):
        self._stop_event.set()

    def should_stop(self):
        return self._stop_event.is_set()



