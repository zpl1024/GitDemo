from homework.api_test.api.address_api import AddressApi
from homework.api_test.testcases.test_base import TestBase


class TestAddress(TestBase):

    def setup_class(self):
        #实例化addressApi基类
        self.address = AddressApi()
        self.address.address_init()
        #实例化测试基类，读出测试数据
        self.testbase = TestBase()
        self.data = self.testbase.read_casedata()
        #不用测试基类，直接打开文件
        # with open("testcase_data.yaml", encoding='UTF-8') as f:
        #     datas = yaml.safe_load(f)
        #     for key in datas.keys():
        #         if  key == 'address_data':
        #             self.data = datas['address_data']


    #关闭session
    def teardown_class(self):
        self.address.close_address()

    def test_creat_member(self):
        #先清理环境，不要存在api006脏数据
        self.address.delete_member(self.data['userid'])
        # 接收返回的成员信息结构体
        dict = self.address.creat_member(self.data)
        #添加后获取一下成员信息，是否确实添加成功
        dict2 = self.address.get_memberinfo(self.data['userid'])
        #添加完后，清理环境
        self.address.delete_member(self.data['userid'])
        assert dict['errcode'] == 0 and dict['errmsg'] == 'created' and dict2['name'] == self.data['name']

    def test_update_memberinfo(self):
        #先准备环境，创建好要更新的用户
        self.address.creat_member(self.data)
        update_name = 'update003'
        #更新成员信息
        self.data['name'] = update_name
        #调用接口更新成员姓名
        dict = self.address.update_memberinfo(self.data)
        #更新完后获取成员信息，用于后面断言，判断是否的确更新成功
        dict2 = self.address.get_memberinfo(self.data['userid'])
        #更新完后，恢复环境，删除该成员
        self.address.delete_member(self.data['userid'])
        assert dict['errcode'] == 0 and dict['errmsg'] == 'updated' and dict2['name'] == update_name

    def test_get_memberinfo(self):
        #先自己创建一个成员，然后再获取信息
        self.address.creat_member(self.data)
        dict = self.address.get_memberinfo(self.data['userid'])
        #获取信息之后，恢复环境，删除该成员
        self.address.delete_member(self.data['userid'])
        #判断获取到的成员信息是否和创建的成员一致，以及响应体中的响应码是否正确
        assert dict['errcode'] == 0 and dict['errmsg'] == 'ok' and dict['name'] == self.data['name']

    def test_delete(self):
        #先准备环境，创建一个待删除的用户信息
        self.address.creat_member(self.data)
        #调用删除接口，删除成员
        dict = self.address.delete_member(self.data['userid'])
        #删除后再去获取用户信息，判断是否确实删除
        dict2 = self.address.get_memberinfo(self.data['userid'])
        assert dict['errcode'] == 0 and dict['errmsg'] == 'deleted' and dict2['errcode'] != 0



