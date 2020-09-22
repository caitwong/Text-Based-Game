print("Welcome to the Oregon Trail 2.0")
path = input("Take the left of right path:  ")

if path == "left":
    print("Your wagon broke! Result: death")
elif path == "right":
    print("Congrats! You lived.")
    food = input("Eat berries or rations:  ")
    if food == "berries":
        print("The berries were poisoned. Result: death")
    elif food == "rations":
        print("Your rations have restored your health!")
        shelter = input("Take shelter in cave or city:  ")
        if shelter == "city":
            print("You got attacked by raiders. Result: death")
        elif shelter == "cave":
            print("You have survived the night!")
else:
    print("You died.")
