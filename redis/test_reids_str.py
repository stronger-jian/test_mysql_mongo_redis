#reedis-py
import redis


class TestString(object):
# r = redis.StrictRedis(host='localhost', port=6379, db=0)
    def __init__(self):
        self.r=redis.StrictRedis(host='localhost', port=6379, db=0)
        
    def test_set(self):
        ''' 使用set '''
        rest=self.r.set('user2','nihao')
        print(rest)
        return rest
        
    def test_get(self):
        ''' 使用get '''
        rest=self.r.get('user2')
        print(rest)
        return rest
        
    def test_mset(self):
        ''' mset 添加多个键值对 '''
        l={
            'user3':'hello',
            'user4':'world'
        }
        rest=self.r.mset(l)
        
    def test_mget(self):
        ''' 获取多个键值对 '''
        g=['user3','user4']
        rest=self.r.mget(g)
        print(rest)
        return rest
        
    def test_delete(self):
        ''' 删除数据 '''
        rest=self.r.delete('user3')
        print(rest)
        return rest
        
def main():
    obj=TestString()
    obj.test_delete()
     
     
if __name__ == '__main__':
        main()