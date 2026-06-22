import pymysql
try:
 db=pymysql.connect(host='localhost',user='root',password='',database='music_stream')
 print("database connected sucesfully")
except Exception as e:
 print(e)
cr=db.cursor()

#delete when id is exist
"""del_data = "delete from playlists where id =2"
try:
 cr.execute(del_data)
 db.commit()
 print("data deleted")
except Exception as e:
 print(e) 
"""
#delete when id does nor exist

playlist_id=0
playlist_id=int(input("enter playlist_id to delete"))
del_data = f"delete from playlists where playlist_id ={playlist_id}"
try:

 rows=cr.execute(del_data)
 db.commit()
 if rows>0:
  print(f"data deleted succesfully of playlist id is {playlist_id}")
 else:
  print(f"no id-{playlist_id} is exist") 
 
 
except Exception as e:
 print(e) 