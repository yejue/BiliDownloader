import threading


class SpiderThread(threading.Thread):
    def __init__(self, name, spider):
        threading.Thread.__init__(self)
        self.name = name
        self.spider = spider

    def run(self):
        print("开始线程：" + self.name)
        self.spider.main()
        print("退出线程：" + self.name)
