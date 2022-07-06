import csv
import os.path
from pathlib import Path
from collections import namedtuple

from HwHelper.HwMySqlConnection import MySqlConnection
from HwModels.EstimateModel import estimateModel
from HwConfig.HwConfigs import HwConfigs
from HwHelper.HwRequest import HwRequest
from HwHelper.HwSpliteFile import HwSpliteFile

class HwRenderData:
    fileExtension = ".csv"
    file = ""

    def __init__(self):
        self.mysql = MySqlConnection()
        self.BasePath = HwConfigs().urlPath()
        self.hwRequest = HwRequest()
        # pass

    def setArea(self,minYear,maxYear):
        for i in range(minYear, maxYear + 1):

            # self.readFileSection(i)

            # filePath = self.BasePath + str(i) + self.fileExtension
            # my_file = Path(filePath)
            # if my_file.is_file():
            print(str(i) + "file site --------")
                # HwSpliteFile().spliteFile(i)
                # self.readFile(filePath)
            self.readFileSection(i)
            # else:
            #     pass


    def readFileSection(self,year):
        for i in range(1,50):
            filePath = self.BasePath + str(year) + "-" + str(i) + self.fileExtension
            spilteFile = Path(filePath)
            if spilteFile.is_file():
                self.readFile(spilteFile,year,i)
                # print(filePath + "is exisit")
            else:
                pass


    def readFile(self,file,year,item):
        with open(file) as f:
            f_csv = csv.reader(f)
            headings = next(f_csv)
            # Row = namedtuple('Row', headings)
            i = 0
            for r in f_csv:
                if year == 2014 and item<=19:
                    if i < 74648:
                        i += 1
                        continue

                model = estimateModel()
                data = model.toDict(headings,r)
                sql =  model.insertItem(data)
                self.mysql.insert(sql)

                i += 1
                print(file)
                print(i)


