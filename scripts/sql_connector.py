import mysql.connector

# Returns a cursor to a MYSQL local database
def db_cursor(password, database, host='localhost', user='root'):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=password,
        database=database
    )
    return db.cursor
