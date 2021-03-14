import allure
import pytest
import yaml

from homework.app_test.framwork.app import App

with open('testcase_deletestaff.yml', encoding='utf-8') as f:
    steps = yaml.safe_load(f)
    test_datas = steps['datas']
    test_names = steps['names']

@pytest.fixture(params=test_datas, ids=test_names)
def get_testdata(request):
    datas = request.param
    #将两个变量的数据切片依次读取回传，然后接着读取下一个切片
    yield datas


@allure.feature('企业微信测试用例')
class TestDeleteStaff:
    def setup(self):
        self.app = App()
        self.app.start()

    def teardown(self):
        pass
        # self.app.driver.quit()
    @allure.story("删除成员用例")
    def test_deletestaff(self,get_testdata):
        username = get_testdata['name']
        with allure.step(f"删除成员{username}"):
            self.app.goto_main().goto_telbook().goto_search().search_staff(username).goto_staffdetail().goto_editstaff().delete_staff().search_result()

