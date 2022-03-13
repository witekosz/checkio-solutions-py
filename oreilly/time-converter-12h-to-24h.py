# TODO refactor

def time_converter(time: str) -> str:
    AM = " a.m."
    PM = " p.m."

    if time[1] == ':':
        time = '0' + time
    print(time[-4])

    if time[0:2] =='12' and PM in time:
        time = time[0:5]
    elif time[0:2] =='12' and AM in time:
        time = "00:" + time[3:5]
    elif time[-4] == 'a':
        time = time[0:5]
    else:
        time_hour = int(time[0:2])
        time_minutes = time[3:5]
        time_hour += 12

        time = str(time_hour) + ":" + time_minutes

    return time


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30 p.m.'))
    print(time_converter('12:00 a.m.'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30 p.m.') == '12:30'
    assert time_converter('9:00 a.m.') == '09:00'
    assert time_converter('11:15 p.m.') == '23:15'
    print("Coding complete? Click 'Check' to earn cool rewards!")
