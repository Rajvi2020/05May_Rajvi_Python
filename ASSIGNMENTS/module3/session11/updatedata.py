import pymysql
try:
 db=pymysql.connect(host='localhost',user='root',password='',database='music_stream')
 print("database connected sucesfully")
except Exception as e:
 print(e)
cr=db.cursor()

#update

up_data="update playlists set name='chill hits' where name='chill vibes'"
try:
 cr.execute(up_data)
 db.commit()
 print("data updated")
except Exception as e:
 print(e)
