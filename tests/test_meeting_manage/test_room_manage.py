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
from pages.meeting_room_manage.meeting_room_list_page import MeetingRoomManagePage

# 配置日志记录器
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

from playwright.sync_api import expect, sync_playwright
import pytest
import logging

# 配置日志记录器
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# @pytest.fixture(scope="function")
# def meeting_room_manage_page():
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
#         context = browser.contexts[0] if browser.contexts else browser.new_context()
#         page = context.pages[0] if context.pages else context.new_page()
#         page.set_default_timeout(3000)  # 设置默认超时时间为 3000 毫秒
#         yield page


@pytest.mark.usefixtures("meeting_room_manage_page")  # 显式声明夹具
class TestAddMeetingRoom(BaseCase):

    @pytest.mark.parametrize(
        "room_name, room_code, capacity, location, status, devices, departments, manager, description, need_approval, approval_person, need_time_limit, days, start_time, end_time, max_duration, users, is_positive",

        [
            # ("新增-成功", "HYS10-506", "10", "天王巷", "正常", ["投影仪"],
            #  ["集成公司", "省DICT研发中心", "项目管理办公室"], "张超/15357703370", True, "张超/15357703370", True,
            #  ["星期一","星期二","星期三"], "08:30", "10:30", "24", ["集成公司", "省DICT研发中心", "项目管理办公室", "张超"], True),
            # (None, "HYS10-506", "10", "天王巷", "正常", ["投影仪"],
            #  ["集成公司", "省DICT研发中心", "项目管理办公室"], "张超/15357703370", "会议室很大，能容纳很多人", True, "张超/15357703370", True,
            #  ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
            #  ["集成公司", "省DICT研发中心", "项目管理办公室", "张超"], False),
            # ("新增-失败-必填项为空-容纳人数", "HYS10-506", None, "天王巷", "正常", ["投影仪"],
            #  ["集成公司", "省DICT研发中心", "项目管理办公室"], "张超/15357703370", "会议室很大，能容纳很多人", True, "张超/15357703370", True,
            #  ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
            #  ["集成公司", "省DICT研发中心", "项目管理办公室", "张超"], False),
            # ("新增-失败-必填项为空-会议室位置", "HYS10-506", "10", None, "正常", ["投影仪"],
            #  ["集成公司", "省DICT研发中心", "项目管理办公室"], "张超/15357703370", "会议室很大，能容纳很多人", True, "张超/15357703370", True,
            #  ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
            #  ["集成公司", "省DICT研发中心", "项目管理办公室", "张超"], False),
            # ("新增-失败-必填项为空-会议室状态", "HYS10-506", "10", "天王巷", None, ["投影仪"],
            #  ["集成公司", "省DICT研发中心", "项目管理办公室"], "张超/15357703370", "会议室很大，能容纳很多人", True, "张超/15357703370", True,
            #  ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
            #  ["集成公司", "省DICT研发中心", "项目管理办公室", "张超"], False),
            # ("新增-失败-必填项为空-会议室设备", "HYS10-506", "10", "天王巷", "正常", None,
            #  ["集成公司", "省DICT研发中心", "项目管理办公室"], "张超/15357703370", "会议室很大，能容纳很多人", True, "张超/15357703370", True,
            #  ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
            #  ["集成公司", "省DICT研发中心", "项目管理办公室", "张超"], False),
            # 管理部门为空时，管理人无法直接选中
            ("新增-失败-必填项为空-管理部门", "HYS10-506", "10", "天王巷", "正常", ["投影仪"],
             None, "张超/15357703370", "会议室很大，能容纳很多人", True, "张超/15357703370", True,
             ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
             ["集成公司", "省DICT研发中心", "项目管理办公室", "张超"], False),
            ("新增-失败-必填项为空-管理人", "HYS10-506", "10", "天王巷", "正常", ["投影仪"],
             ["集成公司", "省DICT研发中心", "项目管理办公室"], None, "会议室很大，能容纳很多人",True, "张超/15357703370", True,
             ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
             ["集成公司", "省DICT研发中心", "项目管理办公室", "张超"], False),
            # ("新增-失败-必填项为空-审批人", "HYS10-506", "10", "天王巷", "正常", ["投影仪"],
            #  ["集成公司", "省DICT研发中心", "项目管理办公室"], "张超/15357703370", "会议室很大，能容纳很多人", True, None, True,
            #  ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
            #  ["集成公司", "省DICT研发中心", "项目管理办公室", "张超"], False),
            # ("新增-失败-必填项为空-可预约的时间范围", "HYS10-506", "10", "天王巷", "正常", ["投影仪"],
            #  ["集成公司", "省DICT研发中心", "项目管理办公室"], "张超/15357703370", "会议室很大，能容纳很多人", True, "张超/15357703370", True,
            #  None, "08:30", "10:30", "24",
            #  ["集成公司", "省DICT研发中心", "项目管理办公室", "张超"], False),
            # 单次可预约最长时间是有保存能力的，需要清空
            ("新增-失败-必填项为空-单次可预约最长时间", "HYS10-506", "10", "天王巷", "正常", ["投影仪"],
             ["集成公司", "省DICT研发中心", "项目管理办公室"], "张超/15357703370", "会议室很大，能容纳很多人", True, "张超/15357703370", True,
             ["星期一", "星期二", "星期三"], "08:30", "10:30", None,
             ["集成公司", "省DICT研发中心", "项目管理办公室", "张超"], False)


            # 添加更多测试数据集
        ],
        # ids=["新增-成功",
        #      "新增-失败-必填项为空-会议室名称",
        #      "新增-失败-必填项为空-容纳人数",
        #      "新增-失败-必填项为空-会议室位置",
        #      "新增-失败-必填项为空-会议室状态",
        #      '新增-失败-必填项为空-会议室设备',
        #      '新增-失败-必填项为空-管理部门',
        #      '新增-失败-必填项为空-管理人',
        #      '新增-失败-必填项为空-审批人',
        #      '新增-失败-必填项为空-可预约的时间范围',
        #      '新增-失败-必填项为空-单次可预约最长时间',

        #      ]
    )
    @allure.step("测试新增会议室")
    def test_add_meeting_room(self, meeting_room_manage_page, room_name, room_code, capacity, location, status, devices,
                              departments, manager, description, need_approval, approval_person, need_time_limit, days, start_time,
                              end_time, max_duration, users, is_positive):
        meeting_room_manage_page = MeetingRoomManagePage(meeting_room_manage_page)
        meeting_room_info_page = meeting_room_manage_page.click_add_button()
        meeting_room_info_page.fill_room_name(room_name)
        meeting_room_info_page.fill_room_code(room_code)
        meeting_room_info_page.fill_capacity(capacity)
        meeting_room_info_page.fill_location(location)
        meeting_room_info_page.select_room_status(status)
        meeting_room_info_page.select_devices(devices)
        meeting_room_info_page.select_departments(departments)
        meeting_room_info_page.select_manager(manager)
        meeting_room_info_page.fill_description(description)
        meeting_room_info_page.toggle_approval(need_approval, approval_person)
        meeting_room_info_page.toggle_time_limit(need_time_limit, days, start_time, end_time, max_duration)
        meeting_room_info_page.select_users(users)
        meeting_room_info_page.click_submit_button()
        if is_positive is True:
            meeting_room_info_page.verify_success_message()
        else:
            meeting_room_info_page.verify_error_miss_message()

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
