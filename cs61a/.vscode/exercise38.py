#导入与连接数据库
import sqlite3
db = sqlite3.connect("n.db")
#创建表
db.execute("CREATE TABLE nums AS SELECT 2 UNION SELECT 3")
#插入数据
db.execute("INSERT INTO nums VALUES (?),(?),(?);", range(4, 7))
#查询数据
print(db.execute("SELECT * FROM nums;").fetchall())
#提交更改
db.commit()



