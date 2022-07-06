# import mysql.connector
# import pymysql

import pymysql.cursors


class MySqlConnection:
    db = pymysql.connect(host='localhost',
                              user='root',
                              password='simon123',
                              database='hwwd')


    def __init__(self):
        self.cursor = self.db.cursor()
        pass



    def connet(self):
        pass

    def insert(self,sql):
        self.cursor.execute(sql)
        self.db.commit()
        pass


    def all(self,sql):
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            # 获取所有记录列表
            results = self.cursor.fetchall()
            return results
        except:
            print("Error: unable to fetch data")


    def one(self,sql):
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
            return result
        except:
            print("Error: find one error")


    def count(self,sql):
        try:
            self.cursor.execute(sql)
            res = self.cursor.fetchone()
            if res:
                return res[0]
            else:
                return 0
        except:
            print("ERROR : GET COUNT ERROR")

    def update(self,sql):
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
            print("success")
        except:
            # 发生错误时回滚
            print("Erro update error")
            self.db.rollback()

        # 关闭数据库连接

    # def __del__(self):
    #     self.db.close()