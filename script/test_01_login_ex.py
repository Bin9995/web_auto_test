import pytest
from script import log
from tools import read_json


class TestLogin:

    @pytest.mark.parametrize("phone,password,expect",read_json("login_data.json"))
    def test_01_login(self,phone,password,expect,a_login):
        """登录成功"""
        # 1.准备数据 2.调用方法 3.打印结果 4.断言
        a_login.login(phone, password)
        if expect == phone:
            result = a_login.get_success_result()
        else:
            result = a_login.get_fail_result()
        log.info(f"登录结果:{result}")
        assert expect in result