#ALISSON LEIVA LAB 17

str = input('Enter a string : ')

words = str.split()

size = len(words)

print()
finalString = ""

for i in range(0,size):
    if size >= 1:
        temp=words[i]
    
        tempStr=temp[1:]+temp[0]
    
        tempStr+="AY "
    
    finalString+=tempStr
print("\n\nFinal String : ",finalString,end="")
   
    


