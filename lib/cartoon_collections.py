CHEESES = ["camembert", "gouda", "cheddar"]

def roll_call_dwarves(dwarves):
    i = 1
    for dwarf in dwarves:
        print(f"{i}. {dwarf}")
        i += 1

def summon_captain_planet(planeteer_calls):
    planeteer_call_list = []
    for element in planeteer_calls:
        planeteer_call_list.append(element.capitalize() + "!")
    return planeteer_call_list
    

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(foods):
    for food in foods:
        if food in CHEESES:
            return food
    return None
