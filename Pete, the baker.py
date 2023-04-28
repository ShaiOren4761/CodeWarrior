#  https://www.codewars.com/kata/525c65e51bf619685c000059/train/python

def cakes(recipe, available):
    return int((min([available[ing]/recipe[ing] if available.get(ing) else 0 for ing in recipe])))


recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
print(cakes(recipe, available))


