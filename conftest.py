import pytest
from playwright.sync_api import Playwright, sync_playwright, Page
from pages.login_page import LoginPage
from pages.home_page import HomePage
import logging
import mysql.connector
from pages.meeting_room_manage.meeting_room_manage_page import MeetingRoomManagePageBase
from tests.test_meeting_manage.test_meeting_room_manage import TestAddMeetingRoom


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
    page.set_default_timeout(7000)
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
    # 点击会议室管理菜单项
    meeting_manage_page.locator("//ul[@role='menubar']/div[3]").click()
    yield MeetingRoomManagePageBase(meeting_manage_page)
    # # 清理逻辑：确保返回到会议室管理首页
    # try:
    #     meeting_manage_page.locator("//ul[@role=’menubar‘]/div[3]").click()
    # except Exception as e:
    #     logging.error(f"清理逻辑执行失败: {e}")

@pytest.fixture(scope="session")
def db_connection():
   # 创建数据库连接
   db_config = {
       "host": "localhost",
       "user": "root",
       "password": "SDZ1t3o5m9916",
       "database": "mysql"
   }
   connection = mysql.connector.connect(**db_config)
   yield connection  # 返回连接对象
   # 测试结束后关闭连接
   connection.close()

# 测试编辑功能的前置操作，保证表格中一定有数据
@pytest.fixture(scope="function")
def meeting_room_manage_edit_pre(meeting_room_manage_page):
    # 等待3秒，防止表格尚未加载出来，导致计算出的表格行数为0
    meeting_room_manage_page.page.wait_for_timeout(3000)
    # 统计表格行数
    rows_count = meeting_room_manage_page.get_table_rows().count()
    if rows_count == 0:
        # 新增一条数据
        test_add_meeting_room = TestAddMeetingRoom()
        test_add_meeting_room.test_add_meeting_room(meeting_room_manage_page, "新增-成功", "HYS10-506", "10", "天王巷", "正常", ["投影仪"],
             ["集成公司", "省DICT研发中心", "项目管理办公室"], "张超/15357703370", "会议室很大，能容纳很多人", True,
             "张超/15357703370", True,
             ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
             ["集成公司", "省DICT研发中心", "项目管理办公室", "张超"], True)
    yield meeting_room_manage_page
