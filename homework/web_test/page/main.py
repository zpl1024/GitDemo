from selenium.webdriver.common.by import By

from homework.web_test.page.addContact import addContact
from homework.web_test.page.basepage import basePage


class Main(basePage):
    #传入待测页面地址
    base_url = 'https://work.weixin.qq.com/wework_admin/frame'
    #选择主页上的添加成员功能进行PO
    def goto_addcontact(self):
        self.find(By.CSS_SELECTOR,'.index_service_cnt_itemWrap:nth-child(1)').click()
        #跳转到添加联系人界面（classname）
        return addContact(self.driver)


