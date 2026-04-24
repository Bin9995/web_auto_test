import os.path
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from config import PATH
from tools import GetLog
from selenium.webdriver.support.select import Select

class BasePage(object):

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.default_timeout = timeout

    def fd_element(self, loc):
        """元素定位的公共方法
            ：param loc:元素定位方式及属性值
            ：return:定位到的元素
        """
        try:
            element = WebDriverWait(self.driver, self.default_timeout).until(EC.presence_of_element_located(loc))
            return element
        except Exception as e:
            GetLog.get_log().error(f"元素定位超时，定位信息:{loc},错误信息：{e}")
            raise

    def get_shot(self,file_name):
        file_path = os.path.join(PATH,'img', file_name)
        self.driver.get_screenshot_as_file(file_path)

    def base_input(self, loc, text):
        # 定位元素
        ele = self.fd_element(loc)
        # 清空输入框
        ele.clear()
        # 输入内容
        ele.send_keys(text)

    def base_click(self, loc):
        self.fd_element(loc).click()

    def base_switch_handle(self, loc):
        WebDriverWait(self.driver, self.default_timeout).until(lambda x:len(x.window_handles)>1)
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        element = self.fd_element(loc)
        return element

    def base_switch_frame(self, loc):
        frame_ele = self.fd_element(loc)
        self.driver.switch_to.frame(frame_ele)

    def base_default_frame(self):
        self.driver.switch_to.default_content()

    def base_select_list(self, loc, text):
        ele = self.fd_element(loc)
        Select(ele).select_by_visible_text(text)