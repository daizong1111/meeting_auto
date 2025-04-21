from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self, page: Page):
        self.page = page


    def get_meeting_room_manage_icon(self):

        return self.locator(r"//div[@class='application-content']/div[8]")

    def click_meeting_room_manage_icon(self):
        self.get_meeting_room_manage_icon().click()
        return self.page


    def get_meeting_room_manage_page(self):
        self.click_meeting_room_manage_icon()
        return self.page
