from datetime import datetime
import sqlite3


def create_book_table():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS books (
            name TEXT PRIMARY KEY, 
            author TEXT, 
            read INTEGER
        );"""
    )

    connection.commit()
    connection.close()


def add_book(name, author):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    cursor.execute(
        """INSERT INTO books
            VALUES (?, ?, 0)
        """,
        (name + str(datetime.now()), author)
    )

    connection.commit()
    connection.close()


def get_all_books():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    cursor.execute(
        """SELECT *
            FROM books
        """
    )
    books = cursor.fetchall()

    print(books)

    connection.close()
