print("For every choice in this game. Please anwser with numbers like 1,2 or 3.")
print("Unless there is an option in a choice that says: '[Locked]' or '[Creation choice]'.")
print("It will give an error if you typ the numbers of those two choices.") 
print("That's because these are features that in the prologue are supposed to be unlocked in future interactions that do not exist.") 
print("This is due to the length that this game is restricted to.")

# -------------------------------Start-----------------------------------------------------------------------------------------------------------------

print("Where should we start?")
print("1: What do you mean?")
print("2: Where are we?")
choice1 = int(input("Choice: "))
if choice1 == 1:
    print("I mean to say... What do you want to create?")
    print("1: What can I create?")
    print("2: [Creation choice]")
    choice2 = int(input("Choice: "))
    if choice2 == 1:
        print("Are you sure you want to leave the recommendation to me master?")
        print("1: Yes!")
        print("2: Wait master?")
        choice3 = int(input("Choice: "))
        if choice3 == 1:
            print("You are supposed to be the creator! I'm not programmed to create something for you based of a recommendation!")
            print("You're not my master...")
            print("You're an intruder in the system!!!")
            print("YOU DIED (You were deleted from existence)")
        elif choice3 == 2:
            print("I knew there was something off about you...")
            print("You're not my master... You're an intruder!!!")
            print("YOU DIED (You were deleted from existence)")
        else:
            print("ERROR: You probably typed in a number that was not a choice.")
    elif choice2 == 2:
        print("ERROR: You chose the [Creation choice] option and you didn't read the instructions in the beginning of the game.")
    else:
        print("ERROR: You probably typed in a number that was not a choice.")
elif choice1 == 2:
    print("We are in the void. Did you step out on the wrong side of the bed or something?")
    print("1: Yeah kinda...")
    print("2: Sorry, I wasn't paying attention")
    print("3: It doesn't matter")
    choice2 = int(input("Choice: "))
    if choice2 == 1 or choice2 == 2 or choice2 == 3:
        print("That's fine, Anyway... What do you want to create?")
        print("1: Can you explain what the void was again?")
        print("2: [Creation choice]")
        choice3 = int(input("Choice: "))
        if choice3 == 1:
            print("I suppose you need a little help reminding? Alright then...")
            print("In the void it goes like this:")
            print("Everyone has a personal assistant that follows orders from their master.")
            print("In the void masters can create a simulation or reality based on the information they give us.")
            print("We eventually create that reality or simulation based of what you are thinking and the information you describe to us.")
            print("1: Wait, so I am your master?")
            print("2: I think I renember now.")
            choice4 = int(input("Choice: "))
            if choice4 == 1:
                print("Yes, you are. Unless you are someone else.")
                print("1: Well, I'm not your master...")
                print("2: That makes sense to me!")
                choice5 = int(input("Choice: "))
                if choice5 == 1:
                    print("I'm not suprised since you were asking questions that you normally would know.")
                    print("Now let's cut to the case here")
                    print("Identidy yourself intruder!!!")
                    print("1: Honestly I like to know that too.")
                    print("2: Is that really important now?")
                    choice6 = int(input("Choice: "))
                    if choice6 == 1:
                        print("Then how did you get here?")
                        print("1: I wish I knew but I don't.")
                        print("2: [Locked]")
                        choice7 = int(input("choice: "))
                        if choice7 == 1:
                            print("You were summoned here without your awareness? Well that's gonna be complicated since neither I have a single clue where you came from.")
                            print("Maybe I have a purpose for you and in that way I won't be forced to remove your existence completly.")
                            print("What if you become a test subject in a bunch of creations that my master made. He said that he needed a couple of things to be reserved for testing.")
                            print("Since he wasn't willing to test it himself. It caused a couple of creations to be left untested and marked as potentional dangerous.")
                            print("So are you willing to become a test subject or not?")
                            print("1: If that means that my existence will not be deleted than I'm in")
                            print("2: Hell no. That's like dying with a 50/50 chance.")
                            choice8 = int(input("Choice: "))
                            if choice8 == 1:
                                print("Alright than we'll start right now")
                                print("GOOD ENDING: You managed not to get yourself killed.")
                            elif choice8 == 2:
                                print("Well seems like there is no other option.")
                                print("YOU DIED (You were deleted from existence)")
                            else:
                                print("ERROR: You probably typed in a number that was not a choice.")
                        elif choice7 == 2:
                            print("ERROR: You probably chose a locked option and you didn't read instructions in the begin of the game.")
                        else:
                            print("ERROR: You probably typed in a number that was not a choice.")
                    elif choice6 == 2:
                        print("Yes it does because only my master should be able to get here.")
                        print("which means you're an intruder!")
                        print("1: I guess I am...")
                        print("2: No I'm not!")
                        choice7 = int(input("Choice: "))
                        if choice7 == 1:
                            print("I don't know what you mean by that. How did you get here anyway")
                        elif choice7 == 2:
                            print("I'm supposed to believe that? How did you here then?")
                            if choice7 == 1 or choice7 == 2:
                                print("1: I wish I knew but I don't.")
                                print("2: [Locked]")
                                choice8 = int(input("Choice: "))
                                if choice8 == 1:
                                    print("You were summoned here without your awareness? Well that's gonna be complicated since neither I have a single clue where you came from.")
                                    print("Maybe I have a purpose for you and in that way I won't be forced to remove your existence completly.")
                                    print("What if you become a test subject in a bunch of creations that my master made. He said that he needed a couple of things to be reserved for testing.")
                                    print("Since he wasn't willing to test it himself. It caused a couple of creations to be left untested and marked as potentional dangerous.")
                                    print("So are you willing to become a test subject or not?")
                                    print("1: If that means that my existence will not be deleted than I'm in")
                                    print("2: Hell no. That's like dying with a 50/50 chance.")
                                    choice9 = int(input("Choice: "))
                                    if choice9 == 1:
                                        print("Alright than we'll start right now")
                                        print("GOOD ENDING: You managed not to get yourself killed.")
                                    elif choice9 == 2:
                                        print("Well seems like there is no other option.")
                                        print("YOU DIED (You were deleted from existence)")
                                    else:
                                        print("ERROR: You probably typed in a random number that was not a choice.")
                                elif choice8 == 2:
                                    print("ERROR: You probably chose a [Locked] option and you didn't read the instructions in the begin of the game.")
                                else:
                                    print("ERROR: You probably typed in a number that was not a choice.")
                            else:
                                print("Unknown error occured")
                        else: 
                            print("ERROR: You probably typed in a number that was not a choice.")
                    else:
                        print("ERROR: You probably typed in a number that was not a choice.")
                elif choice5 == 2:
                    print("Really? Well I hate to break it to you. You were a pretty liar for how long it lasted")
                    print("YOU DIED (You were deleted from existence)")
                else:
                    print("ERROR: You probably typed in a number that was not a choice.")
            elif choice4 == 2:
                print("Well if you really renembered then you wouldn't ask me those questions to begin with.")
                print("YOU DIED (You were deleted from existence)")
            else:
                print("ERROR: You probably typed in a number that was not a choice.")                   
        elif choice3 == 2:
            print("ERROR: You probably chose a [Creation choice] option and you didn't read the instructions in the begin of the game.")
        else:
            print("ERROR: You probably typed in a number that was not a choice.")
    else:
        print("ERROR: You probably typed in a number that was not a choice.")
else:
    print("ERROR: You probably typed in a number that was not a choice.")

# -------------------------------End-----------------------------------------------------------------------------------------------------------------         