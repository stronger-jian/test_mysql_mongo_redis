import redis


class TestSet(object):
    def __init__(self):
        self.r=redis.StrictRedis(host='localhost', port=6379, db=0)
        
    def t_sadd(self):
        l=['cat','tiger']
        rest=self.r.sadd('zoo10',*l)
        print(rest)
        rest=self.r.smembers(rest)
        print(rest)
       
    def t_srem(self):
        rest=self.r.srem('zoo10','cat')
        print(rest)
        rest=self.r.smembers(rest)
        print(rest)
        
        
    def t_sinter(self):
        rest=self.r.sinter('zoo','zoo1')
        # for r in rest:
        print(rest)
        
    
def main():
    obj=TestSet()
    obj.t_sinter()
    
if __name__ == '__main__':
        main()