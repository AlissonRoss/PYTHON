#Loop
def printBox(inputRow,inputCol):
    #For-Loop
    for inputRow in range(1,inputRow+1):
        for inputCol in range(1,inputCol+1):
            #Function in-Loop
            total=inputCol*inputRow
            print(total, end=" ")
        print()
#Input
inputRow=int(input("\n Enter number of rows:"))
inputCol=int(input("\n Enter number of columns:"))

#Print
(printBox(inputRow,inputCol))
