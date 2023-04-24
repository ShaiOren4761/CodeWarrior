# [0]
# [1,0,1]
# [1,2,1,0,2]
# [3,1,2,1,3,2,0]
# [3,1,4,1,3,2,0,4,2]
# [5,3,1,4,1,3,5,2,4,0,2]
# [5,3,1,6,1,3,5,4,2,0,6,2,4]
# 8: [7,5,3,1,8,1,3,5,7,6,4,2,0,8,2,4,6] - if even 0 first
# 9: [9,7,5,3,1,8,1,3,5,7,9,6,4,2,8,0,2,4,6] - if odd 0 second
# 10: [9,7,5,3,1,10,1,3,5,7,9,8,6,4,2,0,10,2,4,6,8]

# len = n*2 + 1

# [descending odd - the biggest even - ascending odd -
# descending even(not including biggest!) -0/biggest even - rising even()not including biggest!]

def generate(num):
    if not num:
        return [0]
    if num % 2 == 0:
        des_odd = [x for x in range(num+1) if x % 2][::-1]

        big_even = [num]

        asc_odd = des_odd.copy()[::-1]

        des_even = [x for x in range(num-1) if x % 2 == 0 and x][::-1]

        big_even_zero = [0, num]

        asc_even = des_even.copy()[::-1]

        return des_odd + big_even + asc_odd + des_even + big_even_zero + asc_even
    else:
        des_odd = [x for x in range(num+1) if x % 2][::-1]

        big_even = [num-1]

        asc_odd = des_odd.copy()[::-1]

        des_even = [x for x in range(num-1) if x % 2 == 0 and x][::-1]

        if num != 1:
            big_even_zero = [num-1, 0]
        else:
            big_even_zero = []

        asc_even = des_even.copy()[::-1]

        return des_odd + big_even + asc_odd + des_even + big_even_zero + asc_even


for i in range(9, 11):
    print(f'i = {i} , {generate(i)}')

