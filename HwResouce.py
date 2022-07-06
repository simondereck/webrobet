import requests
from urllib import request
import gzip
from HwConfig.HwConfigs import HwConfigs


class HwResouce:
    path = "https://cadastre.data.gouv.fr/data/etalab-dvf/latest/csv/"
    filename = "/full.csv.gz"

    fileExtension = ".csv.gz"

    def __init__(self):
        self.BasePath = HwConfigs().urlPath()
        pass


    def setArea(self,minYear,maxYear):
        print("minYear",minYear)
        print("maxYear",maxYear)
        for i in range(minYear,maxYear+1):
            isFile = self.isFileExist(i)
            if isFile:
                print(str(i)+ " file exist --------- ")
                self.download(i)
            else:
                print(str(i) + " not exist")

    def isFileExist(self,year):
        url = self.path + str(year) + self.filename

        try:
            with request.urlopen(url) as file:
                if file.status == 200:
                    return True
                else:
                    return False
        except IOError:
            return False

    def download(self,year):
        url = self.path + str(year) + self.filename
        r = requests.get(url)
        with open(self.BasePath+str(year)+".csv.gz", "wb") as code:
            code.write(r.content)
        print("fini download the file", year)
        self.ungzip(year)


    def ungzip(self,year):
        # 获取文件的名称，去掉后缀名
        print("unzip file")
        file = self.BasePath+str(year) + self.fileExtension
        newFile = file.replace(".gz", "")
        # 开始解压
        g_file = gzip.GzipFile(file)
        # 读取解压后的文件，并写入去掉后缀名的同名文件（即得到解压后的文件）
        open(newFile, "wb+").write(g_file.read())
        g_file.close()

