import mysql.connector


def database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="password",
        database="hospt")

