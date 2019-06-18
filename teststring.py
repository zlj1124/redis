# -*- coding: UTF-8 -*-
import redis
# r=redis.Redis(host=127.0.0.1,port=6379,db=0)
'''
    字符串String相关操作：
    set---设置值
    mset---设置多个键值对
    get---获取值
    mget---获取多个键值对
    del---删除
    append---添加字符串
    incr/decr---增加/减少1

'''
class TestString(object):
    def __init__(self):
        self.r=redis.StrictRedis(host='localhost',port=6379,db=0)
    '''增加一条'''
    def test_set(self):
        rest=self.r.set('user','Amy')
        return rest

    '''增加多条'''
    def test_mset(self):
        data={
            'user':'Amy',
            'user1':'Bod',
            'user2':'candy'
        }
        rest=self.r.mset(data)
        return rest   

    '''查询一条'''
    def test_get(self):
        rest=self.r.get("user1")
        return rest

    '''查询多条'''
    def test_mget(self):
        data=['user1','user2']
        rest=self.r.mget(data)
        return rest  

    '''删除''' 
    def test_del(self):
        rest=self.r.delete('user')
        return rest 

    '''值追加字符串''' 
    def test_append(self):
        rest=self.r.append('user1','aniy')
        return rest    

if __name__ == "__main__":
    obj=TestString()
    print obj.test_append()  
