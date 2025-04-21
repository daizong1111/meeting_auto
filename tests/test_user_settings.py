from playwright.sync_api import Page
import allure
from pages.user_settings_page import UserSettingsPage
from base_case import BaseCase


class TestUserSettings(BaseCase):
    """用户设置页面测试类"""

    @allure.step("测试设置角色的功能")
    def test_edit_functionality(self, logged_in_page: Page):
        """测试编辑功能"""
        user_settings_page = UserSettingsPage(logged_in_page)
        self.log_step("导航到用户设置页面")
        user_settings_page.goto()
        self.log_step("点击点击角色编辑按钮")
        # 点击角色编辑按钮
        user_settings_page.click_settings_button()
        self.log_step("选择学生角色")
        user_settings_page.select_student()
        self.log_step("点击保存按钮")
        user_settings_page.save_settings()
        self.log_step("断言角色为学生")
        assert user_settings_page.student_radio.is_checked()
