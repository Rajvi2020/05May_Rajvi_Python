import pymysql
try:
 db=pymysql.connect(host='localhost',user='root',password='',database='music_stream')
 print("database connected sucesfully")
except Exception as e:
 print(e)
cr=db.cursor()

#select data

se_data="select name,song_Count from playlists where song_Count>10"
try:
 cr.execute(se_data)
 data=cr.fetchall()
 print(data)
except Exception as e:
 print(e) 

  