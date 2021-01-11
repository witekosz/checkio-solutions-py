# TODO refactor

def time_converter(time: str) -> str:
    AM = " a.m."
    PM = " p.m."
    hours = int(time[:2])
    minutes = time[2:5]

    if hours < 10 and hours > 0:
        return time[1:5] + AM
    elif hours < 12 and hours > 10:
        return time + AM
    elif hours == 12:
        return time + PM
    elif hours > 12:
        return str(hours - 12) + minutes + PM
    else:
        return str(hours + 12) + minutes + AM


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
