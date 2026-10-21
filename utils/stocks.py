"""
Author: Alex
Editor: Nicole
Date: 10-14-2026
Description: Contains get_stocks() and list of all stocks
"""
from random import choice
# low/med/high[a]==[(str) stock name, (str) stock description, (float) stock starting price ($), (tuple)(floats) stock variaton: percentages]
# low starting price=100, +variation =.01-.03, -variation=-(+variation/4)
low = [
        ["Sliced Bread", "As safe and simple as it gets.", 100.00, (-.0025, .01)],
        ["Math", "The laws of math stay consistent.", 100.0, (-.0075, .03)],
        ["Boiled Chicken", "The most boring food possible.", 100.0, (-.0025, .01)],
        ["Cheerios", "The most simple cereal immaginable", 100.0, (-.005, .02)],
        ["Library", "You can always go to borrow free books", 100.0, (-.0075, .03)],
        ["World Clock", "Time will always continue forward", 100.0, (-.0025, .01)],
        ["Coffee", "Caffiene keeps life going", 100.0, (-.005, .02)],
        ["Forks", "World's #1 utensil", 100.0, (-.005, .02)],
        ["Pencils", "Pencils will always be used to write things down, and they remain mostly the same.", 100.0, (-.0075, .03)],
        ["The Circle of Life", "The circle of life will continue onwards forever looping", 100.0, (-.0025, .01)]
    ]
# med starting price=500, +variation =.06-.15, -variation=-(+variation/2)
med = [
        ["Popular Music", "Tastes evolve over time, but won't change too much too quickly", 500.0,(-.035, .07)],
        ["The Law", "Interpretations may be different, but should follow the framework.", 500.0, (-.055, .11)],
        ["Weather", "Variable, but with predictable patterns.", 500.0, (-.06, .12)],
        ["Apples", "Numerous kinds, but still the same idea every time", 500.0, (-.065, .13)],
        ["Science", "New discoveries can be made, but will likely take a long time, and even longer for a massive change.", 500.0, (-.0325, .065)],
        ["Social Media Platforms", "Platforms may change features every once in a while, but not very often", 500.0, (-.045, .09)],
        ["Language", "Language will evolve over time but won't change drastically", 500.0, (-.04, .08)],
        ["Evolution", "Creatures will evolve over time, but not too quickly", 500.0, (-.03, .06)],
        ["Technology", "People are constantly searching for inovations in technology, but they take some time to create", 500.0, (-.0375, .075)],
        ["Pizza", "There are many toppings, but no matter which ones you choose it's still pizza", 500.0, (-.07, .14)]
    ]
# high starting price=1000, +variation =.2-.35, -variation=-(+variation)
high = [
        ["Movie Musicals", "Either the best or worst thing ever, no inbetween.", 1000.0, (-.2, .2)],
        ["Mutations", "Who knows what'll happen.", 1000.0, (-.35, .35)],
        ["Superhero Movies", "Could be anywhere from a completely faithful adaptation to a complete bastardization of characters.", 1000.0, (-.21, .21)],
        ["Indie Games", "Could be game of the year, or could be trash, who knows.", 1000.0, (-.26, .26)],
        ["Halloween Candy", "Size and quality may differ drastically.", 1000.0,(-.25, .25)],
        ["Blind Box", "Never any guarantee what'll be there.",1000.0,(-.27, .27)],
        ["Trends", "Trends never seem to stop changing.", 1000.0, (-.28, .28)],
        ["Art", "Art is completely subject to each person's creativity.",1000.0,(-.33, .33)],
        ["Genetics", "Genetics have such an incrediblly large amount of variation", 1000.0, (-.34, .34)],
        ["Taste Buds", "People's tastes have a lot of variation, allowing for people to taste differently", (-.24, .24)]
    ]

def get_stocks(num):
    """
    if num==3: return one stock from each category, 
    if num==2: return one stock from only med and high

    Parameters: (int) num: the number of stocks to return, either 2 or 3

    Returns: either one stock from each section or one from med and one from high depending on num
    """
    
    if num == 3:
        # Pulling stocks and Removing used stocks from lists
        choice_low = choice(low)
        choice_med = choice(med)
        choice_high = choice(high)
        low.remove(choice_low)
        med.remove(choice_med)
        high.remove(choice_high)
        return[choice_low, choice_med, choice_high]
    
    if num == 2:
        choice_med = choice(med)
        choice_high = choice(high)
        med.remove(choice_med)
        high.remove(choice_high)
        return[choice_med, choice_high]