import json

from HwRobortRequest.HwRequest import HwRequest


class Country:
    def __init__(self):
        self.data_url = "https://raw.githubusercontent.com/zhaoweih/countries_json/master/countries.json"
        self.post_url = "https://api.ejoymarket.com/backend/data/country/create"
        # self.post_url = "http://localhost:3001/backend/data/country/create"
        pass

    def getData(self):
        hwRequest = HwRequest()
        hwRequest.setUrl(self.data_url)
        result = hwRequest.getResult()
        data = json.loads(result)
        for item in data:
            params = {
                "name": item["chinese"],
                "english": item["english"],
                "spell": item["spell"],
                "french": item["french"],
                "italian": item["italian"],
                "spanish": item["spanish"],
                "japanese": item["japanese"],
                "germen": item["germen"],
                "code": item["code"],
                "abbr": item["abbr"],
                "russian": item["russian"],
            }

            print(params)
            res = hwRequest.postByData(self.post_url,params)
            print(res.status_code)
            # break
        pass


country = Country()
country.getData()
