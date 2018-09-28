import time

gameExit = False

while gameExit == True:
    print ("Exiting the game!")
    time.sleep(3)
    break

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
    if weapon == "Spoon" or weapon == "spoon":
        print("The monkey deftly slaps the spoon out of your hand.")
        print("You are sad, but the spoon wouldn't have done much anyways.")
        print("Weaponless and eggless, you return home hungry.")
        print("You Lose!")
        gameExit = True
        return gameExit
    elif weapon == "Fork" or weapon == "fork":
        fightGrandma()

#Lose Spoon
def loseSpoon():
    print("The monkey deftly slaps the spoon out of your hand.")
    print("You are sad, but the spoon wouldn't have done much anyways.")
    print("Weaponless and eggless, you return home hungry.")
    print("You Lose!")
    
#Win Spoon
def fightGrandma():
    print("The lava monkey does not like being poked, and he returns to his treetop home opening the way forward.")
    print("You make it inside the Value Grocery store, but by the time you make it to the eggs, a normal grocery store grandma has taken the last dozen!")
    print("You REALLY want that omellete, but would you fight a grandma for it?")
    fight = input("(Yes or No): ")
    if fight == "Yes" or fight == "yes":
        valueEggs()
    elif fight == "No" or fight == "no":
        loseGrandma()

#Lose Grandma 
def loseGrandma():
    print("Although it is tempting to snatch the eggs away from grandma, you decide to let her keep the eggs.")
    print("The Grandma notices your sad face and gives you a lolipop for letting her keep the eggs.")
    print("With a lolipop in your hand, you return to your eggsless home.")
    print("You Lose!")
    gameExit = True
    return gameExit

#Win Grandma
def valueEggs():
    print("You (Gordon Ramsay) have successfully aquired eggs from the Value Market and have made yourself a delicious omellete!")
    print("Since you fought a grandma for eggs in a grocery store, I'm unsure you can call this a moral victory, but you won either way.")
    exit = input("Do you wish to exit the game? (Yes or No): ")
    if exit == "Yes" or exit == "yes":
        gameExit = True
    else:
        print("Too bad! You are leaving either way!")
        gameExit = True
    

"""
Premium Market Route
"""
def waterSlide():
    print("You approach the waterslide, expecting a quick journey, only to find that it is completely dry!")
    print("Being the fantastic chef you are, You are carrying a full stick of butter with you.")
    print("At this point you can either butter yourself up for the slide, or run down it barefoot (to avoid slipping).")
    slide = input("Butter or Run? ")
    if slide == "Butter" or slide == "butter":
        butter()
    elif slide == "Run" or slide == "run":
        run()
    else:
        print("Gordon's inability to decide will force him to run down the slide!")
        run()

def butter():
    print("You quickly whip out your stick of fresh butter and begin to cover yourself in a thick layer of butter.")
    print("Now that you're all buttered up, you get on the slide and start cruising down to the market.")
    print("You finally arrive to the Premium Market and grab the glorious eggs, BUT you realize you don't have enough money!")
    print("Would you steal the eggs for your precious omellete?")
    steal = input("Do you wish to steal the eggs? (Yes or No): ")
    if steal == "Yes" or steal == "yes":
        yesSteal()
    elif steal == "No" or steal == "no":
        noSteal()

#Win Steal
def yesSteal():
    print("You look around aisle to see if anyone is around before carefully hiding the eggs under your jacket.")
    print("As you walk closer and closer to the exit, you dash immediately out of the store after one of your eggs fell on the floor!")
    print("The security guard begins chasing after you, but you manage to get away from him and safely return home.")
    print("Now that you have the eggs, you make the most delicious omellete ever and enjoy your meal.")
    print("You Win!")
    exit = input("Do you wish to exit the game? (Yes or No): ")
    if exit == "Yes" or exit == "yes":
        gameExit = True
    else:
        print("Too bad! You're going to be kicked out!")
        gameExit = True
    
#Lose Steal
def noSteal():
    print("You decide not to steal the eggs because it's the wrong thing to do and you don't want to go to jail.")
    print("You return to your eggless home and decide to just cook some omellete flavored cup noodles instead.")
    print("You Lose!")
    gameExit = True
    return gameExit
    
#Lose Run
def run():
    print("You take off your shoes in order to run down the hot, burning, plastic slide.")
    print("As you run down the slide, you're in agonizing pain because you burned you feet.")
    print("Suddenly the slide begins to work properly again and a gush of water begins to flow down the slide!")
    print("You slip and begin to enjoy the ride until the slide makes you miss Whole Foods and you are separated from your precious eggs.")
    print("You Lose!")
    gameExit = True
    return gameExit

print("You are Gordon Ramsay, and on this particular day you are craving an omellete.")
print("You get out of bed, excited for the ensuing eggselence, only to find that you have no eggs in the fridge.")
print("This means that you will have to make the trip out to one of two grocery stores.")
store = firstChoice()
#First Choice
if store == "Value" or store == "value":
    lavaMonkey()
elif store == "Premium" or store == "premium":
    waterSlide()
    
    
    