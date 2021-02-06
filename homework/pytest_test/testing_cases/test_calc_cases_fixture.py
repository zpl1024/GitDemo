"""补全计算器（加减乘除）的测试用例，编写用例顺序：加-除-减-乘
创建 fixture 方法实现执行测试用例前打印【开始计算】，执行测试用例之后打印【计算结束】
将 fixture 方法存放在 conftest.py ，设置 scope=module
控制测试用例顺序按照【加-减-乘-除】这个顺序执行
结合 allure 生成本地测试报告"""
import allure
import pytest
import yaml

#open带中文的yaml文件时，需要带encoding=‘UTF-8’，否则报编码错误
#另外，ids中含中文时，需要在conftest.py文件中添加内容，使得用例名称显示为中文，非unicode格式
#把setup中的实例化优化成fix方法，方法叫get_calc，并放到conftest.py中，将fix的方法名传给类中方法即可实现调用
#把参数化优化成了各个测试用例对应的fix参数化方法，方法名get_xxdatas，每个测试用例方法可以调用get_xxdatas返回数据
#fix参数化方法不放到conftest中，因为此参数化的数据只有这个模块用，其他模块不用，否则每次测试都要执行，浪费时间

#从yaml文件中分别取出加减乘除的用例数据datas和用例名称casename
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

#针对加减乘除分别获取参数化了的列表数据（列表套列表），并依次返回每个子列表给调用方法
@pytest.fixture(params = add_datas,ids = add_casename)
def get_adddatas(request):
    print("开始计算...")
    data = request.param
    yield data
    print("计算结束")

@pytest.fixture(params = div_datas,ids = div_casename)
def get_divdatas(request):
    print("开始计算...")
    data = request.param
    yield data
    print("计算结束")

@pytest.fixture(params = sub_datas,ids = sub_casename)
def get_subdatas(request):
    print("开始计算...")
    data = request.param
    yield data
    print("计算结束")

@pytest.fixture(params = mul_datas,ids = mul_casename)
def get_muldatas(request):
    print("开始计算...")
    data = request.param
    yield data
    print("计算结束")

@allure.feature("测试计算器")
class Test_cases:
#方法内调用fix的两个方法名，get_adddatas方法每次传一个子列表过来，子列表中有3个数，前2个为加数，第三个数为期望和
    @pytest.mark.run(order=1)
    @allure.story("测试加法")
    def test_add_func(self,get_calc,get_adddatas):
        with allure.step("计算两个数的相加之和"):
            result = get_calc.add_func(get_adddatas[0],get_adddatas[1])
        assert result == get_adddatas[2]
#order参数是为了控制该方法的运行顺序
    @pytest.mark.run(order=4)
    @allure.story("测试除法")
    def test_div_func(self,get_calc,get_divdatas):
        with allure.step("计算两个数相除"):
            result = get_calc.div_func(get_divdatas[0],get_divdatas[1])
        assert round(result,3) == get_divdatas[2]

    @pytest.mark.run(order=2)
    @allure.story("测试减法")
    def test_sub_func(self,get_calc,get_subdatas):
        with allure.step("计算两个数相减"):
            result = get_calc.sub_func(get_subdatas[0],get_subdatas[1])
        assert result == get_subdatas[2]

    @pytest.mark.run(order=3)
    @allure.story("测试乘法")
    def test_mul_func(self,get_calc,get_muldatas):
        with allure.step("计算两个数相乘"):
            result = get_calc.mul_func(get_muldatas[0],get_muldatas[1])
        assert result == get_muldatas[2]