#Constants
GRAVITY_AMT=9.8
DISTANCE_TOTAL=0

#Functions
def fallingDistance(DISTANCE_TOTAL,GRAVITY_AMT,timeFall):
    #While and For Loops
    while timeFall > 0:
        for secondsFall in range(1, timeFall+1):
            DISTANCE_TOTAL=0.5*GRAVITY_AMT*secondsFall*secondsFall
            #Printing
            print ("Time of:",secondsFall,"\n Distance in meters:",DISTANCE_TOTAL)
        return

#Inputs
timeFall= int(input('Enter falling time <in seconds> of the object:'))

#Defining Functions
(fallingDistance(DISTANCE_TOTAL,GRAVITY_AMT,timeFall))



