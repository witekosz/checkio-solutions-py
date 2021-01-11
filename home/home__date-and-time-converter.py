import datetime


def date_time(time: str) -> str:
    datetime_obj = datetime.datetime.strptime(time, "%d.%m.%Y %H:%M")
    datetime_lst = [datetime_obj.day, datetime_obj.strftime('%B %Y'), "year"]

    datetime_lst.append(datetime_obj.hour)
    if datetime_obj.hour == 1:
        datetime_lst.append("hour")
    else:
        datetime_lst.append("hours")

    datetime_lst.append(datetime_obj.minute)
    if datetime_obj.minute == 1:
        datetime_lst.append("minute")
    else:
        datetime_lst.append("minutes")

    return " ".join(str(e) for e in datetime_lst)


if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")
