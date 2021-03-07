from time import sleep
import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

#保存当前driver，并封装自己要用的接口
class basepage:
    #存放黑名单元素，即可以关闭弹窗的元素的by和locator
    black_list=[('xpath','//*[@resource-id="com.tencent.wework:id/bpc"]')]
    #一个字典，格式为：yaml字典中value变量:用例传过来的参数值
    params={}
    # 传入driver并赋值类变量，后续继承的子类都能使用这个driver
    def __init__(self,driver:WebDriver=None):
        self.driver = driver

    def find(self,by,locator):
        try:
            return self.driver.find_elements(*by) if isinstance(by,tuple) else self.driver.find_element(by,locator)

        #找不到元素抛异常，接着处理异常
        except Exception as e:
            #遍历弹窗黑名单
            for black in self.black_list:
                #在当前页面找黑名单中的元素，防止有多个一样的元素，用s
                eles = self.driver.find_elements(*black)
                #判断是否找到
                if eles is not None:
                    #找到就点击该元素关闭弹窗，并重新查找要查找的元素（一个页面弹窗只有1个，取查找元素列表的第一个）
                    eles[0].click()
                    return self.find(by, locator)
            #如果黑名单中元素在当前页面都定位不到，就抛出异常
            raise e

    #读入yaml文件，解析list中dict里的key和value，将元素定位做成数据驱动
    def steps(self,path):
        with open(path,encoding='utf-8') as f:
            steps:list[dict] = yaml.safe_load(f)
            for step in steps:
                if 'by' in step.keys():
                    element = self.find(step['by'],step['locator'])
                if 'action' in step.keys():
                    if 'click' == step['action']:
                        element.click()
                    elif 'send' == step['action']:
                        #将yaml中一个step里的变量传给content
                        content:str = step['keys']
                        #遍历params的keys，和当前content存的比较，有的话就用param的value来替换
                        for param in self.params.keys():
                            content = content.replace(f'{param}',self.params[param])
                        element.send_keys(content)
                    elif 'croll_find_click' == step['action']:
                        search_element = step['text']
                        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 f'text("{search_element}").instance(0));').click()
                if 'sleep' in step.keys():
                    sleep(step['sleep'])
                if 'name' in step.keys():
                    if 'toast' == step['name']:
                        element = self.find(step['by'],step['locator'])
                        return element
                    if 'caps' == step['name']:
                        self.appPackage = step['appPackage']
                        self.appActivity = step['appActivity']










