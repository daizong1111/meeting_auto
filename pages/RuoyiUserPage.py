import mysql.connector
import datetime
class RuoyiUserPage:
    def __init__(self, page):
        self.page = page
    def get_table_rows(self):
        return self.page.locator("(//table[@class='el-table__body'])[1]/tbody/tr")

    def click_next_button(self):
        self.get_next_button().click()
    def get_next_button(self):
        return self.page.locator("//button[@class='btn-next']")
    def get_table_data(self):
        table_rows = self.get_table_rows()
        data = []
        while True:
            for row in table_rows.all():
                columns = row.locator("td")
                row_data = [column.inner_text() for i, column in enumerate(columns.all()[2:-1]) if i != 4]
                data.append(row_data)
            if self.get_next_button().is_enabled():
                self.click_next_button()
            else:
                break
        return data
    def get_db_data(self, user_id=None, user_name=None, status=None, phonenumber=None, begin_time=None, end_time=None, dept_id=None, data_scope=None):
        # 连接到数据库
        db_config = {
            "host": "localhost",
            "user": "root",
            "password": "SDZ1t3o5m9916",
            "database": "meeting_manage"
        }
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)

        # 构建 SQL 查询
        # query = """
        # SELECT room_name, room_code, capacity, device, status, location, approval, departments, manager
        # FROM meeting_rooms
        # WHERE room_name = %s AND capacity = %s AND device = %s AND status = %s AND location = %s AND approval = %s AND departments = %s AND manager = %s
        # """
        #
        # """select u.user_id, u.dept_id, u.nick_name, u.user_name, u.email, u.avatar, u.phonenumber, u.sex, u.status, u.del_flag, u.login_ip, u.login_date, u.create_by, u.create_time, u.remark, d.dept_name, d.leader from sys_user u
		# left join sys_dept d on u.dept_id = d.dept_id
		# where u.del_flag = '0'
		# <if test="userId != null and userId != 0">
		# 	AND u.user_id = #{userId}
		# </if>
		# <if test="userName != null and userName != ''">
		# 	AND u.user_name like concat('%', #{userName}, '%')
		# </if>
		# <if test="status != null and status != ''">
		# 	AND u.status = #{status}
		# </if>
		# <if test="phonenumber != null and phonenumber != ''">
		# 	AND u.phonenumber like concat('%', #{phonenumber}, '%')
		# </if>
		# <if test="params.beginTime != null and params.beginTime != ''"><!-- 开始时间检索 -->
		# 	AND date_format(u.create_time,'%Y%m%d') &gt;= date_format(#{params.beginTime},'%Y%m%d')
		# </if>
		# <if test="params.endTime != null and params.endTime != ''"><!-- 结束时间检索 -->
		# 	AND date_format(u.create_time,'%Y%m%d') &lt;= date_format(#{params.endTime},'%Y%m%d')
		# </if>
		# <if test="deptId != null and deptId != 0">
		# 	AND (u.dept_id = #{deptId} OR u.dept_id IN ( SELECT t.dept_id FROM sys_dept t WHERE find_in_set(#{deptId}, ancestors) ))
		# </if>
		# <!-- 数据范围过滤 -->
		# ${params.dataScope}"""
        query, params = self.get_user_data(user_id, user_name, status, phonenumber, begin_time, end_time, dept_id, data_scope)
        cursor.execute(query, params)
        db_data = cursor.fetchall()

        # 关闭连接
        cursor.close()
        connection.close()

        return db_data

    def get_user_data(self, user_id=None, user_name=None, status=None, phonenumber=None, begin_time=None, end_time=None,
                      dept_id=None, data_scope=None):
        query = """
        SELECT u.user_id, u.dept_id, u.nick_name, u.user_name, u.email, u.avatar, u.phonenumber, u.sex, u.status, u.del_flag, u.login_ip, u.login_date, u.create_by, u.create_time, u.remark, d.dept_name, d.leader 
        FROM sys_user u
        LEFT JOIN sys_dept d ON u.dept_id = d.dept_id
        WHERE u.del_flag = '0'
        """

        params = []

        if user_id is not None and user_id != 0:
            query += " AND u.user_id = %s"
            params.append(user_id)

        if user_name is not None and user_name != '':
            query += " AND u.user_name LIKE %s"
            params.append(f"%{user_name}%")

        if status is not None and status != '':
            query += " AND u.status = %s"
            params.append(status)

        if phonenumber is not None and phonenumber != '':
            query += " AND u.phonenumber LIKE %s"
            params.append(f"%{phonenumber}%")

        if begin_time is not None and begin_time != '':
            query += " AND DATE_FORMAT(u.create_time, '%Y%m%d') >= DATE_FORMAT(%s, '%Y%m%d')"
            params.append(begin_time)

        if end_time is not None and end_time != '':
            query += " AND DATE_FORMAT(u.create_time, '%Y%m%d') <= DATE_FORMAT(%s, '%Y%m%d')"
            params.append(end_time)

        if dept_id is not None and dept_id != 0:
            query += " AND (u.dept_id = %s OR u.dept_id IN (SELECT t.dept_id FROM sys_dept t WHERE FIND_IN_SET(%s, t.ancestors)))"
            params.append(dept_id)
            params.append(dept_id)

        if data_scope is not None:
            query += f" {data_scope}"

        return query, params
    def compare_data(self, page_data, db_data):
        # 将数据库数据转换为列表
        db_list = [
            [row['user_name'], str(row['nick_name']), row['dept_name'], row['phonenumber'],
             row['create_time'].strftime('%Y-%m-%d %H:%M:%S')] for row in db_data]

        # 比较两个数据集
        if page_data == db_list:
            print("数据一致，测试通过")
            return True
        else:
            print("数据不一致，测试不通过")
            print("页面数据:", page_data)
            print("数据库数据:", db_list)
            return False
