import time
import random

def print_pause(msg):
    print(msg)
    time.sleep(2)

def field(weapon):

    while True:
        print_pause("Enter 1 to knock on the door of the house.")
        print_pause("Enter 2 to peer into the cave.")
        print_pause("What would you like to do?")
        print_pause("(Please enter 1 or 2.)")
        response = input();
        if(int(response)==1):
            status = house(weapon)
            if status in ["win", "lose", "exit"]:
                break;
        elif(int(response)==2):
            weapon = cave(weapon)


def house(weapon):
    animal = random.choice(["troll", "wicked fairies"])
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out steps a "+animal+".")
    print_pause("Eep! This is the "+animal+"'s house!")
    print_pause("The "+animal+" attacks you!")

    print_pause("You feel a bit under-prepared for this, what with only having a "+weapon+".")
    print_pause("Would you like to (1) fight or (2) run away?")

    print_pause("(Please enter 1 or 2.)")
    response = input();
    if(int(response)==1):
        status = fight(animal, weapon)
    elif(int(response)==2):
        run_away()
        status="run_away"
    else:
        status="exit"

    return status

def cave(weapon):
    print_pause("You peer cautiously into the cave.")

    if weapon== "Sword of Ogoroth":
        print_pause("You've been here before, and gotten all the good stuff. It's just an empty cave now.")
    else:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take the sword with you.")
        weapon = "Sword of Ogoroth"

    print_pause("You walk back out to the field.")
    return weapon

def fight(animal, weapon):
    status = "lose"
    if(weapon=="Sword of Ogoroth"):
        print_pause("As the "+animal+" moves to attack, you unsheath your new sword.")
        print_pause("The "+weapon+" shines brightly in your hand as you brace yourself for the attack.")
        print_pause("But the "+animal+" takes one look at your shiny new toy and runs away!")
        print_pause("You have rid the town of the "+animal+". You are victorious!")
        status = "win"
    else:
        print_pause("You do your best...")
        print_pause("but your "+weapon+" is no match for the "+animal+".")
        print_pause("You have been defeated!")

    return status


def run_away():
    print("You run back into the field. Luckily, you don't seem to have been followed.")


def play_game():
    print_pause("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a troll is somewhere around here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")

    while True:
        weapon="dagger"
        print_pause("In your hand you hold your trusty (but not very effective) "+weapon+".")
        field(weapon)
        again = input("Would you like to play again? (y/n)")
        if again == "y":
            print("Excellent! Restarting the game ...")
        else:
            print("Thanks for playing! See you next time.")
            break

play_game()
