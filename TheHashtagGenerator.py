# https://www.codewars.com/kata/52449b062fb80683ec000024/train/python


# A space seperates words - groupby space
# Each first letter of each words gets a capital

def generate_hashtag(s):
    if not s:
        return False
    hashtag = '#'+''.join([word.capitalize() for word in s.rsplit(" ")])
    return hashtag if hashtag.__len__() < 141 else False

print(generate_hashtag('test test'))


