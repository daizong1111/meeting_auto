import pytest
from playwright.sync_api import Page
import allure
from pages.login_page import LoginPage
from base_case import BaseCase  # 导入 BaseCase


# 定义登录测试类，继承自BaseCase
class TestLogin(BaseCase):  # 继承 BaseCase
    @pytest.mark.parametrize("email, password, expected_error", [
        ("121292679@qq.com", "", "请输入密码"),
    ])
    @allure.step("测试登录失败")
    def test_login_with_invalid_credentials(self, page: Page, email: str, password: str, expected_error: str):
        login_page = LoginPage(page)
        self.log_step("导航到登录页面")
        login_page.goto()
        self.log_step("填写邮箱")
        login_page.fill_email(email)
        self.log_step("填写密码")
        login_page.fill_password(password)
        self.log_step("点击登录按钮")
        login_page.click_login()
        error_message = login_page.get_error_message()
        self.log_step(f"获取错误信息: {error_message}")
        assert error_message == expected_error, f"错误提示信息不匹配，期望: {expected_error}, 实际: {error_message}"  # 断言错误信息

    # 测试登录成功的参数化测试用例
    @pytest.mark.parametrize("email, password", [
        ("121292679@qq.com", "a546245426"),
    ])
    @allure.step("测试登录成功")
    def test_login_success(self, page: Page, email: str, password: str):
        login_page = LoginPage(page)  # 初始化登录页面
        self.log_step("导航到登录页面")  # 记录导航步骤
        login_page.goto()  # 导航到登录页面
        self.log_step("填写邮箱")  # 记录填写邮箱步骤
        login_page.fill_email(email)  # 填写邮箱
        self.log_step("填写密码")  # 记录填写密码步骤
        login_page.fill_password(password)  # 填写密码
        self.log_step("点击登录按钮")  # 记录点击登录按钮步骤
        login_page.click_login()  # 点击登录按钮
        # 等待2秒
        page.wait_for_timeout(2000)
        # 验证登录成功后的断言
        self.log_step("验证登录成功")  # 记录验证登录成功步骤
        assert page.url == "https://www.ketangpai.cn/#/bindwechat", f"登录失败，当前URL: {page.url}"
