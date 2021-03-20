#打开terminal，在该脚本目录下执行mitmdump -s test_maplocal.py，开启代理服务，将app设置mitmproxy代理，即可代理到脚本里。
import json
import mitmproxy
from mitmproxy import ctx, http
#模拟map local模式
class Counter:

    def response(self, flow:mitmproxy.http.HTTPFlow):
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json" \
                in flow.request.pretty_url:
        # 打开文件，读取文件数据，作为响应返回
            with open("resp_mockdata.json", encoding="utf-8") as f:
                data = json.load(f)
            flow.response.text = json.dumps(data)
addons = [
    Counter()
]