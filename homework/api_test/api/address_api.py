from homework.api_test.api.base import Base

class AddressApi(Base):

    def address_init(self):
        address_api = self.read_file('../api/address_api.yaml')
        self.creat_member_url = address_api['creat_member']
        self.update_memberinfo_url = address_api['update_memberinfo']
        self.get_memberinfo_url = address_api['get_memberinfo']
        self.delete_member_url = address_api['delete_member']

    #接口要求使用json格式传入
    def creat_member(self,data):
        url = self.creat_member_url
        #将成员信息转成json格式，传入请求data和json字段中
        r = self.post(url=url,json=data)
        return r.json()

    def update_memberinfo(self,data):
        url = self.update_memberinfo_url
        # 将成员信息转成json格式，传入请求data和json字段中
        r = self.post(url=url, json=data)
        return r.json()

    def get_memberinfo(self,userid):
        url = self.get_memberinfo_url
        param = {
            'userid':userid
        }
        r = self.get(url=url,params=param)
        #返回成员信息
        return r.json()

    def delete_member(self,userid):
        url = self.delete_member_url
        param = {
            'userid':userid
        }
        r = self.get(url=url,params=param)
        return r.json()

    #关闭通讯录会话
    def close_address(self):
        self.close_session()



