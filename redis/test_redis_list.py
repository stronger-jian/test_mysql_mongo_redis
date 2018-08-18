import redis


class TestList(object):
    
    def __init__(self):
        self.r=redis.StrictRedis(host='localhost', port=6379, db=0)
    
    def test_push(self):
        # xulie=('zhangsan','lisi')
        xulie=['zhangsan','lisi']
        rest=self.r.lpush('li3',*xulie)
        print(rest)
        rest=self.r.lrange('li3',0,-1)
        print(rest)
        
    def test_pop(self):
        rest=self.r.lpop('li3')
        print(rest)
        rest=self.r.lrange('li3',0,-1)
        print(rest)
        
        
def main():
    obj=TestList()
    # obj.test_push()
    obj.test_pop()
     
if __name__ == '__main__':
        main()