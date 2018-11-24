import os,sys
sys.path.append(os.getcwd())

from Page.page_login import PageLogin
from Base.get_driver import get_driver
class TestLogin():
    # 实例化对象
    def setup_class(self):
        self.login=PageLogin(get_driver())
    # 关闭驱动
    def teardown(self):
        self.login.driver.quit()
    # 测试方法
    # 输入用户名
    def test_login(self,username="12345678901",pwd="123456"):
        self.login.page_login_username(username)
    # 输入密码
        self.login.page_login_pwd(pwd)
    # 点击登录
        self.login.page_login_click()

if __name__ == '__main__':
    pytest.main("-s test_login.py")
