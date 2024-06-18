import random


random_number = random.randint(1, 9)
print(random_number)
player_choice = 0
while player_choice != random_number:
    player_choice = int(input("Select a number from 1 to 9: "))
    if player_choice == random_number:
        print("You guessed the number exactly right")
        break
    elif player_choice < random_number:
        print("Your guessed number is lower than the actual number")
    else: 
        print ("Your guessed number is higher than the actual number")
