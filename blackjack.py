import random ## NECESSEARY TO DRAWING CARDS FROM CARDLIST.
import time ## TO GIVE THE PLAYER A LITTLE BIT TIME TO THINK
CASH= 5000 ## THE AMOUNT OF MONEY WHEN PLAYER STARTS THE GAME.
print("Welcome to BLACKJACK. Type 'start' to start Blackjack.")
numberlist = ["2", "3", "4", "5", "6", "7", "8", "9", "10"] ## TO CALCULATE THE VALUES OF CARDS.
## WE WILL GIVE SPECIAL CONDITIONS TO J, Q, K, AND A CARDS. 
time.sleep(1)
while True: ## TO PROVIDE THE CONTINUITY
    CARDLIST = ["A", "2", "3", "4", "5", "6", "7", "8","9", ## FOUR DECKS TO PROVIDE A REALISTIC OUTPUT FROM THE PROGRAM.
                "10","J","Q","K","A", "2", "3", "4", "5", "6",
                "7", "8","9","10","J","Q","K","A", "2", "3", "4", "5",
                "6", "7", "8","9","10","J","Q","K","A", "2", "3", "4",
                "5", "6", "7", "8","9","10","J","Q","K","A", "2", "3", "4",
                "5", "6", "7", "8","9",
                "10","J","Q","K","A", "2", "3", "4", "5", "6",
                "7", "8","9","10","J","Q","K","A", "2", "3", "4", "5",
                "6", "7", "8","9","10","J","Q","K","A", "2", "3", "4",
                "5", "6", "7", "8","9","10","J","Q","K","A", "2", "3", "4",
                "5", "6", "7", "8","9",
                "10","J","Q","K","A", "2", "3", "4", "5", "6",
                "7", "8","9","10","J","Q","K","A", "2", "3", "4", "5",
                "6", "7", "8","9","10","J","Q","K","A", "2", "3", "4",
                "5", "6", "7", "8","9","10","J","Q","K","A", "2", "3", "4",
                "5", "6", "7", "8","9",
                "10","J","Q","K","A", "2", "3", "4", "5", "6",
                "7", "8","9","10","J","Q","K","A", "2", "3", "4", "5",
                "6", "7", "8","9","10","J","Q","K","A", "2", "3", "4",
                "5", "6", "7", "8","9","10","J","Q","K"]
    GAME = input("Type 'start' to start the game.")
    GAME = GAME.upper() # A SIMPLE METHOD TO ELIMINATE UPPER-LOWER DIFFERENCE.
    while GAME != "START":
        GAME = input("Type 'start' to start the game. 'exit' to abort the program.")
    if GAME == "EXIT":
        print("Goodbye!")
        break
    if GAME == "START":
        print("Welcome to BlackJack game. You have ${}.".format(CASH))
        BET = input("Insert the amount of money you want to get in.")
        while BET.isdigit() is False:
            BET = input("Please enter a value with numbers.")
        BET = int(BET)
        print("Cards are dealing.")
        print("...")
        print("...")
        print("...")
        time.sleep(1)
                    ## PLAYER'S CARD DRAWING ##
        firstcard = random.choice(CARDLIST) # PICKING A RANDOM CARD IN DECK.
        CARDLIST.remove(firstcard) # REMOVING THE CARD FROM DECK.
        print("Your first card is {}".format(firstcard))
        print("...")
        time.sleep(1)
        secondcard = random.choice(CARDLIST) # PICKING A RANDOM CARD IN DECK.
        CARDLIST.remove(secondcard) # REMOVING THE CARD FROM DECK.
        print("Your second card is {}".format(secondcard))
        time.sleep(1)
                    ## PLAYER'S CARD DRAWING ##
                    ## DEALER'S CARD DRAWING ##
        dealercard1 = random.choice(CARDLIST)
        CARDLIST.remove(dealercard1)
        dealercard2 = random.choice(CARDLIST)
        CARDLIST.remove(dealercard2)
                    ## DEALER'S CARD DRAWING ##
                    ### DEALER CARDS JQK VALUE CALCULATIONS ###
        if dealercard1 == "J" or dealercard1 == "Q" or dealercard1 == "K":
            dealercard1value = 10
        if dealercard2 == "J" or dealercard2 == "Q" or dealercard2 == "K":
            dealercard2value = 10
                    ### DEALER CARDS JQK VALUE CALCULATIONS ###
                    ### DEALER CARDS NUMBER VALUE CALCULATIONS ###
        if dealercard1 in numberlist:
            dealercard1value = int(dealercard1)
        if dealercard2 in numberlist:
            dealercard2value = int(dealercard2)
                    ### DEALER CARDS NUMBER VALUE CALCULATIONS ###
                    ### DEALER CARDS ACE VALUE CALCULATIONS ###
        if dealercard1 == "A":
            if 11 + dealercard2value > 21:
                dealercard1value = 1
            if 11 + dealercard2value == 21:
                print("UNDER CONSTRUCTION")
            if 11 + dealercard2value < 21:
                        dealercard1value = 11
        if dealercard2 == "A":
            if 11 + dealercard1value >21:
                dealercard2value = 1
            if 11 + dealercard1value == 21:
                print("UNDER CONSTRUCTION")
            if 11 + dealercard1value < 21:
                dealercard2value = 11
                ### DEALER CARDS ACE VALUE CALCULATIONS ###
        time.sleep(1)
        print("DEALER'S CARDS:\n"
              "{} []\n"
              "\n"
              "\n"
              "\n"
              "YOUR CARDS:\n"
              "{} {}".format(dealercard1,firstcard, secondcard))
        time.sleep(1)
        if firstcard == "J" or firstcard == "Q" or firstcard == "K":
            firstcardvalue = 10
        if secondcard == "J" or secondcard == "Q" or secondcard == "K":
            secondcardvalue = 10
        if firstcard in numberlist:
            firstcardvalue = int(firstcard)
        if secondcard in numberlist:
            secondcardvalue = int(secondcard)
        if firstcard == "A":
            if 11 + secondcardvalue > 21:
                firstcardvalue = 1
            if 11 + secondcardvalue == 21:
                print("You've won!")
                CASH += BET
                print("Current money: ${}".format(CASH))
                time.sleep(1)
            if 11 + secondcardvalue < 21:
                firstcardvalue = 11
        if secondcard == "A":
            if 11 + firstcardvalue >21:
                secondcardvalue = 1
            if 11 + firstcardvalue == 21:
                print("UNDER CONSTRUCTION")
            if 11 + firstcardvalue < 21:
                secondcardvalue = 11
        handvalue = firstcardvalue + secondcardvalue
        print("Hand Value: {}".format(handvalue))
        if handvalue == 21:
            print("You've won!")
            CASH += BET
            print("Current money: ${}".format(CASH))
            time.sleep(1)
        if handvalue < 21:
            PROCESS = input("PRESS 'H' TO TAKE A CARD. \n PRESS 'S' TO STAND.\n")
            while PROCESS != "H" and PROCESS != "S":
                PROCESS = input("WRONG INPUT. PRESS 'H' TO TAKE A CARD. \n PRESS 'S' TO STAND.\n")
            if PROCESS == "S":
                time.sleep(1.5)
                print("Dealer's cards are:\n \n {} {}".format(dealercard1,dealercard2))
                print("Value: [{}]".format(dealercard1 + dealercard2))
                if dealercard1value + dealercard2value == 21:
                    print("You've lost. (1)")
                    CASH -= BET
                    print("Current money: ${}".format(CASH))
                    time.sleep(1)
                    dealerhandvalue = dealercard1value + dealercard2value
                if dealercard1value + dealercard2value < 21:
                    dealerhandvalue = dealercard1value + dealercard2value
                    if dealerhandvalue >16:
                        if dealerhandvalue > handvalue:
                            print("You've lost.(2)")
                            CASH -= BET
                            print("Current money: ${}".format(CASH))
                            time.sleep(1)
                        if dealerhandvalue == handvalue:
                            print("You've won!")
                            CASH += BET
                            print("Current money: ${}".format(CASH))
                            time.sleep(1)
                    if dealerhandvalue < 17:
                        dealercard3 = random.choice(CARDLIST)
                        CARDLIST.remove(dealercard3)
                        time.sleep(1)
                        print("Dealer's cards are:\n \n {} {} {}".format(dealercard1,dealercard2,dealercard3))
                        print("Value: [{}]".format(dealercard1 + dealercard2 + dealercard3))
                        time.sleep(1)
                        ### THIRD DEALER CARD VALUE CALCULATION ###
                        if dealercard3 == "J" or dealercard3 == "Q" or dealercard3 == "K":
                            dealercard3value = 10
                        if dealercard3 in numberlist:
                            dealercard3value = int(dealercard3)
                        if dealercard3 == "A":
                            if  dealercard2value + dealercard1value > 21:
                                dealercard3value = 1
                            if  dealercard2value + dealercard1value == 21:
                                print("UNDER CONSTRUCTION")
                            if  dealercard2value + dealercard1value < 21:
                                dealercard3value = 11
                        ### THIRD DEALER CARD VALUE CALCULATION ###
                        dealerhandvalue =  dealercard1value + dealercard2value + dealercard3value
                        if dealerhandvalue > 21:
                            print("You've won!")
                            CASH += BET
                            print("Current money: ${}".format(CASH))
                            time.sleep(1)
                        if dealerhandvalue == 21:
                            if handvalue == 21:
                                print("You've won!")
                                CASH += BET
                                print("Current money: ${}".format(CASH))
                                time.sleep(1)
                            if handvalue < 21:
                                print("You've lost.")
                                CASH -= BET
                                print("Current money: ${}".format(CASH))
                                time.sleep(1)
                                
                        if dealerhandvalue < 21:
                            if dealerhandvalue > handvalue:
                                print
                            print("New card is drawing...")
                            print("")
                            print("")
                            print("")
                            time.sleep(1)
                            dealercard4 = random.choice(CARDLIST)
                            CARDLIST.remove(dealercard4)
                            if dealercard4 == "J" or dealercard4 == "Q" or dealercard4 == "K":
                                dealercard4value = 10
                            if dealercard4 in numberlist:
                                dealercard4value = int(dealercard4)
                            if dealercard4 == "A":
                                if  dealercard2value + dealercard1value + dealercard3value > 21:
                                    dealercard4value = 1
                                if  dealercard2value + dealercard1value + dealercard3value == 21:
                                    print("UNDER CONSTRUCTION")
                                if  dealercard2value + dealercard1value + dealercard3value < 21:
                                    dealercard4value = 11
                            time.sleep(1)
                            print("Dealer's cards are:\n \n {} {} {} {}".format(dealercard1,dealercard2,dealercard3,dealercard4))
                            print("Value: [{}]".format(dealercard1 + dealercard2 + dealercard3+dealercard4))
                            time.sleep(1)
                            dealerhandvalue = dealercard1value + dealercard2value + dealercard3value + dealercard4value
                            if dealerhandvalue == 21:
                                if dealerhandvalue == handvalue:
                                    print("You've won!")
                                    CASH += BET
                                    print("Current money: ${}".format(CASH))
                                    time.sleep(1)
                                if dealerhandvalue > handvalue:
                                    print("You've lost.")
                                    CASH -= BET
                                    print("Current money: ${}".format(CASH))
                                    time.sleep(1)
                            if dealerhandvalue > 21:
                                print("You've won!")
                                CASH += BET
                                print("Current money: ${}".format(CASH))
                                time.sleep(1)
                            if dealerhandvalue < 21:
                                if dealerhandvalue > 16:
                                    if dealerhandvalue > handvalue:
                                        print("You've lost.")
                                        CASH -= BET
                                        print("Current money: ${}".format(CASH))
                                        time.sleep(1)
                                    if dealerhandvalue == handvalue:
                                        print("Draw!")
                                        print("Current money: ${}".format(CASH))
                                        time.sleep(1)
                                    if dealerhandvalue < handvalue:
                                        dealercard5 = random.choice(CARDLIST)
                                        CARDLIST.remove(dealercard5)
                                        if dealercard5 == "J" or dealercard5 == "Q" or dealercard5 == "K":
                                            dealercard5value = 10
                                        if dealercard5 in numberlist:
                                            dealercard5value = int(dealercard5)
                                        if dealercard5 == "A":
                                            if  dealercard2value + dealercard1value + dealercard3value + dealercard4value > 21:
                                                dealercard5value = 1
                                            if  dealercard2value + dealercard1value + dealercard3value + dealercard4value == 21:
                                                print("UNDER CONSTRUCTION")
                                            if  dealercard2value + dealercard1value + dealercard3value + dealercard4value < 21:
                                                dealercard5value = 11
                                        time.sleep(1)
                                        print("Dealer's cards are:\n \n {} {} {} {} {}".format(dealercard1,dealercard2,dealercard3,dealercard4, dealercard5))
                                        print("Value: [{}]".format(dealercard1 + dealercard2 + dealercard3+dealercard4+dealercard5))
                                        dealerhandvalue = dealercard1value + dealercard2value + dealercard3value + dealercard4value + dealercard5value
                                        if dealerhandvalue > 21:
                                            print("You've won!")
                                            CASH += BET
                                            print("Current money: ${}".format(CASH))
                                        if dealerhandvalue == 21:
                                            if dealerhandvalue == handvalue:
                                                print("You've won!")
                                                CASH += BET
                                                print("Current money: ${}".format(CASH))
                                                time.sleep(1)
                                            if dealerhandvalue > handvalue:
                                                print("You've lost.")
                                                CASH -= BET
                                                print("Current money: ${}".format(CASH))
                                                time.sleep(1)
                                                
                                            
            if PROCESS == "H":
                add_card1 = random.choice(CARDLIST)
                CARDLIST.remove(add_card1)
                time.sleep(1)
                print("DEALER'S CARDS:\n"
              "{} []\n"
              "\n"
              "\n"
              "\n"
              "YOUR CARDS:\n"
              "{} {} {}".format(dealercard1,firstcard, secondcard, add_card1))
                time.sleep(1)
                if add_card1 == "J" or add_card1 == "Q" or add_card1 == "K":
                    add_card1value = 10
                if add_card1 in numberlist:
                    add_card1value = int(add_card1)
                if add_card1 == "A":
                    if  secondcardvalue + firstcardvalue > 21:
                        add_card1value = 1
                    if  secondcardvalue + firstcardvalue == 21:
                        print("You've won!")
                        CASH += BET
                        print("Current money: ${}".format(CASH))
                        time.sleep(1)
                    if  secondcardvalue + firstcardvalue < 21:
                        add_card1value = 11
                if firstcardvalue + secondcardvalue + add_card1value > 21:
                    print("You've lost.")
                    CASH -= BET
                    print("You've ${} left.".format(CASH))
                    print("...")
                    print("...")
                    time.sleep(1)
                if firstcardvalue + secondcardvalue + add_card1value == 21:
                        print("You've won!")
                        CASH += BET
                        print("Current money: ${}".format(CASH))
                        time.sleep(1)
                handvalue = firstcardvalue + secondcardvalue + add_card1value
                if firstcardvalue + secondcardvalue + add_card1value< 21:
                    print("Hand value {}".format(handvalue))
                    PROCESS = input("00PRESS 'H' TO TAKE A CARD. \n PRESS 'S' TO STAND.")
                    while PROCESS != "H" and PROCESS != "S":
                        PROCESS = input("00WRONG INPUT. PRESS 'H' TO TAKE A CARD. \n PRESS 'S' TO STAND.")
                    if PROCESS == "S":
                        time.sleep(1)
                        print("Dealer's cards are:\n \n {} {}".format(dealercard1,dealercard2))
                        print("Value: [{}]".format(dealercard1 + dealercard2))
                        time.sleep(1)
                        if dealercard1value + dealercard2value == 21:
                            print("You've lost. (1)")
                            CASH -= BET
                            print("Current money: ${}".format(CASH))
                            time.sleep(1)
                            dealerhandvalue = dealercard1value + dealercard2value
                        if dealercard1value + dealercard2value < 21:
                            dealerhandvalue = dealercard1value + dealercard2value
                            if dealerhandvalue >16:
                                if dealerhandvalue > handvalue:
                                    print("You've lost.(2)")
                                    CASH -= BET
                                    print("Current money: ${}".format(CASH))
                                    time.sleep(1)
                            if dealerhandvalue < 17:
                                dealercard3 = random.choice(CARDLIST)
                                CARDLIST.remove(dealercard3)
                                time.sleep(1)
                                print("Dealer's cards are:\n \n {} {} {}".format(dealercard1,dealercard2,dealercard3))
                                print("Value: [{}]".format(dealercard1 + dealercard2 + dealercard3))
                                time.sleep(1)
                                ### THIRD DEALER CARD VALUE CALCULATION ###
                                if dealercard3 == "J" or dealercard3 == "Q" or dealercard3 == "K":
                                    dealercard3value = 10
                                if dealercard3 in numberlist:
                                    dealercard3value = int(dealercard3)
                                if dealercard3 == "A":
                                    if  dealercard2value + dealercard1value > 21:
                                        dealercard3value = 1
                                    if  dealercard2value + dealercard1value == 21:
                                        print("UNDER CONSTRUCTION")
                                    if  dealercard2value + dealercard1value < 21:
                                        dealercard3value = 11
                                ### THIRD DEALER CARD VALUE CALCULATION ###
                                dealerhandvalue =  dealercard1value + dealercard2value + dealercard3value
                                if dealerhandvalue > 21:
                                    print("You've won!")
                                    CASH += BET
                                    print("Current money: ${}".format(CASH))
                                if dealerhandvalue == 21:
                                    if handvalue == 21:
                                        print("You've won!")
                                        CASH += BET
                                        print("Current money: ${}".format(CASH))
                                    if handvalue < 21:
                                        print("You've lost.")
                                        CASH -= BET
                                        print("Current money: ${}".format(CASH))
                                        
                                if dealerhandvalue < 21:
                                    if dealerhandvalue > handvalue:
                                        print
                                    print("New card is drawing...")
                                    print("")
                                    print("")
                                    print("")
                                    dealercard4 = random.choice(CARDLIST)
                                    CARDLIST.remove(dealercard4)
                                    if dealercard4 == "J" or dealercard4 == "Q" or dealercard4 == "K":
                                        dealercard4value = 10
                                    if dealercard4 in numberlist:
                                        dealercard4value = int(dealercard4)
                                    if dealercard4 == "A":
                                        if  dealercard2value + dealercard1value + dealercard3value > 21:
                                            dealercard4value = 1
                                        if  dealercard2value + dealercard1value + dealercard3value == 21:
                                            print("UNDER CONSTRUCTION")
                                        if  dealercard2value + dealercard1value + dealercard3value < 21:
                                            dealercard4value = 11
                                    time.sleep(1)
                                    print("Dealer's cards are:\n \n {} {} {} {}".format(dealercard1,dealercard2,dealercard3,dealercard4))
                                    print("")
                                    print("")
                                    print("")
                                    print("")
                                    time.sleep(1)
                                    dealerhandvalue = dealercard1value + dealercard2value + dealercard3value + dealercard4value
                                    if dealerhandvalue == 21:
                                        if dealerhandvalue == handvalue:
                                            print("You've won!")
                                            CASH += BET
                                            print("Current money: ${}".format(CASH))
                                            time.sleep(1)
                                        if dealerhandvalue > handvalue:
                                            print("You've lost.")
                                            CASH -= BET
                                            print("Current money: ${}".format(CASH))
                                            time.sleep(1)
                                    if dealerhandvalue > 21:
                                        print("You've won!")
                                        CASH += BET
                                        print("Current money: ${}".format(CASH))
                                        time.sleep(1)
                                    if dealerhandvalue < 21:
                                        if dealerhandvalue > 16:
                                            if dealerhandvalue > handvalue:
                                                print("You've lost.")
                                                CASH -= BET
                                                print("Current money: ${}".format(CASH))
                                                time.sleep(1)
                                            if dealerhandvalue == handvalue:
                                                print("Draw!")
                                                print("Current money: ${}".format(CASH))
                                                time.sleep(1)
                                            if dealerhandvalue < handvalue:
                                                dealercard5 = random.choice(CARDLIST)
                                                CARDLIST.remove(dealercard5)
                                                if dealercard5 == "J" or dealercard5 == "Q" or dealercard5 == "K":
                                                    dealercard5value = 10
                                                if dealercard5 in numberlist:
                                                    dealercard5value = int(dealercard5)
                                                if dealercard5 == "A":
                                                    if  dealercard2value + dealercard1value + dealercard3value + dealercard4value > 21:
                                                        dealercard5value = 1
                                                    if  dealercard2value + dealercard1value + dealercard3value + dealercard4value == 21:
                                                        print("UNDER CONSTRUCTION")
                                                    if  dealercard2value + dealercard1value + dealercard3value + dealercard4value < 21:
                                                        dealercard5value = 11
                                                time.sleep(1)
                                                print("Dealer's cards are:\n \n {} {} {} {} {}".format(dealercard1,dealercard2,dealercard3,dealercard4, dealercard5))
                                                time.sleep(1)
                                                dealerhandvalue = dealercard1value + dealercard2value + dealercard3value + dealercard4value + dealercard5value
                                                if dealerhandvalue > 21:
                                                    print("You've won!")
                                                    CASH += BET
                                                    print("Current money: ${}".format(CASH))
                                                    time.sleep(1)
                                                if dealerhandvalue == 21:
                                                    if dealerhandvalue == handvalue:
                                                        print("You've won!")
                                                        CASH += BET
                                                        print("Current money: ${}".format(CASH))
                                                        time.sleep(1)
                                                    if dealerhandvalue > handvalue:
                                                        print("You've lost.")
                                                        CASH -= BET
                                                        print("Current money: ${}".format(CASH))
                                                        time.sleep(1)                                                        
                    if PROCESS == "H":
                        add_card2 = random.choice(CARDLIST)
                        CARDLIST.remove(add_card2)
                        if add_card2 == "J" or add_card2 == "Q" or add_card2 == "K":
                            add_card2value = 10
                        if add_card2 in numberlist:
                            add_card2value = int(add_card2)
                        if add_card2 == "A":
                            if  secondcardvalue + firstcardvalue + add_card1value > 21:
                                add_card2value = 1
                            if  secondcardvalue + firstcardvalue + add_card1value == 21:
                                print("You've won!")
                                CASH += BET
                                print("Current money: ${}".format(CASH))
                                time.sleep(1)
                            if  secondcardvalue + firstcardvalue + add_card1value < 21:
                                add_card2value = 1
                        handvalue = firstcardvalue + secondcardvalue + add_card1value + add_card2value
                        time.sleep(1)
                        print("DEALER'S CARDS:\n"
                              "{} []\n"
                              "\n"
                              "\n"
                              "\n"
                              "YOUR CARDS:\n"
                              "{} {} {} {}".format(dealercard1,firstcard, secondcard, add_card1, add_card2))
                        time.sleep(1)
                        if handvalue >21:
                            print("You've lost.")
                            CASH -= BET
                            print("You've {} left.".format(CASH))
                        if handvalue == 21:
                            print("You've won!")
                            CASH += BET
                            print("Current money: ${}".format(CASH))
                        if handvalue < 21:
                            PROCESS = input("PRESS 'H' TO TAKE A CARD. \n PRESS 'S' TO STAND.")
                            while PROCESS != "H" and PROCESS != "S":
                                PROCESS = input("WRONG INPUT. PRESS 'H' TO TAKE A CARD. \n PRESS 'S' TO STAND.")
                            if PROCESS == "S":
                                print("Dealer's cards are:\n \n {} {}".format(dealercard1,dealercard2))
                                time.sleep(1)
                                if dealercard1value + dealercard2value == 21:
                                    print("You've lost. (1)")
                                    CASH -= BET
                                    print("Current money: ${}".format(CASH))
                                    time.sleep(1)
                                    dealerhandvalue = dealercard1value + dealercard2value
                                if dealercard1value + dealercard2value < 21:
                                    dealerhandvalue = dealercard1value + dealercard2value
                                    if dealerhandvalue >16:
                                        if dealerhandvalue > handvalue:
                                            print("You've lost.(2)")
                                            CASH -= BET
                                            print("Current money: ${}".format(CASH))
                                            time.sleep(1)
                                    if dealerhandvalue < 17:
                                        dealercard3 = random.choice(CARDLIST)
                                        CARDLIST.remove(dealercard3)
                                        print("Dealer's cards are:\n \n {} {} {}".format(dealercard1,dealercard2,dealercard3))
                                        print("")
                                        print("")
                                        print("")
                                        print("")
                                        time.sleep(1)
                                        ### THIRD DEALER CARD VALUE CALCULATION ###
                                        if dealercard3 == "J" or dealercard3 == "Q" or dealercard3 == "K":
                                            dealercard3value = 10
                                        if dealercard3 in numberlist:
                                            dealercard3value = int(dealercard3)
                                        if dealercard3 == "A":
                                            if  dealercard2value + dealercard1value > 21:
                                                dealercard3value = 1
                                            if  dealercard2value + dealercard1value == 21:
                                                print("UNDER CONSTRUCTION")
                                            if  dealercard2value + dealercard1value < 21:
                                                dealercard3value = 11
                                        ### THIRD DEALER CARD VALUE CALCULATION ###
                                        dealerhandvalue =  dealercard1value + dealercard2value + dealercard3value
                                        if dealerhandvalue > 21:
                                            print("You've won!")
                                            CASH += BET
                                            print("Current money: ${}".format(CASH))
                                        if dealerhandvalue == 21:
                                            if handvalue == 21:
                                                print("You've won!")
                                                CASH += BET
                                                print("Current money: ${}".format(CASH))
                                            if handvalue < 21:
                                                print("You've lost.")
                                                CASH -= BET
                                                print("Current money: ${}".format(CASH))
                                                
                                        if dealerhandvalue < 21:
                                            if dealerhandvalue > handvalue:
                                                print
                                            print("New card is drawing...")
                                            print("")
                                            print("")
                                            print("")
                                            time.sleep(1)
                                            dealercard4 = random.choice(CARDLIST)
                                            CARDLIST.remove(dealercard4)
                                            if dealercard4 == "J" or dealercard4 == "Q" or dealercard4 == "K":
                                                dealercard4value = 10
                                            if dealercard4 in numberlist:
                                                dealercard4value = int(dealercard4)
                                            if dealercard4 == "A":
                                                if  dealercard2value + dealercard1value + dealercard3value > 21:
                                                    dealercard4value = 1
                                                if  dealercard2value + dealercard1value + dealercard3value == 21:
                                                    print("UNDER CONSTRUCTION")
                                                if  dealercard2value + dealercard1value + dealercard3value < 21:
                                                    dealercard4value = 11
                                            print("Dealer's cards are:\n \n {} {} {} {}".format(dealercard1,dealercard2,dealercard3,dealercard4))
                                            print("")
                                            print("")
                                            print("")
                                            print("")
                                            time.sleep(1)
                                            dealerhandvalue = dealercard1value + dealercard2value + dealercard3value + dealercard4value
                                            if dealerhandvalue == 21:
                                                if dealerhandvalue == handvalue:
                                                    print("You've won!")
                                                    CASH += BET
                                                    print("Current money: ${}".format(CASH))
                                                    time.sleep(1)
                                                if dealerhandvalue > handvalue:
                                                    print("You've lost.")
                                                    CASH -= BET
                                                    print("Current money: ${}".format(CASH))
                                                    time.sleep(1)
                                            if dealerhandvalue > 21:
                                                print("You've won!")
                                                CASH += BET
                                                print("Current money: ${}".format(CASH))
                                                time.sleep(1)
                                            if dealerhandvalue < 21:
                                                if dealerhandvalue > 16:
                                                    if dealerhandvalue > handvalue:
                                                        print("You've lost.")
                                                        CASH -= BET
                                                        print("Current money: ${}".format(CASH))
                                                        time.sleep(1)
                                                    if dealerhandvalue == handvalue:
                                                        print("Draw!")
                                                        print("Current money: ${}".format(CASH))
                                                        time.sleep(1)
                                                    if dealerhandvalue < handvalue:
                                                        dealercard5 = random.choice(CARDLIST)
                                                        CARDLIST.remove(dealercard5)
                                                        if dealercard5 == "J" or dealercard5 == "Q" or dealercard5 == "K":
                                                            dealercard5value = 10
                                                        if dealercard5 in numberlist:
                                                            dealercard5value = int(dealercard5)
                                                        if dealercard5 == "A":
                                                            if  dealercard2value + dealercard1value + dealercard3value + dealercard4value > 21:
                                                                dealercard5value = 1
                                                            if  dealercard2value + dealercard1value + dealercard3value + dealercard4value == 21:
                                                                print("UNDER CONSTRUCTION")
                                                            if  dealercard2value + dealercard1value + dealercard3value + dealercard4value < 21:
                                                                dealercard5value = 11
                                                        print("Dealer's cards are:\n \n {} {} {} {} {}".format(dealercard1,dealercard2,dealercard3,dealercard4, dealercard5))
                                                        dealerhandvalue = dealercard1value + dealercard2value + dealercard3value + dealercard4value + dealercard5value
                                                        if dealerhandvalue > 21:
                                                            print("You've won!")
                                                            CASH += BET
                                                            print("Current money: ${}".format(CASH))
                                                            time.sleep(1)
                                                        if dealerhandvalue == 21:
                                                            if dealerhandvalue == handvalue:
                                                                print("You've won!")
                                                                CASH += BET
                                                                print("Current money: ${}".format(CASH))
                                                                time.sleep(1)
                                                            if dealerhandvalue > handvalue:
                                                                print("You've lost.")
                                                                CASH -= BET
                                                                print("Current money: ${}".format(CASH))
                                                                time.sleep(1)
        
                        if PROCESS == "H":
                            add_card3 = random.choice(CARDLIST)
                            CARDLIST.remove(add_card3)
                            if add_card3 == "J" or add_card3 == "Q" or add_card3 == "K":
                                add_card3value = 10
                            if add_card3 in numberlist:
                                add_card3value = int(add_card3)
                            if add_card3 == "A":
                                if  secondcardvalue + firstcardvalue + add_card1value + add_card2value > 21:
                                    add_card3value = 1
                                if  secondcardvalue + firstcardvalue + add_card1value + add_card2value == 21:
                                    print("UNDER CONSTRUCTION")
                                if  secondcardvalue + firstcardvalue + add_card1value + add_card2value < 21:
                                    add_card3value = 11
                            handvalue = firstcardvalue + secondcardvalue + add_card1value + add_card2value + add_card3value
                            print("DEALER'S CARDS:\n"
                              "{} []\n"
                              "\n"
                              "\n"
                              "\n"
                              "YOUR CARDS:\n"
                              "{} {} {} {} {}".format(dealercard1,firstcard, secondcard, add_card1, add_card2, add_card3))
                            print("Hand value: [{}]".format(handvalue))
                            if handvalue > 21:
                                print("You've lost.")
                                CASH -= BET
                                print("You've {} left.".format(CASH))
                                time.sleep(1)
                            if handvalue == 21:
                                print("You've won!")
                                CASH += BET
                                print("Current money: ${}".format(CASH))
                                time.sleep(1)
                            if handvalue < 21:
                                print("You've won!")
                                CASH += BET
                                print("Current money: ${}".format(CASH))
                                time.sleep(1)
                        
                
                
    
