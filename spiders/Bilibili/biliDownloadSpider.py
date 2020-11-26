# -*- coding: utf-8 -*-
# @Time    : 2020/2/22
# @Author  : SunriseCai
# @Software: PyCharm


import os
import re
import json
import time
import requests
import threading
import subprocess

from constants import settings

"""Bilibili视频下载小程序"""

session = requests.session()


class BilibiliSpider:
    def __init__(self, url: str, path: str):
        self.url = url
        self.path = path if path else settings.SAVE_PATH
        print('下载链接：', url)
        print('存放路径：', os.path.realpath(self.path))
        self.pageHeaders = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0',
        }
        self.dataHeaders = {
            'accept': '*/*',
            'accept-encoding': 'identity',
            'accept-language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6,zh-HK;q=0.5',
            'origin': 'https://www.bilibili.com',
            'range': 'bytes=0-169123900000000',
            'referer': 'https://www.bilibili.com/video/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        }

    def get_url(self):
        """
        请求视频播放页面，在源码中获取视音频链接和视频名称
        :return: 视频链接、音频链接、视频名称
        """
        htmlData = requests.get(self.url, headers=self.pageHeaders, verify=False).text
        urlData = json.loads(re.findall('<script>window.__playinfo__=(.*?)</script>', htmlData, re.M)[0])
        videoUrl = urlData['data']['dash']['video'][0]['baseUrl']
        audioUrl = urlData['data']['dash']['audio'][0]['baseUrl']
        name = re.findall('<h1 title="(.*?)" class="video-title">', htmlData, re.M)[0]
        return videoUrl, audioUrl, name

    def download_video(self, videoUrl: str, videoName: str):
        """传入url和名称，开始下载"""
        videoContent = session.get(url=videoUrl, headers=self.dataHeaders).content
        with open(f'{self.path}\\{videoName}.m4s', 'wb') as f:
            f.write(videoContent)
        print('video download Success')

    def download_audio(self, audioUrl: str, audioName: str):
        """传入url和名称，开始下载"""
        audioContent = session.get(url=audioUrl, headers=self.dataHeaders).content
        with open(f'{self.path}\\{audioName}.mp3', 'wb') as f:
            f.write(audioContent)
        print('audio download Success')

    def merge_video_and_audio(self, videoName: str):
        """音视频合并函数，利用ffmpeg 合并音视频"""
        command = f'{settings.FFMPEG_PATH} -i "{self.path}\\{videoName}.m4s" -i "{self.path}\\{videoName}.mp3" -c copy "{self.path}\\{videoName}.mp4" -loglevel quiet -n'
        subprocess.Popen(command, shell=True)
        time.sleep(5)
        print(f'{videoName}.mp4合并完成！！！')

        self.delete_m4s_and_ma3(name=videoName)  # 删除文件

    def delete_m4s_and_ma3(self, name: str):
        """删除视频 和 音频"""
        mp3Path = f'{self.path}\\{name}.mp3'
        m4sPath = f'{self.path}\\{name}.m4s'
        if os.path.exists(mp3Path): os.remove(mp3Path)
        if os.path.exists(m4sPath): os.remove(m4sPath)

    def main(self):
        """ 主程序，利用多线程下载视音频会比较快"""
        videoUrl, audioUrl, name = self.get_url()
        # 双线程
        videoThread = threading.Thread(target=self.download_video, args=(videoUrl, name))
        audioThread = threading.Thread(target=self.download_audio, args=(audioUrl, name))
        videoThread.start()
        audioThread.start()
        videoThread.join()
        audioThread.join()
        # 单线程
        # self.download_video(videoUrl=videoUrl, videoName=name)
        # self.download_audio(audioUrl=audioUrl, audioName=name)
        session.close()  # 退出保持会话
        self.merge_video_and_audio(videoName=name)  # 将视音频合并到一个文件


if __name__ == '__main__':
    url = 'https://www.bilibili.com/video/BV1dK411G765'
    spider = BilibiliSpider(url=url, path='')
    spider.main()
