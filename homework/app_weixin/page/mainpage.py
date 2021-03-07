from appium.webdriver.common.mobileby import MobileBy
from homework.app_weixin.page.basepage import basepage
from homework.app_weixin.page.contactlist import contactlist


class main(basepage):

    def goto_telbook(self):
        #点击通讯录
        self.steps('../page/mainpage.yml')
        return contactlist(self.driver)
