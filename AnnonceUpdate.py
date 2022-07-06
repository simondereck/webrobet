from HwModels.AnnonceModel import AnnonceModel
from HwHelper.HwMySqlConnection import MySqlConnection
import json

if __name__ == '__main__':
    model = AnnonceModel()
    # sql = model.getCountBySql()
    conn = MySqlConnection()
    sql = model.toSelect() + " from %s " % model.TableName
    print(sql)
    result = conn.all(sql)
    models = model.toArray(result)
    # print(models)
    for m in models:
        if m["cover"]==None or m["cover"]=="":
            if m["imgs_json"] and m["imgs_json"]!="null":
                imgs = json.loads(m["imgs_json"])
                for im in imgs:
                    if im != None:
                        updateSql = model.update("id=%d" % m["id"],{"cover":im})
                        conn.update(updateSql)
                        print(im)
                        break
            # print(imgs)
            # print(m["imgs_json"])
            # print(json.loads(m["imgs_json"]))
        # if m["imgs_json"] and m["imgs_json"]!="null":
        #     print(m["imgs_json"])
        # conn.update(updateSql)
    pass