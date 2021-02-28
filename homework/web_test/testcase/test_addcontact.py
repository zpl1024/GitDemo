from homework.web_test.page import contactlist
from homework.web_test.page.main import Main

class TestAddcontact:
    def setup(self):
       self.main = Main()

    def teardown(self):
        pass

    def test_addcontact(self):
        #接收联系人列表的姓名列数据，与新增联系人信息对比
        contact_list = self.main.goto_addcontact().add_contact().contact_list()
        assert 'usr009' in contact_list
