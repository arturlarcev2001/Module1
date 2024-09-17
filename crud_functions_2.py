import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

def initiate_db():
    """
    Создаем нашу базу данных User
    """
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users(
    user_id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INT NOT NULL,
    balance INT NOT NULL
    );
    """)
    # Создаем уникальный ид для каждого нового пользователя
    cursor.execute("""
    CREATE INDEX IF NOT EXISTS user_ids ON Users (user_id)
    """)
    connection.commit()


def remove_user(username):
    """
    Удалем всех пользователей из базы данных
    username -> str
    """
    if username == "all":
        # Если вместо имени пользователя ввести 'all', то будут удалены все пользователи из базы
        cursor.execute(
        "SELECT username FROM Users"
        )
        users = cursor.fetchall()
        for user in users:
            name = user[0]
            cursor.execute(
            "DELETE FROM Users WHERE username =?", (name,)
            )
            connection.commit()
    else:
        # В ином случае удалем только ввденого пользовотеля, если он есть в базе
        if is_included(username):
            cursor.execute(
            "DELETE FROM Users WHERE username =?", (username,)
            )
            connection.commit()
        else:
            return 0


def add_user(username, email, age):
    """
    Добовляем пользователя в базу данных
    username -> str
    email -> str
    age -> int
    user_id -> unique int
    """
    if not is_included(username):
        # Проверяем есть ли пользователь в базе данных, если в базе -> пропускаем, если нету -> добовляем
        cursor.execute(
        "INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (username, email, age, 1000)
        )
        connection.commit()
    else:
        print("Вы не можете добавить пользователя, который уже существует")


def is_included(username):
    # Проверяем есть ли пользователь в базе
    # username -> str
    cursor.execute(
    "SELECT username FROM Users"
    )
    users = cursor.fetchall()
    for user in users:
        if user[0] == username:
            return True
    return False


def main():
    initiate_db()
    remove_user("all")

if __name__ == "__main__":
    initiate_db()
    remove_user("all")
    for i in range(1, 5):
        add_user(f"test{i}", f"test{i}mail.ru", i)
    connection.close()
else:
    main()
