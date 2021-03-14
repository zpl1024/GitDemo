from homework.app_test.conftest import root_log
from homework.app_test.framwork.basepage import basepage
from homework.app_test.page.staff_info import staff_info


class search(basepage):

    def search_staff(self,name):
        self.params = {'{staff_name}':name}
        result = self.steps('../page/search.yml', 'search_staff')
        if result is True:
            root_log.info(f'找到的用户是{name}，一致')
            return staff_info(self.driver)