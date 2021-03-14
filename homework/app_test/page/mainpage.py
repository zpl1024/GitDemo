from homework.app_test.framwork.basepage import basepage
from homework.app_test.page.contactlist import contactlist


class main(basepage):

    def goto_telbook(self):
        #点击通讯录
        self.steps('../page/mainpage.yml', 'goto_telbook')
        return contactlist(self.driver)
