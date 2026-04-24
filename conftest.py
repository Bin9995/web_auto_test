import pytest
from page.page_back_login import PageBackLogin
from page.page_borrow import PageBorrow
from page.page_credit_application import CreditApplication
from page.page_credit_review import PageCreditReview
from page.page_login import PageLogin
from page.page_open_account import PageOpenAccount
from page.page_register import PageRegister
from tools import DriverTools

# 编写浏览器驱动创建和退出
@pytest.fixture()
def browser(request):
    """获取浏览器驱动"""
    driver = DriverTools.get_driver()
    # 返回驱动对象 yeild为前后置界限
    yield driver
    DriverTools.quit_driver()

@pytest.fixture()
def a_login(browser):
    """登录操作"""
    page_login = PageLogin(browser)
    page_login.open_url()
    return page_login


@pytest.fixture()
def a_register(browser):
    """注册页面"""
    page_reg = PageRegister(browser)
    page_reg.open_url()
    return page_reg


@pytest.fixture()
def open_account_ctx(browser):
    """开通账户前置：进入登录页并登录"""
    page_login = PageLogin(browser)
    open_acc = PageOpenAccount(browser)
    open_acc.open_url()
    page_login.login("18873314212", "Aa123456")
    return open_acc


@pytest.fixture()
def credit_app(browser):
    """额度申请前置：登录后返回额度申请页对象"""
    login_page = PageLogin(browser)
    login_page.open_url()
    login_page.login("13800001001", "Aa123456")
    return CreditApplication(browser)


@pytest.fixture()
def back_login_page(browser):
    """后台登录页（含后置截图）"""
    page = PageBackLogin(browser)
    page.open_url()
    yield page
    page.get_shot("back_login.png")


@pytest.fixture()
def credit_review_page(browser):
    """额度审核页（含后置截图）"""
    back_login = PageBackLogin(browser)
    back_login.open_url()
    back_login.back_login(username="admin", password="HM_2023_test", code="8888")

    credit_rev = PageCreditReview(browser)
    credit_rev.menu_manager()
    credit_rev.search_record("13800001001")
    credit_rev.select_record()

    yield credit_rev
    credit_rev.get_shot("credit_review_success.png")


@pytest.fixture()
def borrow_page(browser):
    """借款流程前置：登录后返回借款页面对象"""
    page_login = PageLogin(browser)
    page_login.open_url()
    page_login.login("13873371902", "Aa123456")
    return PageBorrow(browser)
