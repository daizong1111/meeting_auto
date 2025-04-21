from test_data import login_data
import pytest

from page.login_page import LoginPage


class TestLogin:

    @pytest.param(login_data.Success)
    def test_login(self, client, user):
        """
        Test login
        """
        # 登录页面的操作
        login_page = LoginPage()
        login_page.login()
        # 断言
