from typing import Dict

from HwModels.DbModel import DbModel

class VilleModel(DbModel):

    def __init__(self):
        self.TableName = "hw_ville"
        super().__init__()

    # id, code, ctime, label, lat, lng, name, postcode, utime
    def attributes(self):
        return [
            {"name":'id','type':'int'},
            {"name":"code","type":"int"},
            {"name":"lat","type":"string"},
            {"name":"lng","type":"string"},
            {"name":"name","type":"string"},
            {"name":"postcode","type":"string"}
        ]


    def toArray(self,values):
        attrs = self.attributes()
        data = []
        for i in range(0, len(values)):
            dict = {}
            for j in range(0, len(attrs)):
                 dict[attrs[j]["name"]] = values[i][j]
            data.append(dict)
        return data


