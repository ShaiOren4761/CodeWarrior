# https://www.codewars.com/kata/541c8630095125aba6000c00/train/python
from math import log10

# I tried in three ways to split a number into digits. A simple conversion to string solved that.....
# def num_to_list(n):
#     ret = []
#     while n:
#         ret.append(n % 10)
#         n = n // 10
#     ret.reverse()
#     return ret
# def num_to_list_comprehension(n):
# return [n % 10 for _ in range(int(math.log10(n) + 1))][::-1] almost ):
# num_to_lst = lambda n: [n % 10].append(num_to_lst(n//10)) if int(math.log10(n)+1) != 1 else [n % 10]


def digital_root(n):
    if not n:
        return n
    if int(log10(n)+1) > 1:
        n = sum([int(x) for x in str(n)])
    return n if int(log10(n)+1) == 1 else digital_root(n)


def digital_root_ultimate(n):
    return n if n < 10 else digital_root_ultimate(sum(map(int, str(n))))
# The power of string as an iterable.. insane!!!


print(digital_root_ultimate(12345))

