from time import sleep

import allure
import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

#保存当前driver，并封装自己要用的接口
from homework.app_test.conftest import root_log


class basepage:
    #存放黑名单元素，即可以关闭弹窗的元素的by和locator
    #删除成员时的确认对话框假设为黑名单
    black_list=[('xpath',"//*[@resource-id='com.tencent.wework:id/bpc']")]
    #一个字典，格式为：yaml字典中value变量:用例传过来的参数值
    params={}
    # 传入driver并赋值类变量，后续继承的子类都能使用这个driver
    def __init__(self,driver:WebDriver=None):
        self.driver = driver

    def implicitly_wait(self,time):
        self.driver.implicitly_wait(time)

    def find(self,by,locator):
        root_log.info(f'find: by={by},locator={locator}')
        try:
            self.implicitly_wait(10)
            return self.driver.find_element(by,locator)

        #监听异常Exception，如果找不到元素，捕获该异常并进入异常处理
        except Exception as e:
            self.implicitly_wait(2)
            #找不到元素时抓取截图,并在报告中展现
            self.driver.get_screenshot_as_file('tmp.png')
            allure.attach.file('tmp.png',attachment_type=allure.attachment_type.PNG)
            #遍历弹窗黑名单
            for black in self.black_list:
                #使用find_elements（如果没找到会返回空列表），或者用find_element（如果没找到会报错）,不能直接调用find（），会陷入无限递归
                eles = self.driver.find_elements(*black)
                #判断是否找到
                if len(eles) != 0 :
                    #找到就点击该元素关闭弹窗，并重新查找要查找的元素（一次找一个黑名单元素，所以取查找元素列表的第一个）
                    root_log.info(f'当前找到的黑名单元素有：{eles}')
                    eles[0].click()
                    root_log.info('关闭弹窗')
                    return self.find(by, locator)
            #如果黑名单中元素在当前页面都定位不到，就抛出异常
            raise e

    #读入yaml文件，解析list中dict里的key和value，将元素定位做成数据驱动
    def steps(self,path,func):
        with open(path,encoding='utf-8') as f:
            datas:list = yaml.safe_load(f)
            #取出列表中每项，每项均为字典格式，对比每项字典中的key是否与传入的func一致
            for data in datas:
                #如果传入的func在字典data的key中，取出func对应的键值
                if func in data.keys():
                    steps: list[dict] = data[func]
                    #取出的键值为字典列表
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
                            if 'judge' == step['name']:
                                #把{staff_name}赋给content
                                content:str = step['condition']
                                root_log.info(f'替换前的content是{content}')
                                for key,value in self.params.items():
                                    if key == content:
                                        content = content.replace(key,value)
                                        root_log.info(f'替换后的content是{content}')
                                if element.text == content:
                                    print(element.text)
                                    element.click()
                                    return True
                            if 'find' ==step['name']:
                                return element













