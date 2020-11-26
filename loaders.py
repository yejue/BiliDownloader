from PyQt5.QtWidgets import QFileDialog


class SpiderLoader:
    def __init__(self, frame, signals):
        self.frame = frame
        self.save_path = ''
        self.signals = signals
        self.controller()

    def controller(self):
        self.frame.pushButton_download.clicked.connect(lambda: self.emit_download(self.get_url()))
        self.frame.pushButton_save_path.clicked.connect(self.get_path)

    def get_url(self):
        """ 拿到页面的URL """
        url = self.frame.le_url.text()
        return url

    def get_path(self):
        """ 选择保存路径 """
        save_path = QFileDialog.getExistingDirectory()
        self.frame.le_path.setText(save_path)
        self.save_path = save_path
        return save_path

    def emit_download(self, url):
        """ 发射下载信号 """
        self.signals['download_signal'].emit((url, self.save_path))
