'''
	if __name__ == '__main__'的意思是：当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行；
	当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行。
	https://blog.csdn.net/yjk13703623757/article/details/77918633
'''
import pymysql

# Connect to the database
class MysqlSearch(object):
	def __init__(self):
		self.get_conn()

	def get_conn(self):
		self.connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='lijian123',
                             db='news',
                             charset='utf8mb4')
	
	def close_conn(self):
		if self.connection:
			self.connection.close()
	
	def get_one(self):
		#建立cursor
		cursor = self.connection.cursor()
		#创建sql
		sql = 'SELECT * FROM `news` where `types`=%s ORDER BY `created_at` DESC;'
		#执行sql
		cursor.execute(sql,('百家',))
		#print(cursor)
		#print(dir(cursor))  得到cursor的 执行命令
		#print(cursor.rowcount) 
		#fetchone()得到单条数据
		#print(cursor.description)
		rest=dict(zip([k[0] for k in cursor.description],cursor.fetchone()))
		#print(rest['title'])
		#result= cursor.fetchone()
		
	
		#处理数据
		#关闭cursor/链接
		cursor.close()
		self.close_conn()
		return rest
		
	def get_more(self, page, page_size):
		offset=(page-1)*page_size
		#建立cursor
		cursor = self.connection.cursor()
		#创建sql
		sql = 'SELECT * FROM `news` where `types`=%s ORDER BY `created_at` DESC LIMIT %s,%s;'
		#执行sql
		cursor.execute(sql,('百家',offset,page_size))
		rest=[dict(zip([k[0] for k in cursor.description],row))for row in cursor.fetchall()]
		
		cursor.close()
		self.close_conn()
		return rest
		
	#插入数据
	def add_one(self):
		try:
			#sql语句
			sql="INSERT INTO `news` \
				(`title`, `content`, `author`,`is_valid`)\
				VALUE \
				(%s,%s,%s,%s);"
			#获取链接和cursor
			cursor = self.connection.cursor()
			#执行sql
			#提交数据 到数据库
			cursor.execute(sql, ('hello5','hello world3','stronger-jian',1))
			cursor.execute(sql, ('hello6','hello world4','stronger-jian',1,1))
			#提交事务
			self.connection.commit()
			#关闭cursor和链接
			cursor.close()
		except:
			print('error')
			
			#self.connection.commit()  这样会继续提交  没有出错的
			self.connection.rollback()
			
		self.close_conn()
	
def main():
	obj=MysqlSearch()
	#rest=obj.get_one()
	#print(rest['title'])
	#rest=obj.get_more(1,5)
	#for item in rest:
	#	print(item['title'])
	obj.add_one()
	
		
if __name__ == '__main__':
		main()
'''
zip就是把2个数组糅在一起
x=[1, 2, 3, 4, 5 ]
y=[6, 7, 8, 9, 10]
zip(x, y)就得到了
[(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]
'''
		
