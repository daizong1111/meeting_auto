import logging
import allure


# 定义基础测试类，包含日志记录和Allure步骤记录功能
class BaseCase:
    # 将日志记录器的初始化移到类变量中
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    @allure.step("执行测试步骤: {step_name}")
    def log_step(self, step_name: str):
        """记录测试步骤并生成 Allure 步骤信息"""
        self.logger.info(f"执行测试步骤: {step_name}")
