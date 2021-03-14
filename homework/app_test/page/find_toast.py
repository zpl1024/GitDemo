from homework.app_test.framwork.basepage import basepage


class FindToast(basepage):
    #在当前添加方式页面上定位toast，并返回toast的text属性
    def find_toast(self):
        toast_ele = self.steps('../page/findtoast.yml','find_toast')
        toast_name = toast_ele.get_attribute('text')
        return toast_name