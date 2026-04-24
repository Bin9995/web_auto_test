from script import log


class TestLogin:

    def test_01_login_success(self,a_login):
        """登录成功"""
        # 1.准备数据 2.调用方法 3.打印结果 4.断言
        a_login.login("13873371902","Aa123456")
        result = a_login.get_success_result()
        log.info(f"登录结果:{result}")
        assert "13873371902" == result

    def test_02_login_fail_pwd_error(self,a_login):
        a_login.login("13800001001", "123456")
        result = a_login.get_fail_result()
        log.info(f"登录结果:{result}")
        assert "密码错误" in result
