import random
import time

def pause():
    time.sleep(1)
    global next_landmark
    global current_landmark
    print("")
    print(f'You have conqured {current_landmark}, you can:')
    
        
    while True:
        print("1. check crew status,")
        print("2. check inventory,")
        print("3. check next land mark")
        choice = input("4. continue your journey ")
        print("")
        if (choice == '1' or choice == 'check crew status'):
            print("")
            print(f'you have {crew} crew members in good condition')
            print(crew_mood)
            if (afflicted_crew != 0):
                print(f"You have {afflicted_crew} crew members afflicted by lotus")
            print("")
            time.sleep(1)
        elif (choice == '2' or choice == 'check inventory'):
            print("")
            print(f'you have {gold} gold')
            if (wind_bag):
                print("you have a wind bag")
                print("")
            elif (cubit_of_sheep_blood):
                print("you have two sacraficial sheep given to you by the witch Circe")
            elif (lots_of_wine):
                print("you have many barrels of wine for libations")
            print("")
            time.sleep(1)
        elif (choice == '3' or choice == 'check next landmark'):
            print("")
            print(f'the next landmark is {next_landmark}')
            print("")
            time.sleep(1)
        elif (choice == '4'):
            print("")
            time.sleep(.5)
            break
        else:
            print("please chose a valid option")
            print("")
            time.sleep(.5)

def intro():
    print("Intro text __________________________________")
    print("You are legendary Odysseus, the king of Ithaca and a hero of the Trojan War. You command an army 600 strong and you carry 5000 gold, your portion of the Greek army's winnings from defeating the Trojans at war.")
    print("Now your goal is to make it home to Ithaca. your kindom is waiting for their king. Your wife is waiting for her husband. your son is waiting for his father")
    print("you start with 600 crew members and 1000 gold")

def cicones():
    global gold
    global crew
    sub_gold = 0
    sub_crew = 0
    text = input('you have made it to Ismarus, the land of the cicones! [Enter]')
    while True:
        cicones_choice = input("Sack it? y/n ").lower()
        print("")
        if (cicones_choice == 'y'):
            print("")
            print ("You sack the city")
            print("")
            sub_gold = 1500 + random.randint(1,1000)
            gold = gold + sub_gold
            sub_crew = 10 + random.randint(1,30)
            crew = crew - sub_crew
            print(f'you gain {sub_gold} gold, but lose {sub_crew} crew members')
            print("")
            break
        elif (cicones_choice == 'n'):
            print("you don't sack the city")
            break
        else:
            print("You must choose an option")
    
def lotus_island():
    global gold
    global crew
    global afflicted_crew
    global death
    sub_gold = 0
    sub_crew = 0
    text = input("you arrive at the island of the lotus eaters. [Enter]")
    
    while True:
        sub_crew = int(input("How many men do you send to scout? "))
        print("")
        
        if (sub_crew > crew):
            text = input(f"you can't send {sub_crew} men, you only have {crew} crew members")
        elif (sub_crew >= crew / 2):
            text = input("you find it wise to not send so many men")
            print("")
        elif (sub_crew < 1):
            text = input("you can't send a negative number of crew members")
            print("")
        else:
            break
    
    text = input(f"you send {sub_crew} of your men to scout the island. After some time they return bearing fruit. They seem fine, but upon closer inspection, they seem addled, as if something had afflicted them on the island. [Enter]")
    print("")
    afflicted_crew = sub_crew
    crew = crew - afflicted_crew
    lotus_choice = input("do you eat one of the fruit? y/n ")
    print("")
    
    if (lotus_choice == 'y'):
        text = input("you eat one of the fruit. Suddenly your mind is at peace. you want nothing more than to take another bite of this fruit. What was your goal again? It doesn't matter, you have everything you need right here on this island. [Enter]")
        print("")
        death = True
    else:
        text = input("You've heard of this fruit before. This is lotus, a dangerous fruit that takes control of the mind of the person who eats it. you tell the rest of your crew of the dangers of the lotus and command them to get their addled companions on board the ship and to tie them up below deck. [Enter]")
        print("")

