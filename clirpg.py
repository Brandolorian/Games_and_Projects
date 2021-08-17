# Build a CLI RPG game following the instructions from the course.

# Ask the player for their name.

# Display a message that greets them and introduces them to the game world.

# Present them with a choice between two doors.

# If they choose the left door, they'll see an empty room.

# If they choose the right door, then they encounter a dragon.
 
# In both cases, they have the option to return to the previous room or interact further.

# When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.

# When encountering the dragon, they have the choice to fight it.

# If they have the sword from the other room, then they will be able to defeat it and win the game.

# If they don't have the sword, then they will be eaten by the dragon and lose the game.

name = input("Hello! Welcome to the world of DnD. What is your name? ")
print(f"Welcome {name}! Thanks for playing. If at any point you want to stop playing, simply type 'quit'.")
game = True
sword = False

while game == True:
    doors = input("You encounter two doors. A door on your left and a door on your right. Which door would you like to go through? ")
    if doors == "quit":
        print("Game Over. Thanks for playing!")
        game = False
        continue
    elif doors != "left" and doors != "right":
        print("That's not an option. Please only enter left or right.")
        continue
    elif doors == "left":
        while True:
            direction = input("You enter the door on your left, which.... is empty. Would you like to look around? If not, you will return to the beginning. ")
            if direction == "no":
                continue
            if direction == "yes":
                sword = input("Woot! You found a sword! Do you want to take the sword? ")
                if sword == "yes":
                    sword = True
                    print("You take the mighty sword and leave the room. Why not try the door on your right now? ;)")
                    if direction == "yes" and sword == True:
                        break
    elif doors == "right":
        while True:
            direction_two = input("Ah! You encounter a mighty dragon named Grogu! Do you attack Grogu? ")
            if direction_two == "yes" and sword == True:
                print("You have slain the mighty Grogu! Congratulations hero. You win!")
                break
            if direction_two == "yes" and sword == False:
                print(f"Grogu eats {name} whole. You lose. 'Hint: You May Want to Search Around in that Seemingly Empty Room Next Time. ;)'")
                break
            if direction_two == "no" and sword == True:
                print(f"You walk away from the castle with your new sword and head home. Thanks for playing {name}!")
                break
            if direction_two == "no" and sword == False:
                print(f"You walk away from the castle with nothing. Thanks for playing {name}!")
                break
