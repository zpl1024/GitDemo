
class calculator:
    #加法方法
    def add_func(self,a,b):
        sum = a + b
        #浮点数相加时，有时候小数点后会很长，需要截断处理
        if type(a) == float and type(b) == float:
            # print(f'sum为{sum}，要把sum截断到小数后{max(len(str(a)),len(str(b)))}位')
            return round(sum,max(len(str(a)),len(str(b))))
        else:
            return sum
    #减法方法
    def sub_func(self,a,b):
        sub = a - b
        if type(a) == float and type(b) == float:
            return round(sub, max(len(str(a)), len(str(b))))
        else:
            return sub
    #除法方法
    def div_func(self,a,b):
        if b==0:
            print("除数不能为0")
            return 0
        else:
            div = a / b
            return div
    #乘法方法
    def mul_func(self,a,b):
        mul = a * b
        if type(a) == float and type(b) == float:
            # print(f'sum为{sum}，要把sum截断到小数后{max(len(str(a)),len(str(b)))}位')
            return round(mul,max(len(str(a)),len(str(b))))
        return mul

