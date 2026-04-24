from script import log


class TestBorrow:

    def test_01_borrow_tender_flow(self, borrow_page):
        """首页我要借款流程：点击首页 -> 立即投资 -> 输入金额 -> 确认投标"""
        borrow_page.click_home()
        borrow_page.click_invest_now()
        borrow_page.input_invest_money("100")
        borrow_page.click_confirm_tender()

        current_url = borrow_page.get_current_url()
        title = borrow_page.get_page_title()

        log.info(f"确认投标后URL：{current_url}")
        log.info(f"确认投标后标题：{title}")

        assert current_url

