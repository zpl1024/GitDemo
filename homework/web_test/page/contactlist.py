import re
from selenium.webdriver.common.by import By
from homework.web_test.page.basepage import basePage

class contactList(basePage):
    def contact_list(self):
        #获取页面显示的企业总人数
        num_str = self.find(By.CSS_SELECTOR,".js_member_count").get_attribute('innerText')
        # print(f'总人数为 {num_str}')
        #对获取到的字符串利用正则进行整数提取
        lst = re.findall(r"\d+",num_str)
        num = int(lst.pop(0))
        contacts=[]
        #获取企业联系人姓名一列，并存到列表中，最后返回列表
        for i in range(1,num+2):
            contact = self.find(By.XPATH,f'//*[@id="member_list"]/tr[{i}]/td[2]').get_attribute('title')
            contacts.append(contact)
        # print(contacts)
        return contacts

