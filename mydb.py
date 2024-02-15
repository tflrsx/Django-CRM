
import mysql.connector

database = mysql.connector.connect(
    host ='localhost', 
    user ='root', 
    passwd = 'toor'
    )

#   prepare a cursor object
cursorObject = database.cursor()

#   create database
cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")