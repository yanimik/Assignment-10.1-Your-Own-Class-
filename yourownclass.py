#Ian Crisostomo
#Assignment 10.1: Your Own Class

#imports random module to generate random cards with random numbers
import random

#Creates class called Card; based off of playing cards
class Card():
    #Recognizes the suit of the card and the number
    def __init__(self, suit, number):
        self.__suit=suit
        self.__number=number

    #Function that gets the suit of the card you create
    def getsuit(self):
        return str(self.__suit)

    #Function that gets the number of the card you create
    def getnumber(self):
        #If there is the word Ace, value is 1
        if self.__number=="Ace":
            return "1"
        #If there is the word Jack, value is 11
        elif self.__number=="Jack":
            return "11"
        #If there is the word Queen, value is 12
        elif self.__number=="Queen":
            return "12"
        #If there is the word King, value is 13
        elif self.__number=="King":
            return "13"
        #Otherwise, just return the number as a string
        else:
            return str(self.__number)

    #A function that displays the whole deck of cards
    def deckdisplay(self):
        #All suits are located in a list
        suitlist = ["Spades", "Clubs", "Hearts", "Diamonds"]
        #All numbers are located in a list
        numberlist = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        #Creates an empty list where cards will be stored
        cardlist = []
        #Iterates through list of suits
        for suit in suitlist:
            #Also iterates through list of numbers
            for number in numberlist:
                #Assigns suit to iterated number of card and puts them into a string
                #Since suits are also iterated, goes through each suit and repeats the process
                #Adds all of them to empty list
                cardlist.append(str(number)+" of "+str(suit))
        #Returns the list of cards
        return cardlist

    #gofish: goes through random cards until numbers match with card you created
    def gofish(self):
        #Establishes a count
        count = 0
        #Converts the words to values to represent the cards
        if self.__number=="Ace":
            self.__number = "1"
        elif self.__number=="Jack":
            self.__number = "11"
        elif self.__number=="Queen":
            self.__number = "12"
        elif self.__number=="King":
            self.__number = "13"
        else:
            self.__number = str(self.__number)
        #othercard is -1 because probability wise it will never match up
        #Needs the while loop to execute and keep searching through random range numbers
        othercard = -1
        #While they are always unequal to each other:
        while self.__number!=othercard:
            #Assigns random number to other card
            othercard=random.randrange(1, 13)
            #Converts value to string
            othercard = str(othercard)
            #Prints the number to interface
            print(othercard)
            #Adds one to count each time the loop iterates
            count+=1
        #Once the card matches, enter the count to the returned string
        return f"Go fish! It took {count} times to get a matching card."
            
        
    #blackjack: a function which is a game that tests if value goes over 21
    def blackjack(self):
        #converts the words to values to represent the cards
        if self.__number == "Ace":
            self.__number = 1
        elif self.__number == "Jack":
            self.__number = 11
        elif self.__number == "Queen":
            self.__number = 12
        elif self.__number == "King":
            self.__number = 13
        else:
            int(self.__number) == self.__number
        #Uses a while loop to repeat process
        while True:
            #Enters a question which tells you the number of your card
            #Asks a question which has a Yes/No answer
            command = input(f"With your card, the current value is {self.__number}. Would you like to add another card? Yes or No? ")
            #If they answer Yes:
            if command == "Yes":
                #Creates another card with a random generated number
                card2 = random.randrange(1, 13)
                #Card conversion from word to number process
                if self.__number == "Ace":
                    self.__number = 1
                elif self.__number == "Jack":
                    self.__number = 11
                elif self.__number == "Queen":
                    self.__number = 12
                elif self.__number == "King":
                    self.__number = 13
                else:
                    self.__number = int(self.__number)

                #Adds card2 to the number you entered to get new total
                total=int(self.__number)+int(card2)

                #while the total is under 21, you can still have the option to add more cards
                while total < 21:
                    #Shows you your total
                    #Asks a question which has a Yes/No answer
                    command = input(f"You currently have the value of {total} in your deck. Would you like to add another card? Yes or No? ")
                    #If command is yes, adds another random integer to represent another random card
                    #Equals to the new total
                    if command == "Yes":
                        total=total+random.randrange(1, 13)
                    #If command is no, game ends and value of cards are displayed
                    if command == "No":
                        return (f"The total amount of points is {total}. Play again!")
                    #If total is perfectly 21, you won the game!
                    elif total == 21:
                        return ("Congrats! You have reached the perfect score of 21! You have won the game!")
                    #If total excedes 21, you lost the game.                        
                    elif total > 21:
                        return (f"Oh no! Your current amount of points is {total} which excedes 21 by {total-21} points! You lost the game. :(")
        
def main():
    print("This is the Card class! With this class, there are three functions.\nThe deckdisplay() function allows you to display the whole card deck.\nThe gofish() function is a game of go fish by yourself.\nYou pick a card of your card class and random cards will appear until one of the cards have the same matching number as your original card.\nThe blackjack() function is a game of Blackjack with yourself.\nYou will be tested on if you want to add card numbers as close to 21 as possible.\nIf it goes over, you lose!")
    card=Card("Space", "Ace")
    print(card.getsuit())
    print(card.getnumber())
    print(card.deckdisplay())
    print(card.gofish())
    print(card.blackjack())

if __name__ == "__main__":
    main()
        