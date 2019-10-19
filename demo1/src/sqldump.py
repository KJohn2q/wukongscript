import pymysql
import sys

class Sqldump():

    conn = None

    def __init__(self):
        self.cursor = self.get_conn()

    def get_conn(self):

        if self.conn is None:
            try:
                self.conn = pymysql.connect(host='114.115.157.72', user = 'root', password = 'shibajiang@#', db = 'wukong', port=3306, charset = 'utf8')
            except:
                print("连接失败");

        cursor = self.conn.cursor()
        return cursor

    def insert_data(self, data):

        sql = "insert into m_tags(concern_id, name) value(%s, %s)"

        for i in range(len(data)):

            temp_arr = []

            for key,value in data[i].items():
                temp_arr.append(value)

            param = tuple(temp_arr)

            try:
                self.conn.ping(reconnect=True)
                count = self.cursor.execute(sql, param)
            except:
                print("网络延迟，请稍后再试")
        # 提交事务
        self.conn.commit()

    def select_data(self):

        sql = "select distinct concern_id from m_tags"

        # 查询数据
        try:
            self.conn.ping(reconnect=True)
            self.cursor.execute(sql)
        except:
            print("网络延迟，请稍后再试")
        # 获取数据
        tags = self.cursor.fetchall();

        return tags

    def close_conn(self):

        # 关闭资源连接
        self.cursor.close()
        self.conn.close()
