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
@pytest.fixture(scope="session")
def page(playwright):
    logging.info("Starting browser...")
    browser = playwright.chromium.launch(headless=False)  # 启动浏览器
    logging.info("Browser started.")
    context = browser.new_context()  # 创建新的浏览器上下文
    page = context.new_page() # 打开新页面
    page.set_default_timeout(5000)
    yield page
    page.close()  # 关闭页面
    browser.close()  # 关闭浏览器

# 登录的前置操作
@pytest.fixture(scope="session")
def logged_in_page(page: Page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.fill_username("18855056081")
    login_page.fill_password("123456@")
    login_page.fill_captcha("1")
    login_page.click_login()
    login_page.page.wait_for_timeout(2000)
    yield login_page

@pytest.fixture(scope="session")
def home_page(logged_in_page):
    home_page = HomePage(logged_in_page.page)
    yield home_page
@pytest.fixture(scope="module")
def meeting_manage_page(home_page):
    meeting_manage_page = home_page.get_meeting_manage_page()
    yield meeting_manage_page

@pytest.fixture(scope="function")
def meeting_room_manage_page(meeting_manage_page):
    # meeting_manage_page.locator("//span[text()='会议室管理']").click()
    meeting_manage_page.locator("//ul[@role='menubar']/div[3]").click()
    yield meeting_manage_page
    # # 清理逻辑：确保返回到会议室管理首页
    # try:
    #     meeting_manage_page.locator("//ul[@role=’menubar‘]/div[3]").click()
    # except Exception as e:
    #     logging.error(f"清理逻辑执行失败: {e}")



# 测试编辑功能的前置操作，保证表格中一定有数据
@pytest.fixture(scope="function")
def meeting_room_manage_edit_pre(meeting_room_manage_page):
    meeting_manage_page.locator("//ul[@role='menubar']/div[3]").click()
    yield meeting_manage_page
