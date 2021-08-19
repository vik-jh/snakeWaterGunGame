import random

swg = ['s for snake', 'w for water', 'g for gun'  ]
chance = 10
no_of_chance = 0
computer_point = 0
human_point = 0

print("Let's play Snake-Water-Games \n")

print(swg)


while no_of_chance < chance: 
    _input = input("Enter your choice from the list: \n")
    _random = random.choice(swg)

    if _input == _random: 
        print("This is a Tie")

    elif _input == "s" and _random == "g":
        computer_point +=1
        print("Congratulations!! Computer ji!!! You Won!!!! \n")
        print(f"computer point is {computer_point} and your point is {human_point} \n")

    elif _input == "s" and _random == "w":
        human_point +=1
        print("You won! Congratulations!! \n")
        print(f"You have won {human_point} point. \n")
    
    elif _input =="g" and _random == "s":
        human_point +=1
        print("You won! Congratulations!!")
        print(f"You won {human_point} point \n")
    elif _input == "g" and _random == "w":
        computer_point +=1
        print("Congratulations!! computer ji.. You won!! \n")
        print(f"computer point is {computer_point} \n")
    
    elif _input == "w" and _random == "g":
        human_point +=1
        print("You won! Congratulations!!")
        print(f"You won {human_point} point \n")

    elif _input == "w" and _random == "s":
        computer_point +=1
        print("Congratulations!! computer ji.. You won!! \n")
        print(f"computer point is {computer_point} \n")

    else:
        print("Wrong input!! Please Try again with right input \n")

    no_of_chance = no_of_chance + 1
    print(f"You have left{chance - no_of_chance} out of {chance} \n")

    


if computer_point > human_point:
    print("Computer Wins!! Congrats! \n")

elif computer_point < human_point:
    print("Congrats on your victory!! \n")

else:
    print("Tied \n")

print(f"Your point is {human_point} and computer point is {computer_point} \n")








    







