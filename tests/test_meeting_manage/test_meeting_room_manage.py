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
    def test_add_meeting_room(self, meeting_room_manage_page, room_name: object, room_code: object, capacity: object,
                              location: object, status: object,
                              devices: object,
                              departments: object, manager: object, description: object, need_approval: object,
                              approval_person: object,
                              need_time_limit: object,
                              days: object,
                              start_time: object,
                              end_time: object, max_duration: object, users: object, is_positive: object):
        meeting_room_info_page = meeting_room_manage_page.click_add_button()
        self.log_step("点击新增按钮")
        meeting_room_info_page.fill_room_name(room_name)
        self.log_step("填写会议室名称")
        meeting_room_info_page.fill_room_code(room_code)
        self.log_step("填写会议室编号")
        meeting_room_info_page.fill_capacity(capacity)
        self.log_step("填写会议室容量")
        meeting_room_info_page.fill_location(location)
        self.log_step("填写会议室位置")
        meeting_room_info_page.select_room_status(status)
        self.log_step("选择会议室状态")
        meeting_room_info_page.select_devices(devices)
        self.log_step("选择会议室设备")
        meeting_room_info_page.select_departments(departments)
        self.log_step("选择管理部门")
        meeting_room_info_page.select_manager(manager)
        self.log_step("选择管理人")
        meeting_room_info_page.fill_description(description)
        self.log_step("填写相关描述")
        meeting_room_info_page.toggle_approval(need_approval, approval_person)
        self.log_step("选择是否需要审批")
        meeting_room_info_page.toggle_time_limit(need_time_limit, days, start_time, end_time, max_duration)
        self.log_step("选择是否需要时间限制")
        meeting_room_info_page.select_users(users)
        self.log_step("选择可使用者")
        meeting_room_info_page.click_submit_button()
        self.log_step("点击提交按钮")
        if is_positive is True:
            meeting_room_info_page.verify_success_message()
            self.log_step("验证新增成功")

        else:
            meeting_room_info_page.verify_error_miss_message()
            self.log_step("验证新增失败")


