from playwright.sync_api import expect


class MeetingRoomInfoPage:
    def __init__(self, page):
        self.page = page

    def click_add_meeting_room_button(self):
        self.page.get_by_role("button", name="新建").click()
        # logging.info("点击了添加会议室按钮")

    def fill_room_name(self, room_name):
        if room_name:
            self.page.get_by_placeholder('不超过10个字').fill(room_name)
        # logging.info(f"输入了会议室信息: {room_name}")

    def fill_room_code(self, room_code):
        if room_code:
            self.page.get_by_placeholder("请输入,如HYS10-506").fill(room_code)
        # logging.info(f"输入了会议室编号: {room_code}")

    def fill_capacity(self, capacity):
        if capacity:
            self.page.get_by_role("spinbutton").first.fill(capacity)
        # logging.info(f"输入了会议室容量: {capacity}")

    def fill_location(self, location):
        if location:
            self.page.get_by_placeholder("不超过30个字").first.fill(location)
        # logging.info(f"输入了会议室位置: {location}")

    def select_room_status(self, status):
        if status:
            self.page.get_by_placeholder("请选择").first.click()
            room_status_li = self.page.locator("li").filter(has_text=status)
            room_status_li.wait_for(state="visible")
            room_status_li.click()
        # logging.info(f"选择了会议室状态: {status}")

    def select_devices(self, devices):
        if not devices:
            return  # 如果devices为空，直接返回
        if not isinstance(devices, (list, tuple, set)):
            raise TypeError("devices必须是一个可迭代对象（如列表、元组或集合）")
        for device in devices:
            self.page.get_by_text(device).click()
            # logging.info(f"选择了设备: {device}")

    def select_departments(self, departments):
        if not departments:
            return  # 如果devices为空，直接返回
        self.page.get_by_placeholder("请选择").nth(1).click()
        if not isinstance(departments, (list, tuple, set)):
            raise TypeError("departments必须是一个可迭代对象（如列表、元组或集合）")
        for department in departments:
            org_item = self.page.get_by_role("menuitem", name=department).get_by_role("radio")
            org_item.click()
        self.page.mouse.click(x=10, y=10)  # 点击空白处
        # logging.info(f"选择了管理部门: {', '.join(departments)}")

    # 选择完管理部门后，在选择管理员时，默认只能选择该部门下的人员
    def select_manager(self, manager):
        if manager is None:
            return
        self.page.get_by_placeholder("请选择").nth(2).click()
        manager_item = self.page.get_by_role("menuitem", name=manager)
        manager_item.click()
        self.page.mouse.click(x=10, y=10)  # 点击空白处
        # logging.info(f"选择了管理人: {manager}")

    def fill_description(self, description):
        if description is None:
            return
        self.page.get_by_role("textbox", name="请输入", exact=True).fill(description)
        # logging.info(f"输入了相关描述: {description}")

    # 选择完管理部门后，在选择审批人时，默认只能选择该部门下的人员
    def toggle_approval(self, need_approval_switch, approval_person):
        if need_approval_switch:
            # 点击开关
            approval_switch = self.page.locator("(//div[@role='switch'])[1]")
            approval_switch.click()
            # 调试信息：打印 aria-checked 和 approval_person 的值
            aria_checked = approval_switch.get_attribute("aria-checked")
            print(f"aria-checked: {aria_checked}, approval_person: {approval_person}")
            # 若开关为打开状态，则上面这个元素必定拥有aria-checked属性，若该元素没有该属性，get_attribute会返回None
            if approval_switch.get_attribute("aria-checked") == "true" and approval_person is not None:
                self.page.get_by_placeholder("请选择").nth(3).click()
                # 这处定位表达式要改。如果上面的那个张超未选中的话，这里的下标就和之前正常时候不一样了
                approval_item = self.page.get_by_role("menuitem", name=approval_person).nth(1)
                approval_item.click()
                self.page.mouse.click(x=10, y=10)  # 点击空白处
            # logging.info(f"打开了审批开关，并选择了审批人: {approval_person}")

    def toggle_time_limit(self, need_time_switch, days, start_time, end_time, max_duration):
        if need_time_switch:
            # 点击开关
            time_limit_switch = self.page.locator("(//div[@role='switch'])[2]")
            time_limit_switch.click()
            # 若时间限制开关为打开状态
            if time_limit_switch.get_attribute("aria-checked") == "true":
                if days is not None:
                    element = self.page.locator('(//div[@class="el-select el-select--medium"])[2]')
                    element.click()
                    # 将所有的日期选中
                    for day in days:
                        self.page.get_by_text(day).click()
                    self.page.mouse.click(x=10, y=10)  # 点击空白处
                # 点击按钮，弹出选项
                if start_time is not None:
                    self.page.get_by_placeholder("开始时间").click()
                    start_hour, start_minute = start_time.split(":")
                    start_hour_locator = self.page.locator(
                        "(//ul[@class='el-scrollbar__view el-time-spinner__list'])[1]/li").filter(has_text=start_hour)
                    start_hour_locator.scroll_into_view_if_needed()
                    start_hour_locator.click()
                    start_minute_locator = self.page.locator(
                        "(//ul[@class='el-scrollbar__view el-time-spinner__list'])[2]/li").filter(has_text=start_minute)
                    start_minute_locator.scroll_into_view_if_needed()
                    start_minute_locator.click()
                if end_time is not None:
                    self.page.get_by_placeholder("结束时间").click()
                    end_hour, end_minute = end_time.split(":")
                    end_hour_locator = self.page.locator(
                        "(//ul[@class='el-scrollbar__view el-time-spinner__list'])[4]/li").filter(has_text=end_hour)
                    end_hour_locator.scroll_into_view_if_needed()
                    end_hour_locator.click()
                    end_minute_locator = self.page.locator(
                        "(//ul[@class='el-scrollbar__view el-time-spinner__list'])[5]/li").filter(has_text=end_minute)
                    end_minute_locator.scroll_into_view_if_needed()
                    end_minute_locator.click()
                # 输入单次可预约最长时间
                if max_duration is not None:
                    self.page.locator("(//input[@placeholder='请输入'])[3]").fill(max_duration)
                # logging.info(f"打开了时间限制开关，并设置了开始时间为{start_time}，结束时间为{end_time}，单次可预约最长时间为{max_duration}小时")

    def select_users(self, users):
        if users is None:
            return
        self.page.locator(".text_area").click()
        n = len(users)
        for user in users:
            # 若走到最后一个元素，则需要点击该元素前的单选框
            if user == users[n-1]:
                self.page.get_by_label("请选择部门和人员").get_by_text(user).locator("../preceding-sibling::label").click()
            else:
                self.page.get_by_label("请选择部门和人员").get_by_text(user).click()
        self.page.get_by_role("button", name="确 定").click()
        # logging.info(f"选择了可使用者: {', '.join(users)}")

    def click_submit_button(self):
        self.page.get_by_role("button", name="提交").click()
        # logging.info("点击了提交按钮")

    def verify_success_message(self): \
            # 断言操作成功字样在页面出现
        self.page.get_by_text("操作成功").wait_for()
        assert self.page.get_by_text("操作成功").is_visible()
        # assert self.page.get_by_text("操作成功").is_visible()
        # logging.info("验证了添加成功的提示信息")

    def verify_error_miss_message(self):
        self.page.get_by_text("*必填项不能为空").wait_for()
        assert self.page.get_by_text("*必填项不能为空").is_visible()
        # logging.info("验证了添加失败的提示信息")
