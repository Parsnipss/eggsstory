gameExit = False

while gameExit == True:
    break

def lavaMonkey():
    print("While staying away from the lava isn't particularly difficult, a lava monkey stands in the way between you and the eggs you seek.")
    print("Being the fantastic chef you are, you always carry a set of utensils with you at all times.")
    print("In order to get past the monkey, you consider using either the Spoon or the Fork as a weapon.")
    weapon = input("Spoon or Fork? ")
    if weapon == "Spoon" or weapon == "spoon":
        print("The monkey deftly slaps the spoon out of your hand.")
        print("You are sad, but the spoon wouldn't have done much anyways.")
        print("Weaponless and eggless, you return home hungry.")
        print("You lose!")
        gameExit = True
        return gameExit
    elif weapon == "Fork" or weapon == "fork":
        fightGrandma()

#Win Spoon
def fightGrandma():
    print("The lava monkey does not like being poked, and he returns to his treetop home opening the way forward.")
    print("You make it inside the Value Grocery store, but by the time you make it to the eggs, a normal grocery store grandma has taken the last dozen!")
    print("You REALLY want that omellete, but would you fight a grandma for it?")
    fight = input("(Yes or No): ")
    return fight

lavaMonkey()

