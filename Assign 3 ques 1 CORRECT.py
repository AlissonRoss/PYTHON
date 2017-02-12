#Function
def calculationDistance(inputSpeed,inputHours):
    #Loop
    for inputHours in range(1,inputHours+1):
        totalMiles=inputHours*inputSpeed
        print (inputHours,"       ", totalMiles)
        
#Input
inputSpeed=int(input ("\n Enter mph:"))
inputHours=int(input("\n Enter hours:"))


#Print
print ("HOUR","    ","DISTANCE TRAVELED")
calculationDistance(inputSpeed,inputHours)
