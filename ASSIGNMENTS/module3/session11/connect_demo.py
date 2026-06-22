import pymysql
#create database
import pymysql

# Connect to MySQL server
connection = pymysql.connect(
    host="localhost",
    user="root",
    password=""
)

try:
    with connection.cursor() as cursor:
        cursor.execute("CREATE DATABASE mydatabase")
        print("Database created successfully!")

    connection.commit()

except Exception as e:
    print("Error:", e)

