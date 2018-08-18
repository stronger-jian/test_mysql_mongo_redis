import pymysql
# Connect to the database

connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='lijian123',
                             db='news',
                             charset='utf8mb4')
try:
	#获取操作游标 cursor
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM `news` ORDER BY `created_at` DESC;"
        cursor.execute(sql)
		
		# 使用 fetchone() 方法获取单条数据.
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()
