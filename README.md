# B站视频下载工具


## ToDos
<del>[#1] 20-11-26 PyQt5多线程 - 预计下个更新</del>

## 目录

```
|-- BiliDownloader
   |-- constants
   |  |-- settings.py            # 存放爬虫常规设置
   |  |-- spiders                # 存放所有爬虫
   |  |-- Bilibili
   |  |  |-- ffmpeg              # ffmpeg 工具
   |  |  |-- biliDownloadSpider.py	# bili 爬虫程序
   |-- stati                     # 静态文件
   |  |-- img                    # 工具显示图标
   |  |-- qss                    # PyQt5 样式表
   |  |-- video                  # 视频默认存放路径
   |-- template                  # 存放 ui 模板
   |  |-- frames                 # 存放一般页面模板
   |-- uis                       # 存放 designer 生成的 ui
   |-- utils                     # 存放一些工具函数
   |-- allocating.py             # 主程序
   |-- controller.py             # 加载页面
   |-- loaders.py                # 给页面添加功能
   |-- requirements.txt          # 运行环境依赖
   |-- README.md
```

## PyQt5 导入

yejue@github 2020/11/25 提交 



## 简要工作流程 ↓

**allocating.py**

- **controller.py** 加载页面
- **loaders.py** 给页面增添一点儿功能
  - 输入**url**、选择路径、开始下载
  - 开启爬虫

## Original 
执行以下命令，以确保当前运行环境可以成功运行该工具。
```
> pip install -r requirements.txt
```



## 快速使用

在 **allocating.py** 中集合了所有的页面的实例与爬虫操作功能，运行 **allocating.py** 即可启动本应用。
