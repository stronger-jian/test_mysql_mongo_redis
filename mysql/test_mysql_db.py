#https://blog.csdn.net/u012965373/article/details/52315650  遇到了找不到SQLAlchemy的问题

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Boolean, DateTime

#获取链接
engine=create_engine('mysql+pymysql://root:lijian123@localhost:3306/new_test')
#基类模型
Base=declarative_base()
#Session，每当它用于与数据库对话时，一旦开始通信，就开始数据库事务处理 工厂模式
Session=sessionmaker(bind=engine)
class News(Base):
	__tablename__='news'
	id= Column(Integer,primary_key=True)
	title = Column(String(200), nullable=False)
	content = Column(String(2000), nullable=False)
	types = Column(String(10),nullable=False)
	author = Column(String(10))
	image = Column(String(30))
	created_at = Column(DateTime)
	is_valid = Column(Boolean)
	view_count = Column(Integer)
	

#Base.metadata.create_all(engine)


#创建session对象
#session=Session()
class Ormtest(object):
	def __init__(self):
		self.session=Session()
		
	def add_one(self):
		''' 插入一条数据 '''
		try:
			new_obj=News(
				title='title',
				content='content',
				types='百家')
			self.session.add(new_obj)
			self.session.commit()
		except:
			print('插入一条数据失败')
			session.rollback()
	
	def add_more(self):
		''' 插入多条数据 '''
		try:
			self.session.add_all([News(title='1title',content='content',types='百家'),News(title='2title',content='content',types='百家')])
			#self.session.add(new_obj)
			self.session.commit()
			#return new_obj
		except:
			print('插入多条数据失败')
			session.rollback()
			
	def get_one(self):
		''' 查询一条数据 '''
		return self.session.query(News).get(1)
	
	def get_more(self):
		''' 查询多条数据 '''
		return self.session.query(News).filter_by(is_valid=True)
		
	def update_one(self,pk):
		''' 修改一条数据 '''
		
		new_obj=self.session.query(News).get(pk)
		#if type(pk)!="<class 'int'>":
			#print('请输入一个整数')
		if new_obj:
			new_obj.is_valid=0
			self.session.add(new_obj)
			self.session.commit()
			print('插入一条数据成功')
			#return '插入一条数据成功'
		print('插入一条数据失败')
	
	def update_more(self):
		'''修改多条数据 '''
		date_list=self.session.query(News).filter_by(is_valid=False)
		for item in date_list:
			item.is_valid=1
			self.session.add(item)
		self.session.commit()
	
	def delete_one(self,pk):
		''' 删除数据 '''
		new_obj= self.session.query(News).get(pk)
		self.session.delete(new_obj)
		self.session.commit()
	
		
def main():
	orm=Ormtest()
	#rest=orm.add_more()
	#查询数据
	'''rest=orm.get_more()
	if rest:
		for x in rest:
			print('ID:{0}=>{1}'.format(x.title,x.content))'''
	#修改数据
	#orm.update_more()
	#删除数据
	orm.delete_one(1)
	
#测试函数 只在运行.py 的时候会运行
if __name__ == '__main__':
		main()