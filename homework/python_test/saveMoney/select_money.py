"""原有存款 1000元， 发工资之后存款变为2000元
定义模块
1、money.py saved_money = 1000
2、定义发工资模块 send_money，用来增加收入计算
3、定义工资查询模块 select_money，用来展示工资数额
4、定义一个start.py ，启动文件展示最终存款金额"""


def select_money():
    s = int(input("请输入工资："))
    return s

# def send_Money(save_money):
#     salary=select_money()
#     sum=salary+save_money
#     return sum
