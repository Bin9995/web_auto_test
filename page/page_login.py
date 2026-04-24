import time
from selenium.webdriver.common.by import By
from base.base import BasePage
from config import BASE_URL
from tools import DriverTools

# 类的三要素：1、定义页面类 2、设置实例属性 3、定义页面操作方法
class PageLogin(BasePage):
    """初始化方法"""
    def __init__(self,driver,timeout=10):
        #获取driver对象
        # driver = Tools.get_driver()
        super().__init__(driver)
        self.username = (By.ID,'keywords')
        self.password = (By.ID,'password')
        self.login_button = (By.ID,'login-btn')
        #成功结果元素属性
        self.success_result = (By.CLASS_NAME,'a-link1')
        #密码错误失败结果元素属性
        self.fail_result = (By.CSS_SELECTOR,'#err > span')

    def open_url(self):
        """打开网页"""
        self.driver.get(BASE_URL + "/common/member/login")

    def login(self, username, password):
        """登录操作方法"""
        self.base_input(self.username,username)
        self.base_input(self.password,password)
        self.base_click(self.login_button)
        time.sleep(2)

    def get_success_result(self):
        return self.fd_element(self.success_result).text

    def get_fail_result(self):
        return self.fd_element(self.fail_result).text

if __name__ == '__main__':
    # 实例化登录页面对象
    login = PageLogin(DriverTools.get_driver())
    # 打开网页
    login.open_url()
    # 调用登录方法
    login.login("13800001001","Aa123456")