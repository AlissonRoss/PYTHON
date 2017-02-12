#Alisson Leiva CS17 LAB 15
def mainMenu():
    print("\tSelect a Language and I will say good morning!\n")
    print("1. English ")
    print("2. Italian ")
    print("3. Spanish ")
    print("4. German ")
    print("5. End the Program ")
    print()
    userInput = input("Enter your selection:")
    #Validation
    while userInput < "1" or userInput > "5":
        print("\nInvalid selection of ",userInput)
        print("\nIt must be 1, 2, 3, 4, or 5")
        userInput = input("Enter your selection : ")
        
    #Valid input returned   
    return userInput
def english(stringList):
    print(stringList[0])
def italian(stringList):
    print(stringList[1])
def spanish(stringList):
    print(stringList[2])
def german(stringList):
    print(stringList[3])
def exitOut():
    quit()
    
#Array
stringList=["Good Morning","Buongiorno","Bueno Dias","Guten Morgen"]
#Main Logic
repeat = "y" or "Y"
while repeat == "y" or "Y":
    option = mainMenu()

    if option == "1":
        english(stringList)
    elif option == "2":
        italian(stringList)
    elif option == "3":
        spanish(stringList)
    elif option =="4":
        german(stringList)
    elif option =="5":
        exitOut()
    else:
        print("\nOther options not done yet")

    repeat=input("\nRepeat again? y/n : ")

