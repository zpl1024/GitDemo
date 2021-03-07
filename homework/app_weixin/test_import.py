from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestImport:
    def setup(self):
        caps = {}
        caps['platformName'] = 'android'
        caps['deviceName'] = 'weixin'
        caps['appPackage'] = 'com.tencent.wework'
        caps['appActivity'] = '.launch.LaunchSplashActivity'
        caps['noReset'] = True
        caps['automationName'] = 'uiautomator2'
        caps['dontStopAppOnReset'] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        pass
        # self.driver.quit()

    @pytest.mark.skip
    def test_login(self):
        #验证是否成功登录
        text1 = self.driver.find_element(MobileBy.ID,'ig1').get_attribute('text')
        assert '消息' in text1

    def test_addcontact(self):
        #点击通讯录
        self.driver.find_element(MobileBy.XPATH,'//*[@text="通讯录"]').click()
        #边滑边滚动查找“添加成员”文本信息，查到后点击
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 'text("添加成员").instance(0));').click()
        #点击手动输入添加
        self.driver.find_element(MobileBy.XPATH,'//*[@text="手动输入添加"]').click()
        #输入联系人信息
        #注：姓名后有空格，所以要用contains，不能用=，或者//*[contains(@text,'姓名')]/..//*[@class='android.widget.EditText']
        self.driver.find_element(MobileBy.XPATH,'//*[contains(@text,"姓名")]/..//android.widget.EditText').send_keys("appusr007")
        self.driver.find_element(MobileBy.XPATH,'//*[@text="手机号"]').send_keys("13112345007")
        self.driver.find_element(MobileBy.XPATH,'//*[@text="性别"]/../android.widget.RelativeLayout').click()
        #等待3秒，确保浮窗显示完好
        sleep(3)
        self.driver.find_element(MobileBy.XPATH, '//*[@text="女"]').click()
        #保存联系人信息
        self.driver.find_element(MobileBy.XPATH, '//*[@text="保存"]').click()
        #定位toast
        ele = self.driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]')
        #对toast信息进行断言
        assert ele.text == '添加成功'


