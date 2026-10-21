"""
Author: Alex
Date: 10-15-2026
Description: Gives information on what upgrades the player should have access to
"""
def get_active_upgrades(day):
    """
    Description: takes day and returns boolean list depending on what upgrades the player should have unlocked
    Parameters: (int) day: the current day the player is on
    Return: upgrades: a list of 6 booleans that represent the upgrades the player has (index0=day2)
    """
    upgrades = {a:True if day >= a else False for a in range( 2, 8 )}
    return upgrades
print(get_active_upgrades(1))