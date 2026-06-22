import pymysql
try:
 db=pymysql.connect(host='localhost',user='root',password='',database='music_stream')
 print("database connected sucesfully")
except Exception as e:
 print(e)
cr=db.cursor()
#create table
"""cre_table="create table playlists(id int primary key auto_increment,name varchar(20), song_count int)"
try:
 cr.execute(cre_table)
 db.commit()
 print("table created")
except Exception as e:
 print(e)  """

#insert data
ins_data="insert into playlists(name,song_count) values ('deevana',1),('ram or shayma',4),('dil',5)"
try:
 cr.execute(ins_data)
 db.commit()
 print("data inserterd")
except Exception as e:
 print(e)

