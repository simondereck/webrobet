from HwModels.DbModel import  DbModel
from HwHelper.HwMySqlConnection import MySqlConnection
import time

class AlarmModel(DbModel):

    def __init__(self):
        self.TableName = "hw_alarm"
        super().__init__()
        #
        # long id; # long totalAnnonces;# long successAnnonces;# long contractAnnonces;# long
        # emptyAnnonces;# String utime;# String date;# String ctime;

    def attributes(self):
        return [
            {"name":"id","type":"int"},
            {"name":"total_annonces","type":"int"},
            {"name":"success_annonces","type":"int"},
            {"name":"contract_annonces","type":"int"},
            {"name":"empty_annonces","type":"int"},
            {"name":"utime","type":"string"},
            {"name":"ctime","type":"string"}
        ]


    def toArray(self,value):
        attrs = self.attributes()
        dict = {}
        for j in range(0, len(attrs)):
             dict[attrs[j]["name"]] = value[j]
        return dict




    def findAlarmByDate(self,date):
        self.sqlHelper.conditions.clear()
        self.sqlHelper.addAndCondition("date","\'%s\'" % date)
        sql = self.getOne()
        # print(sql)
        sqlConn = MySqlConnection()
        return sqlConn.one(sql)
