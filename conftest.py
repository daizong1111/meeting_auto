import pytest
from playwright.sync_api import Playwright, sync_playwright, Page
from pages.login_page import LoginPage


# 定义Playwright fixture，用于初始化Playwright实例
@pytest.fixture(scope="session")
def playwright() -> Playwright:
    with sync_playwright() as p:
        yield p


# page fixture，用于每条测试用例单独打开浏览器
@pytest.fixture(scope="function")
def page(playwright):
    browser = playwright.chromium.launch(headless=False)  # 启动浏览器
    context = browser.new_context()  # 创建新的浏览器上下文
    page = context.new_page()  # 打开新页面
    yield page
    page.close()  # 关闭页面
    browser.close()  # 关闭浏览器


# 登录的前置操作
@pytest.fixture(scope="function")
def logged_in_page(page: Page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.fill_email("121292679@qq.com")
    login_page.fill_password("a546245426")
    login_page.click_login()
    page.wait_for_timeout(2000)
    yield page
