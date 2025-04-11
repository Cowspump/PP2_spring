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
        print("Привет! это телефонная книга.\n"
              "Вы можете добавить в книгу:\n"
              "*Свой номер\n"
              "*Свое имя\n\n"
              "Добавить информацию можно через:\n"
              "терминал вводя ваши данные,\n"
              "*csv file\n\n"
              )
    else:
        print("Варианты действий и их коды:\n"
              "1-2: Добавить данные через терминал,\n"
              "Добавить данные через csv file\n"
              "3: Обновить телефон по имени\n"
              "4: Обновить имя по телефону\n"
              "5: Вывести номера с именами начинающимися на букву: Ваш ввод\n"
              "6: Удалить данные по номеру.\n"
              "7: Выйти.\n\n"
              "Что вы хотите сделать ?: ",end="")

        user_choice = int(input())

        if user_choice == 1:
            user_name :str
            user_phone :str
            user_name = input("Введите свое имя: ")
            user_phone = input("Введите свой номер: ")

            cur.execute("SELECT MAX(id) FROM users;")
            max_id_result = cur.fetchone()[0]
            if max_id_result is None:
                last_id = 1
            else:
                last_id = max_id_result + 1


            try:
                cur.execute("""
                               INSERT INTO users (id,username, user_phone)
                               VALUES (%s,%s, %s);
                           """, (last_id, user_name, user_phone))
                conn.commit()

                print("\nУспешно! ваши данные добавлены в книгу.\n")
            except Exception as e:
                print(e)

        elif user_choice == 2:

            csv_file_path = input("\nВведите путь до вашего csv file: ")
            with open(csv_file_path, 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                next(csv_reader)  # Skip the header row (if it has one)

                for row in csv_reader:
                    try:
                        # Assuming CSV format is [id, username, user_phone]
                        cur.execute("""
                            INSERT INTO users (id, username, user_phone)
                            VALUES (%s, %s, %s);
                        """, (row[0], row[1], row[2]))

                    except Exception as e:
                        print(f"Error inserting row {row}: {e}")

            # Commit the changes
            conn.commit()
            print("\nУспешно! данные были добавлены в книгу.\n")

        elif user_choice == 3:

            user_name = input("Введите имя для замены номера: ")
            user_phone = input("Введите новый номер: ")

            try:
                cur.execute("""UPDATE users SET user_phone = %s
                WHERE username = %s
                """, (user_phone, user_name))
                conn.commit()

                print("\nУспешно! ваш номер был изменен.\n")
            except Exception as e:
                print(e)

        elif user_choice == 4:
            user_phone = input("Введите номер для замены имени: ")
            user_name = input("Введите новое имя: ")


            try:
                cur.execute("""UPDATE users SET username = %s
                            WHERE user_phone = %s
                            """, (user_name, user_phone))
                conn.commit()

                print("\nУспешно! ваше имя было изменено.\n")
            except Exception as e:
                print(e)

        elif user_choice == 5:


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


        elif user_choice == 6:

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

        if user_choice == 7:
            break



#to send stuff into databse
conn.commit()
cur.close()
conn.close()
