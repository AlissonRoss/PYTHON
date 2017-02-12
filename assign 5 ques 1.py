#Alisson Leiva Assignment 5 Question 1 (Payroll)
idNum=["56588","45201","78951","87775","84512","13028","75804"]
i=0

array1=[]
array2=[]
array3=[]

hours=[]
payRate=[]
wagesAmt=[]

def hoursIn():
    num=int(input("Input employee's hours:"))
    array1.append(num)
    return array1
def payrateIn():
    num2=float(input("Input pay rate:"))
    array2.append(num2)
    return array2
def wagesIn():
    num3=hours[i]*payRate[i]
    array3.append(num3)
    return array3

while i < len(idNum):
    print("Employee's ID number:",idNum[i])
    hours= hoursIn()
    payRate= payrateIn()
    wagesAmt=wagesIn()
    print(idNum[i],"earned",wagesAmt[i])
    print()
    i= i+1
    
