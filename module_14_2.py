# Импортируем модуль базы sqlite3
import sqlite3

# Подключаемся к нашей базе данных,
# если базы нет, то автоматически
# создастя новая с именем,
# которое вы указали
connection = sqlite3.connect("not_telegram.db")


# Создаем курсор для управления ДБ
cursor = connection.cursor()


# Выполняем комманды для создания и заполнения базы данных
# id - целое число, первичный ключ
# username - текст (не пустой)
# email - текст (не пустой)
# age - целое число
# balance - целое число (не пустой)
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

def _show_db():
    # Вывести из базы данных поля -> возраст не равен 60
    # На вывод подаем username email age balance
    cursor.execute(
    "SELECT username, email, age, balance FROM Users WHERE age != ?", (60,)
    )
    users = cursor.fetchall()
    for user in users:
        print(
        f"Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}"
        )



# Заполните ее 10 записями
for i in range(1, 11):
    cursor.execute(
    "INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"User{i}", f"example{i}@gmail.com", 10*i, 1000)
    )


# Обновите balance у каждой 2ой записи начиная с 1ой на 500:
for i in range(1, 11, 2):
    cursor.execute(
    "UPDATE Users SET balance = ? WHERE id = ?", (500, i)
    )


# Удалите каждую 3ую запись в таблице начиная с 1ой:
for i in range(1, 11, 3):
    cursor.execute(
    "DELETE FROM Users WHERE id = ?", (i, )
    )

cursor.execute("DELETE FROM Users WHERE id = 6")

cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]
cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]
average_balance = all_balances / total_users


if __name__ == "__main__":
    print(average_balance)
    # Коммитим изменения из курсора в базу
    connection.commit()
    # Закрываем базу данных
    connection.close()



