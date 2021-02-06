"""
补全计算器中加法和除法的测试用例
使用参数化完成测试用例的自动生成
在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
注意：
使用等价类，边界值，因果图等设计测试用例
测试用例中添加断言，验证结果
灵活使用 setup(), teardown() , setup_class(), teardown_class()
   """
import allure
import pytest
import yaml
from homework.pytest_test.python_code.calc_code import calculator
#open带中文的yaml文件时，需要带encoding=‘UTF-8’，否则报编码错误
#另外，ids中含中文时，需要再testcase同级目录下增加conftest.py文件，使得用例名称显示为中文，非unicode格式

with open('datas_all.yaml', encoding='UTF-8') as f:
     dict = yaml.safe_load(f)
     add_datas = dict['add']['datas']
     add_casename = dict['add']['caseid']
     div_datas = dict['div']['datas']
     div_casename = dict['div']['caseid']
     sub_datas = dict['sub']['datas']
     sub_casename = dict['sub']['caseid']
     mul_datas = dict['mul']['datas']
     mul_casename = dict['mul']['caseid']

@allure.feature("预习课测试计算器")
class Test_cases:
    def setup_class(self):
        self.calcu = calculator()

    def setup(self):
        print("开始计算...")

    def teardown(self):
        print("计算结束")

    @pytest.mark.run(order=5)
    @allure.story("测试加法")
    @pytest.mark.parametrize("a,b,expect",add_datas,ids = add_casename)
    def test_add_func(self,a,b,expect):
        result = self.calcu.add_func(a,b)
        # print(f'{a}和{b}的和为{result}')
        assert result == expect

    @pytest.mark.run(order=8)
    @allure.story("测试除法")
    @pytest.mark.parametrize("a,b,expect",div_datas,ids = div_casename)
    def test_div_func(self,a,b,expect):
        result = self.calcu.div_func(a,b)
        assert round(result,3) == expect

    @pytest.mark.run(order=6)
    @allure.story("测试减法")
    @pytest.mark.parametrize("a,b,expect",sub_datas, ids = sub_casename)
    def test_sub_func(self,a,b,expect):
        result = self.calcu.sub_func(a,b)
        assert result == expect

    @pytest.mark.run(order=7)
    @allure.story("测试乘法")
    @pytest.mark.parametrize("a,b,expect", mul_datas, ids = mul_casename)
    def test_mul_func(self,a,b,expect):
        result = self.calcu.mul_func(a,b)
        assert result == expect