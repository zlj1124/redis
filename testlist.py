# -*- coding: UTF-8 -*-
import redis
# r=redis.Redis(host=127.0.0.1,port=6379,db=0)
"""
lpush/rpush---从左/右插入数据
lrange--获取指定长度的数据
ltrim---截取一定长度的数据
lpop/rpop---移除最左/右的元素并返回
lpushx/rpushx--key存在的时候才插入数据，不存在的时候不做任何操作
"""

class TestList(object):
    def __init__(self):
        self.r=redis.StrictRedis(host='localhost',port=6379,db=0)

    '''lpush/rpush---从左/右插入数据'''
    def test_lpush(self):
        data=['cat','dog','monkey']
        rest=self.r.lpush('zoo',*data)
        print rest
        rest=self.r.lrange('zoo', 0, -1)
        print rest

    '''lpop/rpop---移除最左/右的元素并返回'''  
    def test_lpop(self):
        rest=self.r.lpop('zoo')
        print rest
        rest=self.r.lrange('zoo', 0, -1)
        print rest 

    '''ltrim---截取一定长度的数据'''  
    def test_ltrim(self):
        rest=self.r.ltrim('zoo',0,2)
        print rest
        rest=self.r.lrange('zoo', 0, -1)
        print rest     
       

if __name__ == "__main__":
    obj=TestList()
    obj.test_ltrim()