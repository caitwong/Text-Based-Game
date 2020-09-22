print("Welcome to the Oregon Trail")
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

else:
    print("You died.")
