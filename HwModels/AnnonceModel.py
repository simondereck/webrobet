from HwModels.DbModel import DbModel
from HwHelper.HwMySqlConnection import MySqlConnection
class AnnonceModel(DbModel):

    def __init__(self):
        self.TableName = "hw_annonce"
        super().__init__()


    def attributes(self):
        return [
            {"name":"id","type":"int"},
            {"name":"status","type":"int"},
            {"name":"type","type":"int"},
            {"name":"cover","type":"string"},
            {"name":"imgs_json","type":"string"},
            {"name":"ctime","type":"string"}
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


    def getAllCountsByStatus(self):
        data = {}

        sql = self.getCountBySql()
        sqlConn = MySqlConnection()
        count = sqlConn.count(sql)
        data[0] = count

        self.sqlHelper.addAndCondition("status", 1, "=")
        sql = self.getCountBySql()
        count1 = sqlConn.count(sql)
        data[1] = count1

        self.sqlHelper.conditions.clear()
        self.sqlHelper.addAndCondition("status", 2, "=")
        sql = self.getCountBySql()
        count2 = sqlConn.count(sql)
        data[2] = count2

        self.sqlHelper.conditions.clear()
        self.sqlHelper.addAndCondition("status", 3, "=")
        sql = self.getCountBySql()
        count3 = sqlConn.count(sql)
        data[3] = count3
        return data