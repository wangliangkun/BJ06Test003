from selenium.webdriver.support.wait import WebDriverWait

class Base():
    # 初始化方法
    def __init__(self,driver):
        self.driver=driver
    # 获取元素
    def base_find_element(self,loc,timeout=30,poll=0.5):
        return WebDriverWait(self.driver,timeout,poll_frequency=poll).until(lambda x:x.find_element(*loc))
    # 点击元素
    def base_click_element(self,loc):
        self.base_find_element(loc).click()
    # 输入元素
    def base_input_element(self,loc,text):
        self.base_find_element(loc).clear()
        self.base_find_element(loc).send_keys(text)
