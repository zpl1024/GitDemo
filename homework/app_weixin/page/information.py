from homework.app_weixin.page.basepage import basepage
from homework.app_weixin.page.find_toast import FindToast


class information(basepage):
    #输入用户信息，并保存，回跳转到添加方式页面，定位toast
    def add_contact(self,name,phone):
        self.params={'{usrname}':name,'{telephone}':phone}
        self.steps('../page/information.yml')
        return FindToast(self.driver)
