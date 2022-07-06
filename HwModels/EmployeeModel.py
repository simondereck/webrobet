from HwModels.DbModel import DbModel
from HwHelper.HwMySqlConnection import MySqlConnection
import json

class EmployeeModel(DbModel):

    def __init__(self):
        self.TableName = "hw_admin_employee_model"
        super().__init__()


    uid:int

    date:str

    id:int

    utime:str

    ctime:str

    detail:str

    opt = 0

    breaktimes = 0

    items = []

    def attributes(self):
        return [
            {"name":"id","type":"int"},
            {"name":"date","type":"string"},
            {"name":"uid","type":"int"},
            {"name":"utime","type":"string"},
            {"name":"ctime","type":"string"},
            {"name":"detail","type":"string"}
        ]

    def saveModel(self):
        sql = "INSERT INTO %s(date,uid,utime,ctime,detail,opt,breaktimes)" % self.TableName
        sql += " VALUES(\'%s\',%d,\'%s\',\'%s\',\'%s\',%d,%d)" % \
               (self.date,self.uid,self.utime,self.ctime,json.dumps(self.items),self.opt,self.breaktimes)
        return sql

    def save(self,sql):
        myConn = MySqlConnection()
        myConn.insert(sql)