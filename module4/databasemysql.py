import pymysql
try:
  db=pymysql.connect(host='localhost',user='root',password='',database='newdb')
  print("database connected")
except Exception as e:
  print(e)

cr=db.cursor()
'''create table
tab_create="create table studinfo (id integer primary key auto_increment ,name varchar(20),city varchar(20))"
try:
  cr.execute(tab_create)
  db.commit()
except Exception as e:
  print(e)
'''
#insert data
"""ins_data="insert into studinfo(name,city) values ('rajvi','mahuva'),('kishan','rajkot'),('kiran','jasdan'),('dharmendra','kundheli')"
try:
  cr.execute(ins_data)
  db.commit()
except Exception as e:
  print(e)
"""

#update data
"""up_data="update studinfo set city='rajula' where id =4"
try:
  cr.execute(up_data)
  db.commit()
except Exception as e:
  print(e)"""

#delete data
"""del_Data="delete from studinfo where id=4"
try:
  cr.execute(del_Data)
  db.commit()
except Exception as e:
  print(e)"""

#select data
sel_data="select * from studinfo"
try:
  cr.execute(sel_data)
  #data=cr.fetchall()
  #data=cr.fetchone()
  data=cr.fetchmany()
  #print(data)
  for i in data:
    print(i)
except Exception as e:
  print(e)    


