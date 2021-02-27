"""使用cookie登录企业微信，导入联系人，加上断言验证"""
import shelve

from selenium import webdriver
from selenium.webdriver.common.by import By

class TestDemo:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://work.weixin.qq.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        #点击登录
        self.driver.find_element_by_css_selector('[id="indexTop"] a:nth-child(1)').click()
        #从db中获取列表形式的cookies并关闭db
        db = shelve.open('./dbs_cookie')
        self.cookies = db['cookie']
        db.close()

    def teardown(self):
        self.driver.quit()

    def test_cookie(self):
        #将列表形式的cookie中的每个字典元素取出，加到add_cookie中，，如果字典中含expirykey，则pop调这个key和对应的值
        for cookie in self.cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        #刷新当前加过cookie的页面
        self.driver.refresh()
        #点击导入联系人
        self.driver.find_element(By.CSS_SELECTOR,'.index_service_cnt_itemWrap:nth-child(2)').click()
        #上传文件
        self.driver.find_element(By.ID,'js_upload_file_input').send_keys('D:\\BaiduNetdiskDownload\通讯录.xls')
        #点击确认导入
        self.driver.find_element(By.ID,'submit_csv').click()
        #断言验证导入成功页面，前往查看按钮
        ele = self.driver.find_element_by_css_selector('[class="import_cnt import_autoNotice_autoImport"]>a')
        textname = ele.get_attribute('text')
        assert  textname == '前往查看'










