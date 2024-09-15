import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

def initiate_db():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products(
    id INT,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
);
""")
    connection.commit()

initiate_db()

def _insert_info():
    for i in range(1, 5):
        cursor.execute(
        "INSERT INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)", (i, f"Продукт {i}", f"Описание {i}", i*100)
        )
    connection.commit()

_insert_info()


def get_all_products():
    cursor.execute("SELECT title, description, price FROM Products")
    products = cursor.fetchall()
    return products

