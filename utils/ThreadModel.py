import threading
from PyQt5.QtCore import QThread


class SpiderThread(threading.Thread):
    def __init__(self, name, spider):
        threading.Thread.__init__(self)
        self.name = name
        self.spider = spider

    def run(self):
        print("开始线程：" + self.name)
        self.spider.main()
        print("退出线程：" + self.name)


class SpiderThread2(QThread):
    def __init__(self, name, spider):
        super().__init__()
        self.name = name
        self.spider = spider

    def run(self):
        print("开始线程：" + self.name)
        self.spider.main()
        print("退出线程：" + self.name)
