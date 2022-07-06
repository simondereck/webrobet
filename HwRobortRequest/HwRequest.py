import urllib

import requests


class HwRequest:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.103 Safari/537.36'}

    encoding = "utf-8"

    def __init__(self):
        # 添加头部，伪装浏览器，字典格式

        # 增加headers参数
        # response = requests.get(url=url, headers=headers)
        # response.encoding = 'utf-8'
        # html = response.text
        # print(html)
        pass

    def setUrl(self, url):
        self.url = url

    def getResult(self):
        response = requests.get(url=self.url, headers=self.headers)
        response.encoding = self.encoding
        html = response.text
        return html

    def getByurlib(self):
        resquest = urllib.request.Request(url=self.url, headers=self.headers)
        response = urllib.request.urlopen(resquest).read()
        html = response.decode(self.encoding)
        return html

    def postByData(self, url, data: dict):
        # requests
        # resp = requests.post(URL, data=data, params=params,
        #                      verify=False, timeout=10)
        resp = requests.post(url, data)
        return resp
