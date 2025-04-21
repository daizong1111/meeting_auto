import pytest
from playwright.sync_api import Playwright, sync_playwright, Page
from pages.login_page import LoginPage
from pages.home_page import HomePage
import logging

# 定义Playwright fixture，用于初始化Playwright实例
@pytest.fixture(scope="session")
def playwright() -> Playwright:
    with sync_playwright() as p:
        yield p


# page fixture，用于每条测试用例单独打开浏览器
@pytest.fixture(scope="function")
def page(playwright):
    logging.info("Starting browser...")
    browser = playwright.chromium.launch(headless=False)  # 启动浏览器
    logging.info("Browser started.")
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
    login_page.fill_username("18855056081")
    login_page.fill_password("123456@")
    login_page.fill_captcha("1")
    login_page.click_login()

    home_page = HomePage(login_page.page)
    page = home_page.get_meeting_room_manage_page()
    # # 等待新标签页打开
    # with page.expect_popup() as popup_info:
    #     home_page = HomePage(page).click_meeting_room_manage_icon()
    #
    # # 获取新打开的标签页
    # new_page = popup_info.value

    # # 切换到新标签页
    # page = new_page


    page.wait_for_timeout(2000)
    yield page
