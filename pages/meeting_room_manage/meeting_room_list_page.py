# 前置步骤函数，导航到会议室管理页面
from pages.meeting_room_manage.meeting_room_info_page import MeetingRoomInfoPage

def setup_meeting_room_page(page):
    page.locator("//span[text()='会议室管理']").click()
    # logging.info("登录并导航到会议室管理页面")
    return page

class MeetingRoomListPage:
    def __init__(self, page):
        self.page = page

    def get_add_button(self):
        return self.page.get_by_role("button", name="新建")

    def click_add_button(self):
        self.get_add_button().click()
        # logging.info("点击了添加会议室按钮")
        return MeetingRoomInfoPage(self.page)
