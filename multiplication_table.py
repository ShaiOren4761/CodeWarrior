# https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08/train/python

def multiplication_table(size):
    return [[i*ml for i in range(1, size+1)] for ml in range(1, size+1)]


print(multiplication_table(3))

