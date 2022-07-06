from typing import Dict

import pymysql
from HwHelper.HwPageHelper import  HwPageHelper

class HwSqlHelper:
    conditions = []
    select = ""
    order = ""

    def __init__(self,TableName):
        self.TableName =  TableName

    def insert(self,attributes,values):
        sql = """INSERT INTO %s(""" % self.TableName
        for i in range(0,len(attributes)):
            if i==len(attributes)-1:
                sql += attributes[i]["name"]
            else:
                sql += attributes[i]["name"] + ","
        sql += ") VALUES ("

        for j in range(0,len(attributes)):
            if j==len(attributes)-1:
                if values[attributes[j]["name"]]:
                    val = str(values[attributes[j]["name"]])
                    val = val.replace("\"", "\'")
                    sql += """\"""" + val +"""\""""
                else:
                    if attributes[j]["type"] != "string":
                        sql += "0"
                    else:
                        sql += "\'\'"
            else:
                if values[attributes[j]["name"]]:
                    val = str(values[attributes[j]["name"]])
                    val = val.replace("\"","\'")
                    sql += """\""""+ val +"""\" ,"""
                else:
                    if attributes[j]["type"] != "string":
                        sql += "0,"
                    else:
                        sql += "\'\',"
        sql += ")"
        return sql




    def count(self):
        sql = "select count(*) from %s " % self.TableName
        if len(self.conditions) > 0:
            sql += " where "
            for condition in self.conditions:
                sql += condition
        return sql


    def addAndCondition(self,colum,value,option = "="):
        if not option:
            option = "="
        condition = ""
        if len(self.conditions)>0:
            condition = " and %s %s %s " % (colum,option,value)
        else:
            condition = " %s %s %s " % (colum,option,value)

        self.conditions.append(condition)



    def addOrCondition(self,colum,value,option):
        if not option:
            option = "="
        condition = ""
        if len(self.conditions)>0:
            condition = " or %s %s %s " % (colum,option,value)
        else:
            condition = " %s %s %s " % (colum,option,value)

        self.conditions.append(condition)


    def addAndBetweenCondition(self,colum,val1,val2):
        condition = ""
        if len(self.conditions)>0:
            condition = " and %s between %s and %s " % (colum,val1,val2)
        else:
            condition = " %s between %s and %s " % (colum,val1,val2)
        self.conditions.append(condition)


    def addOrBetweenCondition(self,colum,val1,val2):
        condition = ""
        if len(self.conditions)>0:
            condition = " or %s between %s and %s " % (colum,val1,val2)
        else:
            condition = " %s between %s and %s " % (colum, val1, val2)
        self.conditions.append(condition)


    def orderBy(self,colum,desc):
        self.order = " order by %s %s " % (colum,desc)

    def setSelect(self,selectStr):
        self.select = selectStr

    def setPageHelper(self,pageHelper:HwPageHelper):
        self.pageHelper = pageHelper


    def toSql(self):
        sql = ""
        if self.pageHelper:
            if self.select:
               sql += self.select
            else:
                sql += "select * "

            sql += " from %s " % self.TableName

            for conds in self.conditions:
                sql += conds

            if self.order:
                sql += self.order

            if self.pageHelper:
                sql += " limit %d offset %d " % (self.pageHelper.limit,self.pageHelper.getOffset())

        return sql

    def update(self,condition,values:Dict):
        sql = "update %s set " % self.TableName
        for item in values:
            sql +=  " %s = \'%s\' " % (item,values[item])

        sql += " where %s " % condition

        return sql

