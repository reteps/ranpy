import skilstak.colors as c
from time import sleep

def createcards():
    suits = ['diamonds','clubs','hearts','spades']
    values = [['ace',11],['jack',10],['queen',10],['king',10],['2',2],['3',3],['4',4],['5',5],['6',6],['7',7],['8',8],['9',9],['10',10]]
    standardDeck=[]
    for cardList in values:
        for suit in suits:
            word = cardList[0] + " of " + suit
            value = cardList[1]
            minilist = [word, value]
            standardDeck.append(minilist)
    return standardDeck

def printrules():
    print('''
{}Objective{}:Get as close to 21 points without going over.
{}How to win{}:Be the closest to 21 points. If you go over, you lose.
{}Point values{}:All cards are worth the value on the card, and face cards are worth 10.
{}Aces{}:Aces can be used as 1 or 11 points.
'''.format(c.y,c.x,c.y,c.x,c.y,c.x,c.y,c.x))
    input('Press enter to continue.\n')

def knowsHowToPlay():
    answered = False
    while answered == False:
        answer = input("{}{}Does everyone know how to play blackjack? ({}Y{}/{}n{}) > {}".format(c.x,c.cl,c.g,c.x,c.r,c.x,c.c)).lower().strip()
        if 'y' in answer:
            answered = True
        elif 'n' in answer:
            answered = True
            printrules()
        else:
            print('{}Invalid. Please say {}yes{} or {}no{}.'.format(c.x,c.g,c.x,c.r,c.x))

def isAce(card):
    if 'ace' in card:
        return True
    return False

def hasAce(aces):
    hasAce = False
    for ace in aces:
        if ace == 11:
            aces.remove(11)
            aces.append(1)
            hasAce = True
            break

    return hasAce, aces


def getTwoCards(deck):
    card =deck.pop()
    card2 = deck.pop()
    if isAce(card[0]) and isAce(card2[0]):
        total = 12
    else:
        total = card[1] + card2[1]
        
    titleOne = card[0]
    titleTwo = card2[0]
    return titleOne, titleTwo, total, deck

def getPlayers():
    try:
        while True:
            players = input('How many players? > ' + c.c)
            if players.isdigit():
                return int(players)
            else:
                print('{}Please type a {}number{}.'.format(c.x,c.r,c.x))
    except KeyboardInterrupt:
        print(c.cl)
        exit()

def printHand(titleOne, titleTwo, total):
    print("Your hand contains the " + c.b+titleOne + c.x+" and the " + c.b+titleTwo+c.x + " for a total of"+c.m,total,c.x+"points.")
def getOneMoreCard(deck,total):
    card = deck.pop()
    title = card[0]
            
    total += card[1]
    print(c.x+"Your new card is the "+c.b+title+c.x+". You now have"+c.m,total,c.x+'Points.')
    return total, deck, title
def askToHit(hand, firstTime):
    try:
        while True:
            itemstring = "Your hand contains:"
            for item in hand:
                itemstring += item + " "
            if firstTime == False:
                print(itemstring)
            wantToHit = input('Would you like to hit (take another card)? > ' + c.c).strip().lower()
            if 'y' in wantToHit:
                return True
                break
            elif 'n' in wantToHit:
                return False
                break
            else:
                print('{}Please type {}yes{} or {}no{}.'.format(c.x,c.g,c.x,c.r,c.x))
    except KeyboardInterrupt:
        print(c.cl)
        exit()
def getroundvalues(players):
    firstTime = []
    hands = []
    totals = []
    aces = []
    for x in range(players):
        firstTime.append(True)
        totals.append(0)
        hands.append([])
        aces.append([])
    return firstTime, hands, totals, aces
def getpermvalues(players):
    playerNames = []
    losses = []
    wins = []
    ties = []
    for x in range(players):
        playerNames.append("Player "+str(x + 1))
        wins.append(0)
        ties.append(0)
        losses.append(0)
    return playerNames, wins, ties, losses
def findBest(totals,hands):
    highest = 0
    shortest = 999
    for total in totals:
        if total < 22:
            if total > highest:
                highest = total
    for x in range(len(totals)):
        if totals[x] == highest and len(hands[x]) < shortest:
            shortest  = len(hands[x])

    return highest, shortest
def findWinners(totals, hands, losses):
    highest, shortest = findBest(totals,hands)
    winners = []
    for x in range(len(totals)):
        if totals[x] == highest and len(hands[x]) == shortest:
            winners.append(x)
        else:
            losses[x] += 1
    return winners, losses
def addAces(card1,card2,aces):
    if isAce(card1):
        aces.append(11)
    elif isAce(card2):
        aces.append(11)
    return aces
def printWinners(playerNames,winners,wins,ties):
    if len(winners) > 1:
        names = ""
        string = "The winners are:"
        for name in winners:
            ties[name] += 1
            names += playerNames[name] + " "
        print(string + c.o+names+c.x)
    elif len(winners) == 1:
        print(c.x+'The winner is '+c.g+playerNames[winners[0]]+c.x,"!")
        wins[winners[0]] += 1
    else:
        print(c.r+'Nobody'+c.x+' won this round!')
    return wins, ties
def printData(playerNames, wins, ties, losses, stage,hands,totals):
    for i in range(len(playerNames)):
        hand = ""
        for card in hands[i]:
            hand += (card + ", ")
        hand = hand[:-2]
        print(c.m+playerNames[i]+c.x+" card's include: "+c.y+hand+c.x+" for a total of:"+c.b,totals[i],c.x+"points.")
    print('\nplayer  |wins|ties|losses|%win/tie|%lose')
    for x in range(len(playerNames)):
        losspercent = round(losses[x]/(stage+1)*100,2)
        winpercent = 100 - losspercent
        print('{}|{}   |{}   |{}     |{}    |{}    '.format(playerNames[x],wins[x],ties[x],losses[x],winpercent,losspercent))
    print('\n\n')
def print_intro():
    print('''{}{}Welcome to {}Blackjack{}!
Created by: {}Peter S.{}
Version: {}0.9.5{}'''.format(c.x,c.cl,c.g,c.x,c.b,c.x,c.m,c.x))
def print_starting_data(rounds):
    print('''{}{}
Maximum rounds:{}{}{}
Decks used: {}8{}
{}Note{}: Earlier players are at a disadvantage
if you let other people look at your screen.'''.format(c.cl,c.x,c.y,rounds-1,c.x,c.y,c.x,c.y,c.x))