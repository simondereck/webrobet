import time
import datetime


class HwTool:

    def __init__(self):
        pass

    def getDay(self):
        return time.strftime("%Y-%m-%d", time.localtime())

    def getTime(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def getYesterday(self):
        today = datetime.date.today()
        oneday = datetime.timedelta(days=1)
        yesterday = today - oneday
        return yesterday.strftime("%Y-%m-%d")

    def getTimeStamps(self,date):
        timeArray = time.strptime(date, "%Y-%m-%d %H:%M:%S")
        return int(time.mktime(timeArray))

