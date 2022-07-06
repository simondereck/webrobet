from HwConfig.HwConfigs import HwConfigs
import csv
import os
class HwSpliteFile:
    fileExtension = ".csv"

    def __init__(self):
        self.path = HwConfigs().urlPath()

    def spliteFile(self,year):
        # if year<2019:
        #     return

        filePath = self.path + str(year) + self.fileExtension

        with open(filePath, 'r', newline='') as file:
            csvreader = csv.reader(file)
            a = next(csvreader)
            i = j = 0
            for row in csvreader:
                # 每128个就j加1， 然后就有一个新的文件名

                if i % 100000 == 0:
                    j += 1
                    print(f"csv {j} 生成成功")

                # if year == 2019:
                #     if j<29:
                #         i += 1
                #         continue

                newFilePath = self.path + str(year) + "-" + str(j) + self.fileExtension
                # 不存在此文件的时候，就创建
                if not os.path.exists(os.path.dirname(newFilePath)):
                    os.makedirs(os.path.dirname(newFilePath))
                    with open(newFilePath, 'w', newline='') as file:
                        csvwriter = csv.writer(file)
                        if i % 100000 == 0:
                            csvwriter.writerow(a)
                        csvwriter.writerow(row)
                    i += 1

                # 存在的时候就往里面添加
                else:
                    with open(newFilePath, 'a', newline='') as file:
                        csvwriter = csv.writer(file)
                        if i % 100000 == 0:
                            csvwriter.writerow(a)
                        csvwriter.writerow(row)
                    i += 1
                print(newFilePath)
                print(i)

