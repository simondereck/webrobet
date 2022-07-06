from HwModels.DbModel import DbModel
from HwHelper.HwTool import HwTool
import difflib

class NeufModel(DbModel):

    id:int
    images:str
    address_full:str
    description:str
    status:int

    def __init__(self):
        self.TableName = "hw_neuf_model"
        super().__init__()

    # programe["name"] = rows[i].find("div", {"class": "ProgramCard_name__1t0JA"}).text
    # programe["location"] = rows[i].find("div", {"class": "ProgramCard_location__3Xaq8"}).text
    # programe["href"] = rows[i].find("a", {"class": "ProgramCard_link__2e-NJ"})["href"]
    # programe["style"] = rows[i].find("a", {"class": "ProgramCard_link__2e-NJ"})["style"]
    # programe["status"] = rows[i].find("div", {"class": "Pill_red__1TKZ9"}).text
    # programe["date"]


    def attributes(self):
        return [
            {"name":"title","type":"string"},
            {"name":"location","type":"string"},
            {"name":"href","type":"string"},
            {"name":"status_string","type":"string"},
            {"name":"date","type":"string"},
            {"name":"style","type":"string"},
            {"name":"images","type":"string"}
        ]

    def setModel(self,item:dict):
        self.title = item["name"]
        self.address = item["location"]
        self.href = item["href"]
        self.style = item["style"]
        self.status = item["status"]
        self.date = item["date"]



    def insertItem(self,value):
        sql = """INSERT INTO %s(""" % self.TableName
        sql += "title,address,link,cover,status_string,date,utime,ctime,ville"
        sql += ")"
        sql += """ VALUES ("%s","%s","%s",'%s',"%s","%s","%s","%s",%d) """ % \
               (
                   self.title,
                   self.address,
                   self.href,
                   self.style,
                   self.status,
                   self.date,
                   HwTool().getTime(),
                   HwTool().getTime(),
                   0
               )
        return sql

    def getAll(self):
        sql = "select id,title,address,link,status_string from %s" % self.TableName
        return sql

    # id: int
    # images: str
    # address_full: str
    # description: str
    # status: int
    def updateDetail(self):
        sql = """update %s set images='%s',address_full="%s",description="%s" where id=%d""" % (self.TableName,self.images,self.address_full,self.description.replace("\"","'"),self.id)
        return sql

    def updateStatus(self):
        sql = "update %s set status=%d where id=%d" % (self.TableName,self.status,self.id)
        return sql


