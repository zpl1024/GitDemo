from homework.app_test.framwork.basepage import basepage
from homework.app_test.page.delete_result import delete_result


class edit_staff(basepage):
    def delete_staff(self):
        self.steps('../page/edit_staff.yml', 'delete_staff')
        return delete_result(self.driver)


