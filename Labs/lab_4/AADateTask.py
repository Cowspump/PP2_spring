import datetime

#first

def five_days_ago():
    cur = datetime.date.today()

    print(f"Current day: {cur}")

    ago = datetime.date.today() - datetime.timedelta(days=5)

    print(f"Five days ago was: {ago}", '\n')


if __name__ == "__main__":
    five_days_ago()

#_____________second_____________

def three_days():

    days = {"yesterday":-1, "today":0, "tomorrow": 1}


    for day in days:

        cur =  datetime.date.today() - datetime.timedelta(days=days[day])

        print(f"{day}: {cur}", '\n')


if __name__ == "__main__":
    three_days()



#third

def datetime_without_ms():

    cur = datetime.datetime.now()

    print(f"Daytime with ms: {cur}")

    def drop_ms(dt):
        return dt.replace(microsecond=0)

    print(f"Daytime without ms: {drop_ms(cur)}",'\n')


if __name__ == "__main__":
    datetime_without_ms()


#last

def diff_betw_seconds(day1, day2):

    d_format = "%Y-%m-%d"

    date1 = datetime.datetime.strptime(day1, d_format)
    date2 = datetime.datetime.strptime(day2, d_format)

    diff = date2 - date1


    return diff.total_seconds()



if __name__ == "__main__":
    seconds = diff_betw_seconds("2000-01-15", "2005-01-15")

    print(f"seconds between 15.01.15 and 15.01.00 = {seconds}", end='\n')

    years = seconds / (3.2 * 10 **7)

    print(f"{seconds} sec = {years} years.", '\n')





