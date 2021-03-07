from homework.app_weixin.page.basepage import basepage
from homework.app_weixin.page.information import information

class add_type(basepage):
    #进入添加方式页面，选择手动加入联系人，跳转到输入联系人信息页面
    def goto_information(self):
        self.steps('../page/addtype.yml')
        return information(self.driver)