def cyclops():
    global gold
    global crew
    global death
    global sub_crew
    sub_gold = 0
    crew_lost = 0
    text = input("You have arrived on the island of the cyclopes. You pack some wine as libations and set out to explore. [Enter]")
    while True:
        sub_crew = int(input("How many men do you bring with you? "))
        print("")
        if (sub_crew > crew):
            print(f"you can't bring {sub_crew} men, you only have {crew} men who are able to explore. [Enter]")
            print("")
        elif (sub_crew < 0):
            print("you can't bring a negative number of crew members. [Enter]")
            print("")
        elif (sub_crew < 7):
            print("you find it wise to bring more crew members than that. [Enter]")
            print("")
        else:
            break
    
    text = input(f'After some exploring of the island you come to a cave. You enter the cave with your {sub_crew} crew members. Inside the cave there are a lot of sheep. [Enter]')
    
    while True:
        cyclopes_choice = input("Do you kill one? y/n ").lower()
        print("")
        if (cyclopes_choice == 'y'):
            text = input("As you kill the sheep, A cyclops enters the cave. Seeing what you have done it lets out a tremendous roar. It blocks the exit and bears down, ready to fight you. [Enter]")
            print("")
            cyclops_fight()
            break
        
        elif(cyclopes_choice == 'n'):
            time.sleep(1)
            print("")
            text = input("you decide to wait to see the sheep's shepard. After some time, a cyclops comes in, blocks the exit and begins to tend his sheep. After tending his sheep he sees you and your men. [Enter]")
            print("")
            text = input("the cyclops then asks of your intentions. You lie to him, saying that you are greeks who have conqured Troy, but unfortunate winds have blown you to his island, and you have been shipwrecked here. you only came to this cave seeking refuge. [Enter]")
            print("")
            text = input("without reply the cyclops raises his fist high and knocks two of your men against the ground like puppies, killing them and devouring their bodies. [Enter]")
            crew_lost = 2
            sub_crew = sub_crew - 2
            crew = crew - 2
            
            while True:
                print("")
                cyclopes_choice_2 = input("Seeing this do you, 1. come up with a plan to trick him, or 2. command your men to defend themselves like the warriors they are.")
                print("")
                if(cyclopes_choice_2 == '1'):
                    print("")
                    print ("Realizing his ruthlesness, you formulate a plan.")
                    time.sleep(1)
                    print("")
                    text = input("you, cunning Odysseus, decide to offer him your wine you brought as libations, telling him you brought it as a holy offering, but will give it to him to quell his rage. [Enter]")
                    print("")
                    text = input('he drinks down the strong sweet wine. As he finishes, he asks of your name. You reply "I am known as Nobody." He then says "Nobody, for your gift I have one to reply, first I will eat the rest of your crew, then last I will devour you". [Enter]')
                    print("")
                    text = input("with that he immediately colapses into a drunken stupor. You waste no time, shouting to your men to grab his great club and sharpen its tip. Your men immediately set to work and do not finish until it is as sharp as can be. Once they are finished, you drive the spear into his eye. [Enter]")
                    print("")
                    text = input('With this he wakes up howling in pain. then from outside the cave you hear many other cyclopes call out "Polyphemus! Why do you cry? are you badly hurt?" [Enter]')
                    print("")
                    text = input('Great Polyphemus replies, "Nobody has blinded me, Nobody is killing me!" the other cyclopes respond, "if nobody hurts you, you are all alone" and they begin to leave. [Enter]')
                    print("")
                    text = input('Polyphemus shouts out for them to stay and listen, but they continue to go. The once terifying cyclops then pulls the boulder away from the mouth of his cave and chases after the other cyclopes trying to explain who Nobody is. [Enter]')
                    print("")
                    text = input("With that, you and the rest of your men are able to escape the cyclops's cave and return safely to your ships. [Enter]")
                    break
                
                elif (cyclopes_choice_2 == '2'):
                    print("")
                    text = input("You, legendary Odysseus, command your men to avenge their fallen comrades and fight the wicked beast who has shown nothing but cruelty to you")
                    cyclops_fight()
                    break
                
                else:
                    print("You must chose either option 1. or option 2.")
                    print("")
            break
        else:
            print("You must choose one of the options")

