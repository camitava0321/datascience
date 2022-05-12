# -*- coding: utf-8 -*-
#author : Amitava Chakraborty

import random
import numpy as np
import matplotlib.pyplot as plt
#%%
def rollDice():
    roll = random.randint(1,100)
    return roll


def checkRoll(roll):
    if roll == 100:
        #print roll,'roll was 100, you lose. What are the odds?! Play again!'
        return False
    if roll <= 51:
        #print roll,'roll was 1-50, you lose.'
        return False
    if 100 > roll >= 51:
        #print roll,'roll was 51-99, you win! *pretty lights flash* (play more!)'
        return True


'''
Simple bettor, betting the same amount each time.
'''
def simple_bettor(funds,initial_wager,wager_count):
    value = funds
    wager = initial_wager
    # wager X
    wX = []
    #value Y
    vY = []

    plt.ylabel('Account Value')
    plt.xlabel('Wager Count')
    # starts with 1, to avoid confusion so we start @ wager 1
    currentWager = 1

    while currentWager <= wager_count:
        roll = rollDice()
        if checkRoll(roll):
            value += wager
        else:
            value -= wager

        wX.append(currentWager)
        vY.append(value)
        currentWager += 1
        plt.plot(wX,vY)
        if value < 0:
            value = 'Broke!'
            break
        #print 'Attempt: ',currentWager, 'Funds:', value

def complex_bettor(funds):
    value=funds
    #Complexity 1: Random Initial (or Fixed) Wager
    wager = random.randrange(100,value/10,100)
    #Complexity 2: Max How many times to play 
    maxWagers=random.randrange(80,120,10)
    # wager X
    wX = []
    #value Y
    vY = []

    plt.ylabel('Account Value')
    plt.xlabel('Wager Count')
    # starts with 1, to avoid confusion so we start @ wager 1
    currentWager = 1

    while value>0:
        quitted=False
        roll = rollDice()
        if checkRoll(roll):
            value += wager
        else:
            value -= wager

        wX.append(currentWager)
        vY.append(value)
        #Complexity 3: Next wager is always 10th of the value remaining, minimum 100
        wager = min(100, value/10)
        currentWager += 1
        plt.plot(wX,vY)
        if currentWager==maxWagers:
            break;
        #Complexity 4: After 75% of the game, player is given choice to quit
        gameFraction=float(currentWager)/float(maxWagers)
        if gameFraction>=0.75:
            quitted=quitGame(gameFraction, value/funds)
            #print(quitted)
            if quitted is True:
                break
    return currentWager, value, quitted
    

def quitGame(gameFraction, valueFraction):
    numberOfFalses=np.full(int(gameFraction*100), False)
    numberOfTruths=np.full(int(valueFraction*100), True)
    listOfTrueFalses =  np.concatenate((numberOfFalses, numberOfTruths), axis=None)
    print (listOfTrueFalses)
    return random.choice(listOfTrueFalses)
        
    

#%%
simple_bettor(10000,100,100)


#%%
x = 0

# start this off @ 1, then add, and increase 50 to 500, then 1000
while x < 10000:
    simple_bettor(10000,1000,10)
    x += 1
plt.show()

#%%
x = 0

# start this off @ 1, then add, and increase 50 to 500, then 1000
playersShare=0 ; casinoShare = 0
while x < 100:
    wagers, finalFund, quitted = complex_bettor(10000)
    print("Player: ", x, "---# of wagers: ", wagers, 'Final Funds: ', finalFund, 'Quit: ', quitted)
    if finalFund>10000:
        playersShare += finalFund
    else:
        casinoShare += abs(finalFund)
    x += 1

print ("Total Fund Played: ",10000*100, "Players: ", playersShare, "Casino: ", casinoShare)
plt.show()

#%%
# Now, just to test our dice, let's roll the dice 100 times. 
x = 0
while x < 100:
    result = rollDice()
    print(result)
    x+=1


    