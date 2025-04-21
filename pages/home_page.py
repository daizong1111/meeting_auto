from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self, page: Page):
        self.page = page


    def get_meeting_room_manage_icon(self):

        return self.page.locator("div:nth-child(8) > img")
        # return self.page.locator(r"//div[@class='application-content']/div[8]")

    def click_meeting_room_manage_icon(self):
        self.get_meeting_room_manage_icon().click()


    def get_meeting_room_manage_page(self):
        with self.page.expect_popup() as page1_info:
            self.click_meeting_room_manage_icon()
        page1 = page1_info.value
        return page1
