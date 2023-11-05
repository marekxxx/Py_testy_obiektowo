import random

# stałe przedstawiając karty
SUIT_TUPLE = ('pik', 'kier', 'trefl', 'karo')
RANK_TUPLE = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'walet', 'dama', 'król', 'as')
NCARDS = 8

# Przekazanie karty. Wartością zwrotną jest losowa karta za tali
def getCard(deckListIn):
    thisCard = deckListIn.pop() # pobranie karty z góry tali.
    return thisCard

# Przekazanie tali, Wartością zwrotną jest funkcji jest talia w której karty są ułożone losowo.
def shuffle(deckListIn):
    deckListOut = deckListIn.copy() # utwożenie kopi talii początkowej
    random.shuffle(deckListOut) # potasowanie kopi talii 
    return deckListOut

print ('Witaj w grze większa lub mniejsza.')
print ('Musisz odgadnąc, czy następna karta będzie miała wartość większą czy mniejszą od aktualnej karty')
print ('Jeżeli odgadniesz zdobywasz 20 punktów. W przeciwnym wypadku tracisz 15 punktów.')
print ('Na początek masz 50 pkt.')
print ('')

startingDeckList = []
for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):
        cardDict = {'rank':rank, 'suit':suit, 'value':thisValue + 1}
        startingDeckList.append(cardDict)

score = 50

while True:
    print()
    gameDeckList = shuffle(startingDeckList) # Pobranie na nowo potasowanej tali.
    currentCardDict = getCard(gameDeckList) # Pobranie karty z góry tali
    currentCardRank = currentCardDict['rank'] # przekazanie do zmienej rangi tej konkretnej karty
    currentCardValue = currentCardDict['value'] # przekazanie do zmiennej wartości karty
    currentCardSuit = currentCardDict['suit'] # przekazanie do zmiennej koloru karty.

    print ('Pierwsza karta to:', currentCardRank + ' ' + currentCardSuit )
    print()

    for cardNumber in range(0, NCARDS):
        answer = input('Jaka będzie następna karta: większa czy mniejsza niż' + currentCardRank + currentCardSuit + '? (wpisz w lub m):')
        answer.casefold() # wymuszenie małych liter.
        nextCardDict = getCard(gameDeckList)
        nextCardRank = nextCardDict['rank']
        nextCardSuit = nextCardDict['suit']
        nextCardValue = nextCardDict['value']
        print('Następna karta to:', nextCardRank, nextCardSuit)

        if answer == 'w':
            if nextCardValue > currentCardValue:
                print('Masz rację, karta miała większą wartość')
                score = score +20
            else:
                print('Nietety karta nie miała większej wartości')
                score = score - 15
        elif answer == 'm':
            if nextCardValue < currentCardValue:
                print('Masz rację karta ma mniejszą wertość')
                score = score +20
            else:
                print('Niestety karta nie miała niższej wartości')
                score = score -15
        print('Twój wynik:', score)
        print()
        currentCardRank = nextCardRank
        currentCardValue = nextCardValue

    goAgain = input('Naciśnij ENTER, aby zagrać ponownie, "q" aby zakończyć grę')
    if goAgain == 'q':
        break
print('Żekgaj !!!')


                       