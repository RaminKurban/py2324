import redis # быстрая база данных

r = redis.StrictRedis(host='nadejnei.net', port=16379, password='123456') # подкдючение
r.set ('ramin', '89657823256'ex = 20)
result = r.get('kirill')
print(result.decode())
