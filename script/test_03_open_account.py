from script import log

class TestOpenAccount:

    def test_01_open_account_success(self, open_account_ctx):
        open_account_ctx.open_account("吴波","511381197106209820")
        result = open_account_ctx.get_success_result()
        log.info(f"开户结果：{result}")
        assert "OK" in result