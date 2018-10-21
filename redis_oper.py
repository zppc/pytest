import  redis

conner = redis.Redis(host='192.168.6.141',port=6379,password='123456')

conner.set('zpp','good man')
result = conner.get('zpp')
print(result)