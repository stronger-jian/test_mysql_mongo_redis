from pymongo import MongoClient
from datetime import datetime
from bson.objectid import ObjectId


class TestMongo(object):
    ''' 连接数据 '''
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client['students']
		
    def add_one(self):
        ''' 新增一条数据 '''
        post = {
            'title': '文章标题',
            'content': '文章内容',
            'created_at': datetime.now()
        }
        return self.db.posts.insert_one(post)
		
    def add_many(self):
        ''' 新增多条数据 '''
        return self.db.students.insert_many([{'x':i} for i in range(2)])
		
	#查询数据
    def get_one(self):
        ''' 查询一条数据 '''
        return self.db.students.find_one()
		
    def get_many(self):
        ''' 查询多条数据 '''
        return self.db.students.find({'x':1})
	
    def get_by_oid(self,oid):
        ''' 根据_id 查询数据 '''
        oid= ObjectId(oid)
        return self.db.students.find({'_id':oid})

    def update(self):
        ''' 修改数据 '''
        #修改一条数据
        #return self.db.students.update_one({'x':0},{'$inc':{'x':100}})
		
        #修改多条数据
        return self.db.students.update_many({},{'$inc':{'x':100}})
		
    def delete(self):
        ''' 删除数据 '''
        #删除一条数据
        #return self.db.students.delete_one({'x':100})
        #删除duo条数据
        return self.db.students.delete_many({'x':100})
		
def main():
    obj = TestMongo()
    #rest=obj.add_many()
    #print(rest.inserted_ids)
	
    #rest=obj.get_many()
    #for item in rest:
        #print(item['_id'])
    #rest=obj.get_by_oid('5b74dd8b5d880ab39577fbc0')
    #print(rest)
	
    #rest=obj.update()
    #print(rest.matched_count)
    #print(rest.modified_count)
    rest=obj.delete()
    print(rest.deleted_count)
	
		
if __name__ == '__main__':
        main()