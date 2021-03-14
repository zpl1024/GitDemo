from homework.app_test.framwork.basepage import basepage
from homework.app_test.page.find_toast import FindToast


class information(basepage):
    #输入用户信息，并保存，回跳转到添加方式页面，定位toast
    def add_contact(self,name,phone):
        self.params={'{usrname}':name,'{telephone}':phone}
        self.steps('../page/information.yml','add_contact')
        return FindToast(self.driver)
