import sqlite3
#connected with database if not exist then it will make new database
try:
  db=sqlite3.connect('top.db')
  print("database connected")
except Exception as e:
  print(e)

#create table
"""cre_table="create table studinfo(id integer primary key autoincrement ,name varchar(20),city varchar(20))"
try:
  db.execute(cre_table)
  db.commit()
except Exception as e:
  print(e)  """

#insert data
"""ins_data="insert into studinfo(name,city)values('rajvi','mahuva'),('kishan','rajkot'),('kiran','adanadpur'),('dharmendra','kundheli'),('shruti','junagadh')"
try:
  db.execute(ins_data)
  db.commit()
  print("record inserted")
except Exception as e:
  print(e)
"""
#update data

"""up_data="update studinfo set name='kidi' where id=3"
try:
  db.execute(up_data)
  db.commit()
  print("data updated")
except Exception as e:
  print(e)

"""
#delete data
"""del_data="delete from studinfo where id=3"
try:
  db.execute(del_data)
  db.commit()
except Exception as e:
  print(e)"""

#select data
cr=db.cursor()
sel_data="select * from studinfo"
try:
  cr.execute(sel_data)
  data=cr.fetchall()
  #data=cr.fetchone()
  #data=cr.fetchmany()
  #print(data)
  for i in data:
    print(i)  #in for loop we can get more structured form 
except Exception as e:
  print(e)



