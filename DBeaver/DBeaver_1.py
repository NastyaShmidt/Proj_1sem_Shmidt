import sqlite3 as sq

with sq.connect('saper.db') as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    sex INTEGER NOT NULL DEFAULT 1,
    old INTEGER,
    score INTEGER
    )""")
    # ЗАДАНИЕ 8: ВНЕСТИ ИНФОРМАЦИЮ ОБ ИГРОКАХ
    info_users = [
        ('Алексей', 1, 22, 1000),
        ('Миша', 1, 19, 800),
        ('Сергей', 1, 19, 900),
        ('Мария', 2, 18, 1500),
        ('Александр', 1, 20, 1100)
    ]
    cur.executemany("INSERT INTO users (name, sex, old, score) "
                    "VALUES ( ?, ?, ?, ?)", info_users)
    cur.execute("SELECT * FROM users")
    result = cur.fetchall()
    print(result)

    # ЗАДАНИЕ 9:

    # выбор всех игроков из таблицы
    cur.execute("SELECT name FROM users")
    result = cur.fetchall()
    print(result)

    # выбор всех игроков женского пола из таблицы
    cur.execute("SELECT name, sex FROM users WHERE sex = 2")
    result = cur.fetchall()
    print(result)

    # выбор всех игроков с результатом меньше 1000 из таблицы
    cur.execute("SELECT name, score FROM users WHERE score < 1000")
    result = cur.fetchall()
    print(result)

    # выбрать игрока с наилучшим результатом из таблицы
    cur.execute("SELECT name, score FROM users WHERE score = "
                "(SELECT MAX(score) FROM users)")
    result = cur.fetchall()
    print(result)

    # выбрать всех игроков с возрастом 18-20 лет из таблицы
    cur.execute("SELECT name, old FROM users WHERE old BETWEEN 18 AND 20")
    result = cur.fetchall()
    print(result)


    # ЗАДАНИЕ 11:

    # изменить возраст 19-летних игроков на 20
    cur.execute("UPDATE users SET old=20 WHERE old=19")

    # всем игрокам, имеющим менее 1000 очков, добавить 300 очков
    cur.execute("UPDATE users SET score = score+300 WHERE score<1000")

    # игрокам, достигшим возраста 20 лет добавить 100 очков
    cur.execute("UPDATE users SET score = score+100 WHERE old=20")

    # удалить игроков с результатами менее 1000 очков
    cur.execute("DELETE FROM users WHERE score<1000")

    cur.execute("SELECT * FROM users")
    result = cur.fetchall()
    print(result)
