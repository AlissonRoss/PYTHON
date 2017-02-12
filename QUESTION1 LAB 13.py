#A list to store sales figure
sales=[]
days=['Mon','Tues','Wed','Thurs','Fri']

#Functions
def arrayLoop():
    array=[]
    arrayCount = 0
    #Array of the Input
    while arrayCount < 5:
        #Input 
        salesFigure=int(input("Enter sales figure:"))
        arrayCount=arrayCount+1
        array.append(salesFigure)
        
    #Returning to Array
    return array
sales=arrayLoop()
#Printing Max Value
def findMax():
    
    max(sales)
print()
print("Max value is:",max(sales))
#Printing Total
def findTotal():
    sum(sales)
print()
print("Total value is:",sum(sales))

#Printing Array
def myPrint(sales):
    arrayCount=0
    while arrayCount < 5:
        #Printing
        print (days[arrayCount])
        print (sales[arrayCount])
        
        arrayCount=arrayCount+1       
#Defined Variables
(myPrint(sales))
