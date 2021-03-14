import yaml
def test_steps():
    path = '../page/search.yml'
    func = 'search_staff'
    with open(path, encoding='utf-8') as f:
        datas: list = yaml.safe_load(f)
        print(datas)
        print(type(datas))

        # 取出yaml中key为func的字典列表
        for data in datas:
            print(data.keys())
            if func in data.keys():
                print(data[func])
                steps: list[dict] = data[func]

                for step in steps:
                    if 'by' in step.keys():
                        BY = step['by']
                        Locator = step['locator']
                    if 'action' in step.keys():
                        if 'click' == step['action']:
                            print('click')
                        # elif 'send' == step['action']:
                        #     # 将yaml中一个step里的变量传给content
                        #     content: str = step['keys']
                        #     # 遍历params的keys，和当前content存的比较，有的话就用param的value来替换
                        #     for param in params.keys():
                        #         content = content.replace(f'{param}', self.params[param])
                        #     element.send_keys(content)
                        # elif 'croll_find_click' == step['action']:
                        #     search_element = step['text']
                        #     self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                        #                              'new UiScrollable(new UiSelector().'
                        #                              'scrollable(true).instance(0)).'
                        #                              'scrollIntoView(new UiSelector().'
                        #                              f'text("{search_element}").instance(0));').click()
                    # if 'sleep' in step.keys():
                    #     sleep(step['sleep'])
                    if 'name' in step.keys():
                        if 'toast' == step['name']:
                            BY = step['by']
                            lOCATOR = step['locator']
                            print(f'{BY},{lOCATOR}')
                        if 'caps' == step['name']:
                            appPackage = step['appPackage']
                            appActivity = step['appActivity']
                            print(f'{appPackage},{appActivity}')