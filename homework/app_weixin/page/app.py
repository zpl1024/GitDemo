import yaml
from appium import webdriver
from homework.app_weixin.page.basepage import basepage
from homework.app_weixin.page.mainpage import main

#修改配置yaml文件格式统一，复用基类中解析yaml方法steps
class App(basepage):
    #继承basepage后，直接使用basepage的init，这里可以不用重构,basepage中已定义一个driver，子类app可直接用
    # def __init__(self):
    #     self.start()
    #读入配置文件，获取应用包名和页面名

    #启动app，并创建一个driver
    def start(self):
        #判断在调用start时，是否有driver传入，即是第一次还是非首次调用start
        if self.driver is None:
            #加载APP配置文件
            self.steps('../page/app.yml')
            caps = dict()
            caps['platformName'] = 'android'
            caps['deviceName'] = 'weixin'
            caps['appPackage'] = self.appPackage
            caps['appActivity'] = self.appActivity
            caps['noReset'] = True
            caps['automationName'] = 'uiautomator2'
            caps['dontStopAppOnReset'] = True
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub',caps)
            self.driver.implicitly_wait(5)
        #这个else在实际中怎么用到
        else:
            self.driver.start_activity(self.appPackage,self.appActivity)
            self.driver.implicitly_wait(5)
        return self
    #从主页面开始
    def goto_main(self):
        return main(self.driver)