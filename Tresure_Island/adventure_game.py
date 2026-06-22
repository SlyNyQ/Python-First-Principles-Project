print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input('You\'re at a crossroad. Where would you like to go'
                  '\n    Type "left" or "right"').lower()

game_over = False
if direction == "left":
    #print("Going to the left")
    swim_wait = input(
        'You\'ve come to a lake. There is an island in the middle of the lake.'
        '\n    Type "wait" to wait for a boat. Type "swim" to swim across.').lower()
    if swim_wait == "wait":
        door = input(
            "You arrive at the island unharmed. There is a house with 3 doors."
            "\n     One red, one yellow and one blue. Which colour do you choose?").lower()
        if door == "yellow":
            print("You found the treasure! You Win!")
        elif door == "blue":
            print("You are Eaten by beasts. Game Over.")
        elif door == "red":
            print("You are Burned by fire.Game Over.")
        else:
            print("Game Over. You lose!")
    elif swim_wait == "swim":
        print("You are Attacked by trout.")
elif direction == "right":
    print("You Fall into a hole")
    game_over = True