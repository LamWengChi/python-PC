import pymysql
class MySQLPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host='localhost',
            port=3306,
            db='JD',
            user='root',
            passwd='ddd123',
            charset='utf8',
            use_unicode=True)
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        self.cursor.execute(
            """insert into seleniumjd(url, name_s, price, comment) value (%s, %s,%s,%s)""",
            (item['url'],
             item['name_s'],
             item['price'],
             item['comment'],
             ))
        self.connect.commit()
        return item

