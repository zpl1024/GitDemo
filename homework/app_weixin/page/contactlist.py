from homework.app_weixin.page.basepage import basepage
from homework.app_weixin.page.addtype import add_type


class contactlist(basepage):
    #进入联系人列表页面，滑动查找“添加成员”，跳转到添加方式页面
    def goto_type(self):
        self.steps('../page/contactlist.yml')
        return add_type(self.driver)