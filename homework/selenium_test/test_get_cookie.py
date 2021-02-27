"""
复用浏览器，取得登录后的token并打印出来
"""
import shelve
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class TestDemo:
    def setup(self):
        #复用浏览器，打开已登录企业微信，并传入webdriver
        option = Options()
        option.debugger_address='127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_cookie(self):
        #选择页面欢迎提示语，验证是否正确登录
        ele = self.driver.find_element_by_css_selector('[class="index_explore_title"]')
        assert '开始探索企业微信' in ele.text
        cookies = self.driver.get_cookies()
         #将获取到的cookies存到db中，并关闭db
        db = shelve.open('./dbs_cookie')
        db['cookie'] = cookies
        db.close()


