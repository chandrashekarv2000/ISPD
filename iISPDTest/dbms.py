import mysql.connector
from mysql.connector.authentication import get_auth_plugin
mydb=mysql.connector.connect(host="localhost",user="root",passwd="tiger",auth_plugin="mysql_native_password")
print(mydb)