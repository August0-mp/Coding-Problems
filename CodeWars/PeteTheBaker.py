def cakes(recipe, available):
    try:
        return min(available[k] // recipe[k] for k in recipe)
    except KeyError:
        return 0
