# 会议管理系统Web自动化测试项目

## 项目概述
本项目使用Python + Playwright + pytest实现对会议管理系统的Web自动化测试。包含会议室管理等功能的测试用例，通过Page Object模式组织代码，并使用Allure生成测试报告。

## 技术栈
- Python 3.7+
- Playwright
- pytest
- MySQL
- Allure

## 环境要求
- Windows/Linux/macOS
- Python 3.7+
- pip包管理器
- Docker（可选）

## 安装和使用步骤
1. 克隆仓库
2. 安装依赖：`pip install -r requirements.txt`
3. 安装Playwright及其浏览器：`playwright install`
4. 安装chrome浏览器，将其路径配置到系统环境变量中
5. 安装pycharm
6. 运行命令chrome --remote-debugging-port=9222 #在9222远程调试端口打开chrome浏览器
7. 跳转到网址：http://134.84.202.69:9081/meeting-web/#/login
8. 使用账号密码登录 admin/Lzs@1991070214
9. 使用pycharm运行main.py文件

## 常用命令
- 如何运行所有测试：`pytest tests/`
- 如何运行单个测试文件：`pytest tests/test_meeting_manage/test_meeting_room_manage.py`
- 如何生成测试报告：`allure serve allure-results_<timestamp>`

## 测试目录结构
解释了主要目录和文件的作用：
- pages/：页面对象类
- tests/：测试用例
- utils/：工具类
- allure-report/：Allure报告相关文件
- allure-results_*/：测试结果数据