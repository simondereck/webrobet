from HwModels.AdminLoginModel import AdminLoginModel
from HwHelper.HwTool import HwTool
from HwModels.EmployeeModel import  EmployeeModel

if __name__ == '__main__':
    loginModel = AdminLoginModel()
    tool = HwTool()
    date = tool.getYesterday()
    # date = tool.getDay()
    # date = "2021-03-03"
    res = loginModel.getAllByDate(date)
    arr = loginModel.toArray(res)
    data = {}
    for item in arr:
        if item["uid"] in data:
            data[item["uid"]].append(item)
        else:
            data[item["uid"]] = []
            data[item["uid"]].append(item)

    for dkey in data:
        dalist = data[dkey]
        employee = EmployeeModel()
        dateTime = tool.getTime()
        employee.utime = dateTime
        employee.ctime = dateTime

        stamps0 = 0
        for i in range(0,len(dalist)):
            stamps = tool.getTimeStamps("%s %s" % (dalist[i]["date"],dalist[i]["etime"]))
            if stamps - stamps0 > 60*30:
                # print(stamps)
                if i-1>0:
                    employee.breaktimes = employee.breaktimes + 1
                    dalist[i-1]["lasted"] = True
                    employee.items.append(dalist[i-1])
                dalist[i]["lasted"] = False
                employee.uid = dalist[i]["uid"]
                employee.date = dalist[i]["date"]
                employee.items.append(dalist[i])
            else:
                employee.opt = employee.opt + 1

            stamps0 = stamps

        sql = employee.saveModel()
        employee.save(sql)



