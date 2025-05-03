from pages.meeting_room_manage.meeting_room_info_page import MeetingRoomInfoPage
from pages.base_query_page import BaseQueryPage


class MeetingRoomManagePageBase(BaseQueryPage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page

    def get_add_button(self):
        return self.page.get_by_role("button", name="新建")

    def click_add_button(self):
        self.get_add_button().click()
        return MeetingRoomInfoPage(self.page)

    def get_room_input(self):
        return self.page.locator("//input[@placeholder='会议室编号/名称']")

    def input_room(self, room):
        if room is None:
            return
        self.get_room_input().fill(room)

    def get_capacity_input(self):
        return self.page.locator("//input[@placeholder='最少容纳人数']")

    def input_capacity(self, capacity):
        if capacity is None:
            return
        self.get_capacity_input().fill(capacity)

    def get_device_input(self):
        return self.page.locator("(//input[@placeholder='请选择'])[1]")

    def get_device_span(self, device):
        return self.page.locator(f"//span[text()='{device}']")

    def choose_device(self, device):
        if device is None:
            return
        if device == "":
            # 清空选择框
            self.get_device_input().evaluate("element => element.value = ''")
            return
        self.get_device_input().click()
        self.get_device_span(device).click()

    def get_status_input(self):
        return self.page.locator("(//input[@placeholder='请选择'])[2]")

    def get_status_span(self, status):
        # return self.page.get_by_role("menuitem", name=f"{status}")
        return self.page.locator(f"//li[contains(@class, 'el-select-dropdown__item')]/span[text()='{status}']")

    def choose_status(self, status):
        if status is None:
            return
        if status == "":
            # 清空选择框内容
            self.get_status_input().evaluate("element => element.value=''")
            return
        self.get_status_input().click()
        self.get_status_span(status).wait_for(state='visible')
        self.get_status_span(status).click()
        self.page.mouse.click(x=10, y=10)

    def get_location_input(self):
        return self.page.locator("//input[@placeholder='会议室所在位置']")

    def input_location(self, location):
        if location is None:
            return
        self.get_location_input().fill(location)

    def get_approval_input(self):
        return self.page.locator("(//input[@placeholder='请选择'])[3]")

    def get_approval_span(self, approval):
        return self.page.locator(f"//span[text()='{approval}']")

    def choose_approval(self, approval):
        if approval is None:
            return
        if approval == "":
            # 清空选择框内容
            self.get_approval_input().evaluate("element => element.value = ''")
            return
        self.get_approval_input().click()
        self.get_approval_span(approval).click()

    def get_department_input(self):
        return self.page.locator("(//input[@placeholder='请选择'])[4]")

    def get_department_label(self, department):
        return self.page.locator(f"//span[text()='{department}']/preceding-sibling::label")

    def choose_department(self, departments):
        if departments is None:
            return
        if departments == "":
            self.get_department_input().evaluate("element => element.value = ''")
            return
        self.get_department_input().click()
        for department in departments:
            self.get_department_label(department).click()
        self.page.mouse.click(x=10, y=10)

    def get_manager_input(self):
        return self.page.locator("//input[@placeholder='请输入姓名']")

    def input_manager(self, manager):
        if manager is None:
            return
        self.get_manager_input().fill(manager)

    def get_edit_button(self):
        # return self.page.get_by_role("button", name="编辑")
        # return self.page.locator("(//span[text()='编辑 '])[1]/..")

        return self.page.locator("//span[text()='编辑 ']").first

    def click_edit_button(self):
        # if self.get_edit_button().is_visible():
        #     print("-------------------------------------------------------")
        #     self.get_edit_button().click()
        # self.get_edit_button().click()
        # 这个元素直接点击无效，必须使用evaluate函数执行js代码来点击
        self.get_edit_button().evaluate("(element) => element.click()")
        return MeetingRoomInfoPage(self.page)

    def get_query_button(self):
        return self.page.locator("//span[text()=' 查询']")

    def click_query_button(self):
        self.get_query_button().click()

    def get_next_button(self):
        return self.page.locator("//button[@class='btn-next']")

    def click_next_button(self):
        self.get_next_button().click()

    def get_delete_button(self):
        return self.page.locator("//span[text()='删除 ']").first

    def click_delete_button(self):
        self.get_delete_button().evaluate("(element) => element.click()")
        self.page.get_by_role("button", name="确定").click()

    def click_delete_button_cancel(self):
        self.get_delete_button().evaluate("(element) => element.click()")
        self.page.get_by_role("button", name="取消").click()

    def verify_delete_success_message(self, count_pre, count_after):
        self.page.get_by_role("alert").get_by_text("删除成功").wait_for()
        assert self.page.get_by_role("alert").get_by_text("删除成功").is_visible() and count_pre - 1 == count_after

    def verify_delete_cancel_message(self, count_pre, count_after):
        # 等待“删除成功”消息消失
        delete_success_message = self.page.get_by_role("alert").get_by_text("删除成功")
        delete_success_message.wait_for(state='hidden', timeout=7000)
        assert not self.page.get_by_role("alert").get_by_text("删除成功").is_visible() and count_pre == count_after

    def get_table_rows(self):
        return self.page.locator("(//table[@class='el-table__body'])[1]/tbody/tr")


