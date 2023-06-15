# https://www.codewars.com/kata/5993fb6c4f5d9f770c0000f2

def sum_no_duplicates(lst):
    return sum([x for x in lst if lst.count(x) == 1])


def sum_no_duplicates_ultimate(lst):
    return sum([x for x in set(lst) if lst.count(x) == 1])


test = [1, 1, 111]

print(sum_no_duplicates(test))
print(sum_no_duplicates_ultimate(test))


