from Base.base import Base
from selenium.webdriver.common.by import By

# loc为元组，值有没有括号pycharm都可以识别为元组，注意：无括号时两个值以上为元组
loc_username = (By.ID, "com.vcooline.aike:id/etxt_username")
loc_pwd = By.ID, "com.vcooline.aike:id/etxt_pwd"
loc_login_btn = By.ID, "com.vcooline.aike:id/btn_login"

class PageLogin(Base):
    # 输入用户名
    def page_login_username(self,text):
        self.base_input_element(loc_username,text)
    # 输入密码
    def page_login_pwd(self,text):
        self.base_input_element(loc_pwd,text)
    # 点击登录
    def page_login_click(self):
        self.base_click_element(loc_login_btn)
