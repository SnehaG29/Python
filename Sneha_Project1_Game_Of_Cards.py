import random
import time



## Game starts with the welcome banner
'''print("*********************************************************************************************************")
print("************************************************WELCOME**************************************************")
print("************************************************TO THE***************************************************")
print("*********************************************GAME OF CARDS***********************************************")
print("**************************************************$$$$***************************************************")
print("*********************************************************************************************************")'''


def banner(message,
           border='*'):  # Banner function definition with message as positional argument and border as keyword argument with default value
    line = border * 6 * len(message)  #
    print(line)
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t" + message)
    print(line)


bnr = banner("WELCOME TO THE GAME OF CARDS",
             '@')  # Banner function call does not return anything. It is assigned to a variable bnr


# optional value of '@' is used here in the border line


# Testing point 1
##Show time
def show_time(st=time.ctime()):
    print(st)


show_time()

# Generates a goal_score (random number) between a given positive range of 20 to 40
goal_score = random.randint(25, 40)
print(" The goal score for this round is between 25 and 40 and that number is:  % s" % (goal_score))

##Enter the Players name
Players = []
PlayersName = input("Enter your Name or a nickname:") #input() function is used to fetch names from the terminal
Players.append(PlayersName)
print("Hi," + PlayersName + "." + " Lets kickstart the game") #Conactenation of string and variable
# print(Players) #weakness

for P_names in Players:
    print("All The Best " + P_names)

# Create a deck of cards
playing = True
#Using a dictionary data structure to create a deck
WholeCards = {'Clubs_Ace': 13, 'Clubs_Two': 2, 'Clubs_Three': 3, 'Clubs_Four': 4, 'Clubs_Five': 5, 'Clubs_Six': 6,
              'Clubs_Seven': 7, 'Clubs_Eight': 8, 'Clubs_Nine': 9, 'Clubs_Ten': 10, 'Clubs_Jack': 10, 'Clubs_Queen': 11,
              'Clubs_King': 12,
              'Diamonds_Ace': 13, 'Diamonds_Two': 2, 'Diamonds_Three': 3, 'Diamonds_Four': 4, 'Diamonds_Five': 5,
              'Diamonds_Six': 6, 'Diamonds_Seven': 7, 'Diamonds_Eight': 8, 'Diamonds_Nine': 9, 'Diamonds_Ten': 10,
              'Diamonds_Jack': 10, 'Diamonds_Queen': 11, 'Diamonds_King': 12,
              'Hearts_Ace': 13, 'Hearts_Two': 2, 'Hearts_Three': 3, 'Hearts_Four': 4, 'Hearts_Five': 5, 'Hearts_Six': 6,
              'Hearts_Seven': 7, 'Hearts_Eight': 8, 'Hearts_Nine': 9, 'Hearts_Ten': 10, 'Hearts_Jack': 10,
              'Hearts_Queen': 11, 'Hearts_King': 12,
              'Spades_Ace': 13, 'Spades_Two': 2, 'Spades_Three': 3, 'Spades_Four': 4, 'Spades_Five': 5, 'Spades_Six': 6,
              'Spades_Seven': 7, 'Spades_Eight': 8, 'Spades_Nine': 9, 'Spades_Ten': 10, 'Spades_Jack': 10,
              'Spades_Queen': 11, 'Spades_King': 12}

# Adding keys and values in different lists
allkeyvalues = list(WholeCards.keys())
allvalues = list(WholeCards.values())

# Variables defined here
dealer = False
PlayersCards = []
DealersCards = []
PlayersTotalValue = 0
DealersTotalValue = 0
global PlayersScore, DealersScore
P = 0
D = 0


# shuffle Function
def shuffle():
    random.shuffle(allkeyvalues) #random.shuffle() is an inbuilt function in random package that shuffles the items


# Add cards function to add keys and values of the dictionary in separate lists
def AddCardRound():
    PlayersCards.append(allkeyvalues[1:3])
    DealersCards.append(allkeyvalues[4:6])
    print(" Cards selected for " + PlayersName + ":" + str(PlayersCards))
    print(" Cards selected for Dealer: Hidden")
    #print(" Cards selected for Dealer: ", DealersCards)


'''def AddCardRound2():
    PlayersCards.append(allkeyvalues[1:2])
    DealersCards.append(allkeyvalues[4:5])
    print("Round 2 cards for" + PlayersName + ":" + str(PlayersCards))
    print(DealersCards)'''


