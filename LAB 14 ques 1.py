#- Alisson Leiva -LAB 14 Ques # 1
#Arrays
scoresArray=[]
count=0
total=0

#Function
def function(scoresArray,count,total):
    #While Loop
    while count < 8:
        #Input
        inputScore=int(input("Enter 8 integers:"))
        scoresArray.append(inputScore)
        #Total Calculation
        total=inputScore+total
        count=count+1
        #Average Calculation
        totalAverage=(total/8)
    #Defining Arrays for Lowest and Highest
    lowest=scoresArray[0]
    highest=scoresArray[0]
    
    #For Loops for Lowest and Highest integers
    for count in range(1,count):
        if scoresArray[count] < lowest:
            lowest=scoresArray[count]
    for count in range(1,count):
        if scoresArray[count] > highest:
            highest=scoresArray[count]   
    #Printing in Loop
    print()  
    print ("Lowest integer inputted:",lowest)
    print("Highest integer inputted:",highest)
    print("Total is:",total)
    print("Average of integers:",totalAverage)
#Defining Variables
(function(scoresArray,count,total))





                  
      




