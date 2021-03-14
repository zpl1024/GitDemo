from homework.app_test.framwork.basepage import basepage
from homework.app_test.page.addtype import add_type
from homework.app_test.page.search import search


class contactlist(basepage):

    #进入联系人列表页面，滑动查找“添加成员”，跳转到添加方式页面
    def goto_type(self):
        self.steps('../page/contactlist.yml', 'goto_type')
        return add_type(self.driver)

    def goto_search(self):
        self.steps('../page/contactlist.yml', 'goto_search')
        return search(self.driver)