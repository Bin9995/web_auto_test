from base.base import BasePage
from config import BASE_URL
import time

class PageRegister(BasePage):

    def __init__(self,driver):
        """元素定位"""
        super().__init__(driver)
        from selenium.webdriver.common.by import By
        self.phone = (By.ID,'phone')
        self.pwd = (By.ID,'password')
        self.img_code = (By.ID,'verifycode')
        self.phone_click = (By.ID,'get_phone_code')
        self.phone_code = (By.ID,'phone_code')
        self.reg = (By.CLASS_NAME,'lg-btn')
        self.success_result = (By.CSS_SELECTOR,"div.reg-step-last > h1")
        self.fail_result = (By.CSS_SELECTOR,"#reg_form > div.reg-title")

    def open_url(self):
        self.driver.get(BASE_URL + "/common/member/reg")

    def register(self,phone,pwd,img_code,phone_code):
        self.base_input(self.phone,phone)
        self.base_input(self.pwd,pwd)
        self.base_input(self.img_code,img_code)
        self.base_click(self.phone_click)
        time.sleep(4)
        self.base_input(self.phone_code,phone_code)
        self.base_click(self.reg)

    def get_success_result(self):
        return self.fd_element(self.success_result).text

    def get_fail_result(self):
        return self.fd_element(self.fail_result).text