"""
此模块使用 Playwright 框架实现会议室管理模块的 UI 自动化测试，
包含增、删、改、查功能的测试用例。
"""
# from tracemalloc import start
# import re

import logging
# from playwright.sync_api import expect, sync_playwright
# import pytest

# 获取当前脚本所在的目录，并向上查找目标模块
import os
import sys

import allure

from base_case import BaseCase
from pages.meeting_room_manage.meeting_room_list_page import MeetingRoomListPage
# 显式引入测试夹具
from conftest import logged_in_page

# 配置日志记录器
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# @pytest.fixture(scope="function")
# def page():
#     # 连接到已打开的浏览器实例，方便调试
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
#         context = browser.contexts[0] if browser.contexts else browser.new_context()
#         page = context.pages[0] if context.pages else context.new_page()
#         page.set_default_timeout(3000)  # 设置默认超时时间为 5000 毫秒
#         yield page
#         # page.close()
#         # context.close()
#         # browser.close()
#     """
#     为每个测试用例提供浏览器页面实例，测试结束后关闭浏览器。
#     """
    # with sync_playwright() as p:
    #     browser = p.chromium.launch(headless=False)
    #     page = browser.new_page()
    #     page.goto("http://www.iworkos.com:30100/digital-oa-web/#/login")  # 替换为实际系统 URL
    #     # 输入用户名和密码并登录
    #     page.get_by_placeholder("请输入您的手机号").fill("18855056081")
    #     page.get_by_placeholder("请输入密码").fill("123456@") 
    #     page.get_by_placeholder("短信验证码").fill("1")
    #     page.get_by_role("button", name="登录").click()
    #     with page.expect_popup() as page1_info:
    #         page.locator("div:nth-child(6) > img").click()
    #     page1 = page1_info.value
    #     page1.set_default_timeout(5000)
    #     page1.get_by_role("link", name="会议室管理").click()
    #     yield page1
    #     # yield page
    #     browser.close()



from playwright.sync_api import expect, sync_playwright
import pytest
import logging

# 配置日志记录器
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# @pytest.fixture(scope="function")
# def page():
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
#         context = browser.contexts[0] if browser.contexts else browser.new_context()
#         page = context.pages[0] if context.pages else context.new_page()
#         page.set_default_timeout(3000)  # 设置默认超时时间为 3000 毫秒
#         yield page



class TestAddMeetingRoom(BaseCase):

    @pytest.mark.parametrize(
        "room_name, room_code, capacity, location, status, devices, departments, manager, need_approval, approval_person, need_time_limit, start_time, end_time, max_duration, users",
        [
            ("会议室009", "HYS10-506", "10", "天王巷", "正常", ["投影仪"], ["集成公司", "省DICT研发中心", "项目管理办公室"], "张超/15357703370", True, "张超/15357703370", True, "08:30", "10:30", "24", ["集成公司", "省DICT研发中心", "项目管理办公室", "张超"]),
            ("会议室010", "HYS10-507", "20", "天王巷2号", "正常", ["投影仪", "白板"], ["集成公司", "省DICT研发中心"], "李华/15357703371", False, None, False, None, None, None, ["集成公司", "省DICT研发中心", "李华"]),
            # 添加更多测试数据集
        ]
    )
    @allure.step("测试新增会议室")
    def test_add_meeting_room(self, logged_in_page, room_name, room_code, capacity, location, status, devices, departments, manager, need_approval, approval_person, need_time_limit, start_time, end_time, max_duration, users):
        meeting_room_list_page = MeetingRoomListPage(logged_in_page)
        meeting_room_info_page = meeting_room_list_page.click_add_button()       
        meeting_room_info_page.fill_room_name(room_name)
        meeting_room_info_page.fill_room_code(room_code)
        meeting_room_info_page.fill_capacity(capacity)
        meeting_room_info_page.fill_location(location)
        meeting_room_info_page.select_room_statuss(status)
        meeting_room_info_page.select_devices(devices)
        meeting_room_info_page.select_departments(departments)
        meeting_room_info_page.select_manager(manager)
        meeting_room_info_page.fill_description(f"{room_name} 很大，能容纳很多人")
        meeting_room_info_page.toggle_approval(need_approval, approval_person)
        meeting_room_info_page.toggle_time_limit(need_time_limit, start_time, end_time, max_duration)
        meeting_room_info_page.select_users(users)
        meeting_room_info_page.click_submit_button()
        meeting_room_info_page.verify_success_message()



# def test_delete_meeting_room(browser_page):
#     """
#     测试删除会议室功能。
#     """
#     page = browser_page
#     # 查找要删除的会议室并点击删除按钮
#     page.click("//td[text()='测试会议室 1']/following-sibling::td/button[text()='删除']")  # 替换为实际元素选择器

#     # 点击确认删除按钮
#     page.click("#confirm-delete-button")  # 替换为实际按钮选择器

#     # 验证会议室是否删除成功
#     page.wait_for_selector("//td[text()='测试会议室 1']", state="hidden")  # 替换为实际元素选择器
#     assert not page.is_visible("//td[text()='测试会议室 1']")


