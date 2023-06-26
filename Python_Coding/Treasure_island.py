# treasure island game using python
print("Welcome to treasure island\n")
print("Your mission is to find the Treasure\n")
route=input("There is Diversion where do yoou want to go Left or Right\n ")
if route == "Right" or route=="right"  :
    print("You Fell on the pit !!! Game Over\n")
else :
    route=input("Do you want to swim or wait \n")
    if route== "swim" or route== "Swim" :
        print("You got flushed away by the wave!!! Game Over\n")
    else :
        route=input("which door you want to choose among the three doors RED BLUE & YELLOW\n")
        if route=="RED" :
            print("You fell into the furnace!!! Game Over\n")
        elif route == "BLUE" :
            print("The Tiger separated you into two halfs!!! Game Over \n")
        else :
            print("You Found the Treasure BRAVO!!!! YOU WON !!! CONGRATULATIONS")
    
