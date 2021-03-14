from homework.app_test.framwork.basepage import basepage
from homework.app_test.page.information import information


class add_type(basepage):
    #进入添加方式页面，选择手动加入联系人，跳转到输入联系人信息页面
    def goto_information(self):
        self.steps('../page/addtype.yml','goto_information')
        return information(self.driver)
