#Alisson Leiva LAB 14 Ques 2
#Parallel Arrays
rowName=["Ali","Kim","Jim","Jun","Hana","Zak","Jameson","McCree"]
colsPhone=[2094523428,2094325678,4523416823,1582532679,1234567891,2345678912,5678901235,5678912345]
#Variable to find data
find=len(rowName)
index=7
#Function
def inputName(colsPhone,rowName,index):
    #Input
    nameIn=input(str("Enter name:"))
    #Finding Data
    for index in range(0,find):
        if nameIn == rowName[index]:
            print(rowName[index],":",colsPhone[index])
        else:
            print("Enter Valid name")
#Defining Variable
(inputName(colsPhone,rowName,index))
        


        
        
        
        
