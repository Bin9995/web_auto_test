from selenium.webdriver.common.by import By
from base.base import BasePage
from config import BASE_URL
import time

class PageOpenAccount(BasePage):
    """开通托管资金账户页面"""
    def __init__(self,driver):
        # 定义浏览器驱动
        super().__init__(driver)
        # 页面元素定位
        self.im_open = (By.LINK_TEXT, '立即开通')
        self.name = (By.NAME, 'realname')
        self.card = (By.NAME, 'card_id')
        self.submit_btn = (By.CLASS_NAME, 'btn')
        self.im_btn = (By.CSS_SELECTOR, '#successForm > input')
        self.success_result = (By.CSS_SELECTOR, 'body')


    def open_url(self):
        self.driver.get(BASE_URL + "/common/member/login")

    def open_account(self,name,card):
        """开户操作"""
        self.base_click(self.im_open)
        self.base_input(self.name, name)
        self.base_input(self.card, card)
        self.base_click(self.submit_btn)
        time.sleep(2)
        self.base_click(self.im_btn)

    def get_success_result(self):
        """获取开户成功的结果"""
        return self.base_switch_handle(self.success_result).text
