from playwright.sync_api import Page, expect


# 定义登录页面的类，包含页面元素和操作方法
class LoginPage:
    def __init__(self, page: Page):
        # 初始化页面对象和页面元素
        self.page = page
        self.username_input = page.get_by_placeholder("请输入您的手机号")  # 邮箱输入框
        self.password_input = page.get_by_placeholder("请输入密码")  # 密码输入框
        self.captcha_input = page.get_by_placeholder("短信验证码") # 验证码
        self.login_button = page.get_by_role("button", name="登录")  # 登录按钮

    def goto(self):
        # 导航到登录页面
        self.page.goto("http://www.iworkos.com:30100/digital-oa-web/#/login")

    def fill_username(self, username: str):
        # 填写用户名
        self.username_input.fill(username)

    def fill_password(self, password: str):
        # 填写密码
        self.password_input.fill(password)

    def fill_captcha(self, captcha: str):
        # 填写验证码
        self.captcha_input.fill(captcha)

    def click_login(self):
        # 点击登录按钮
        self.login_button.click()

    def get_error_message(self):
        # 获取错误信息
        return self.page.locator(".error-message").text_content()


