from time import sleep

from homework.app_test.conftest import root_log
from homework.app_test.framwork.basepage import basepage


class delete_result(basepage):
    def search_result(self):
        sleep(3)
        ele = self.steps('../page/delete_result.yml', 'search_result')
        root_log.info(ele.text)
        assert ele.text == "无搜索结果"