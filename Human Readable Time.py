# https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python


def make_readable(seconds):
    hour = seconds // 3600  # hour = 3600 seconds
    minute = seconds % 3600 // 60  # minute = 60 seconds
    second = seconds % 60  # second = 1

    return f'{hour if hour > 9 else "0" + str(hour)}:' \
           f'{minute if minute > 9 else "0" + str(minute)}:' \
           f'{second if second > 9 else "0" + str(second)}'



