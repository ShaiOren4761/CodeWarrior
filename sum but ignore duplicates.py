

def sum_no_duplicates(l):
    return sum([x for x in l if l.count(x) == 1])

def sum_no_duplicates_ultimate(l):
    return sum([x for x in set(l) if l.count(x) == 1])

l = [1, 1, 111]

print(sum_no_duplicates(l))
print(sum_no_duplicates_ultimate(l))


