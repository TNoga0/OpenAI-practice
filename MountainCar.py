import gym
import universe
import numpy as np

envir = gym.make('MountainCar-v0')
observation = envir.reset()
action = 0

lastpos = 0
boundarypos = -1.2
score = 0
lastscore = 0
lowestscore = -20000

flagAccel = False

oldpos = observation[0]
newpos = observation[0]
i = 0

def czycofa(akcja):
    if akcja == 0:
        return True
    else:
        return False


while True:
    if flagAccel:
        while observation[0] < 0.494:
            action = 2
            observation, reward, done, info = envir.step(action)
            envir.render()
            score = score + reward
            if done:
                flagAccel = False
                action = 0
                envir.reset()
                score = 0
    else:
        observation, reward, done, info = envir.step(action)
        envir.render()
        score = score + reward
        i = i+1
        if i == 3:
            oldpos = newpos
            newpos = observation[0]
            i = 0

        if newpos > boundarypos - 0.03 and newpos < boundarypos + 0.03 and czycofa(action):
            flagAccel = True
        else:
            if newpos > oldpos:
                action = 2
            elif newpos < oldpos:
                lastpos = newpos
                action = 0



    #pozycja 0.5 oznacza ze dotarl i reset
    if observation[0] >= 0.494:
        flagAccel = False
        action = 0
        print score
        lastscore = score
        if lastscore > lowestscore:
            lowestscore = lastscore
            boundarypos = lastpos
            score = 0
    if done:
        flagAccel = False
        action = 0
        envir.reset()
        score = 0