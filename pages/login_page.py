from playwright.sync_api import Page, expect


# 定义登录页面的类，包含页面元素和操作方法
class LoginPage:
    def __init__(self, page: Page):
        # 初始化页面对象和页面元素
        self.page = page
        self.email_input = page.get_by_placeholder("请输入邮箱/手机号/账号")  # 邮箱输入框
        self.password_input = page.get_by_placeholder("请输入密码")  # 密码输入框
        self.login_button = page.get_by_role('button', name='登录')  # 登录按钮

    def goto(self):
        # 导航到登录页面
        self.page.goto("https://www.ketangpai.cn/#/login")

    def fill_email(self, email: str):
        # 填写邮箱
        self.email_input.fill(email)

    def fill_password(self, password: str):
        # 填写密码
        self.password_input.fill(password)

    def click_login(self):
        # 点击登录按钮
        self.login_button.click()

    def get_error_message(self):
        # 获取错误信息
        return self.page.locator(".error-message").text_content()
