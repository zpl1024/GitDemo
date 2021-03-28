import yaml


class TestBase:
    def read_casedata(self):
        with open("testcase_data.yaml", encoding='UTF-8') as f:
            datas = yaml.safe_load(f)
            for key in datas.keys():
                if  key == 'address_data':
                    data = datas['address_data']
                    return data