import mysql.connector

address = r"C:\Users\C605\Desktop\marvel.txt"
f = open(address)
x = f.readlines()



def insert_values():
    try:
        database = mysql.connector.connect(
            host='localhost',
            user='root',
            database='mydatabase',
            password='')
        cursor = database.cursor()
        insertQuery = """ INSERT INTO Marvel(ID,MOVIE,DATE,MCU_PHASE) VALUES (%s,%s,%s,%s)"""
        for i in x:
            cursor.executemany(insertQuery, i)
        database.commit()
        print("Recorded")

    except mysql.connector.Error as error:
        print("yalan oldu {}".format(error))


DataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

Cursor = DataBase.cursor()
Cursor.execute("DROP DATABASE mydatabase")
Cursor.execute("CREATE DATABASE mydatabase")

DataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase"
)
try:
    DataBase = mysql.connector.connect(
        host='localhost',
        database='mydatabase',
        user='root',
        password="")
    tableQuery = """ CREATE TABLE Marvel(
    ID INT(11) NOT NULL, 
    MOVIE VARCHAR(100) NOT NULL,
    DATE VARCHAR(100) NOT NULL,
    MCU_PHASE VARCHAR(100)) """

    Cursor = DataBase.cursor()
    Cursor.execute(tableQuery)
    DataBase.commit()


except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
insert_values()
