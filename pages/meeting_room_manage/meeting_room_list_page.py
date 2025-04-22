from pages.meeting_room_manage.meeting_room_info_page import MeetingRoomInfoPage

class MeetingRoomManagePage:
    def __init__(self, page):
        self.page = page

    def get_add_button(self):
        return self.page.get_by_role("button", name="新建")

    def click_add_button(self):
        self.get_add_button().click()
        return MeetingRoomInfoPage(self.page)
