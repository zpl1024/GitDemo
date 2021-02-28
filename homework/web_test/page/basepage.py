from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver

class basePage:

    base_url = ''
    def __init__(self,driver:WebDriver=None):
        #第一次Main（）没有传入driver，需要从本地复用浏览器,从已登录状态开始
        self.driver = ''
        if driver is None:
            options = Options()
            options.debugger_address = '127.0.0.1:9222'
            self.driver = webdriver.Chrome(options=options)
            self.driver.maximize_window()
        #第二次以后，会传入driver，保证return前后页面连续
        else:
            self.driver = driver
        if self.base_url !='':
            self.driver.get(self.base_url)
            self.driver.implicitly_wait(5)

    def find(self,by,locator):
        return self.driver.find_element(by,locator)

    # def quit(self):
    #     self.driver.quit()
