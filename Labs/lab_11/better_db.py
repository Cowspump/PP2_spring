import csv

import psycopg2 as pcg

conn = pcg.connect(host ='localhost',dbname = "postgres", user = "postgres",
                   password = "1234", port = 5432)

cur = conn.cursor()

#do smth with database
first_start = True


cur.execute("""CREATE TABLE IF NOT EXISTS users (
    id INT Primary Key,
    username VARCHAR(255),
    user_phone VARCHAR(255)
)
""")



while True:

    if first_start:
        first_start = False
        print("Привет! это телефонная книга2.\n\n")
    else:
        print("\n\nВарианты действий и их коды:\n"
              "1:Показать номера по паттерну\n"
              "2:Добавить или обновить номер если уже есть\n"
              "3:Добавить много номеров\n"
              "4:Пагинация\n"
              "5:Удалить номер по телефону.\n"
              "6:выход\n\n" 
              "Что вы хотите сделать ?: ",end="")

        user_choice = int(input())

        if user_choice == 1:
            try:
                print("\nВведите буквку с которой должно начинаться имя: ",end="")
                user_letter = input()

                cur.execute("""SELECT * FROM users WHERE username ILIKE %s;""", (user_letter + '%',))

                rows = cur.fetchall()

                for row in rows:
                    print(row[1], row[2])

                print(f"\nУспешно! были выведены все номера с именем начинающимися на букву:{user_letter}\n")
            except Exception as e:
                print(e)
        elif user_choice == 2:
            user_name = input("Введите свое имя: ")
            user_phone = input("Введите свой номер: ")

            # Проверяем, существует ли пользователь
            cur.execute("SELECT id FROM users WHERE username = %s;", (user_name,))
            user = cur.fetchone()

            try:
                if user:
                    # Если пользователь уже есть, обновляем его номер
                    cur.execute("""
                        UPDATE users
                        SET user_phone = %s
                        WHERE username = %s;
                    """, (user_phone, user_name))
                    print("\nНомер успешно обновлён.\n")
                else:
                    # Если пользователя нет, добавляем его
                    cur.execute("SELECT MAX(id) FROM users;")
                    max_id_result = cur.fetchone()[0]
                    last_id = 1 if max_id_result is None else max_id_result + 1

                    cur.execute("""
                        INSERT INTO users (id, username, user_phone)
                        VALUES (%s, %s, %s);
                    """, (last_id, user_name, user_phone))
                    print("\nУспешно! Ваши данные добавлены в книгу.\n")

                conn.commit()

            except Exception as e:
                print("Произошла ошибка:", e)
        elif user_choice == 3:
            times_add = int(input("Сколько добавить контактов?: "))

            for time in range(times_add):

                user_name = input("Введите свое имя: ")
                user_phone = input("Введите свой номер: ")

                # Проверяем, существует ли пользователь
                cur.execute("SELECT id FROM users WHERE username = %s;", (user_name,))
                user = cur.fetchone()

                try:
                    if user:
                        # Если пользователь уже есть, обновляем его номер
                        cur.execute("""
                                        UPDATE users
                                        SET user_phone = %s
                                        WHERE username = %s;
                                    """, (user_phone, user_name))
                        print("\nНомер успешно обновлён.\n")
                    else:
                        # Если пользователя нет, добавляем его
                        cur.execute("SELECT MAX(id) FROM users;")
                        max_id_result = cur.fetchone()[0]
                        last_id = 1 if max_id_result is None else max_id_result + 1

                        cur.execute("""
                                        INSERT INTO users (id, username, user_phone)
                                        VALUES (%s, %s, %s);
                                    """, (last_id, user_name, user_phone))
                        print("\nУспешно! Ваши данные добавлены в книгу.\n")

                    conn.commit()

                except Exception as e:
                    print("Произошла ошибка:", e)
        elif user_choice == 4:
            first_id = int(input("Введите первый айди: "))
            second_id = int(input("Введите второй айди: "))

            try:
                cur.execute("""
                    SELECT * FROM users
                    WHERE id BETWEEN %s AND %s
                    ORDER BY id;
                """, (first_id, second_id))

                rows = cur.fetchall()

                if rows:
                    print("\nНайденные пользователи:")
                    for row in rows:
                        print(f"ID: {row[0]}, Имя: {row[1]}, Телефон: {row[2]}")
                else:
                    print("\nНет пользователей в указанном диапазоне ID.")

            except Exception as e:
                print("Ошибка при выполнении запроса:", e)



        elif user_choice == 5:

            try:
                user_phone = input("\nВведите ваш номер, чтобы удалить из книги: ")

                # Проверяем, существует ли номер в базе данных
                cur.execute("""SELECT * FROM users WHERE user_phone = %s;""", (user_phone,))
                user_exists = cur.fetchone()

                if user_exists:
                    cur.execute("""DELETE FROM users WHERE user_phone = %s;""", (user_phone,))
                    conn.commit()
                    print("\nУспешно! ваши данные были удалены.\n")
                else:
                    print("\nПользователь с таким номером не найден.\n")

            except Exception as e:
                print("Ошибка при удалении данных:", e)

        if user_choice == 6:
            break



#to send stuff into databse
conn.commit()
cur.close()
conn.close()
