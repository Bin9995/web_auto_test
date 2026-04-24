class TestCreditApplication:

    def test_01_credit_application_successs(self, credit_app):
        """测试额度申请成功"""
        # 1. 切换角色
        credit_app.switch_role()
        # 2. 点击申请额度
        credit_app.click_application()
        # 3. 填写信息并提交
        credit_app.credit_application("10000", "买车")
        # 4. 断言结果
        result = credit_app.get_result_text()
        assert "10000" in result or "10,000" in result