def cyclops_fight():
    global gold
    global crew
    global death
    global sub_crew
    sub_gold = 0
    if(sub_crew >= 50):
        time.sleep(1)
        print("")
        crew_lost = random.randint(15,50)
        text = input(f'The cyclops is fierce and kills {crew_lost} of your men, but the sheer numbers of your crew are able to overwhelm the cyclops and you blind him before escaping back to your ship. [Enter]')
        print("")
        crew = crew - crew_lost
    
    elif (sub_crew < 50):
        print("")
        text = input("Your men fight valiantly but their numbers are not enough to take down the cyclops. He picks them off one by one and as the final man falls, he turns toward you. With no where to run, you make a brave last stand but the cyclops overpowers you. He brings his fist down on you and in an instant you are dead.")
        print("")
        time.sleep(1)
        death = True

def island_in_the_sky():
    global gold
    global crew
    global death
    global wind_bag
    sub_crew = 0
    sub_gold = 0
    text = input("Sailing away from cyclopes island [Enter]")
    print("")
    text = input("big storm [Enter]")
    print("")
    text = input("see an island in the sky [Enter]")
    print("")
    text = input("Aeolus dialogue [Enter]")
    print("")
    text = input("get wind bag [Enter]")
    wind_bag = True
    print("")

    loops = 0
    while (loops < 10):
        # this is a loop that executes menu_choices(), a function that increases the variable n_choices depending on how many rounds the loop has gone for
        # n_choices is used to tell stay_awake() how many print statements to output
        # stay_awake() is used to output a bunch of print statements with only one being the correct one, if the user doesn't choose the correct one, they fall asleep and something bad happens
        loops += 1
        n_choices = menu_choices(loops)
        
        if stay_awake(n_choices):
            # They stayed awake
            print("you stay awake")
            time.sleep(1)
            print("")
        else:
            # They fell asleep
            text = input("you fell asleep and died lol")
            death = True
    #printed after the while loop, which only happens after 
    print("you survive the big storm made by Posseidon")
def menu_choices(round: int) -> int:
    # round is the same as loops in the island_in_the_sky
    # turns the number of loops in the island_in_the_sky function into a number of choices which is used in the stay_awake function
    if (round == 1):
        n_choices = 2
    elif (round == 2):
        n_choices = 5
    elif (round == 3):
        n_choices = 10
    elif (round == 4):
        n_choices = 20
    elif (round == 5):
        n_choices = 50
    elif (round == 6):
        n_choices = 100
    elif (round == 7):
        n_choices = 250
    elif (round == 8):
        n_choices = 500
    elif (round == 9):
        n_choices = 750
    elif (round == 10):
        n_choices = 1000
    else:
        print("something's broken. this is in menu_choices() after the if statement about what round the sleepy while loop is on")
    return n_choices

def stay_awake(n_choices):
    count = 0
    wake_up = random.randint(1,n_choices)
    print("You feel sleepy, your options are:")
    while (count < n_choices):
        count += 1
        if (count == wake_up):
            print(f"{count}. stay awake")
        else:
            print(f"{count}. fall asleep")
    while True:
        choice = int(input())
        if (choice <= 0 or choice > n_choices):
            print("invalid input")
        else:
            return choice == wake_up
            
#******************************
death = False
Play_again = 'y'
while (not death and Play_again =='y'): #make a play again prompt at the end
    
    crew = 600
    crew_mood = ' '
    gold = 5000
    afflicted_crew = 0
    wind_bag = False
    cubit_of_sheep_blood = False
    lots_of_wine = True
    death = False


    intro()
    next_landmark = 'the land of the cicconies'
    current_landmark = 'Troy'
    pause()
    
    cicones()
    next_landmark = 'the lotus eaters island'
    current_landmark = 'the land of the cicconies'
    pause()
    
    lotus_island()
    if death:
        break
    next_landmark = 'the island of the cyclopes'
    current_landmark = 'the lotus eaters island'
    pause()
    
    cyclops()
    if death:
        break
    next_landmark = "Aeolis's island"
    current_landmark = 'the island of the cyclopes'
    pause()
    
    island_in_the_sky()
    if death:
        break
    next_landmark = "The land of the giants"
    current_landmark = "Aeolis's island"
    pause()

    Play_again = input("Thank you for playing The Odyssey Trail, would you like to play again? y/n ").lower()
    print("")
    time.sleep(1)
if death:
        print("Aw dang you died, better luck next time")
        print() #make an end game points function, the total is halved if you die