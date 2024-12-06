import sqlite3

def create_connection():
    conn = sqlite3.connect('property_management.db')
    return conn

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS properties (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        address TEXT NOT NULL,
        price REAL NOT NULL,
        area REAL NOT NULL,
        description TEXT,
        status TEXT NOT NULL
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        phone TEXT NOT NULL,
        email TEXT NOT NULL,
        interested_properties TEXT 
    )''')

    conn.commit()
    conn.close()

create_tables()
