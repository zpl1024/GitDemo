"""
补全计算器中加法和除法的测试用例
使用参数化完成测试用例的自动生成
在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
注意：
使用等价类，边界值，因果图等设计测试用例
测试用例中添加断言，验证结果
灵活使用 setup(), teardown() , setup_class(), teardown_class()
   """
import pytest
import yaml
from homework.pytest_test.python_code.calc_code import calculator
#open带中文的yaml文件时，需要带encoding=‘UTF-8’，否则报编码错误
#另外，ids中含中文时，需要再testcase同级目录下增加conftest.py文件，使得用例名称显示为中文，非unicode格式

with open('./datas.yaml',encoding='UTF-8') as f:
     add_data = yaml.safe_load(f)['add']
     add_datas = add_data['datas']
     add_casename = add_data['caseid']
     div_data = add_data['div']
     div_datas = div_data['datas']
     div_casename = div_data['caseid']

class Test_cases:
    def setup_class(self):
        self.calcu = calculator()

    def setup(self):
        print("开始计算...")

    def teardown(self):
        print("计算结束")

    @pytest.mark.parametrize("a,b,expect",add_datas,ids = add_casename)
    def test_add_func(self,a,b,expect):
        result = self.calcu.add_func(a,b)
        # print(f'{a}和{b}的和为{result}')
        assert result == expect

    @pytest.mark.parametrize("a,b,expect",div_datas,ids=div_casename)
    def test_div_func(self,a,b,expect):
        result = self.calcu.div_func(a,b)
        assert round(result,3) == expect

