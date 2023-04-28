# https://www.codewars.com/kata/59015f8cc842a3e7f10000a4

#
# def Check_Prime(n):
#     if n == 1:
#         return False
#     elif n == 2:
#         return True
#     else:
#         return all(n % i for i in (2, n+1)) # This Doesn't work!! Why???????


def Check_Prime(n):
    if n <= 1:
        return False
    n = abs(n)
    for i in range(2, int(n ** 0.5)+1):
        if not n % i:
            return False
    return True


def simplified_array(a):
    ret = []
    temp = []
    flag = 'p' if a and Check_Prime(a[0]) else 'np'  # p for prime, np for non prime

    for i in a:
        bflag = Check_Prime(i)

        if flag == 'p' and not bflag:
            flag = 'np'
            ret.append(sum(temp))
            temp.clear()
        elif flag == 'np' and bflag:
            flag = 'p'
            ret.append(sum(temp))
            temp.clear()

        temp.append(i)

    bflag = Check_Prime(i)
    if flag == 'p' and not bflag:
        ret.append(sum(temp))
        ret.append(i)
    elif flag == 'np' and bflag:
        ret.append(sum(temp))
        ret.append(i)
    else:
        ret.append(sum(temp))

    return ret if ret == a else simplified_array(ret)


print(simplified_array([-3, 4, 5, 2, 0, -10]))
# Test [-3, 4, 5, 2, 0, -10] --> [(-3 + 4), (5 + 2), (0 + -10)] --> [1, 7, -10]
# -3 and 4 are not meant to be sum'd
# Cannot continue to solution as impossible test was put as a hurdle in the way..
# Or I missed something. Either way I'll return here once someone responded to my comment on the Kata.
