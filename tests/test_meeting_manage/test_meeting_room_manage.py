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
from pages.meeting_room_manage.meeting_room_manage_page import MeetingRoomManagePageBase

# 配置日志记录器
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

from playwright.sync_api import expect, sync_playwright
import pytest
import logging

# 配置日志记录器
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


@pytest.fixture(scope="function")
def meeting_room_manage_page():
    with sync_playwright() as playwright:
        # browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
        browser = playwright.chromium.connect_over_cdp("http://127.0.0.1:9222")
        context = browser.contexts[0] if browser.contexts else browser.new_context()
        page = context.pages[0] if context.pages else context.new_page()
        page.set_default_timeout(3000)  # 设置默认超时时间为 3000 毫秒
        page.locator("//ul[@role='menubar']/div[3]").click()
        page = MeetingRoomManagePageBase(page)
        yield page


@pytest.mark.usefixtures("meeting_room_manage_page")  # 显式声明夹具
class TestAddMeetingRoom(BaseCase):

    @pytest.mark.parametrize(
        "room_name, room_code, capacity, location, status, devices, departments, manager, description, need_approval, approval_person, need_time_limit, days, start_time, end_time, max_duration, users, is_positive",

        [
            ("新增-成功", "HYS10-506", "10", "天王巷", "正常", ["投影仪"],
             ["集成公司", "省DICT研发中心", "项目管理办公室"], "张超/15357703370", "会议室很大，能容纳很多人", True,
             "张超/15357703370", True,
             ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
             ["集成公司", "省DICT研发中心", "项目管理办公室", "张超"], True),
            ("", "HYS10-506", "10", "天王巷", "正常", ["投影仪"],
             ["集成公司", "省DICT研发中心", "项目管理办公室"], "张超/15357703370", "会议室很大，能容纳很多人", True,
             "张超/15357703370", True,
             ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
             ["集成公司", "省DICT研发中心", "项目管理办公室", "张超"], False),
            ("新增-失败-必填项为空-容纳人数", "HYS10-506", "", "天王巷", "正常", ["投影仪"],
             ["集成公司", "省DICT研发中心", "项目管理办公室"], "张超/15357703370", "会议室很大，能容纳很多人", True,
             "张超/15357703370", True,
             ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
             ["集成公司", "省DICT研发中心", "项目管理办公室", "张超"], False),
            ("新增-失败-必填项为空-会议室位置", "HYS10-506", "10", "", "正常", ["投影仪"],
             ["集成公司", "省DICT研发中心", "项目管理办公室"], "张超/15357703370", "会议室很大，能容纳很多人", True,
             "张超/15357703370", True,
             ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
             ["集成公司", "省DICT研发中心", "项目管理办公室", "张超"], False),
            ("新增-失败-必填项为空-会议室状态", "HYS10-506", "10", "天王巷", "", ["投影仪"],
             ["集成公司", "省DICT研发中心", "项目管理办公室"], "张超/15357703370", "会议室很大，能容纳很多人", True,
             "张超/15357703370", True,
             ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
             ["集成公司", "省DICT研发中心", "项目管理办公室", "张超"], False),
            ("新增-失败-必填项为空-会议室设备", "HYS10-506", "10", "天王巷", "正常", "",
             ["集成公司", "省DICT研发中心", "项目管理办公室"], "张超/15357703370", "会议室很大，能容纳很多人", True,
             "张超/15357703370", True,
             ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
             ["集成公司", "省DICT研发中心", "项目管理办公室", "张超"], False),
            ("新增-失败-必填项为空-管理部门和管理人和审批人", "HYS10-506", "10", "天王巷", "正常", ["投影仪"],
             "", "", "会议室很大，能容纳很多人", True, "", True,
             ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
             ["集成公司", "省DICT研发中心", "项目管理办公室", "张超"], False),
            ("新增-失败-必填项为空-管理人", "HYS10-506", "10", "天王巷", "正常", ["投影仪"],
             ["集成公司", "省DICT研发中心", "项目管理办公室"], "", "会议室很大，能容纳很多人", True,
             "张超/15357703370", True,
             ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
             ["集成公司", "省DICT研发中心", "项目管理办公室", "张超"], False),
            ("新增-失败-必填项为空-审批人", "HYS10-506", "10", "天王巷", "正常", ["投影仪"],
             ["集成公司", "省DICT研发中心", "项目管理办公室"], "张超/15357703370", "会议室很大，能容纳很多人", True,
             "", True,
             ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
             ["集成公司", "省DICT研发中心", "项目管理办公室", "张超"], False),
            ("新增-失败-必填项为空-可预约的时间范围", "HYS10-506", "10", "天王巷", "正常", ["投影仪"],
             ["集成公司", "省DICT研发中心", "项目管理办公室"], "张超/15357703370", "会议室很大，能容纳很多人", True,
             "张超/15357703370", True,
             "", "08:30", "10:30", "24",
             ["集成公司", "省DICT研发中心", "项目管理办公室", "张超"], False),
            ("新增-失败-必填项为空-单次可预约最长时间", "HYS10-506", "10", "天王巷", "正常", ["投影仪"],
             ["集成公司", "省DICT研发中心", "项目管理办公室"], "张超/15357703370", "会议室很大，能容纳很多人", True,
             "张超/15357703370", True,
             ["星期一", "星期二", "星期三"], "08:30", "10:30", "",
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
    def test_add_meeting_room(self, meeting_room_manage_page, room_name: object, room_code: object, capacity: object, location: object, status: object,
                              devices: object,
                              departments: object, manager: object, description: object, need_approval: object, approval_person: object,
                              need_time_limit: object,
                              days: object,
                              start_time: object,
                              end_time: object, max_duration: object, users: object, is_positive: object):
        # meeting_room_manage_page = MeetingRoomManagePage(meeting_room_manage_page)
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


@pytest.mark.usefixtures("meeting_room_manage_page")  # 显式声明夹具
class TestEditMeetingRoom(BaseCase):
    # @pytest.fixture(autouse=True)
    # def setup_method(self, meeting_room_manage_page):
    #     # 使用夹具获取page对象
    #     page = self.meeting_room_manage_page = MeetingRoomManagePage(meeting_room_manage_page)
    #     rows_count = self.meeting_room_manage_page.get_table_rows().count()
    #
    #     if rows_count == 0:
    #         test_add_meeting_room_instance = TestAddMeetingRoom()
    #         test_add_meeting_room_instance.test_add_meeting_room(
    #             page,
    #             room_name="新增-成功",
    #             room_code="HYS10-506",
    #             capacity="10",
    #             location="天王巷",
    #             status="正常",
    #             devices=["投影仪"],
    #             departments=["集成公司", "省DICT研发中心", "项目管理办公室"],
    #             manager="张超/15357703370",
    #             description="会议室很大，能容纳很多人",
    #             need_approval=True,
    #             approval_person="张超/15357703370",
    #             need_time_limit=True,
    #             days=["星期一", "星期二", "星期三"],
    #             start_time="08:30",
    #             end_time="10:30",
    #             max_duration="24",
    #             users=["集成公司", "省DICT研发中心", "项目管理办公室", "张超"],
    #             is_positive=True
    #         )
    @pytest.mark.parametrize(
        "room_name, room_code, capacity, location, status, devices, departments, manager, description, need_approval, approval_person, need_time_limit, days, start_time, end_time, max_duration, users, is_positive",

        [
            # ("", "", "", "", "", "",
            #  "", "", "", True,
            #  "", True,
            #  "", "", "", "",
            #  "", False),
            # ("修改-成功", "HYS10-506", "10", "天王巷", "正常", ["投影仪"],
            #  ["集成公司", "省DICT研发中心", "项目管理办公室"], "张超/15357703370", "会议室很大，能容纳很多人", True,
            #  "张超/15357703370", True,
            #  ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
            #  ["集成公司", "省DICT研发中心", "项目管理办公室", "张超"], True),
            # ("", "HYS10-506", "10", "天王巷", "正常", ["投影仪"],
            #  ["集成公司", "省DICT研发中心", "项目管理办公室"], "张超/15357703370", "会议室很大，能容纳很多人", True,
            #  "张超/15357703370", True,
            #  ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
            #  ["集成公司", "省DICT研发中心", "项目管理办公室", "张超"], False),
            # ("编辑-失败-必填项为空-容纳人数", "HYS10-506", "", "天王巷", "正常", ["投影仪"],
            #  ["集成公司", "省DICT研发中心", "项目管理办公室"], "张超/15357703370", "会议室很大，能容纳很多人", True,
            #  "张超/15357703370", True,
            #  ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
            #  ["集成公司", "省DICT研发中心", "项目管理办公室", "张超"], False),
            # ("编辑-失败-必填项为空-会议室位置", "HYS10-506", "10", "", "正常", ["投影仪"],
            #  ["集成公司", "省DICT研发中心", "项目管理办公室"], "张超/15357703370", "会议室很大，能容纳很多人", True,
            #  "张超/15357703370", True,
            #  ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
            #  ["集成公司", "省DICT研发中心", "项目管理办公室", "张超"], False),
            ("编辑-失败-必填项为空-会议室状态", "HYS10-506", "10", "天王巷", "", ["投影仪"],
             ["集成公司", "省DICT研发中心", "项目管理办公室"], "张超/15357703370", "会议室很大，能容纳很多人", True,
             "张超/15357703370", True,
             ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
             ["集成公司", "省DICT研发中心", "项目管理办公室", "张超"], False),
            # ("编辑-失败-必填项为空-会议室设备", "HYS10-506", "10", "天王巷", "正常", "",
            #  ["集成公司", "省DICT研发中心", "项目管理办公室"], "张超/15357703370", "会议室很大，能容纳很多人", True,
            #  "张超/15357703370", True,
            #  ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
            #  ["集成公司", "省DICT研发中心", "项目管理办公室", "张超"], False),
            ("编辑-失败-必填项为空-管理部门和管理人和审批人", "HYS10-506", "10", "天王巷", "正常", ["投影仪"],
             "", "", "会议室很大，能容纳很多人", True, "", True,
             ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
             ["集成公司", "省DICT研发中心", "项目管理办公室", "张超"], False),
            # ("编辑-失败-必填项为空-管理人", "HYS10-506", "10", "天王巷", "正常", ["投影仪"],
            #  ["集成公司", "省DICT研发中心", "项目管理办公室"], "", "会议室很大，能容纳很多人", True,
            #  "张超/15357703370", True,
            #  ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
            #  ["集成公司", "省DICT研发中心", "项目管理办公室", "张超"], False),
            ("编辑-失败-必填项为空-审批人", "HYS10-506", "10", "天王巷", "正常", ["投影仪"],
             ["集成公司", "省DICT研发中心", "项目管理办公室"], "张超/15357703370", "会议室很大，能容纳很多人", True,
             "", True,
             ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
             ["集成公司", "省DICT研发中心", "项目管理办公室", "张超"], False),
            # ("编辑-失败-必填项为空-可预约的时间范围", "HYS10-506", "10", "天王巷", "正常", ["投影仪"],
            #  ["集成公司", "省DICT研发中心", "项目管理办公室"], "张超/15357703370", "会议室很大，能容纳很多人", True,
            #  "张超/15357703370", True,
            #  "", "08:30", "10:30", "24",
            #  ["集成公司", "省DICT研发中心", "项目管理办公室", "张超"], False),
            # ("编辑-失败-必填项为空-单次可预约最长时间", "HYS10-506", "10", "天王巷", "正常", ["投影仪"],
            #  ["集成公司", "省DICT研发中心", "项目管理办公室"], "张超/15357703370", "会议室很大，能容纳很多人", True,
            #  "张超/15357703370", True,
            #  ["星期一", "星期二", "星期三"], "08:30", "10:30", "",
            #  ["集成公司", "省DICT研发中心", "项目管理办公室", "张超"], False)

            # 添加更多测试数据集
        ],
        # ids=["修改-成功",
        #      "修改-失败-必填项为空-会议室名称",
        #      "修改-失败-必填项为空-容纳人数",
        #      "修改-失败-必填项为空-会议室位置",
        #      "修改-失败-必填项为空-会议室状态",
        #      '修改-失败-必填项为空-会议室设备',
        #      '修改-失败-必填项为空-管理部门',
        #      '修改-失败-必填项为空-管理人',
        #      '修改-失败-必填项为空-审批人',
        #      '修改-失败-必填项为空-可预约的时间范围',
        #      '修改-失败-必填项为空-单次可预约最长时间',
        #      ]
    )
    @allure.step("测试修改会议室")
    def test_edit_meeting_room(self, meeting_room_manage_edit_pre, room_name, room_code, capacity, location, status,
                               devices,
                               departments, manager, description, need_approval, approval_person, need_time_limit, days,
                               start_time,
                               end_time, max_duration, users, is_positive):

        # meeting_room_manage_page = MeetingRoomManagePage(meeting_room_manage_page)
        meeting_room_info_page = meeting_room_manage_edit_pre.click_edit_button()

        # # 若当前页面无编辑按钮，则先执行一条新增操作

        # meeting_room_info_page = meeting_room_manage_page.click_edit_button()
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


class TestQueryMeetingRoom:
    @pytest.mark.parametrize(
        "room, capacity, device, status, location, approval, departments, manager",
        [
            ("新增-成功", "10", "投影仪", "正常", "天王巷", "是", ["集成公司", "省DICT研发中心", "项目管理办公室"],
             "张超"),
            # 未做空值处理，有bug
            # ("", "", "", "", "", "", "",
            #  ""),
            # ("新增-成功", "10", "投影仪", "正常", "天王巷", "是", ["集成公司", "省DICT研发中心", "项目管理办公室"], "张超")
        ]
    )
    def test_query_meeting_room(self, meeting_room_manage_page, db_connection, room, capacity, device, status, location, approval,
                                departments, manager):
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
        # 等待查询结果加载
        meeting_room_manage_page.page.wait_for_timeout(2000)  # 等待 2 秒

        pages_data, pages_data_count = meeting_room_manage_page.get_table_data()
        # pages_data = []

        # 从数据库中提取数据
        db_data = meeting_room_manage_page.get_db_data(db_connection, query= """
                SELECT * from user
                """)

        # 比较两个数据集
        assert meeting_room_manage_page.compare_data(pages_data, db_data, ['Host', 'User', 'Select_priv']), "页面数据与数据库数据不一致"

class TestDeleteMeetingRoom:
    def test_delete_meeting_room(self, meeting_room_manage_page):
        count_pre = meeting_room_manage_page.get_table_rows().count()
        meeting_room_manage_page.click_delete_button()
        count_after = meeting_room_manage_page.get_table_rows().count()
        meeting_room_manage_page.verify_delete_success_message(count_pre, count_after)

    def test_delete_meeting_room_cancel(self, meeting_room_manage_page):
        # 点击删除按钮之前，表格中的行数
        count_pre = meeting_room_manage_page.get_table_rows().count()
        meeting_room_manage_page.click_delete_button_cancel()
        # 点击删除按钮之后，表格中的行数
        count_after = meeting_room_manage_page.get_table_rows().count()
        meeting_room_manage_page.verify_delete_cancel_message(count_pre, count_after)
