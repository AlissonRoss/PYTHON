#-Alisson Leiva-
#Array
dates=['January','February','March','April','May','June','July','August','September','October','November','December']
days=[31,28,31,30,31,30,31,31,30,31,30,31];

#Function
def arrayFunct(days,dates):
    count=0
    #Array for Loop
    arrayDates=[]
    arrayDays=[]
    while count < 12:
        #Declaring Arrays
        arrayDates=dates
        arrayDays=days
        #Printing in Loop
        print ((arrayDates[count]),'has',(arrayDays[count]),'days.')
        
        #Count in Loop
        count=count+1
     #Returning Arrays   
    return arrayDates
    return arrayDays
#Defining Variables
(arrayFunct(days,dates))
