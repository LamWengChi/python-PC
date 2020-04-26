import pymysql
class MySQLPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host='localhost',
            port=3306,
            db='Lianjia',
            user='root',
            passwd='ddd123',
            charset='utf8',
            use_unicode=True)
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        self.cursor.execute(
            """insert into lianjia(title, atime,allprice,price ,addtime) value (%s, %s,%s,%s,%s)""",
            (item['title'],
             item['atime'],
             item['allprice'],
             item['price'],
             item['addtime'],))
        self.connect.commit()
        return item

