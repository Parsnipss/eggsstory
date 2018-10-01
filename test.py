lives = 5

gameExit = False

while (gameExit == True):
    break

def firstChoice(lives):
    print("The Value Grocery store lies at the end of a forest with a lava floor.")
    print("The Premium Grocery store is accessible through a large waterside outside your house.")
    print("Both of these grocery stores have the eggs for your omellete.")
    choice = input("Which grocery store do you want to get the eggs from? (Value or Premium): ")
    if lives == 0:
        print("Clearly confused, Gordon heads back inside to get more sleep.")
        gameExit = True
        return gameExit
    
    if choice == "Value" or choice == "value":  #See "Value Route"
        print("s")
    elif choice == "Premium" or choice == "premium":    #See "Premium Route"
        print("l")
    else:   #The Catch
        lives = lives - 1
        print("You look around, but do not see a store by that name.")
        firstChoice(lives)
        
firstChoice(lives)

