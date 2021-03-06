import pytest
import yaml
from homework.app_weixin.page.app import App

#使用fixture来参数化用例数据，加载的yml文件是testcase_data.yml
with open('testcase_data.yml', encoding='utf-8') as f:
    steps = yaml.safe_load(f)
    test_datas = steps['datas']
    test_names = steps['names']


@pytest.fixture(params=test_datas, ids=test_names)
def get_testdata(request):
    datas = request.param
    yield datas

class TestContact:
    def setup(self):
        #先进行App类的实例化，使init方法执行，否则不能使用实例变量self.driver
        self.app = App()
        self.app.start()

    def teardown(self):
        self.app.driver.quit()

    def test_addcontact(self,get_testdata):
        #将传过来的一个字典拆解
        usrname = get_testdata['name']
        tel = get_testdata['telephone']
        # gender = get_testdata['gender']
        tips = self.app.goto_main().goto_telbook().goto_type().goto_information().add_contact(usrname,tel).find_toast()
        assert tips == '添加成功'

