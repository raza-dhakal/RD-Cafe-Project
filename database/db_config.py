import mysql.connector
def get_connection():
    return mysql.connector.connect(
        host="localhost",      # या '127.0.0.1'
        user="root",           # MySQL username
        password="razan2409",  # MySQL password
        database="rdcafe_db"   # तिमीले बनाएको database
    )