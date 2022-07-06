from urllib import request, parse
import json


class HwRequest:

    def __init__(self):
        pass

    def post(self,url,data):
        data = parse.urlencode(data).encode("ascii")
        res = request.urlopen(url, data=data).read()
        print(res)


    def postJson(self,url,data):
        # Data dict
        # data = {'test1': 10, 'test2': 20}
        data = json.dumps(data)
        # Convert to String
        data = str(data)
        # Convert string to byte
        data = data.encode('utf-8')
        # Post Method is invoked if data != None
        req = request.Request(url, data = data)
        # Response
        resp = request.urlopen(req)

        html = resp.read()

        print(html)