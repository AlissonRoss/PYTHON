#Functions

def readScore(score):
    while score < 0 or score > 20:
        print ('Enter score no less than 0 or greater than 20:')
        score=int(input('Enter score from 0 to 20:'))
        return (score)

def passOrFail(score):
    if score >= 0 and score < 10:
        print ('FAIL')
        return
    else: score >= 10 and score <= 20
    print ('PASS')

#Input
score=int(input('Enter score from 0 to 20:'))

#Defining Variables
scoreInvalid=(readScore(score))
scoreOut=(passOrFail(score))