@pytest.mark.usefixtures("meeting_room_manage_page")  # 显式声明夹具
class TestEditMeetingRoom(BaseCase):
    @pytest.mark.parametrize(
        "room_name, room_code, capacity, location, status, devices, departments, manager, description, need_approval, approval_person, need_time_limit, days, start_time, end_time, max_duration, users, is_positive",

        [
            ("", "", "", "", "", "",
             "", "", "", True,
             "", True,
             "", "", "", "",
             "", False),
            ("修改-成功", "HYS10-506", "10", "天王巷", "正常", ["投影仪"],
             ["集成公司", "省DICT研发中心", "项目管理办公室"], "张超/15357703370", "会议室很大，能容纳很多人", True,
             "张超/15357703370", True,
             ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
             ["集成公司", "省DICT研发中心", "项目管理办公室", "张超"], True),
            ("", "HYS10-506", "10", "天王巷", "正常", ["投影仪"],
             ["集成公司", "省DICT研发中心", "项目管理办公室"], "张超/15357703370", "会议室很大，能容纳很多人", True,
             "张超/15357703370", True,
             ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
             ["集成公司", "省DICT研发中心", "项目管理办公室", "张超"], False),
            ("编辑-失败-必填项为空-容纳人数", "HYS10-506", "", "天王巷", "正常", ["投影仪"],
             ["集成公司", "省DICT研发中心", "项目管理办公室"], "张超/15357703370", "会议室很大，能容纳很多人", True,
             "张超/15357703370", True,
             ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
             ["集成公司", "省DICT研发中心", "项目管理办公室", "张超"], False),
            ("编辑-失败-必填项为空-会议室位置", "HYS10-506", "10", "", "正常", ["投影仪"],
             ["集成公司", "省DICT研发中心", "项目管理办公室"], "张超/15357703370", "会议室很大，能容纳很多人", True,
             "张超/15357703370", True,
             ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
             ["集成公司", "省DICT研发中心", "项目管理办公室", "张超"], False),
            ("编辑-失败-必填项为空-会议室状态", "HYS10-506", "10", "天王巷", "", ["投影仪"],
             ["集成公司", "省DICT研发中心", "项目管理办公室"], "张超/15357703370", "会议室很大，能容纳很多人", True,
             "张超/15357703370", True,
             ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
             ["集成公司", "省DICT研发中心", "项目管理办公室", "张超"], False),
            ("编辑-失败-必填项为空-会议室设备", "HYS10-506", "10", "天王巷", "正常", "",
             ["集成公司", "省DICT研发中心", "项目管理办公室"], "张超/15357703370", "会议室很大，能容纳很多人", True,
             "张超/15357703370", True,
             ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
             ["集成公司", "省DICT研发中心", "项目管理办公室", "张超"], False),
            ("编辑-失败-必填项为空-管理部门和管理人和审批人", "HYS10-506", "10", "天王巷", "正常", ["投影仪"],
             "", "", "会议室很大，能容纳很多人", True, "", True,
             ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
             ["集成公司", "省DICT研发中心", "项目管理办公室", "张超"], False),
            ("编辑-失败-必填项为空-管理人", "HYS10-506", "10", "天王巷", "正常", ["投影仪"],
             ["集成公司", "省DICT研发中心", "项目管理办公室"], "", "会议室很大，能容纳很多人", True,
             "张超/15357703370", True,
             ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
             ["集成公司", "省DICT研发中心", "项目管理办公室", "张超"], False),
            ("编辑-失败-必填项为空-审批人", "HYS10-506", "10", "天王巷", "正常", ["投影仪"],
             ["集成公司", "省DICT研发中心", "项目管理办公室"], "张超/15357703370", "会议室很大，能容纳很多人", True,
             "", True,
             ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
             ["集成公司", "省DICT研发中心", "项目管理办公室", "张超"], False),
            ("编辑-失败-必填项为空-可预约的时间范围", "HYS10-506", "10", "天王巷", "正常", ["投影仪"],
             ["集成公司", "省DICT研发中心", "项目管理办公室"], "张超/15357703370", "会议室很大，能容纳很多人", True,
             "张超/15357703370", True,
             "", "08:30", "10:30", "24",
             ["集成公司", "省DICT研发中心", "项目管理办公室", "张超"], False),
            ("编辑-失败-必填项为空-单次可预约最长时间", "HYS10-506", "10", "天王巷", "正常", ["投影仪"],
             ["集成公司", "省DICT研发中心", "项目管理办公室"], "张超/15357703370", "会议室很大，能容纳很多人", True,
             "张超/15357703370", True,
             ["星期一", "星期二", "星期三"], "08:30", "10:30", "",
             ["集成公司", "省DICT研发中心", "项目管理办公室", "张超"], False)

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
        meeting_room_info_page = meeting_room_manage_edit_pre.click_edit_button()
        self.log_step("点击编辑按钮")
        meeting_room_info_page.fill_room_name(room_name)
        self.log_step("填写会议室名称")
        meeting_room_info_page.fill_room_code(room_code)
        self.log_step("填写会议室编号")
        meeting_room_info_page.fill_capacity(capacity)
        self.log_step("填写会议室容量")
        meeting_room_info_page.fill_location(location)
        self.log_step("填写会议室位置")
        meeting_room_info_page.select_room_status(status)
        self.log_step("选择会议室状态")
        meeting_room_info_page.select_devices(devices)
        self.log_step("选择会议室设备")
        meeting_room_info_page.select_departments(departments)
        self.log_step("选择管理部门")
        meeting_room_info_page.select_manager(manager)
        self.log_step("选择管理人")
        meeting_room_info_page.fill_description(description)
        self.log_step("填写相关描述")
        meeting_room_info_page.toggle_approval(need_approval, approval_person)
        self.log_step("选择是否需要审批")
        meeting_room_info_page.toggle_time_limit(need_time_limit, days, start_time, end_time, max_duration)
        self.log_step("选择是否需要时间限制")
        meeting_room_info_page.select_users(users)
        self.log_step("选择可使用者")
        meeting_room_info_page.click_submit_button()
        self.log_step("点击提交按钮")
        if is_positive is True:
            meeting_room_info_page.verify_success_message()
            self.log_step("验证新增成功")

        else:
            meeting_room_info_page.verify_error_miss_message()
            self.log_step("验证新增失败")


class TestQueryMeetingRoom(BaseCase):
    @pytest.mark.parametrize(
        "room, capacity, device, status, location, approval, departments, manager",
        [
            ("新增-成功", "10", "投影仪", "正常", "天王巷", "是", ["集成公司", "省DICT研发中心", "项目管理办公室"],
             "张超"),
            ("21231", "", "", "", "", "", "",
             ""),
            ("使用接口新建会议室", "12", "电视", "正常", "天王巷6楼", "全部", ["集成公司", "综合业务中心"],
             "龚存志"),
            # ("业务场景", "", "", "", "", "", "",
            #  ""),

        ]
    )
    def test_query_meeting_room(self, meeting_room_manage_page, db_connection, room, capacity, device, status, location,
                                approval,
                                departments, manager):
        # 输入查询条件
        meeting_room_manage_page.input_room(room)
        self.log_step("输入会议室编号/名称")
        meeting_room_manage_page.input_capacity(capacity)
        self.log_step("输入容纳人数")
        meeting_room_manage_page.choose_device(device)
        self.log_step("选择会议室设备")
        meeting_room_manage_page.choose_status(status)
        self.log_step("选择会议室状态")
        meeting_room_manage_page.input_location(location)
        self.log_step("输入会议室位置")
        meeting_room_manage_page.choose_approval(approval)
        self.log_step("选择是否需要审批")
        meeting_room_manage_page.choose_department(departments)
        self.log_step("选择会议室部门")
        meeting_room_manage_page.input_manager(manager)
        self.log_step("输入管理人")
        # 点击查询按钮
        meeting_room_manage_page.click_query_button()
        self.log_step("点击查询按钮")
        # 等待查询结果加载
        meeting_room_manage_page.page.wait_for_timeout(2000)  # 等待 2 秒
        self.log_step("等待查询结果加载")
        pages_data, pages_data_count = meeting_room_manage_page.get_table_data()
        self.log_step("获取表格数据")
        # pages_data = []

        # 从数据库中提取数据
        db_data = meeting_room_manage_page.get_db_data(db_connection, query="""
                SELECT * from user
                """)
        self.log_step("从数据库中提取数据")

        # 比较两个数据集
        assert meeting_room_manage_page.compare_data(pages_data, db_data,['Host', 'User', 'Select_priv']), "页面数据与数据库数据不一致"
        self.log_step("比较两个数据集")


class TestDeleteMeetingRoom(BaseCase):
    def test_delete_meeting_room(self, meeting_room_manage_page):
        count_pre = meeting_room_manage_page.get_table_rows().count()
        self.log_step("统计删除操作前表格行数")
        meeting_room_manage_page.click_delete_button()
        self.log_step("点击删除按钮,弹窗后点击确定按钮")
        count_after = meeting_room_manage_page.get_table_rows().count()
        self.log_step("统计删除成功操作后表格行数")
        meeting_room_manage_page.verify_delete_success_message(count_pre, count_after)
        self.log_step("验证删除成功")

    def test_delete_meeting_room_cancel(self, meeting_room_manage_page):
        # 点击删除按钮之前，表格中的行数
        count_pre = meeting_room_manage_page.get_table_rows().count()
        self.log_step("统计删除操作前表格行数")
        meeting_room_manage_page.click_delete_button_cancel()
        self.log_step("点击删除按钮，弹窗后点击取消按钮")
        # 点击删除按钮之后，表格中的行数
        count_after = meeting_room_manage_page.get_table_rows().count()
        self.log_step("统计删除取消操作后表格行数")
        meeting_room_manage_page.verify_delete_cancel_message(count_pre, count_after)
        self.log_step("验证删除取消")