# Calculate total value of a hand for Players and Dealer
def CalculatePlayersValue(Pvalue):
    global PlayersScore
    for card in PlayersCards:
        if "Hearts_Ace" in card:
            Pvalue += 13
            print(Pvalue)
        if "Hearts_Jack" in card:
            Pvalue += 10
            print(Pvalue)
        if "Hearts_Queen" in card:
            Pvalue += 11
            print(Pvalue)
        if "Hearts_King" in card:
            Pvalue += 12
            print(Pvalue)
        if "Hearts_Two" in card:
            Pvalue += 2
            print(Pvalue)
        if "Hearts_Three" in card:
            Pvalue += 3
            print(Pvalue)
        if "Hearts_Four" in card:
            Pvalue += 4
            print(Pvalue)
        if "Hearts_Five" in card:
            Pvalue += 5
            print(Pvalue)
        if "Hearts_Six" in card:
            Pvalue += 6
            print(Pvalue)
        if "Hearts_Seven" in card:
            Pvalue += 7
            print(Pvalue)
        if "Hearts_Eight" in card:
            Pvalue += 8
            print(Pvalue)
        if "Hearts_Nine" in card:
            Pvalue += 9
            print(Pvalue)
        if "Hearts_Ten" in card:
            Pvalue += 10
            print(Pvalue)
        if "Spades_Ace" in card:
            Pvalue += 13
            print(Pvalue)
        if "Spades_Jack" in card:
            Pvalue += 10
            print(Pvalue)
        if "Spades_Queen" in card:
            Pvalue += 11
            print(Pvalue)
        if "Spades_King" in card:
            Pvalue += 12
            print(Pvalue)
        if "Spades_Two" in card:
            Pvalue += 2
            print(Pvalue)
        if "Spades_Three" in card:
            Pvalue += 3
            print(Pvalue)
        if "Spades_Four" in card:
            Pvalue += 4
            print(Pvalue)
        if "Spades_Five" in card:
            Pvalue += 5
            print(Pvalue)
        if "Spades_Six" in card:
            Pvalue += 6
            print(Pvalue)
        if "Spades_Seven" in card:
            Pvalue += 7
            print(Pvalue)
        if "Spades_Eight" in card:
            Pvalue += 8
            print(Pvalue)
        if "Spades_Nine" in card:
            Pvalue += 9
            print(Pvalue)
        if "Spades_Ten" in card:
            Pvalue += 10
            print(Pvalue)
        if "Clubs_Ace" in card:
            Pvalue += 13
            print(Pvalue)
        if "Clubs_Jack" in card:
            Pvalue += 10
            print(Pvalue)
        if "Clubs_Queen" in card:
            Pvalue += 11
            print(Pvalue)
        if "Clubs_King" in card:
            Pvalue += 12
            print(Pvalue)
        if "Clubs_Two" in card:
            Pvalue += 2
            print(Pvalue)
        if "Clubs_Three" in card:
            Pvalue += 3
            print(Pvalue)
        if "Clubs_Four" in card:
            Pvalue += 4
            print(Pvalue)
        if "Clubs_Five" in card:
            Pvalue += 5
            print(Pvalue)
        if "Clubs_Six" in card:
            Pvalue += 6
            print(Pvalue)
        if "Clubs_Seven" in card:
            Pvalue += 7
            print(Pvalue)
        if "Clubs_Eight" in card:
            Pvalue += 8
            print(Pvalue)
        if "Clubs_Nine" in card:
            Pvalue += 9
            print(Pvalue)
        if "Clubs_Ten" in card:
            Pvalue += 10
            print(Pvalue)
        if "Diamonds_Ace" in card:
            Pvalue += 13
            print(Pvalue)
        if "Diamonds_Jack" in card:
            Pvalue += 10
            print(Pvalue)
        if "Diamonds_Queen" in card:
            Pvalue += 11
            print(Pvalue)
        if "Diamonds_King" in card:
            Pvalue += 12
            print(Pvalue)
        if "Diamonds_Two" in card:
            Pvalue += 2
            print(Pvalue)
        if "Diamonds_Three" in card:
            Pvalue += 3
            print(Pvalue)
        if "Diamonds_Four" in card:
            Pvalue += 4
            print(Pvalue)
        if "Diamonds_Five" in card:
            Pvalue += 5
            print(Pvalue)
        if "Diamonds_Six" in card:
            Pvalue += 6
            print(Pvalue)
        if "Diamonds_Seven" in card:
            Pvalue += 7
            print(Pvalue)
        if "Diamonds_Eight" in card:
            Pvalue += 8
            print(Pvalue)
        if "Diamonds_Nine" in card:
            Pvalue += 9
            print(Pvalue)
        if "Diamonds_Ten" in card:
            Pvalue += 10
            print(Pvalue)
        print("Players Total Value:", Pvalue)
    return Pvalue


