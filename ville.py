from HwModels.VilleModel import VilleModel
from HwHelper.HwMySqlConnection import MySqlConnection
from HwHelper.HwPageHelper import HwPageHelper
if __name__ == '__main__':

    model = VilleModel()
    sql = model.getCountBySql()


    sqlConn = MySqlConnection()
    count = sqlConn.count(sql)
    pageHelper = HwPageHelper()
    pageHelper.setCount(count)
    pageHelper.setLimit(1000)
    m = 0
    for i in range(0,pageHelper.getPages()):
        pageHelper.setCurrentPage(i)
        sql = model.getAllByPage(pageHelper)
        res = sqlConn.all(sql)
        result = model.toArray(res)
        for item in result:
            if(len(item["postcode"])<5):
                # print(item)
                item["postcode"] = "0%s" % item["postcode"]
                m = m + 1
                condition = "id = %d " % item["id"]
                sql = model.update(condition,{"postcode":item["postcode"]})
                print(sql)
                sqlConn.update(sql)

    print("in total :")
    print(m)

        # break