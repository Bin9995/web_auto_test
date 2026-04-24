from base.base import BasePage
from selenium.webdriver.common.by import By

class CreditApplication(BasePage):
    """额度申请页面"""
    def __init__(self,driver):
        super().__init__(driver)
        # 页面元素定位信息
        self.role = (By.XPATH, '//*[text()="借款账户"]')
        self.application = (By.LINK_TEXT,"申请额度")
        self.money = (By.ID,"amount_account")
        self.detail = (By.NAME,"remark")
        self.code = (By.ID,"verifycode")
        self.submit = (By.CSS_SELECTOR,".btn-submit.btn-md")
        self.success_text = (By.XPATH,'//*[@id="amount_list"]/tr/td[3]')

    def switch_role(self):
        """点击切换角色"""
        self.base_click(self.role)

    def click_application(self):
        """"点击申请额度"""
        self.base_click(self.application)

    def credit_application(self,money,detail):
        """输入信息、点击提交"""
        self.base_input(self.money,money)
        self.base_input(self.detail,detail)
        self.base_input(self.code,"8888")
        self.base_click(self.submit)

    def get_result_text(self):
        return self.fd_element(self.success_text).text