import time
from script import log

class TestRegister:

    def test_01_register_success(self, a_register):
        a_register.register("18873314212","Aa123456","8888","666666")
        time.sleep(5)
        result = a_register.get_success_result()
        log.info(f"注册结果：{result}")
        assert "注册成功" in result

    def test_02_register_fail_phone_exist(self, a_register):
        a_register.register("13873321002", "Aa123456", "8888", "666666")
        result = a_register.get_fail_result()
        log.info(f"注册结果：{result}")
        assert "注册" in result