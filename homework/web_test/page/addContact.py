from selenium.webdriver.common.by import By
from homework.web_test.page.basepage import basePage
from homework.web_test.page.contactlist import contactList

class addContact(basePage):
    username = 'usr009'
    memberAdd_english_name = 'men009'
    memberAdd_acctid = '13012345009'
    gender = '2'
    memberAdd_phone = '13012345009'
    def add_contact(self):
        #填写增加联系人的信息
        self.find(By.ID,'username').send_keys(self.username)
        self.find(By.ID,'memberAdd_english_name').send_keys(self.memberAdd_english_name)
        self.find(By.ID,'memberAdd_acctid').send_keys(self.memberAdd_acctid)
        #勾选性别单选框
        self.find(By.XPATH,f'(//*[@name="gender"])[{self.gender}]').click()
        self.find(By.ID,'memberAdd_phone').send_keys(self.memberAdd_phone)
        #点击保存
        self.find(By.XPATH,'(//*[@class="member_colRight_operationBar ww_operationBar"]/a[2])[1]').click()
        return contactList(self.driver)
