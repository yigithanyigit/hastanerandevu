import mysql.connector

def mysqlConnect():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="password")
    return mydb


# Creates database connection for dynamically
def database():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="password",
        database="hospt")
    return mydb