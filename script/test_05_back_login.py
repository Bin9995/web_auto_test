from script import log


class TestBackLogin:

    def test_01_back_login_success(self, back_login_page):
        back_login_page.back_login("admin","HM_2023_test","8888")
        result = back_login_page.get_success_result()
        log.info(f"后台登陆结果：{result}")
        assert "admin" in result