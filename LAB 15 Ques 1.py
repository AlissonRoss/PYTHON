#Alisson Leiva CS17 LAB 15

def getMenuOption():
    print("\tMailing List Menu\n")
    print("1. Add a name to the list ")
    print("2. Delete name from the list ")
    print("3. Change name in the list ")
    print("4. Print names in the list ")
    print()
    option = input("Enter your selection : ")

    #Validation here
    while option < "1" or option > "4":
        print("\nInvalid selection of ",option)
        print("\nIt must be 1, 2, 3 or 4")
        option = input("Enter your selection : ")
        
    #only valid option returned    
    return option

#Action 1
def addName(nameList):
    newName = input("Enter name to add : ")
    nameList.append(newName)
    #Printing
    print("\n\nNew List ...")
    return(printList(nameList))
    
#Action 2
def removeNameList(nameList):
    #Input
    nameRemove=input("Enter name to remove:")
    #Removing Name
    nameList.remove(nameRemove)
    return(printList(nameList))
#Action 3
def replaceName(nameList):
    
    nameReplaced=input("Enter name to be replace:")
    
    newName=input("Enter new name:")
    
    if nameReplaced in nameList:
        #Finding Position
        position=nameList.index(nameReplaced)
        #Replacing
        nameList.remove(nameReplaced)
        nameList.insert(position,newName)
        #Printing
        return(printList(nameList))   
    else:
        #Invalid Entry
        print("Enter Valid Name")
        return
#Action 4
def printList(nameList):
    for i in range(0,len(nameList)):
        print(nameList[i],end=" ")        
                      
#initial list   
nameList = ["Bob","Tom","Abe","James","Joe"]
#Action #4
#main logic code
repeat = "y" or "Y"
while repeat == "y" or "Y":
    option = getMenuOption()

    if option == "1":
        addName(nameList)
    elif option == "2":
        removeNameList(nameList)
    elif option == "3":
        replaceName(nameList)
    elif option =="4":
        printList(nameList)
    else:
        print("\nOther options not done yet")

    repeat=input("\nRepeat again? y/n : ")

