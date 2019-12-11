# created by Allison Dixon
# last modified on December 11, 2019
# unit 9 option 1: this program creates a game of Compare (a small game of War) between the user and the dealer

import deck


def deal_cards(my_deck):
    """
    This function deals five cards to a player.
    :param my_deck: calls the deck class
    :return: the players' cards
    """
    user_cards = []
    for x in range(5):
        user_card = my_deck.deal()
        user_cards.append(user_card)
    return user_cards


def compare_cards(user_card, dealer_card):
    """
    This function compares one of the user's and dealer's cards and prints who won.
    :param user_card: The user's card being compared
    :param dealer_card: the dealer's card being compared
    :return: True if the user won and false if the dealer won
    """
    if user_card > dealer_card:
        print("The user wins!")
        print("")
        return True
    else:
        print("The dealer wins!")
        print("")
        return False


def main():
    # this line calls the deck class
    my_deck = deck.Deck()
    # this line calls from the deck class to shuffle the cards
    my_deck.shuffle()
    # the following two lines keep track of the user's hand and the dealer's hand
    user_deal = deal_cards(my_deck)
    dealer_deal = deal_cards(my_deck)
    # the following two lines help keep track of the amount of wins
    user_wins = 0
    dealer_wins = 0
    # this for loop prints the user's and dealer's cards and compares them, adding 1 to the user's wins if they win,
    # or to the dealer's wins if they win
    for x in range(5):
        print("The user has", user_deal[x])
        print("The dealer has", dealer_deal[x])
        if compare_cards(user_deal[x], dealer_deal[x]):
            user_wins += 1
        else:
            dealer_wins += 1
    # this if statement prints who won the game based on who won more games
    if user_wins > dealer_wins:
        print("The user won the game!")
    else:
        print("The dealer won the game!")


main()
