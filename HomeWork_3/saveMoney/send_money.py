"""原有存款 1000元， 发工资之后存款变为2000元
定义模块
1、money.py saved_money = 1000
2、定义发工资模块 send_money，用来增加收入计算
3、定义工资查询模块 select_money，用来展示工资数额
4、定义一个start.py ，启动文件展示最终存款金额

在被start.py调用时，start.py的函数名__name__为__main__
但是本模块中的函数名__name__为HomeWork_3.saveMoney.send_money，
不是__main__,所以下面if条件不成立，模块函数入口不执行"""
# print('我是send_money 导入前的第一句话:')
from HomeWork_3.saveMoney.select_money import select_money


# print('我是send_money 导入下的第一句话:')

def send_Money(save_money):
    # print('我是send_money 函数里第一句话:')
    salary = select_money()
    sums = salary + save_money
    return sums


# print('send_money name:')
# print(__name__)

if __name__ == '__main__':
    print('send_money inside_name')
    print(__name__)
