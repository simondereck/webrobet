from typing import Dict

from HwHelper.HwMySqlConnection import MySqlConnection
from HwHelper.HwSqlHelper import HwSqlHelper
from HwHelper.HwPageHelper import HwPageHelper

class DbModel:

    TableName = ""
    #
    # def setPageHelper(self,pageHelper:HwPageHelper):
    #     self.pageHelper = pageHelper

    def attributes(self):
        return []

    def __init__(self):
        self.sqlHelper = HwSqlHelper(self.TableName)
        # super().__init__()


    def toDict(self,heads,value):
        attrs = self.attributes()
        dict = {}
        for i in range(0, len(attrs)):
            for j in range(0,len(heads)):
                if attrs[i]["name"] == heads[j]:
                    dict[attrs[i]["name"]] = value[j]
        return dict

    def insertItem(self,value):
        # self.sqlHelper = HwSqlHelper(self.TableName)
        sql = self.sqlHelper.insert(self.attributes(), value)
        return sql

    def insertItemByAttributeAndValue(self,attribute,value):
        pass


    def getCountBySql(self):
        sql = self.sqlHelper.count()
        return sql

    def getOne(self):
        sql = self.toSelect()
        sql += " from %s where " %self.TableName
        for conditon in self.sqlHelper.conditions:
            sql +=  "%s " % conditon
        sql += " limit 1"
        return sql

    def getItems(self):
        pass

    def toSelect(self):
        selectStr = "select "
        for i in range(0,len(self.attributes())):
            if i == len(self.attributes())-1:
                selectStr += "`" + self.attributes()[i]["name"] + "`"
            else:
                selectStr += "`" + self.attributes()[i]["name"] + "`" + ","
        return selectStr

    def getAllByPage(self,pageHelper:HwPageHelper):
        # self.sqlHelper = HwSqlHelper(self.TableName)
        self.sqlHelper.setSelect(self.toSelect())
        self.sqlHelper.setPageHelper(pageHelper)
        return self.sqlHelper.toSql()

    def getAll(self):
        sql = self.toSelect()
        sql += " from %s where" % self.TableName
        for conn in self.sqlHelper.conditions:
            sql += conn

        return sql


    def update(self,condition,values:Dict):
        # self.sqlHelper = HwSqlHelper(self.TableName)
        return self.sqlHelper.update(condition,values)

        # self.sqlHelper.setSelect(self)
        # self.sqlHelper.
