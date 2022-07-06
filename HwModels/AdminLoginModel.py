from HwModels.DbModel import DbModel
from HwHelper.HwMySqlConnection import MySqlConnection

class AdminLoginModel(DbModel):


    # public long id;
    # public long uid;
    # public String etime; //记录时间
    # public String date; //日期
    # public String ctime; //创建时间
    def __init__(self):
        self.TableName = "hw_admin_login"
        super().__init__()

    def attributes(self):
        return [
            {"name":"id","type":"int"},
            {"name":"uid","type":"int"},
            {"name":"etime","type":"string"},
            {"name":"date","type":"string"},
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


    def getAllByDate(self,date):
        sqlConn = MySqlConnection()
        self.sqlHelper.addAndCondition("date","\'%s\'" % date)
        sql = self.getAll()
        return sqlConn.all(sql)
