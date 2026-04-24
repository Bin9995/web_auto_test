from script import log


class TestCreditReview:

    def test_01_credit_review_success(self, credit_review_page):
        credit_review_page.review_commit(note="审核通过", code="8888")
        credit_review_page.application_record("13800001001")
        result = credit_review_page.get_success_result()
        log.info(f"额度审核结果：{result}")
        assert "通过" == result