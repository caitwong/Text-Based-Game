print("")
print("------------------------")
print("")
print("Welcome to the Oregon Trail 2.0")
path = input("Take the left or right path:  ")

if path == "right":
    print("Congrats! You lived.")
    print("")
    print("------------------------")
    print("")
    food = input("Eat berries or rations:  ")

    if food == "rations":
        print("Your rations have restored your health!")
        print("")
        print("------------------------")
        print("")
        shelter = input("Take shelter in cave or city:  ")
    
        if shelter == "cave":
            print("You have survived the night!")
            print("")
            print("------------------------")
            print("")
            river = input("There's a river up ahead. Swim or use a boat:  ")

            if river == "boat":
                print("You have evaded the crocodiles!")
                print("")
                print("------------------------")
                print("")
                water = input("Filter your water before drinking?")

                if water == "yes":
                    print("Congrats! You have made it to Oregon!")
                    print("")
                    print("------------------------")
                    print("")

                else:
                    print("You have died of dysentary.")
                    print("")
                    print("------------------------")
                    print("")
            else:
                print("You got eaten by crocodiles. Result: death")
                print("")
                print("------------------------")
                print("")

        else:
            print("You got attacked by raiders. Result: death")
            print("")
            print("------------------------")
            print("")

    else:
        print("The berries were poisoned. Result: death")
        print("")
        print("------------------------")
        print("")
        
else:
    print("Your wagon broke! Result: death")
    print("")
    print("------------------------")
    print("")
