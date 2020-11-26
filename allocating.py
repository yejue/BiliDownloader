import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap

from controller import MainController
from utils.ThreadModel import SpiderThread
from loaders import SpiderLoader
from spiders.Bilibili.biliDownloadSpider import BilibiliSpider


class RenderCenter(MainController):
    download_signal = pyqtSignal(tuple)       # 下载信号

    def __init__(self):
        super().__init__()
        self.controller()
        self.signals = {'download_signal': self.download_signal}    # 自定义信号表
        # 页面功能加载，下发信号表
        self.spider_loader = SpiderLoader(self, self.signals)

    def controller(self):
        """ 信号绑定槽 """
        self.download_signal.connect(self.downloader)

    def downloader(self, params):
        spider = BilibiliSpider(*params)
        thread1 = SpiderThread('Thread-1', spider)
        thread1.start()
        thread1.join()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = RenderCenter()
    icon = QIcon()
    icon.addPixmap(QPixmap("static/imgs/demo.jpg"), QIcon.Normal, QIcon.Off)
    win.setWindowIcon(icon)
    win.show()
    sys.exit(app.exec_())
