# https://www.codewars.com/kata/59015f8cc842a3e7f10000a4


def Check_Prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        return all(n % i for i in (2, n+1))

def simplified_array(a):
    flag = ''  # p for prime, np for non prime
    ret = []
    temp = []

    for i in a:
        bflag = Check_Prime(i)

        if flag == 'p' and not bflag:
            ret.append(sum(temp))
            temp.clear()
            flag = 'np'
        elif flag == 'np' and bflag:
            ret.append(sum(temp))
            temp.clear()
            flag = 'p'
        elif not flag:
            if bflag:
                flag = 'p'
            else:
                flag = 'np'
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


print(simplified_array([21, 5]))
# Something is seriously wrong with Check_Prime, as the function claims that 21 is a prime number. It is not.
# Despite using all() which only returns True if ALL returned true, it still manages to return true
# despite 21%7 being 0!!!!
# At this point of testing I have realized that the code is rebelling and the universe is now AI.

