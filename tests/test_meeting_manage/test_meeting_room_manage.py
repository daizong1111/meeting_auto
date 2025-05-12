"""
此模块使用 Playwright 框架实现会议室管理模块的 UI 自动化测试，
包含增、删、改、查功能的测试用例。
"""
# import re

import logging
import random

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
        page.set_default_timeout(10000)  # 设置默认超时时间为 3000 毫秒
        page.locator("//ul[@role='menubar']/div[3]").click()
        page = MeetingRoomManagePageBase(page)
        yield page


@pytest.mark.usefixtures("meeting_room_manage_page")  # 显式声明夹具
class TestAddMeetingRoom(BaseCase):

    @pytest.mark.parametrize(
        "room_name, room_code, capacity, location, status, devices, departments, manager, description, need_approval, approval_person, need_time_limit, days, start_time, end_time, max_duration, users, is_positive",

        [
            ("新增-成功", "HYS10-506", "10", "天王巷", "正常", ["投影仪"],
             ["集成公司", "省DICT研发中心", "项目管理办公室"], "刘富豪/17356523872", "会议室很大，能容纳很多人", True,
             "刘富豪/17356523872", True,
             ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
             ["集成公司", "省DICT研发中心", "项目管理办公室", "刘富豪"], True),
            # ("新增-成功3", "HYS10-507", "20", "天王巷", "维修中", ["白板"],
            #  ["集成公司", "省DICT研发中心", "项目管理办公室"], "李四/19999999817", "会议室很大，能容纳很多人", True,
            #  "李四/19999999817", True,
            #  ["星期一"], "08:30", "10:30", "24",
            #  ["集成公司", "省DICT研发中心", "项目管理办公室", "刘富豪"], True),
            # ("新增-成功4", "HYS10-508", "30", "三孝口", "暂时关闭", ["无纸化设备"],
            #  ["集成公司", "省DICT研发中心", "技术架构团队"], "陈伟/18110988875", "会议室很大，能容纳很多人", True,
            #  "陈伟/18110988875", True,
            #  ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
            #  ["集成公司", "省DICT研发中心", "项目管理办公室", "刘富豪"], True),
            # ("新增-成功5", "HYS10-509", "40", "五里墩", "暂时关闭", ["视频"],
            #  ["集成公司", "省DICT研发中心", "综合业务中心"], "李韬/18105602573", "会议室很大，能容纳很多人", True,
            #  "李韬/18105602573", True,
            #  ["星期二"], "08:30", "10:30", "24",
            #  ["集成公司", "省DICT研发中心", "项目管理办公室", "刘富豪"], True),
            # ("新增-成功6", "HYS10-510", "50", "一里井", "暂时关闭", ["白板"],
            #  ["集成公司", "省DICT研发中心", "综合业务中心"], "李韬/18105602573", "会议室很大，能容纳很多人", True,
            #  "李韬/18105602573", True,
            #  ["星期二"], "08:30", "10:30", "24",
            #  ["集成公司", "省DICT研发中心", "项目管理办公室", "刘富豪"], True),
            # ("新增-成功7", "HYS10-511", "60", "二人巷", "正常", ["桌子"],
            #  ["集成公司", "省DICT研发中心", "综合业务中心"], "张杰/13162890525", "会议室很大，能容纳很多人", True,
            #  "张杰/13162890525", True,
            #  ["星期二"], "08:30", "10:30", "24",
            #  ["集成公司", "省DICT研发中心", "项目管理办公室", "刘富豪"], True),
            # ("新增-成功8", "HYS10-512", "70", "福禄园", "维修中", ["电视"],
            #  ["集成公司", "省DICT研发中心", "项目交付中心"], "李锋/18158870952", "会议室很大，能容纳很多人", True,
            #  "李锋/18158870952", True,
            #  ["星期二"], "08:30", "10:30", "24",
            #  ["集成公司", "省DICT研发中心", "项目管理办公室", "刘富豪"], True),
            # ("新增-成功9", "HYS10-513", "80", "长寿街", "暂时关闭", ["电视"],
            #  ["集成公司", "省DICT研发中心", "项目交付中心"], "李锋/18158870952", "会议室很大，能容纳很多人", True,
            #  "李锋/18158870952", True,
            #  ["星期二"], "08:30", "10:30", "24",
            #  ["集成公司", "省DICT研发中心", "项目管理办公室", "刘富豪"], True),
            # ("新增-成功10", "HYS10-514", "90", "诸葛庐", "正常", ["桌子"],
            #  ["集成公司", "省DICT研发中心", "项目交付中心"], "李锋/18158870952", "会议室很大，能容纳很多人", True,
            #  "李锋/18158870952", True,
            #  ["星期二"], "08:30", "10:30", "24",
            #  ["集成公司", "省DICT研发中心", "项目管理办公室", "刘富豪"], True),
            # 添加更多测试数据集
        ],
        # ids=["新增-成功"
        #
        #      ]
    )
    @allure.step("测试新增会议室-成功")
    def test_add_meeting_room_success(self, meeting_room_manage_page, db_connection, room_name: object, room_code: object, capacity: object,
                              location: object, status: object,
                              devices: object,
                              departments: object, manager: object, description: object, need_approval: object,
                              approval_person: object,
                              need_time_limit: object,
                              days: object,
                              start_time: object,
                              end_time: object, max_duration: object, users: object, is_positive: object):
        count_pre = meeting_room_manage_page.excute_query_count(db_connection)
        meeting_room_info_page = meeting_room_manage_page.click_add_button()
        self.log_step("点击新增按钮")
        meeting_room_info_page.fill_basic_info(room_name, room_code, capacity, location, status, devices, departments,
                                               manager, description)
        self.log_step("填写基本信息")
        meeting_room_info_page.fill_high_level_info(need_approval, approval_person, need_time_limit, days, start_time,
                                                    end_time, max_duration, users)
        self.log_step("填写高级信息")
        meeting_room_info_page.click_submit_button()
        self.log_step("点击提交按钮")
        meeting_room_info_page.page.wait_for_timeout(1000)
        # 重新连接数据库，并提交事务
        db_connection.ping(reconnect=True)
        db_connection.commit()  # 提交事务确保可见，必须加上这段代码，否则读取到的数据数仍然是新增之前的
        count_after = meeting_room_manage_page.excute_query_count(db_connection)
        meeting_room_info_page.verify_add_success_message(count_pre, count_after)
        self.log_step("验证新增成功")

    @pytest.mark.parametrize(
        "room_name, room_code, capacity, location, status, devices, departments, manager, description, need_approval, approval_person, need_time_limit, days, start_time, end_time, max_duration, users, is_positive",

        [
            ("", "HYS10-506", "10", "天王巷", "正常", ["投影仪"],
             ["集成公司", "省DICT研发中心", "项目管理办公室"], "刘富豪/17356523872", "会议室很大，能容纳很多人", True,
             "刘富豪/17356523872", True,
             ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
             ["集成公司", "省DICT研发中心", "项目管理办公室", "刘富豪"], False),
            ("新增-失败-必填项为空-容纳人数", "HYS10-506", "", "天王巷", "正常", ["投影仪"],
             ["集成公司", "省DICT研发中心", "项目管理办公室"], "刘富豪/17356523872", "会议室很大，能容纳很多人", True,
             "刘富豪/17356523872", True,
             ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
             ["集成公司", "省DICT研发中心", "项目管理办公室", "刘富豪"], False),
            ("新增-失败-必填项为空-会议室位置", "HYS10-506", "10", "", "正常", ["投影仪"],
             ["集成公司", "省DICT研发中心", "项目管理办公室"], "刘富豪/17356523872", "会议室很大，能容纳很多人", True,
             "刘富豪/17356523872", True,
             ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
             ["集成公司", "省DICT研发中心", "项目管理办公室", "刘富豪"], False),
            ("新增-失败-必填项为空-会议室状态", "HYS10-506", "10", "天王巷", "", ["投影仪"],
             ["集成公司", "省DICT研发中心", "项目管理办公室"], "刘富豪/17356523872", "会议室很大，能容纳很多人", True,
             "刘富豪/17356523872", True,
             ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
             ["集成公司", "省DICT研发中心", "项目管理办公室", "刘富豪"], False),
            ("新增-失败-必填项为空-会议室设备", "HYS10-506", "10", "天王巷", "正常", "",
             ["集成公司", "省DICT研发中心", "项目管理办公室"], "刘富豪/17356523872", "会议室很大，能容纳很多人", True,
             "刘富豪/17356523872", True,
             ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
             ["集成公司", "省DICT研发中心", "项目管理办公室", "刘富豪"], False),
            ("新增-失败-必填项为空-管理部门和管理人和审批人", "HYS10-506", "10", "天王巷", "正常", ["投影仪"],
             "", "", "会议室很大，能容纳很多人", True, "", True,
             ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
             ["集成公司", "省DICT研发中心", "项目管理办公室", "刘富豪"], False),
            ("新增-失败-必填项为空-管理人", "HYS10-506", "10", "天王巷", "正常", ["投影仪"],
             ["集成公司", "省DICT研发中心", "项目管理办公室"], "", "会议室很大，能容纳很多人", True,
             "刘富豪/17356523872", True,
             ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
             ["集成公司", "省DICT研发中心", "项目管理办公室", "刘富豪"], False),
            ("新增-失败-必填项为空-审批人", "HYS10-506", "10", "天王巷", "正常", ["投影仪"],
             ["集成公司", "省DICT研发中心", "项目管理办公室"], "刘富豪/17356523872", "会议室很大，能容纳很多人", True,
             "", True,
             ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
             ["集成公司", "省DICT研发中心", "项目管理办公室", "刘富豪"], False),
            ("新增-失败-必填项为空-可预约的时间范围", "HYS10-506", "10", "天王巷", "正常", ["投影仪"],
             ["集成公司", "省DICT研发中心", "项目管理办公室"], "刘富豪/17356523872", "会议室很大，能容纳很多人", True,
             "刘富豪/17356523872", True,
             "", "08:30", "10:30", "24",
             ["集成公司", "省DICT研发中心", "项目管理办公室", "刘富豪"], False),
            ("新增-失败-必填项为空-单次可预约最长时间", "HYS10-506", "10", "天王巷", "正常", ["投影仪"],
             ["集成公司", "省DICT研发中心", "项目管理办公室"], "刘富豪/17356523872", "会议室很大，能容纳很多人", True,
             "刘富豪/17356523872", True,
             ["星期一", "星期二", "星期三"], "08:30", "10:30", "",
             ["集成公司", "省DICT研发中心", "项目管理办公室", "刘富豪"], False)

            # 添加更多测试数据集
        ],
        # ids=[
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
    @allure.step("测试新增会议室-失败-必填项缺失")
    def test_add_meeting_room_miss_data(self, meeting_room_manage_page, db_connection, room_name: object, room_code: object,
                              capacity: object,
                              location: object, status: object,
                              devices: object,
                              departments: object, manager: object, description: object, need_approval: object,
                              approval_person: object,
                              need_time_limit: object,
                              days: object,
                              start_time: object,
                              end_time: object, max_duration: object, users: object, is_positive: object):
        count_pre = meeting_room_manage_page.excute_query_count(db_connection)
        meeting_room_info_page = meeting_room_manage_page.click_add_button()
        self.log_step("点击新增按钮")
        meeting_room_info_page.fill_basic_info(room_name, room_code, capacity, location, status, devices, departments,
                                               manager, description)
        self.log_step("填写基本信息")
        meeting_room_info_page.fill_high_level_info(need_approval, approval_person, need_time_limit, days, start_time,
                                                    end_time, max_duration, users)
        self.log_step("填写高级信息")
        meeting_room_info_page.click_submit_button()
        self.log_step("点击提交按钮")
        meeting_room_info_page.page.wait_for_timeout(1000)
        # 重新连接数据库，并提交事务
        db_connection.ping(reconnect=True)
        db_connection.commit()  # 提交事务确保可见，必须加上这段代码，否则读取到的数据数仍然是新增之前的
        count_after = meeting_room_manage_page.excute_query_count(db_connection)
        meeting_room_info_page.verify_error_add_miss_message(count_pre, count_after)
        self.log_step("验证新增失败-必填项缺失")

    @allure.step("测试新增会议室-前端格式校验与数据合法性")
    def test_add_meeting_room_frontend_validation(
            self, meeting_room_manage_page, db_connection,
    ):

        meeting_room_info_page = meeting_room_manage_page.click_add_button()
        self.log_step("点击新增按钮")

        meeting_room_info_page.fill_room_name_by_press("新增会议室名称过长示例" * 2)
        self.log_step("填写会议室名称")
        meeting_room_name = meeting_room_info_page.get_room_name()
        assert len(meeting_room_name) <= 10
        self.log_step("校验会议室名称长度小于等于10")

        meeting_room_info_page.fill_room_code_by_press("HYS10-506" * 4)
        self.log_step("填写会议室编号")
        meeting_room_code = meeting_room_info_page.get_room_code()
        assert len(meeting_room_code) <= 30

        meeting_room_info_page.fill_capacity_by_press("1001")
        self.log_step("填写会议室容量")
        assert meeting_room_info_page.get_capacity() == "1000"
        self.log_step("校验会议室容量小于等于1000")

        meeting_room_info_page.fill_capacity_by_press("3.4")
        self.log_step("填写会议室容量")
        assert meeting_room_info_page.get_capacity() == "34"
        self.log_step("校验会议室容量无法输入小数")

        meeting_room_info_page.fill_capacity_by_press("3/4")
        self.log_step("填写会议室容量")
        assert meeting_room_info_page.get_capacity() == "34"
        self.log_step("校验会议室容量无法输入分数")

        meeting_room_info_page.fill_capacity_by_press("-1")
        self.log_step("填写会议室容量")
        assert meeting_room_info_page.get_capacity() == "1"
        self.log_step("校验会议室容量无法输入负数")

        meeting_room_info_page.fill_capacity_by_press("abc")
        self.log_step("填写会议室容量")
        assert meeting_room_info_page.get_capacity() == ""
        self.log_step("校验会议室容量无法输入字母")

        meeting_room_info_page.fill_capacity_by_press("￥￥￥￥￥")
        self.log_step("填写会议室容量")
        assert meeting_room_info_page.get_capacity() == ""
        self.log_step("校验会议室容量无法输入特殊字符")

        meeting_room_info_page.fill_capacity_by_press("中文")
        self.log_step("填写会议室容量")
        assert meeting_room_info_page.get_capacity() == ""
        self.log_step("校验会议室容量无法输入中文")

        meeting_room_info_page.fill_location_by_press("天王巷" * 15)
        self.log_step("填写会议室位置")
        assert len(meeting_room_info_page.get_location()) <= 40
        self.log_step("校验会议室位置长度小于等于40")

        meeting_room_info_page.toggle_time_limit(True, None, None, None, "25")
        self.log_step("填写可预约最长时间")
        assert meeting_room_info_page.get_max_duration() == "24"
        self.log_step("校验可预约最长时间小于等于24")

        meeting_room_info_page.fill_max_duration_by_press("3/4")
        self.log_step("填写可预约最长时间")
        assert meeting_room_info_page.get_max_duration() == "24"
        self.log_step("校验可预约最长时间无法输入分数")

        meeting_room_info_page.fill_max_duration_by_press("-1")
        self.log_step("填写可预约最长时间")
        assert meeting_room_info_page.get_max_duration() == "1"
        self.log_step("校验可预约最长时间无法输入负数")

        meeting_room_info_page.fill_max_duration_by_press("abc")
        self.log_step("填写可预约最长时间")
        assert meeting_room_info_page.get_max_duration() == ""
        self.log_step("校验可预约最长时间无法输入字母")

        meeting_room_info_page.fill_max_duration_by_press("$$$$")
        self.log_step("填写可预约最长时间")
        assert meeting_room_info_page.get_max_duration() == ""
        self.log_step("校验可预约最长时间无法输入特殊字符")

        meeting_room_info_page.fill_max_duration_by_press("中文")
        self.log_step("填写可预约最长时间")
        assert meeting_room_info_page.get_max_duration() == ""
        self.log_step("校验可预约最长时间无法输入中文")




@pytest.mark.usefixtures("meeting_room_manage_page")  # 显式声明夹具
class TestEditMeetingRoom(BaseCase):
    @pytest.mark.parametrize(
        "room_name, room_code, capacity, location, status, devices, departments, manager, description, need_approval, approval_person, need_time_limit, days, start_time, end_time, max_duration, users, is_positive",

        [
            ("修改-成功", "HYS10-506", "10", "天王巷", "正常", ["投影仪"],
             ["集成公司", "省DICT研发中心", "项目管理办公室"], "刘富豪/17356523872", "会议室很大，能容纳很多人", True,
             "刘富豪/17356523872", True,
             ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
             ["集成公司", "省DICT研发中心", "项目管理办公室", "刘富豪"], True),
            # 添加更多测试数据集
        ],
        # ids=["修改-成功"]
    )
    @allure.step("测试修改会议室")
    def test_edit_meeting_room_success(self, meeting_room_manage_edit_and_del_pre,db_connection, room_name, room_code, capacity, location, status,
                               devices,
                               departments, manager, description, need_approval, approval_person, need_time_limit, days,
                               start_time,
                               end_time, max_duration, users, is_positive):
        # 对于正向用例，生成一段随机数字，6位的，插入到会议室名称和编号的尾部
        random_code = str(random.randint(10000, 99999))
        room_name = room_name + random_code
        room_code = room_code + random_code
        meeting_room_info_page = meeting_room_manage_edit_and_del_pre.click_edit_button()
        self.log_step("点击编辑按钮")
        meeting_room_info_page.fill_basic_info(room_name, room_code, capacity, location, status, devices, departments, manager, description)
        self.log_step("填写基本信息")
        meeting_room_info_page.fill_high_level_info(need_approval, approval_person, need_time_limit, days, start_time, end_time, max_duration, users)
        self.log_step("填写高级信息")
        meeting_room_info_page.click_submit_button()
        self.log_step("点击提交按钮")
        meeting_room_manage_edit_and_del_pre.page.wait_for_timeout(1000)
        # 重新连接数据库，并提交事务
        db_connection.ping(reconnect=True)
        db_connection.commit()  # 提交事务确保可见，必须加上这段代码，否则读取到的数据数仍然是修改之前的
        # 执行sql查询，断言一定能查到修改后的数据
        db_data = meeting_room_manage_edit_and_del_pre.get_db_data(db_connection,
                                                                  "SELECT count(*) as count FROM meeting_room WHERE name = %(room_name)s and number = %(room_code)s and del_flag = 0",
                                                                   {"room_name":room_name, "room_code":room_code})
        count = db_data[0]["count"]
        meeting_room_info_page.verify_edit_success_message(count)
        self.log_step("验证修改成功")


    @pytest.mark.parametrize(
        "room_name, room_code, capacity, location, status, devices, departments, manager, description, need_approval, approval_person, need_time_limit, days, start_time, end_time, max_duration, users, is_positive",

        [
            ("", "HYS10-506", "10", "天王巷", "正常", ["投影仪"],
             ["集成公司", "省DICT研发中心", "项目管理办公室"], "刘富豪/17356523872", "会议室很大，能容纳很多人", True,
             "刘富豪/17356523872", True,
             ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
             ["集成公司", "省DICT研发中心", "项目管理办公室", "刘富豪"], False),
            ("编辑-失败-必填项为空-容纳人数", "HYS10-506", "", "天王巷", "正常", ["投影仪"],
             ["集成公司", "省DICT研发中心", "项目管理办公室"], "刘富豪/17356523872", "会议室很大，能容纳很多人", True,
             "刘富豪/17356523872", True,
             ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
             ["集成公司", "省DICT研发中心", "项目管理办公室", "刘富豪"], False),
            ("编辑-失败-必填项为空-会议室位置", "HYS10-506", "10", "", "正常", ["投影仪"],
             ["集成公司", "省DICT研发中心", "项目管理办公室"], "刘富豪/17356523872", "会议室很大，能容纳很多人", True,
             "刘富豪/17356523872", True,
             ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
             ["集成公司", "省DICT研发中心", "项目管理办公室", "刘富豪"], False),
            ("编辑-失败-必填项为空-会议室状态", "HYS10-506", "10", "天王巷", "", ["投影仪"],
             ["集成公司", "省DICT研发中心", "项目管理办公室"], "刘富豪/17356523872", "会议室很大，能容纳很多人", True,
             "刘富豪/17356523872", True,
             ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
             ["集成公司", "省DICT研发中心", "项目管理办公室", "刘富豪"], False),
            ("编辑-失败-必填项为空-会议室设备", "HYS10-506", "10", "天王巷", "正常", "",
             ["集成公司", "省DICT研发中心", "项目管理办公室"], "刘富豪/17356523872", "会议室很大，能容纳很多人", True,
             "刘富豪/17356523872", True,
             ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
             ["集成公司", "省DICT研发中心", "项目管理办公室", "刘富豪"], False),
            ("编辑-失败-必填项为空-管理部门和管理人和审批人", "HYS10-506", "10", "天王巷", "正常", ["投影仪"],
             "", "", "会议室很大，能容纳很多人", True, "", True,
             ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
             ["集成公司", "省DICT研发中心", "项目管理办公室", "刘富豪"], False),
            ("编辑-失败-必填项为空-管理人", "HYS10-506", "10", "天王巷", "正常", ["投影仪"],
             ["集成公司", "省DICT研发中心", "项目管理办公室"], "", "会议室很大，能容纳很多人", True,
             "刘富豪/17356523872", True,
             ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
             ["集成公司", "省DICT研发中心", "项目管理办公室", "刘富豪"], False),
            ("编辑-失败-必填项为空-审批人", "HYS10-506", "10", "天王巷", "正常", ["投影仪"],
             ["集成公司", "省DICT研发中心", "项目管理办公室"], "刘富豪/17356523872", "会议室很大，能容纳很多人", True,
             "", True,
             ["星期一", "星期二", "星期三"], "08:30", "10:30", "24",
             ["集成公司", "省DICT研发中心", "项目管理办公室", "刘富豪"], False),
            ("编辑-失败-必填项为空-可预约的时间范围", "HYS10-506", "10", "天王巷", "正常", ["投影仪"],
             ["集成公司", "省DICT研发中心", "项目管理办公室"], "刘富豪/17356523872", "会议室很大，能容纳很多人", True,
             "刘富豪/17356523872", True,
             "", "08:30", "10:30", "24",
             ["集成公司", "省DICT研发中心", "项目管理办公室", "刘富豪"], False),
            ("编辑-失败-必填项为空-单次可预约最长时间", "HYS10-506", "10", "天王巷", "正常", ["投影仪"],
             ["集成公司", "省DICT研发中心", "项目管理办公室"], "刘富豪/17356523872", "会议室很大，能容纳很多人", True,
             "刘富豪/17356523872", True,
             ["星期一", "星期二", "星期三"], "08:30", "10:30", "",
             ["集成公司", "省DICT研发中心", "项目管理办公室", "刘富豪"], False),
            # 添加更多测试数据集
        ],
        # ids=[
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
    @allure.step("测试修改会议室-必填项缺失")
    def test_edit_meeting_room_miss_data(self, meeting_room_manage_edit_and_del_pre, db_connection, room_name, room_code,
                               capacity, location, status,
                               devices,
                               departments, manager, description, need_approval, approval_person, need_time_limit, days,
                               start_time,
                               end_time, max_duration, users, is_positive):
        meeting_room_info_page = meeting_room_manage_edit_and_del_pre.click_edit_button()
        self.log_step("点击编辑按钮")
        meeting_room_info_page.fill_basic_info(room_name, room_code, capacity, location, status, devices, departments, manager, description)
        self.log_step("填写基本信息")
        meeting_room_info_page.fill_high_level_info(need_approval, approval_person, need_time_limit, days, start_time, end_time, max_duration, users)
        self.log_step("填写高级信息")
        meeting_room_info_page.click_submit_button()
        self.log_step("点击提交按钮")
        meeting_room_info_page.verify_error_edit_miss_message()
        self.log_step("验证修改失败-必填项缺失")

    @allure.step("测试修改会议室-前端格式校验与数据合法性")
    def test_edit_meeting_room_frontend_validation(
            self, meeting_room_manage_edit_and_del_pre, db_connection,
    ):

        meeting_room_info_page = meeting_room_manage_edit_and_del_pre.click_edit_button()
        self.log_step("点击编辑按钮")

        meeting_room_info_page.fill_room_name_by_press("新增会议室名称过长示例" * 2)
        self.log_step("填写会议室名称")
        meeting_room_name = meeting_room_info_page.get_room_name()
        assert len(meeting_room_name) <= 10
        self.log_step("校验会议室名称长度小于等于10")

        meeting_room_info_page.fill_room_code_by_press("HYS10-506" * 4)
        self.log_step("填写会议室编号")
        meeting_room_code = meeting_room_info_page.get_room_code()
        assert len(meeting_room_code) <= 30

        meeting_room_info_page.fill_capacity_by_press("1001")
        self.log_step("填写会议室容量")
        assert meeting_room_info_page.get_capacity() == "1000"
        self.log_step("校验会议室容量小于等于1000")

        meeting_room_info_page.fill_capacity_by_press("3.4")
        self.log_step("填写会议室容量")
        assert meeting_room_info_page.get_capacity() == "34"
        self.log_step("校验会议室容量无法输入小数")

        meeting_room_info_page.fill_capacity_by_press("3/4")
        self.log_step("填写会议室容量")
        assert meeting_room_info_page.get_capacity() == "34"
        self.log_step("校验会议室容量无法输入分数")

        meeting_room_info_page.fill_capacity_by_press("-1")
        self.log_step("填写会议室容量")
        assert meeting_room_info_page.get_capacity() == "1"
        self.log_step("校验会议室容量无法输入负数")

        meeting_room_info_page.fill_capacity_by_press("abc")
        self.log_step("填写会议室容量")
        assert meeting_room_info_page.get_capacity() == ""
        self.log_step("校验会议室容量无法输入字母")

        meeting_room_info_page.fill_capacity_by_press("￥￥￥￥￥")
        self.log_step("填写会议室容量")
        assert meeting_room_info_page.get_capacity() == ""
        self.log_step("校验会议室容量无法输入特殊字符")

        meeting_room_info_page.fill_capacity_by_press("中文")
        self.log_step("填写会议室容量")
        assert meeting_room_info_page.get_capacity() == ""
        self.log_step("校验会议室容量无法输入中文")

        meeting_room_info_page.fill_location_by_press("天王巷" * 15)
        self.log_step("填写会议室位置")
        assert len(meeting_room_info_page.get_location()) <= 40
        self.log_step("校验会议室位置长度小于等于40")

        meeting_room_info_page.toggle_time_limit(True, None, None, None, "25")
        self.log_step("填写可预约最长时间")
        assert meeting_room_info_page.get_max_duration() == "24"
        self.log_step("校验可预约最长时间小于等于24")

        meeting_room_info_page.fill_max_duration_by_press("3/4")
        self.log_step("填写可预约最长时间")
        assert meeting_room_info_page.get_max_duration() == "24"
        self.log_step("校验可预约最长时间无法输入分数")

        meeting_room_info_page.fill_max_duration_by_press("-1")
        self.log_step("填写可预约最长时间")
        assert meeting_room_info_page.get_max_duration() == "1"
        self.log_step("校验可预约最长时间无法输入负数")

        meeting_room_info_page.fill_max_duration_by_press("abc")
        self.log_step("填写可预约最长时间")
        assert meeting_room_info_page.get_max_duration() == ""
        self.log_step("校验可预约最长时间无法输入字母")

        meeting_room_info_page.fill_max_duration_by_press("$$$$")
        self.log_step("填写可预约最长时间")
        assert meeting_room_info_page.get_max_duration() == ""
        self.log_step("校验可预约最长时间无法输入特殊字符")

        meeting_room_info_page.fill_max_duration_by_press("中文")
        self.log_step("填写可预约最长时间")
        assert meeting_room_info_page.get_max_duration() == ""
        self.log_step("校验可预约最长时间无法输入中文")


def get_department_ids(db_connection, department_names):
    """
    根据部门名称列表获取对应的部门 ID 列表。
    """
    if not department_names or not isinstance(department_names, list):
        return []

    # 构造参数化 SQL 查询
    placeholders = "%s"
    sql = f"""
        SELECT dept_id 
        FROM sys_dept 
        WHERE dept_name IN ({placeholders}) AND status = '0' AND del_flag = '0'
    """

    # 使用参数化查询防止 SQL 注入
    results = db_connection.execute_query(sql, params=department_names[-1])
    dept_ids = [row["dept_id"] for row in results]
    return dept_ids


def build_meeting_room_sql(room=None, capacity=None, device=None, status=None,
                           location=None, approval=None, dept_ids=None, manager=None):
    """
    根据给定参数动态生成会议室查询 SQL。
    """
    sql = """
            SELECT mr.id, mr.name, mr.number, mr.capacity, mr.facility, mr.state, 
                   sdd.dict_label AS stateName, mr.enable_approve, mr.location, 
                   sd.dept_id AS managementId, sd.dept_name AS managementName, 
                   su1.phonenumber AS managerPhone, su1.nick_name AS managerName, 
                   su2.phonenumber AS operatorPhone, su2.nick_name AS operatorName, 
                   mr.update_time AS operate_time
            FROM (SELECT * FROM meeting_room WHERE del_flag=0
            
        """

    conditions = []
    params = {}

    if room:
        conditions.append("AND (name LIKE %(room)s OR number LIKE %(room)s)")
        params["room"] = f"%{room}%"

    if capacity is not None and capacity.strip():
        conditions.append("AND capacity >= %(capacity)s")
        params["capacity"] = capacity

    if device:
        conditions.append("AND facility LIKE %(device)s")
        params["device"] = f"%{device}%"

    if status:
        if status == "全部":
            pass
        if status == "正常":
            conditions.append("AND state = 0")
        if status == "维修中":
            conditions.append("AND state = 1")
        if status == "暂时关闭":
            conditions.append("AND state = 2")

    if location:
        conditions.append("AND location LIKE %(location)s")
        params["location"] = f"%{location}%"

    if approval:
        # 假设 "是" 表示启用审批，即 enable_approve = 1；"否" 为 0；"全部" 不加条件
        if approval == "是":
            conditions.append("AND enable_approve = 1")
        elif approval == "否":
            conditions.append("AND enable_approve = 0")

    if dept_ids != "" and dept_ids != [] and isinstance(dept_ids, list):
        placeholders = ','.join(str(int(dept_id)) for dept_id in dept_ids)
        conditions.append(f"AND management IN ({placeholders})")

    sql += " " + " ".join(conditions)
    sql += ') as mr '
    sql += """LEFT JOIN (SELECT * FROM sys_dept WHERE status='0' AND del_flag='0') as sd ON mr.management=sd.dept_id
            LEFT JOIN (SELECT * FROM sys_user WHERE status='0' AND del_flag='0') as su1 ON mr.manager=su1.user_id
            LEFT JOIN (SELECT * FROM sys_user WHERE status='0' AND del_flag='0') as su2 ON mr.update_by=su2.user_name
            LEFT JOIN (SELECT * FROM sys_dict_data WHERE status='0' AND dict_type='meeting_room_state') as sdd ON mr.state=sdd.dict_value
            """
    sql += """ WHERE 1=1 """

    if manager:
        params["manager"] = f"%{manager}%"
        sql +="""AND su1.nick_name LIKE %(manager)s"""

    sql += " ORDER BY mr.create_time DESC;"

    return sql, params


class TestQueryMeetingRoom(BaseCase):

    @pytest.mark.parametrize(
        "room, capacity, device, status, location, approval, departments, manager",
        [
            ("新增-成功", "", "", "", "", "", "",
             ""),
            ("", "50", "", "", "", "", "",
             ""),
            ("", "", "电视", "", "", "", "",
             ""),
            ("", "", "", "维修中", "", "", "",
             ""),
            ("", "", "", "", "天王巷", "", "",
             ""),
            ("", "", "", "", "", "否", "",
             ""),
            ("", "", "", "", "", "", ["集成公司", "省DICT研发中心", "项目管理办公室"],
             ""),
            ("", "", "", "", "", "", "",
             "张杰"),
            ("新增-成功", "60", "白板", "正常", "天王巷", "全部", ["集成公司", "省DICT研发中心", "产品需求团队"],
             "刘汪汉"),
        ]
    )
    def test_query_meeting_room(self, meeting_room_manage_query, db_connection, room, capacity, device, status, location,
                                approval,
                                departments, manager):
        # 输入查询条件
        meeting_room_manage_query.input_room(room)
        self.log_step("输入会议室编号/名称")
        meeting_room_manage_query.input_capacity(capacity)
        self.log_step("输入容纳人数")
        meeting_room_manage_query.choose_device(device)
        self.log_step("选择会议室设备")
        meeting_room_manage_query.choose_status(status)
        self.log_step("选择会议室状态")
        meeting_room_manage_query.input_location(location)
        self.log_step("输入会议室位置")
        meeting_room_manage_query.choose_approval(approval)
        self.log_step("选择是否需要审批")
        meeting_room_manage_query.choose_department(departments)
        self.log_step("选择会议室部门")
        meeting_room_manage_query.input_manager(manager)
        self.log_step("输入管理人")
        # 点击查询按钮
        meeting_room_manage_query.click_query_button()
        self.log_step("点击查询按钮")
        # 等待查询结果加载
        meeting_room_manage_query.page.wait_for_timeout(2000)  # 等待 2 秒
        self.log_step("等待查询结果加载")
        pages_data, pages_data_count = meeting_room_manage_query.get_table_data()
        self.log_step("获取表格数据")

        # 获取部门 ID 列表
        if departments and departments != "" and isinstance(departments, list):
            # 构造参数化 SQL 查询
            sql = "SELECT dept_id FROM sys_dept WHERE dept_name = %(dept_name)s AND status = '0' AND del_flag = '0'"
            # params = {"dept_name": "集成公司"}
            db_data_dept_ids = meeting_room_manage_query.get_db_data(db_connection, query=sql,
                                                                    params={"dept_name": departments[-1]})
            dept_ids = [row["dept_id"] for row in db_data_dept_ids]
        else:
            dept_ids = []

        # 构建 SQL 查询
        sql, params = build_meeting_room_sql(room=room, capacity=capacity, device=device, status=status,
                                             location=location, approval=approval, dept_ids=dept_ids,
                                             manager=manager)

        db_data = meeting_room_manage_query.get_db_data(db_connection, query=sql, params=params)
        self.log_step("从数据库中提取数据")

        # 比较两个数据集
        assert meeting_room_manage_query.compare_data(pages_data, db_data,
                                                     ['name', 'number', 'capacity', 'facility', 'stateName', 'enable_approve','location', 'managementName', 'managerName','operatorName','operate_time']), "页面数据与数据库数据不一致"
        self.log_step("比较两个数据集")


class TestDeleteMeetingRoom(BaseCase):
    def test_delete_meeting_room(self, meeting_room_manage_edit_and_del_pre, db_connection):
        db_data_pre = meeting_room_manage_edit_and_del_pre.get_db_data(
            db_connection,
            query="SELECT count(*) as count FROM meeting_room WHERE del_flag = '1'",
        )
        db_count_pre = db_data_pre[0]["count"]
        _, count_pre = meeting_room_manage_edit_and_del_pre.get_table_data()
        self.log_step("统计删除操作前表格行数")
        meeting_room_manage_edit_and_del_pre.click_delete_button()
        self.log_step("点击删除按钮,弹窗后点击确定按钮")
        meeting_room_manage_edit_and_del_pre.verify_delete_success_message()
        self.log_step("验证页面出现删除成功字样")
        meeting_room_manage_edit_and_del_pre.page.wait_for_timeout(1000)
        _, count_after = meeting_room_manage_edit_and_del_pre.get_table_data()
        self.log_step("统计删除成功操作后表格行数")
        assert count_after == count_pre - 1, "表格中的行数未减少"
        # 验证数据库中的数据是否已删除（或标记为已删除）
        db_connection.ping(reconnect=True)  # 确保数据库连接有效
        db_connection.commit()
        db_data_after = meeting_room_manage_edit_and_del_pre.get_db_data(
            db_connection,
            query="SELECT count(*) as count FROM meeting_room WHERE del_flag = '1'",
        )
        db_count_after = db_data_after[0]["count"]
        assert db_count_after == db_count_pre + 1, "数据库中的数据未删除"
        self.log_step("验证数据库中的数据是否已删除")

    def test_delete_meeting_room_cancel(self, meeting_room_manage_edit_and_del_pre, db_connection):
        db_data_pre = meeting_room_manage_edit_and_del_pre.get_db_data(
            db_connection,
            query="SELECT count(*) as count FROM meeting_room WHERE del_flag = '1'",
        )
        db_count_pre = db_data_pre[0]["count"]
        # 点击删除按钮之前，表格中的行数
        _, count_pre = meeting_room_manage_edit_and_del_pre.get_table_data()
        self.log_step("统计删除操作前表格行数")
        meeting_room_manage_edit_and_del_pre.click_delete_button_cancel()
        self.log_step("点击删除按钮，弹窗后点击取消按钮")
        # 点击删除按钮之后，表格中的行数
        _, count_after = meeting_room_manage_edit_and_del_pre.get_table_data()
        self.log_step("统计删除取消操作后表格行数")
        meeting_room_manage_edit_and_del_pre.verify_delete_cancel_message(count_pre, count_after)
        self.log_step("验证删除取消")
        meeting_room_manage_edit_and_del_pre.page.wait_for_timeout(1000)
        # 验证数据库中的数据是否已删除（或标记为已删除）
        db_connection.ping(reconnect=True)  # 确保数据库连接有效
        db_connection.commit()
        db_data_after = meeting_room_manage_edit_and_del_pre.get_db_data(
            db_connection,
            query="SELECT count(*) as count FROM meeting_room WHERE del_flag = '1'",
        )
        db_count_after = db_data_after[0]["count"]
        assert db_count_after == db_count_pre, "数据库中的数据被误删除"
