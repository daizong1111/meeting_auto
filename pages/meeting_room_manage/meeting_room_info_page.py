class MeetingRoomInfoPage:
    def __init__(self, page):
        self.page = page

    def click_add_meeting_room_button(self):
        self.page.get_by_role("button", name="新建").click()
        # logging.info("点击了添加会议室按钮")

    def fill_room_name(self, room_name):
        self.page.get_by_placeholder('不超过10个字').fill(room_name)
        # logging.info(f"输入了会议室信息: {room_name}")

    def fill_room_code(self, room_code):
        self.page.get_by_placeholder("请输入,如HYS10-506").fill(room_code)
        # logging.info(f"输入了会议室编号: {room_code}")

    def fill_capacity(self, capacity):
        self.page.get_by_role("spinbutton").first.fill(capacity)
        # logging.info(f"输入了会议室容量: {capacity}")

    def fill_location(self, location):
        self.page.get_by_placeholder("不超过30个字").first.fill(location)
        # logging.info(f"输入了会议室位置: {location}")

    def select_room_status(self, status):
        self.page.get_by_placeholder("请选择").first.click()
        room_status_li = self.page.locator("li").filter(has_text=status)
        room_status_li.wait_for(state="visible")
        room_status_li.click()
        # logging.info(f"选择了会议室状态: {status}")

    def select_devices(self, devices):
        for device in devices:
            self.page.get_by_text(device).click()
            # logging.info(f"选择了设备: {device}")

    def select_departments(self, departments):
        self.page.get_by_placeholder("请选择").nth(1).click()
        for department in departments:
            org_item = self.page.get_by_role("menuitem", name=department).get_by_role("radio")
            org_item.click()
        self.page.mouse.click(x=10, y=10)  # 点击空白处
        # logging.info(f"选择了管理部门: {', '.join(departments)}")

    def select_manager(self, manager):
        self.page.get_by_placeholder("请选择").nth(2).click()
        manager_item = self.page.get_by_role("menuitem", name=manager)
        manager_item.click()
        self.page.mouse.click(x=10, y=10)  # 点击空白处
        # logging.info(f"选择了管理人: {manager}")

    def fill_description(self, description):
        self.page.get_by_role("textbox", name="请输入", exact=True).fill(description)
        # logging.info(f"输入了相关描述: {description}")

    def toggle_approval(self, need_approval, approval_person):
        if need_approval:
            self.page.locator("(//div[@role='switch'])[1]").click()
            self.page.get_by_placeholder("请选择").nth(3).click()
            approval_item = self.page.get_by_role("menuitem", name=approval_person).nth(1)
            approval_item.click()
            self.page.mouse.click(x=10, y=10)  # 点击空白处
            # logging.info(f"打开了审批开关，并选择了审批人: {approval_person}")

    def toggle_time_limit(self, need_time_limit, start_time, end_time, max_duration):
        if need_time_limit:
            self.page.locator("(//div[@role='switch'])[2]").click()
            element = self.page.get_by_placeholder("请选择").nth(4)
            if element.is_visible():
                element.click()
                self.page.get_by_text("星期一").click()
                self.page.mouse.click(x=10, y=10)  # 点击空白处
            # 点击按钮，弹出选项
            self.page.get_by_placeholder("开始时间").click()
            start_hour, start_minute = start_time.split(":")
            start_hour_locator = self.page.locator("(//ul[@class='el-scrollbar__view el-time-spinner__list'])[1]/li").filter(has_text=start_hour)
            start_hour_locator.scroll_into_view_if_needed()
            start_hour_locator.click()
            start_minute_locator = self.page.locator("(//ul[@class='el-scrollbar__view el-time-spinner__list'])[2]/li").filter(has_text=start_minute)
            start_minute_locator.scroll_into_view_if_needed()
            start_minute_locator.click()
            end_hour, end_minute = end_time.split(":")
            end_hour_locator = self.page.locator("(//ul[@class='el-scrollbar__view el-time-spinner__list'])[4]/li").filter(has_text=end_hour)
            end_hour_locator.scroll_into_view_if_needed()
            end_hour_locator.click()
            end_minute_locator = self.page.locator("(//ul[@class='el-scrollbar__view el-time-spinner__list'])[5]/li").filter(has_text=end_minute)
            end_minute_locator.scroll_into_view_if_needed()
            end_minute_locator.click()
            # 输入单次可预约最长时间
            self.page.locator("(//input[@placeholder='请输入'])[3]").fill(max_duration)
            # logging.info(f"打开了时间限制开关，并设置了开始时间为{start_time}，结束时间为{end_time}，单次可预约最长时间为{max_duration}小时")

    def select_users(self, users):
        self.page.locator(".text_area").click()
        for user in users:
            self.page.get_by_label("请选择部门和人员").get_by_text(user).click()
        self.page.get_by_role("button", name="确 定").click()
        # logging.info(f"选择了可使用者: {', '.join(users)}")

    def click_submit_button(self):
        self.page.get_by_role("button", name="提交").click()
        # logging.info("点击了提交按钮")

    def verify_success_message(self):
        assert self.page.get_by_text("操作成功").to_be_visible()
        # logging.info("验证了添加成功的提示信息")