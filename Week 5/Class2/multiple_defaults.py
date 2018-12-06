def favourites (colour="transparent", food="lasagna"):
# transparent and lasagna are the default values
    print("Your favourite colour: {0} ".format(colour))
    print("Your favourite food: {0} ".format(food))
    print()

favourites("red", "beer")
# The next one uses the default values
favourites()
# The next one use the default for food
favourites("A")
# The next one usea the default for colour
favourites(food="Anything")

