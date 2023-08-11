#  https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/train/python
from difflib import SequenceMatcher

def solution(args):
    if not args:
        return []

    result = ""
    current_group = [args[0]]

    for i in range(1, len(args)):
        if abs(args[i] - current_group[-1]) == 1:
            current_group.append(args[i])
        else:
            if len(current_group) == 1:
                result += f'{current_group[0]},'
            elif len(current_group) == 2:
                result += f'{current_group[0]},{current_group[1]},'
            else:
                result += f'{current_group[0]}-{current_group[-1]},'
            current_group = [args[i]]

    if len(current_group) == 1:
        result += f'{current_group[0]}'
    elif len(current_group) == 2:
        result += f'{current_group[0]},{current_group[1]}'
    else:
        result += f'{current_group[0]}-{current_group[-1]}'

    return result


lst = [-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]

print()