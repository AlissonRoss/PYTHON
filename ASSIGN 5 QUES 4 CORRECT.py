#Alisson Leiva Assignment 5 Question 4 (Telephone Number Translator) **ATTEMPT**
#Array for Alphabet

#Parallel Array
alphArray=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"],\
              ["P","Q","R","S","T","U","V","W","X","Y","Z"]
numArray= ["2","3","4","5","6","7","8","9","1","0"]

#Input
numIn=input("Enter phone number in (XXX-XXX-XXXX):")
    
#Splitting input    
splitNum= numIn.split("-")


def FunctLog():    
    #Loop that checks invalid numbers
    listLength1,listLength2,listLength3 = listLengths(splitNum)
    if listLength1 != 3 or listLength2 != 3 or \
       listLength3 != 4:
        print("Number should be in (XXX-XXX-XXXX)")
    #Else prints the number entered    
    else:    
        print("Number entered:")
        print(splitNum[0].upper(),"-",splitNum[1].upper(),\
              "-",splitNum[2].upper(),sep="")
        (translation(splitNum))
#Converts numbers in the array        
def convertNum(num,numArray,alphArray):
    if num in numArray:
        return num
    else:
        for row in range (len(alphArray)):
            for column in range(len(alphArray[row])):
                if num == alphArray [row] [column]:
                    return numArray[row]
#Function for printing the translation in each array
def translation(splitNum):
        print("Number translated:")
        #Array 1
        
        for num in splitNum[0]:
            numUpper = num.upper()
            results = (convertNum(numUpper,numArray,alphArray))
            print(results,end=" ")
        print("-",end=" ")
        #Array 2
        for num in splitNum[1]:
            numUpper = num.upper()
            results = (convertNum(numUpper,numArray,alphArray))
            print(results,end=" ")
        print("-",end=" ")
        #Array 3
        for num in splitNum[2]:
            numUpper = num.upper()
            results = (convertNum(numUpper,numArray,alphArray))
            print(results,end=" ")
#Lists of the three Arrays
def listLengths(anyList):
    array1=len(anyList[0])
    array2=len(anyList[1])
    array3=len(anyList[2])
    return array1,array2,array3
#Calls main Function
(FunctLog())
        
