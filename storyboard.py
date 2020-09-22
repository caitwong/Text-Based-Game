print("")
print("------------------------")
print("")
print("Welcome to the Oregon Trail 2.0")
path = input("Take the left of right path:  ")

if path == "left":
    print("Your wagon broke! Result: death")
    print("")
    print("------------------------")
    print("")
elif path == "right":
    print("Congrats! You lived.")
    print("")
    print("------------------------")
    print("")
    food = input("Eat berries or rations:  ")
    if food == "berries":
        print("The berries were poisoned. Result: death")
        print("")
        print("------------------------")
        print("")
    elif food == "rations":
        print("Your rations have restored your health!")
        print("")
        print("------------------------")
        print("")
        shelter = input("Take shelter in cave or city:  ")
        if shelter == "city":
            print("You got attacked by raiders. Result: death")
            print("")
            print("------------------------")
            print("")
        elif shelter == "cave":
            print("You have survived the night!")
            print("")
            print("------------------------")
            print("")
else:
    print("You died.")
