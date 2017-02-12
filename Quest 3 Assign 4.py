#Alisson Leiva Assignment 4 Question 3

arrayScore=['B','D','A','A','C']
arrayQues=[1,2,3,4,5]
inputAnswer=[]
#Function
def scoreOut(arrayScore,arrayQues):
    count=0
    inCount=0
    corCount=0

    while count < 5:
        #Input
        answerIn=input(str("Enter answer for question with caps lock on:"))
        #Appending Input
        inputAnswer.append(answerIn)
         

        if inputAnswer[count] == arrayScore[count]:
            print ("Correct")
            corCount=corCount+1     
            count=count+1
        else:
            print ("Incorrect")
            inCount=inCount+1
            count=count+1 
    correctAmount=(corCount/len(arrayScore))*100
    print (correctAmount,'%')
    if correctAmount < 70:
        print  ("FAILED")
        
    else:
        print ("PASSED")
(scoreOut(arrayScore,arrayQues))

