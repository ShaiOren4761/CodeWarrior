# https://www.codewars.com/kata/5264d2b162488dc400000001/python
def spin_words(sentence):
    ret = ''
    count = 0

    for i, c in enumerate(sentence):
        if c.isalpha():
            count += 1
        elif count >= 5:
            ret += sentence[i:i - count:-1]
            count = 0
        else:
            ret += sentence[i - count:i + 1]
            count = 0
    else:
        # i += 1
        if count >= 5:
            sentence = ' ' + sentence
            ret += sentence[i+1:i - count + 1:-1]
        else:
            ret += sentence[i - count:i + 1]

    return ret


# print(spin_words('Welcome'))
# print(spin_words('Hey fellow warriors'))

# s = 'Hey fellow warriors'
# counter = 6
# i = 10


def spin_words_better(sentence):
    ret = ''
    word = ''

    for i, c in enumerate(sentence):
        if c.isalpha():
            word += c
        elif len(word) >= 5:
            ret += word[::-1] + ' '
            word = ''
        else:
            ret += word + ' '
            word = ''
    else:
        if len(word) >= 5:
            ret += word[::-1]
        else:
            ret += word

    return ret


def spin_words_ultimate(sentence):
    # Your code goes here
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])


print(spin_words_ultimate('This sentence is a sentence'))
