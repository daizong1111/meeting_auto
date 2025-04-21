# @Author  : 木森
# @weixin: python771

from playwright.sync_api import Page, expect


class UserSettingsPage:
    """用户设置页面"""

    def __init__(self, page: Page):
        self.page = page
        # 页面元素定位器
        self.settings_button = self.page.locator("//span[text()='去设置']")
        # 选择单选框学生
        self.student_radio = self.page.get_by_role('radio', name='学生')
        # 选择单选框教师
        self.teacher_radio = self.page.get_by_role('radio', name='老师')
        # 确认按钮
        self.save_button = self.page.get_by_role('button', name='确定')

    def goto(self):
        """打开用户设置页面"""
        self.page.goto("https://www.ketangpai.cn/#/main/UserSetting")

    def select_student(self):
        """选择学生角色"""
        self.student_radio.click()

    def select_teacher(self):
        """选择教师角色"""
        self.teacher_radio.click()

    def save_settings(self):
        """保存设置"""
        self.save_button.click()

    def click_settings_button(self):
        """点击去设置按钮"""
        self.settings_button.evaluate("el => el.click()")