def CalculateDealersValue(value):
    global DealersScore
    for card in DealersCards:
        if "Hearts_Ace" in card:
            value += 13
            print(value)

        if "Hearts_Jack" in card:
            value += 10
            print(value)

        if "Hearts_Queen" in card:
            value += 11
            print(value)

        if "Hearts_King" in card:
            value += 12
            print(value)

        if "Hearts_Two" in card:
            value += 2
            print(value)

        if "Hearts_Three" in card:
            value += 3
            print(value)

        if "Hearts_Four" in card:
            value += 4
            print(value)

        if "Hearts_Five" in card:
            value += 5
            print(value)

        if "Hearts_Six" in card:
            value += 6
            print(value)

        if "Hearts_Seven" in card:
            value += 7
            print(value)

        if "Hearts_Eight" in card:
            value += 8
            print(value)

        if "Hearts_Nine" in card:
            value += 9
            print(value)

        if "Hearts_Ten" in card:
            value += 10
            print(value)

        if "Spades_Ace" in card:
            value += 13
            print(value)

        if "Spades_Jack" in card:
            value += 10
            print(value)

        if "Spades_Queen" in card:
            value += 11
            print(value)

        if "Spades_King" in card:
            value += 12
            print(value)

        if "Spades_Two" in card:
            value += 2
            print(value)

        if "Spades_Three" in card:
            value += 3
            print(value)

        if "Spades_Four" in card:
            value += 4
            print(value)

        if "Spades_Five" in card:
            value += 5
            print(value)

        if "Spades_Six" in card:
            value += 6
            print(value)

        if "Spades_Seven" in card:
            value += 7
            print(value)

        if "Spades_Eight" in card:
            value += 8
            print(value)

        if "Spades_Nine" in card:
            value += 9
            print(value)

        if "Spades_Ten" in card:
            value += 10
            print(value)

        if "Clubs_Ace" in card:
            value += 13
            print(value)

        if "Clubs_Jack" in card:
            value += 10
            print(value)

        if "Clubs_Queen" in card:
            value += 11
            print(value)

        if "Clubs_King" in card:
            value += 12
            print(value)

        if "Clubs_Two" in card:
            value += 2
            print(value)

        if "Clubs_Three" in card:
            value += 3
            print(value)

        if "Clubs_Four" in card:
            value += 4
            print(value)

        if "Clubs_Five" in card:
            value += 5
            print(value)

        if "Clubs_Six" in card:
            value += 6
            print(value)

        if "Clubs_Seven" in card:
            value += 7
            print(value)

        if "Clubs_Eight" in card:
            value += 8
            print(value)

        if "Clubs_Nine" in card:
            value += 9
            print(value)

        if "Clubs_Ten" in card:
            value += 10
            print(value)

        if "Diamonds_Ace" in card:
            value += 13
            print(value)

        if "Diamonds_Jack" in card:
            value += 10
            print(value)

        if "Diamonds_Queen" in card:
            value += 11
            print(value)

        if "Diamonds_King" in card:
            value += 12
            print(value)

        if "Diamonds_Two" in card:
            value += 2
            print(value)

        if "Diamonds_Three" in card:
            value += 3
            print(value)

        if "Diamonds_Four" in card:
            value += 4
            print(value)

        if "Diamonds_Five" in card:
            value += 5
            print(value)

        if "Diamonds_Six" in card:
            value += 6
            print(value)

        if "Diamonds_Seven" in card:
            value += 7
            print(value)

        if "Diamonds_Eight" in card:
            value += 8
            print(value)

        if "Diamonds_Nine" in card:
            value += 9
            print(value)

        if "Diamonds_Ten" in card:
            value += 10
            print(value)
    print("Dealers Total Value:", value)
    return value



global PlayersScore, DealersScore
# Play one round of game
def DoRound():
    global P,D   #Defining global variables within the function and outside the scope of the function
    shuffle()
    AddCardRound()
    P = CalculatePlayersValue(PlayersTotalValue) #Pvalue is returned in P
    D = CalculateDealersValue(DealersTotalValue) #value is returned in D

def EndGame():
    print("Dear" + PlayersName + "You have won a trip to Vegas Huraayyyyy!!!")


def see_who_won():
    player = False
    dealer = False
    if PlayersTotalValue >= goal_score:
        player = True
    if DealersTotalValue >= goal_score:
        dealer = True
    return player, dealer


def GameResults(has_player_won, has_dealer_won):
    if has_player_won and has_dealer_won:
        print("Its a draw")
    elif has_player_won:
        print("You have won the game")
    elif has_dealer_won:
        print("You lost the game. Dealer Wins.")

def StartGame():
    #global PlayersTotalValue , DealersTotalValue

    play = True

    #while play:
    for i in range(1):
        DoRound() #infinite loop issue  if  for loop is not included'''

#while continue_game = True
    choice = input("Do you want to draw card? Enter [yes/no]").lower()
    if choice in ['yes', 'y']:   # IN operator to check the input values
        DoRound()
        for k in range(1):
            if P > goal_score:
                print("You have won the game")
                print(P)

            elif P == D:
                print("Its a draw")
                print(P)
                print(D)
            elif D > goal_score:
                print("You have lost.")
    elif choice in ['no', 'n']:
        End = input("Do you wan to quit the game? [yes/no]").lower()
        if End in ['yes', 'y']:
            print("Your game ends")
        elif End in ['no', 'n']:
            print("Lets compare the total values of the player and dealer")
            for k in range(1):
                if P > goal_score:
                    print("You have won the game")
                    print(P)

                elif P == D:
                    print("Its a draw")
                    print(P)
                    print(D)
                elif D> goal_score:
                    print("You have lost.")

StartGame()
