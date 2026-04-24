from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base import BasePage


class PageBorrow(BasePage):
    """首页“我要借款”功能模块"""

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)

        # 首页导航
        self.home_link_candidates = [
            (By.LINK_TEXT, "首页"),
            (By.PARTIAL_LINK_TEXT, "首页"),
            (By.XPATH, "//*[normalize-space()='首页']"),
        ]

        # “我要借款”卡片/入口
        self.borrow_card_candidates = [
            (By.XPATH, "//li[contains(@class,'card') and .//*[normalize-space()='我要借款']]") ,
            (By.XPATH, "//*[normalize-space()='我要借款']/ancestor::li[1]"),
            (By.XPATH, "//a[contains(normalize-space(),'我要借款')]/ancestor::li[1]"),
        ]

        # 立即投资按钮
        self.invest_button_candidates = [
            (By.XPATH, "//a[contains(@class,'buy-btn') and normalize-space()='立即投资']"),
            (By.XPATH, "//a[contains(@class,'buy-btn') and contains(.,'立即投资')]"),
            (By.XPATH, "//span[contains(@class,'last')]//a[contains(.,'立即投资')]") ,
        ]

        # 投标金额输入框
        self.money_input_candidates = [
            (By.ID, "money"),
            (By.NAME, "tz-cash"),
            (By.XPATH, "//input[contains(@placeholder,'投资金额') or contains(@placeholder,'请输入投资金额')]") ,
        ]

        # 确认投标按钮
        self.confirm_button_candidates = [
            (By.CSS_SELECTOR, "input.tender-sub[value='确认投标']"),
            (By.XPATH, "//input[@type='submit' and @value='确认投标']"),
            (By.XPATH, "//input[contains(@class,'tender-sub') and @value='确认投标']"),
        ]

    def _find_first(self, candidates):
        """按候选定位顺序返回第一个可用元素"""
        last_error = None
        for loc in candidates:
            try:
                return self.fd_element(loc)
            except Exception as e:
                last_error = e
        raise AssertionError(f"未找到目标元素，最后错误：{last_error}")

    def _safe_click(self, candidates):
        """优先直接点击，失败后使用 JS 点击"""
        last_error = None
        for loc in candidates:
            try:
                WebDriverWait(self.driver, self.default_timeout).until(EC.element_to_be_clickable(loc)).click()
                return loc
            except Exception as e:
                last_error = e
                try:
                    ele = self.fd_element(loc)
                    self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", ele)
                    self.driver.execute_script("arguments[0].click();", ele)
                    return loc
                except Exception:
                    continue
        raise AssertionError(f"点击失败，最后错误：{last_error}")

    def click_home(self):
        """点击首页"""
        return self._safe_click(self.home_link_candidates)

    def click_invest_now(self):
        """点击我要借款卡片中的立即投资"""
        card = self._find_first(self.borrow_card_candidates)
        ActionChains(self.driver).move_to_element(card).pause(0.5).perform()
        return self._safe_click(self.invest_button_candidates)

    def input_invest_money(self, money):
        """输入投资金额"""
        money_ele = self._find_first(self.money_input_candidates)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", money_ele)
        money_ele.clear()
        money_ele.send_keys(money)

    def click_confirm_tender(self):
        """点击确认投标"""
        return self._safe_click(self.confirm_button_candidates)

    def invest_flow(self, money):
        """完整的借款投标流程：首页 -> 立即投资 -> 输入金额 -> 确认投标"""
        self.click_home()
        self.click_invest_now()
        self.input_invest_money(money)
        self.click_confirm_tender()

    def get_current_url(self):
        """获取当前页面 URL"""
        return self.driver.current_url

    def get_page_title(self):
        """获取当前页面标题"""
        return self.driver.title