# -*- coding: UTF-8 -*-
import redis
# r=redis.Redis(host=127.0.0.1,port=6379,db=0)
"""
sadd/srem--添加/删除元素
sismember--判断是否为set的一个元素
smembers--返回该集合所有成员
sdiff--返回一个集合与其它集合的差异
sinter--返回几个集合的交集
sunion--返回几个集合的并集
"""
class TestSet(object):
    def __init__(self):
        self.r=redis.StrictRedis(host='localhost',port=6379,db=0)

    '''sadd--添加元素'''
    def test_sadd(self):
        data=['Monday','Tuesday','wednesday','Thursday']
        rest=self.r.sadd('day',*data)
        print rest
        rest=self.r.smembers('day')
        print rest

    '''srem--删除元素'''
    def test_srem(self):
        
        rest=self.r.srem('day','wednesday')
        print rest
        rest=self.r.smembers('day')
        print rest

    '''sinter--删除元素'''
    def test_sunion(self): 
        rest=self.r.sunion('day1','day2')
        print rest    
    

if __name__ == "__main__":
    obj=TestSet()
    obj.test_srem()

