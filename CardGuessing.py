#Initializatin of the list of strings of cards in a deck (Order of this deck is Important!!!)
deck = ['A_C','A_D', 'A_H', 'A_S','2_C','2_D', '2_H', '2_S','3_C','3_D','3_H','3_S','4_C','4_D','4_H','4_S','5_C','5_D','5_H','5_S',
        '6_C','6_D','6_H','6_S','7_C','7_D','7_H','7_S','8_C','8_D','8_H','8_S','9_C','9_D','9_H','9_S','10_C','10_D','10_H','10_S'
        ,'J_C','J_D','J_H','J_S','Q_C','Q_D','Q_H','Q_S','K_C','K_D','K_H','K_S']

# This is a very cool algorithm that decides which should be the first card that is picked
# It reveals 3 more cards that are decoded in order to find the last  hidden card to make a guess
# the first and the hidden card will always be in the same suit  
# it decodes the hidden number based on a low, Medium, High System
# if the values are the same then it uses a system which ranks Clubs, Diamonds, Hearts, and Spades in that order

# Encode 1: Low Medium High
# Encode 2: Low High Medium
# Encode 3: Medium Low High
# Encode 4: Medium High Low
# Encode 5: High Low Medium 
# Encode 6: High Medium Low 

# Here is an example that explains this algorithm
# 1) If you draw a J_H, J_S, A_H, 6_H, K_S then you could use J_H as the 1st card and A_H as the hidden card
#    So you would then decode a 3 within the next 3 cards because Jack is 3 away from Ace
#    you would put the cards in this order J_H, J_D, 6_H, K_S and the hidden card is A_H

# this function is with a person going through and manually ordering the cards

# call method where I would give it the four cards in the proper order and it has to guess the 5th card
def guess_card():
    print('Cards are character strings shown below. ')
    print('Ordering is ', deck)
    cards,cind = [],[]
    for i in range(4):
        print('Please give card ',i + 1, end = ' ')
        card = input('in above format: ')
        cards.append(card)
        n = deck.index(card)
        cind.append(n)
        if i == 0:
            suit = n %4
            number = n // 4

    if cind[1] < cind[2] and cind[1] < cind[3]:
        if cind[2]<  cind[3]:
            encode = 1
        else:
            encode = 2
    elif((cind[1] , cind[2] and cind[1] > cind[3]) or (cind[1] > cind[2] and cind[1]< cind[3])):
        if cind[2] < cind[3]:
            encode = 3
        else:
            encode = 4
    elif cind[1] > cind[2] and cind[1] > cind[3]:
        if cind[2] < cind[3]:
            encode = 5
        else:
            encode  = 6
    
    hiddennumber = (number + encode) % 13
    index = hiddennumber * 4 + suit

    print('Hidden card is ', deck[index])


guess_card() 
