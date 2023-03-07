import mysql.connector
from mysql.connector.authentication import get_auth_plugin
mydb=mysql.connector.connect(host="localhost",user="root",passwd="tiger",auth_plugin="mysql_native_password",database="ispd")
mycursor=mydb.cursor()
sql="insert into login(videosample) values ('record')"
mycursor.execute(sql)
mydb.commit()
mycursor.execute("select * from login order by video desc limit 1")
myresult = mycursor.fetchall()



def criminal_details(id):
    sql="select * from criminals where criminal_id=%s"
    val=(id,)
    mycursor.execute(sql,val)
    re= mycursor.fetchall()
    return re

def capture():
    sql1 = "insert into capture(capture_photo) values ('capture')"
    mycursor.execute(sql1)
    mydb.commit()
    mycursor.execute("select * from capture order by capture1 desc limit 1")
    myresult1 = mycursor.fetchall()
    return myresult1