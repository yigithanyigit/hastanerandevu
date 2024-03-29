from database.database_connection import database, mysqlConnect

def tablelist(*args, table):
    mydb = mysqlConnect()
    query = "SELECT table_name FROM information_schema.tables WHERE table_schema =%s"
    cursor = mydb.cursor()
    databasea = args
    cursor.execute(query, databasea)
    myresult = cursor.fetchall()
    if not myresult :
        raise ValueError("Could not find database (%s) " % databasea)
    else:
        for x in myresult:
            print(x)


def inserttable(*args, table=None, sql=None):
    mydb = database()
    cursor = mydb.cursor()
    if not sql:
        sql = "INSERT INTO {} (TC, AD, SOYAD, ANA_ADI, CINSIYET) VALUES (%s, %s, %s, %s, %s)".format(table)
    cursor.execute(sql, args)
    mydb.commit()
    return print(cursor.rowcount, "Kayıt Girildi")

def query(*args,sql=None, fetch=False):
    mydb = database()
    if not sql:
        sql = "SELECT * FROM patients WHERE TC = %s"
    cursor = mydb.cursor()
    cursor.execute(sql,args)
    result = cursor.fetchall()
    if result:
        if not fetch:
            print("var")
            return True
        else:
            return result
    else:
       return print("yok")

