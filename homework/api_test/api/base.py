import requests
import yaml

class Base:

    def __init__(self):
        #读取base配置文件
        token_params = self.read_file('../api/base.yaml')
        self.corpid = token_params['corpid']
        self.corpsecret = token_params['corpsecret']
        self.token_url = token_params['token_url']
        #创建一个Session对象，
        self.sess = requests.session()
        #使用新创建的seesion对象去获取token
        token = self.get_token(self.sess)
        #将token塞进session的params里，这样后续session发送请求时，params中就会带有access_token字段，拼接到url中
        #即后续请求都在这个session中，不用再另外传access_token
        self.sess.params = {'access_token':f'{token}'}

    def close_session(self):
        self.sess.close()

    def read_file(self,path):
        #获取配置文件中的相关接口信息
        with open(path,encoding='UTF-8') as f:
            conf = yaml.safe_load(f)
            for key in conf.keys():
                if key == 'base':
                    token_params = conf['base']
                    return token_params

                if key == 'address_api':
                    address_url = conf['address_api']
                    return address_url


    #获取token，用来塞进session对象的params中
    def get_token(self,s):

        #获取token的接口url
        url = self.token_url
        #url太长，不便于读，所以将其中param部分截出来，在get的时候再传进去
        params = f'corpid={self.corpid}&corpsecret={self.corpsecret}'
        #也可以不传seesion过来，使用requests重新创建一个session，获取token，但是就浪费了新建的这个session
        r = s.get(url=url,params=params)
        token = r.json()['access_token']
        return token

    #封装post请求
    def post(self,url,json):
        return self.sess.post(url=url,json=json)

    #封装get请求
    def get(self,url,params):
        return self.sess.get(url=url,params=params)

    #封装delete请求
    def delete(self,url,json):
        return self.sess.delete(url=url,json=json)







