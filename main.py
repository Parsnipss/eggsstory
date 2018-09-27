#Functions

def firstChoice():
    print("The Value Grocery store lies at the end of a forest with a lava floor.")
    print("The Premium Grocery is accessible through a large waterside outside your house.")
    print("Both of these grocery stores have the eggs for your omellete.")
    choice = input("Which grocery store do you want to get the eggs from? (Value or Premium): ")
    return choice

"""
Value Market Route
"""
def lavaMonkey():
    print("While staying away from the lava isn't particularly difficult, a lava monkey stands in the way between you and the eggs you seek.")
    print("Being the fantastic chef you are, you always carry a set of utensils with you at all times.")
    print("In order to get past the monkey, you consider using either the Spoon or the Fork as a weapon.")
    weapon = input("Spoon or Fork? ")
    return weapon

#Lose Spoon
def loseSpoon():
    print("The monkey deftly slaps the spoon out of your hand.")
    print("You are sad, but the spoon wouldn't have done much anyways.")
    print("Weaponless and eggless, you return home hungry.")
    print("You lose!")
    
#Win Spoon
def fightGrandma():
    print("The lava monkey does not like being poked, and he returns to his treetop home opening the way forward.")
    print("You make it inside the Value Grocery store, but by the time you make it to the eggs, a normal grocery store grandma has taken the last dozen!")
    print("You REALLY want that omellete, but would you fight a grandma for it?")
    fight = input("(Yes or No): ")
    return fight

#Lose Grandma 
def loseGrandma():
    print("Although it is tempting to snatch the eggs away from grandma, you decide to let her keep the eggs.")
    print("The Grandma notices your sad face and gives you a lolipop for letting her keep the eggs.")
    print("With a lolipop in your hand, you return to your eggsless home.")
    print("You lose!")

#Win Grandma
def valueEggs():
    print("You (Gordon Ramsay) have successfully aquired eggs from the Value Market and have made yourself a delicious omellete!")
    print("Since you fought a grandma for eggs in a grocery store, I'm unsure you can call this a moral victory, but you won either way.")
    exit = input("Do you wish to exit the game? (Yes or No): ")
    return exit
"""
    if exit == "Yes" or exit == "yes":
        break
    else:
        print("Too bad! You are leaving either way!")
        break
"""


"""
Premium Market Route
"""
def waterSlide():
    print("You approach the waterslide, expecting a quick journey, only to find that it is completely dry!")
    print("Being the fantastic chef you are, You are carrying a full stick of butter with you.")
    print("At this point you can either butter yourself up for the slide, or run down it barefoot (to avoid slipping).")
    slide = input("Butter or Run? ")
    return slide
    
store = firstChoice()
weapon = lavaMonkey()
fight = fightGrandma()
endOne = valueEggs()

print("You are Gordon Ramsay, and on this particular day you are craving an omellete.")
print("You get out of bed, excited for the ensuing eggselence, only to find that you have no eggs in the fridge.")
print("This means that you will have to make the trip out to one of two grocery stores.")
firstChoice()
#First Choice
if store == "Value" or store == "value":
    lavaMonkey()
elif store == "Premium" or store == "premium":
    waterSlide()
    
#ValueRoute
if weapon == "Spoon" or weapon == "spoon":
    loseSpoon()
elif weapon == "Fork" or weapon == "fork":
    fightGrandma()
    
    