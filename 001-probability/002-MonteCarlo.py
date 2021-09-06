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
    elif roll <= 50:
        #print roll,'roll was 1-50, you lose.'
        return False
    elif 100 > roll >= 50:
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
    wager = np.choice()
        

#%%
simple_bettor(10000,100,100)


#%%
x = 0

# start this off @ 1, then add, and increase 50 to 500, then 1000
while x < 10000:
    simple_bettor(10000,1000,10)
    x += 1



#%%
plt.ylabel('Account Value')
plt.xlabel('Wager Count')
plt.show()

#%%
# Now, just to test our dice, let's roll the dice 100 times. 
x = 0
while x < 100:
    result = rollDice()
    print(result)
    x+=1


    