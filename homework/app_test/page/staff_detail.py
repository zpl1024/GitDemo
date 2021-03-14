from homework.app_test.framwork.basepage import basepage
from homework.app_test.page.edit_staff import edit_staff


class staff_detail(basepage):
    def goto_editstaff(self):
        self.steps('../page/staff_detail.yml', 'goto_editstaff')
        return edit_staff(self.driver)