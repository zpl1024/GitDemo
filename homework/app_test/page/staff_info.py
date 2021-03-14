from homework.app_test.framwork.basepage import basepage
from homework.app_test.page.staff_detail import staff_detail


class staff_info(basepage):
    def goto_staffdetail(self):
        self.steps('../page/staff_info.yml', 'goto_staffdetail')
        return staff_detail(self.driver)