import mysql.connector
from mysql.connector import Error


def create_database():
    try:

        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="@Robel161927",
            database=" alx_book_store"
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error:
        print(f"Error while connecting to MySQL: {Error}")
    finally:
        if connection.is_connected:
            cursor.close()
            connection.close()


if __name__ == "__main__":
    create_database()
