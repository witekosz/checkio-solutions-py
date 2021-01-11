def sun_angle(time: str):
    time_min = int(time[0:2])*60 + int(time[3:5])

    if time_min >= 360 and time_min <= 1080:
        return (time_min - 360) * 0.25
    else:
        return  "I don't see the sun!"


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
