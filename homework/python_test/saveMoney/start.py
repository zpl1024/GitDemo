"""原有存款 1000元， 发工资之后存款变为2000元
定义模块
1、money.py saved_money = 1000
2、定义发工资模块 send_money，用来增加收入计算
3、定义工资查询模块 select_money，用来展示工资数额
4、定义一个start.py ，启动文件展示最终存款金额
启动函数按顺序执行：从上到下
先按导入的顺序执行语句，去money.py中执行语句，即输入当前存款金额，然后去send_money.py中从上到下执行，不执行导入和函数定义
再往下执行然后执行到main，开始进入函数执行，调用函数时再去被调用函数内部执行，被调用模块内，被调用函数的外的不再执行
如果被调用函数又调用其他函数，方法一样"""

from homework.saveMoney.money import saved_money
from homework.saveMoney.send_money import send_Money
# print('start.py main')
# print(__name__)

if __name__ == '__main__':
    # print('我是main下第一句话')
    sumSalary = send_Money(saved_money)
    # print('我已完成send_money执行，下面是打印最后一句话')
    print(f'您的原有存款{saved_money}元，发工资之后存款变为{sumSalary}')