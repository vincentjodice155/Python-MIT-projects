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

# Here is an examples that explain this algorithm
# 1) If you draw a J_H, J_S, A_H, 6_H, K_S then you could use J_H as the 1st card and A_H as the hidden card
#    So you would then decode a 3 within the next 3 cards because Jack is 3 away from Ace
#    you would put the cards in this order J_H, J_D, 6_H, K_S and the hidden card is A_H

# this function is with a person going through and manually ordering the cards
def person_ordering_cards():
    print('Cards are character strings as shown below. ')
    print('Order is ', deck)

    #intitializing variables
    cards,cind,cardsuits,cnumbers = [], [], [], []
    numsuits = [0,0,0,0]

    for i in range(5):
        print('Please give card ', i + 1, end = ' ')
        card = input('in above format:')
        cards.append(card)
        n = deck.index(card)
        cind.append(n)
        # %4 is always going to display the same suit as the 5 cards that are chosen
        cardsuits.appen(n % 4)
        cnumbers.append(n // 4)
        numsuits[n % 4] += 1
        if numsuits[n % 4] > 1:
            pairsuit = n % 4
    
    cardh = []
    for i in range(5):
        if cardsuits[i]  == pairsuit:
            cardh.append(i)
    
    # hidden stands for the one card that is hidden, encode is the first card, other represents the other 3 cards
    hidden,other,encode = output_first_card(cnumbers,cardh,cards)

    remindices = []
    for i in range(5):
        if i != hidden and i != other:
            remindices.append(cind[i])

    # order three cards base on ascending order
    sort_list(remindices)

    output_next_three_cards(encode,remindices)

    return

# helps determine between two cards which one should be hidden (both cards have the same suit)
def output_first_card(numbers, oneTwo,cards):

    encode = (numbers[oneTwo[0]] - numbers[oneTwo[1]]) %  13
    if encode > 0 and encode <= 6:
        hidden = oneTwo[0]
        other = oneTwo[1]
    else:
        hidden = oneTwo[1]
        other = oneTwo[0]
        encode = (numbers[oneTwo[1]] - numbers[oneTwo[0]]) %  13
    
    print('First card is ', cards[other])

    return hidden,other,encode

# this function helps determine which cards should be put in the next three slots

def output_next_three_cards(code, ind):
    if code == 1:
        second,third,fourth  = ind[0],ind[1], ind[2]
    elif code == 2:
        second,third,fourth = ind[0],ind[2], ind[1]
    elif code == 3:
        second,third,fourth = ind[1],ind[0], ind[2]
    elif code == 4:
        second,third,fourth = ind[1],ind[2], ind[0]
    elif code == 5:
        second,third,fourth = ind[2],ind[0], ind[1]
    else:
        second,third,fourth = ind[2],ind[1], ind[0]
    
    print('Second Card is ',deck[second])
    print('Third card is ',deck[third])
    print('Fourth card is ', deck[fourth])

def sort_list(listneedingsort):
    for index in range(0, len(listneedingsort) - 1):
        ismall = index
        for i in range(index, len(listneedingsort)):
            if listneedingsort[ismall] > listneedingsort[i]:
                ismall = i
        listneedingsort[index], listneedingsort[ismall] = listneedingsort[ismall],listneedingsort[index]
    return

# call method where I would give it the four cards in the proper order and it has to guess the 5th card
def guess_card():
    print('Cards are character strings shown below. ')
    print('Ordering is ', deck)
    cards,cind = [],[]
    for i in range(4):
        print('Please give cards ',i + 1, end = ' ')
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
