#https://www.codewars.com/kata/525c65e51bf619685c000059/train/python

def cakes(recipe, available):
    return min([available[x] / recipe[x] if x in list(available.keys()) else 0 for x in list(recipe.keys())])
