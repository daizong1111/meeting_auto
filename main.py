import pytest


# 定义运行测试的函数
def run_tests():


    # 构建 pytest 参数
    pytest_args = ['-v',
                   '--alluredir=allure-results',
                   # 执行指定的用例文件(不写则执行所有的用例)
                   # 'tests/test_user_settings.py',
                   # 'tests/test_meeting_manage/test_room_manage.py::TestAddMeetingRoom::test_add_meeting_room',
                   # 'tests/test_meeting_manage/test_room_manage.py::TestDeleteMeetingRoom',
                   'tests/test_meeting_manage/test_room_manage.py::TestEditMeetingRoom::test_edit_meeting_room',
                   # 'tests/test_meeting_manage/test_room_manage.py::TestQueryMeetingRoom::test_query_meeting_room'
                   # 'tests/test_meeting_manage/test_ruoyi_user_manage.py::TestQueryUsers::test_query_users',

                   ]
    # 运行 pytest
    pytest.main(pytest_args)


# 主程序入口
if __name__ == "__main__":
    run_tests()  # 运行测试
