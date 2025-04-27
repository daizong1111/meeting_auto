"""
此模块使用 Playwright 框架实现会议室管理模块的 UI 自动化测试，
包含增、删、改、查功能的测试用例。
"""
# import re

import logging
# from playwright.sync_api import expect, sync_playwright
# import pytest

import allure

from base_case import BaseCase
from pages.meeting_room_manage.meeting_room_manage_page import MeetingRoomManagePage

# 配置日志记录器
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
from pages.RuoyiUserPage import RuoyiUserPage

from playwright.sync_api import expect, sync_playwright
import pytest
import logging

# 配置日志记录器
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


@pytest.fixture(scope="function")
def ruoyi_user_page():
    with sync_playwright() as playwright:
        # browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
        browser = playwright.chromium.connect_over_cdp("http://127.0.0.1:9222")
        context = browser.contexts[0] if browser.contexts else browser.new_context()
        page = context.pages[0] if context.pages else context.new_page()
        page.set_default_timeout(3000)  # 设置默认超时时间为 3000 毫秒
        yield page



class TestQueryUsers:
    @pytest.mark.parametrize(
        "user_id, user_name, status, phonenumber, begin_time, end_time, dept_id, data_scope",
        [
            (None, None, None, None, None, None, None, None),
        ]
    )
    def test_query_users(self, ruoyi_user_page, user_id, user_name, status, phonenumber, begin_time, end_time, dept_id, data_scope):
        ruoyi_user_page = RuoyiUserPage(ruoyi_user_page)
        # 输入查询条件
        # meeting_room_manage_page.input_room(room)
        # meeting_room_manage_page.input_capacity(capacity)
        # meeting_room_manage_page.choose_device(device)
        # meeting_room_manage_page.choose_status(status)
        # meeting_room_manage_page.input_location(location)
        # meeting_room_manage_page.choose_approval(approval)
        # meeting_room_manage_page.choose_department(departments)
        # meeting_room_manage_page.input_manager(manager)
        # # 点击查询按钮
        # meeting_room_manage_page.click_query_button()
        # # 等待查询结果加载
        # meeting_room_manage_page.page.wait_for_timeout(2000)  # 等待 2 秒

        pages_data = ruoyi_user_page.get_table_data()

        # 从数据库中提取数据
        db_data = ruoyi_user_page.get_db_data(user_id, user_name, status, phonenumber, begin_time, end_time, dept_id, data_scope)

        # 比较两个数据集
        assert ruoyi_user_page.compare_data(pages_data, db_data), "页面数据与数据库数据不一致"

