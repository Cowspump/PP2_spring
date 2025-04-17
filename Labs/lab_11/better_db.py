import psycopg2
import csv
import ast

try:
    connection = psycopg2.connect(
        host='localhost', dbname="postgres", user="postgres",
        password="1234", port=5432
    )

    connection.autocommit = True  # for autocommiting all changes

    curs = connection.cursor()

    with connection.cursor() as curs:
        curs.execute(
            "SELECT version();"
        )
        print(f"server version: {curs.fetchone()}")


    with connection.cursor() as curs:
        # curs.execute("DELETE FROM users WHERE username = 'username'")
        curs.execute("SELECT * FROM users")
        print(curs.fetchall())

except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)


def inputData() -> None:
    print("Hello! Please, carefully input your data by following steps")
    fname = input("Firstname: ").strip()
    lname = input("Lastname: ").strip()
    phone = input("Phone number: ").strip()
    curs.execute("CALL insert_or_update_user(%s, %s, %s)", (fname, lname, phone))


def importFromCSV() -> None:
    with open("info.csv", 'r') as file:
        reader = csv.reader(file)
        li = []
        for row in reader:
            li.append(row)
        curs.execute("CALL insert_multiple_users(%s)", (li,))


def update_contact() -> bool:
    limit = int(input("Limit: ").strip())
    offset = int(input("Offset ").strip())
    curs.execute('SELECT * FROM get_records_with_pagination(%s, %s);', (limit, offset))
    print(curs.fetchall())


def queryData() -> None:
    print("""Select filter to querying\n\
            [1] id, name, phone\n\
            [2] Name, phone\n\
            [3] Name\n\
            [4] Phone\n\
            [5] Exit""")
    filter = input("Your choice: ")
    curs.execute(' SELECT * FROM search_records_pattern(%s)', str(filter))
    data = (curs.fetchall())
    with open("queredData.txt", "w") as file:
        for row in data:
            print(row)
            file.write(f"{str(row[0])}\n")


def deleteData() -> None:
    print("Enter lastname that you want to delete, then input phone number:")
    lname = input("Lastname: ").strip()
    phone = input("Phone number: ").strip()
    print(f"""Are you sure to delete user {lname} from database?\n\
        [1] - Yes\n\
        [2] - No""")
    sure = input()
    if sure == "1":
        print("Initializing deleting...")
        curs.execute("CALL delete_records(%s, %s)", (lname, phone))
        print("User deleted")


def deleteAllData() -> None:
    sure = input("Are you absolutely shure about that?: ")
    if sure == "1":
        print("Initializing deleting...")
        curs.execute(' DELETE FROM users  ')
        print("All data successfully deleted!")
    else:
        print("Data not deleted")


done = False
while not done:
    curs = connection.cursor()
    print("What do you want to do?\n\
          [1] Input data from console\n\
          [2] Upload form csv file\n\
          [3] Users by limit and offset\n\
          [4] Query data from the table\n\
          [5] Delete data from table by person name\n\
          [6] Delete all data from table\n\
          [7] Exit")
    x = int(input("Enter number 1-7: "))
    if (x == 1):
        inputData()
    elif (x == 2):
        importFromCSV()
    elif (x == 3):
        if not update_contact():
            update_contact()

    elif (x == 4):
        queryData()
    elif (x == 5):
        deleteData()
    elif (x == 6):
        deleteAllData()
    else:
        done = True

curs.close()
connection.close()