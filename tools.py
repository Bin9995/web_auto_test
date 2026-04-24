import json
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import logging
from config import PATH
from logging import handlers


class DriverTools:
    """管理浏览器驱动的类"""
    driver = None

    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            """获取浏览器驱动"""
            # 获取谷歌浏览器对象（创建浏览器驱动对象）
            path = r"D:\gooledriver\chromedriver-win64\chromedriver-win64\chromedriver.exe"
            ser = Service(executable_path=path)
            cls.driver = webdriver.Chrome(service=ser)
            # 浏览器最大化
            cls.driver.maximize_window()
            cls.driver.implicitly_wait(10)
        # 返回浏览器驱动对象
        return cls.driver

    @classmethod
    def quit_driver(cls):
        """退出浏览器驱动"""
        if cls.driver is not None:
            # 暂停3秒
            sleep(3)
            # 退出浏览器驱动
            cls.driver.quit()
            # 置空
            cls.driver = None


def read_json(file_name):
    """
    读取JSON文件并转换格式为【（），（）。。。】的列表
    :param file_name: json文件名
    :return: 列表
    """
    data = [] #空列表
    file_path = PATH + "/data/" + file_name #json文件路径
    with open(file_path, mode='r', encoding='utf-8') as f:
        #读取JSON文件并解析为python对象
        tmp = json.load(f)
        for i in tmp:
            a = tuple(i.values())
            data.append(a)
        return data


class GetLog:
    # 日志器
    __log = None

    @classmethod
    def get_log(cls):
        if cls.__log is None:
            # 获取日志器
            cls.__log = logging.getLogger()
            # 设置入口级别
            cls.__log.setLevel(logging.INFO)
            # 获取处理器
            filename = PATH + "/log/" + "web.log"
            tf = logging.handlers.TimedRotatingFileHandler(filename=filename,
                                                           when='midnight',
                                                           interval=1,
                                                           backupCount=3,
                                                           encoding='utf-8')
            # 获取格式器
            fmt = "%(asctime)s %(levelname)s [%(filename)s(%(funcName)s):%(lineno)d] - %(message)s"
            fm = logging.Formatter(fmt)
            # 将格式器添加到处理器
            tf.setFormatter(fm)
            cls.__log.addHandler(tf)
        return cls.__log

if __name__ == '__main__':
    print(read_json("login_data.json"))
