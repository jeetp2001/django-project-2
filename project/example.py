import MySQLdb

db = MySQLdb.connect(host = '0.0.0.0',user='root',password='G0d!sgreat',database='mydb')
cur = db.cursor()
q1 = 'select * from user'
cur.execute(q1)
data = cur.fetchall()
e = 'def.com'
q2 = 'select name from user where email=%s'
t2=(e,)
cur.execute(q2,t2)
data2 = cur.fetchall()
print(data2[0][0])
