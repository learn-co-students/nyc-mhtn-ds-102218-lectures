import sqlite3

conn = sqlite3.connect('google_books.db')
# conn.execute('select * from books;')

cursor = conn.cursor()

def create_books():
    create_sql = """
    CREATE TABLE books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        year INTEGER
    );
    """
    return create_sql

class Book():
    @classmethod
def select_by_name(name):
    select_sql = """
        select * from books where title = 'Prince and the Pauper';
    """
    cursor.execute(select_sql)
    return cursor.fetchall()


create_authors_sql = open('create_authors.sql', 'r').read()
#
cursor.execute(create_authors_sql)
