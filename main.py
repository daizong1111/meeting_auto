import pytest


# 定义运行测试的函数
def run_tests():


    # 构建 pytest 参数
    pytest_args = ['-v',
                   '-s',
                   '--alluredir=allure-results',
                   # 执行指定的用例文件(不写则执行所有的用例)
                   # 'tests/test_meeting_manage/test_meeting_room_manage.py',
                   # 'tests/test_meeting_manage/test_meeting_room_manage.py::TestAddMeetingRoom::test_add_meeting_room_success',
                   # 'tests/test_meeting_manage/test_meeting_room_manage.py::TestDeleteMeetingRoom',
                   'tests/test_meeting_manage/test_meeting_room_manage.py::TestEditMeetingRoom',
                   # 'tests/test_meeting_manage/test_meeting_room_manage.py::TestQueryMeetingRoom'
                   ]
    # 运行 pytest
    pytest.main(pytest_args)


# 主程序入口
if __name__ == "__main__":
    run_tests()  # 运行测试
