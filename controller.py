from PyQt5.QtCore import Qt

from templates.frames import MainPage

from uis.bililiDownloader import Ui_bilili_downloader


class MainController(MainPage, Ui_bilili_downloader):
    """ 主窗口 """
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setStyleSheet(self.load_style('home.qss'))

        # 无边框
        self.setWindowFlags(Qt.FramelessWindowHint)

        # 阴影
        effect_shadow = self.setShadow((34, 203, 255), 5)
        self.pushButton_save_path.setGraphicsEffect(effect_shadow)
        self.pushButton_download.setGraphicsEffect(effect_shadow)
        # 圆角
        self.setCircle(self)
