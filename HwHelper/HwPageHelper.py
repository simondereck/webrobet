import math

class HwPageHelper:
    limit = 20
    count = 0
    currentPage = 0
    page = 0
    offset = 0
    # select * from hw_ville where xxxx order by id desc offset 1000 limit 10000

    def __init__(self):
        pass

    def setLimit(self,limit):
        self.limit = limit

    def setCount(self,count):
        self.count = count


    def setCurrentPage(self,page):
        # self.page = math.ceil(self.count/self.limit)
        if self.page < page:
            self.currentPage = 0
            return

        self.currentPage = page

    def getPages(self):
        self.page = math.ceil(self.count/self.limit)
        return self.page

    def getOffset(self):
        # self.page = math.ceil(self.count/self.limit)
        self.offset = self.currentPage * self.limit
        return self.offset

