from homework.api_test.api.base import Base

class AddressApi(Base):

    #接口要求使用json格式传入
    def creat_member(self,data):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create'
        #将成员信息转成json格式，传入请求data和json字段中
        r = self.post(url=url,json=data)
        #方法一 取出响应体中的errorcode和errmsg字段值，并返回该列表
        # errorcode = r.json()['errcode']
        # errmsg = r.json()['errmsg']
        # return errorcode,errmsg
        #方法二 直接返回响应结构体
        return r.json()

    def update_memberinfo(self,data):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update'
        # 将成员信息转成json格式，传入请求data和json字段中
        r = self.post(url=url, json=data)
        return r.json()

    def get_memberinfo(self,userid):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/user/get'
        param = {
            'userid':userid
        }
        r = self.get(url=url,params=param)
        #返回成员信息
        return r.json()

    def delete_member(self,userid):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete'
        param = {
            'userid':userid
        }
        r = self.get(url=url,params=param)
        return r.json()



