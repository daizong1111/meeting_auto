# 数据库中的数据可能有datetime类型的，需要做处理
from datetime import datetime


class BaseQueryPage:
    def __init__(self, page):
        self.page = page
    def get_first_page_button(self):
        return self.page.locator('//li[text()=1]')

    def get_table_data(self):
        numbers = 0
        # 将当前页置为第一页
        self.get_first_page_button().click()
        table_rows = self.get_table_rows()
        data = []
        while True:
            for row in table_rows.all():
                columns = row.locator("td")
                row_data = [column.inner_text() for column in columns.all()[:-1]]
                data.append(row_data)
            numbers += table_rows.count()
            if self.get_next_button().is_enabled():
                self.click_next_button()
            else:
                break
        return data, numbers

    def get_db_data(self, connection, query):
        cursor = connection.cursor(dictionary=True)
        # 执行查询
        cursor.execute(query)
        db_data = cursor.fetchall()
        return db_data

    def compare_data(self, page_data, db_data, fields):
        """
        比较页面数据和数据库数据。

        :param page_data: 页面数据，格式为二维列表。
        :param db_data: 数据库数据，格式为字典列表。
        :param fields: 需要比较的字段名列表，例如 ['room_name', 'room_code', 'capacity']。
        :return: 如果数据一致返回 True，否则返回 False。
        """
        # 将数据库数据转换为列表
        db_list = []
        for row in db_data:
            row_data = []
            for field in fields:
                value = row.get(field, "")
                if isinstance(value, datetime):  # 检查是否为 datetime 类型
                    value = value.strftime('%Y-%m-%d %H:%M:%S')  # 转换为指定格式的字符串
                row_data.append(str(value))
            db_list.append(row_data)

        # 比较两个数据集
        if page_data == db_list:
            print("数据一致，测试通过")
            return True
        else:
            print("数据不一致，测试不通过")
            print("页面数据:", page_data)
            print("数据库数据:", db_list)
            return False

    def get_next_button(self):
        pass

    def click_next_button(self):
        pass

    def get_table_rows(self):
        pass