# def test_edit_meeting_room(browser_page):
#     """
#     测试编辑会议室功能。
#     """
#     page = browser_page
#     # 点击添加会议室按钮
#     # page.get_by_role("button", name="新建").click()  # 替换为实际按钮选择器
#     table = page.get_by_role("table")
#     # 获取该表格的行数
#     row_count = table.locator("tr").count()
#     print(row_count)
#     if row_count == 0:
#         # 如果表格为空，则添加一个会议室
#         test_add_meeting_room(page, need_approval=False, need_time_limit=False)
#
#     # 如果表格不为空，则点击第一个会议室的编辑按钮
#     # 点击表格的第一行的修改按钮
#     table.locator("tr").first.get_by_role("button", name="编辑").click()
#
#     page.screenshot(path="edit_meeting_room.png")
#
#     # 输入会议室信息
#     page.get_by_role("textbox", name="会议室名称：").fill("会议室1")
#     # 输入会议室编号
#     # page.get_by_role("textbox", name="会议室编号:").fill("HYS101")
#     # # 输入会议室容量
#     # page.get_by_role("textbox", name="* 容纳人数:").fill("10")
#     # # 输入会议室位置
#     # page.get_by_role("textbox", name="* 会议室位置:").fill("天王巷4楼")
#     # 选择会议室状态
#     page.get_by_placeholder("请选择").first.click()
#     room_status_li = page.locator("li").filter(has_text="正常")
#     room_status_li.wait_for(state="visible")
#     room_status_li.click()
#     # # 选择设备
#     page.get_by_text("投影仪").click()
#     # 选择管理部门
#     page.get_by_placeholder("请选择").nth(1).click()
#     org_item1 = page.get_by_role("menuitem", name="集成公司").get_by_role("radio")
#     org_item1.click()
#     org_item2 = page.get_by_role("menuitem", name="省DICT研发中心").get_by_role("radio")
#     org_item2.click()
#     org_item3 = page.get_by_role("menuitem", name="项目管理办公室").get_by_role("radio")
#     org_item3.click()
#     page.mouse.click(x=10, y=10)  # 点击空白处
#     # 选择管理人
#     page.get_by_placeholder("请选择").nth(2).click()
#     manager_item3 = page.get_by_role("menuitem", name="张超/15357703370")
#     manager_item3.click()
#     page.mouse.click(x=10, y=10)  # 点击空白处
#     # 输入相关描述
#     # page.get_by_role("textbox", name="相关描述：").fill("这个会议室很大，能容纳很多人")
#     if need_approval:
#         # 打开审批开关
#         page.locator("(//div[@role='switch'])[1]").click()
#         page.get_by_placeholder("请选择").nth(3).click()
#         # page.get_by_role("menuitem", name="集成公司").click()
#         # approval_item1 = page.get_by_role("menuitem", name="集成公司")
#         # approval_item1.wait_for(state="visible")
#         # approval_item1.click()
#         # approval_item2 = page.get_by_role("menuitem", name="省政企")
#         # approval_item2.wait_for(state="visible")
#         # approval_item2.click()
#         approval_item3 = page.get_by_role("menuitem", name="张超/15357703370").nth(1)
#         approval_item3.click()
#         # 先点击空白处再选择
#         page.mouse.click(x=10, y=10)  # 点击空白处
#     if need_time_limit:
#         # 打开时间限制开关
#         page.locator("(//div[@role='switch'])[2]").click()
#         element = page.get_by_placeholder("请选择").nth(4)
#         if element.is_visible():
#             element.click()
#             page.get_by_text("星期一").click()
#             # 先点击空白处再选择
#             page.mouse.click(x=10, y=10)  # 点击空白处
#         # 点击按钮，弹出选项
#         page.get_by_placeholder("开始时间").click()
#         start_hour_locator = page.locator("(//ul[@class='el-scrollbar__view el-time-spinner__list'])[1]/li").filter(has_text="08")
#         start_hour_locator.scroll_into_view_if_needed()
#         start_hour_locator.click()
#         start_minute_locator = page.locator("(//ul[@class='el-scrollbar__view el-time-spinner__list'])[2]/li").filter(has_text="30")
#         start_minute_locator.scroll_into_view_if_needed()
#         start_minute_locator.click()
#         end_hour_locator = page.locator("(//ul[@class='el-scrollbar__view el-time-spinner__list'])[4]/li").filter(has_text="10")
#         end_hour_locator.scroll_into_view_if_needed()
#         end_hour_locator.click()
#         end_minute_locator = page.locator("(//ul[@class='el-scrollbar__view el-time-spinner__list'])[5]/li").filter(has_text="30")
#         end_minute_locator.scroll_into_view_if_needed()
#         end_minute_locator.click()
#         # 输入单次可预约最长时间
#         page.locator("(//input[@placeholder='请输入'])[3]").fill("24")
#     # 选择可使用者
#     page.locator(".text_area").click()
#     page.get_by_label("请选择部门和人员").get_by_text("集成公司").click()
#     page.get_by_label("请选择部门和人员").get_by_text("省DICT研发中心").click()
#     page.get_by_label("请选择部门和人员").get_by_text("项目管理办公室").click()
#     # page.get_by_label("请选择部门和人员").get_by_text("张超").locator("label span").nth(1).click()
#     page.locator("//span[text()='张超']/../../label").click()
#     # page.get_by_role("checkbox", name="张超").click()
#     page.get_by_role("button", name="确 定").click()
#     # 点击提交按钮
#     page.get_by_role("button", name="提交").click()
#     # 断言页面出现了添加成功字样的提示信息
#     expect(page.get_by_text("操作成功")).to_be_visible()
#
#
# # def test_search_meeting_room(browser_page):
#     """
#     测试搜索会议室功能。
#     """
#     page = browser_page
#     # 输入搜索关键词
#     page.fill("#search-input", "测试会议室 1")  # 替换为实际输入框选择器
#
#     # 点击搜索按钮
#     page.click("#search-button")  # 替换为实际按钮选择器
#
#     # 等待元素加载并验证搜索结果是否正确
#     page.wait_for_selector("//td[text()='测试会议室 1']")  # 替换为实际元素选择器
#     assert page.is_visible("//td[text()='测试会议室 1']")