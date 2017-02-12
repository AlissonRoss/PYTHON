#Alisson Leiva Assignment 5 Question 3
#Astronomy Helper
def mainMenu():
    print("Select a Planet by entering corresponding number")
    print("1. Mercury")
    print("2. Venus")
    print("3. Earth")
    print("4. Mars")
    print("5. Exit the program")
    planetIn=input("Enter your selection from the Main menu:")
    
#Main Logic
    #Loop for Mercury
    if planetIn == "1":
        mercuryChosen=(mercuryMenu()) 
        if mercuryChosen == "1":
            (mercuryAv())
                
        elif mercuryChosen == "2":
            (mercuryMass())
                
        elif mercuryChosen == "3":
            (mercurySurf())
        elif mercuryChosen == "4":
            (mainMenu())
                
    #Loop for Venus            
    elif planetIn == "2":
        venusChosen=(venusMenu())
        if venusChosen == "1":
            (venusAv())
        elif venusChosen == "2":
            (venusMass())
        elif venusChosen == "3":
            (venusSurf())
        elif venusChosen == "4":
            (mainMenu())
    #Loop for Earth
    elif planetIn == "3":
        earthChosen=(earthMenu())
        if earthChosen == "1":
            (earthAv())
        elif earthChosen == "2":
            (earthMass())
        elif earthChosen == "3":
            (earthSurf())
        elif earthChosen == "4":
            (mainMenu())
    #Loop for Mars
    elif planetIn == "4":
        marsChosen=(marsMenu())
        if marsChosen == "1":
            (marsAv())
        elif marsChosen == "2":
            (marsMass())
        elif marsChosen == "3":
            (marsSurf())
        elif marsChosen == "4":
            (mainMenu())
    #Quit the program
    elif planetIn == "5":
        quit()
    #Prints when Input isn't valid
    else:
        planetIn=input("Invalid selection. Enter selection again:")       
        
#Functions for planets

#MERCURY           
def mercuryMenu():
    print("Mercury Menu")
    (allOptions())

    mercuryIn=input("Enter your selection from the Mercury menu:")
    return mercuryIn
    while mercuryIn < "1" or mercuryIn > "4":
        mercuryIn=input("Try again:")
    

#Mercury's Average
def mercuryAv():
    print("Average distance from the sun: 57.9 million kilometers")
    return
#Mercury's Mass
def mercuryMass():
    print("Mass: 3.31 x 10^23 kg")
    return
#Mercury's Surface
def mercurySurf():
    print("-173 to 430 degrees Celsius")
    return
    
# VENUS
def venusMenu():
    print("Venus Menu")
    (allOptions())
    venusIn=input("Enter your selection from the Venus menu:")
    return venusIn
    while venusIn < "1" or venusIn > "4":
        venusIn=input("Try again:")

#Venus's Average
def venusAv():
    print("Average distance from the sun: 108.2 million kilometers")
    return
#Venus's Mass
def venusMass():
    print("Mass: 4.87 x 10^24 kg")
    return
#Venus's Surface
def venusSurf():
    print("Surface temperature: 472 degress Celsius")
    return


# EARTH
def earthMenu():
    print("Earth Menu")
    (allOptions())
    earthIn=input("Enter your selection from the Earth menu:")
    return earthIn
    while earthIn < "1" or earthIn > "4":
        earthIn=input("Try again:")
#Earth's average
def earthAv():
    print("Average distance from the sun: 149.6 million kilometers")
    return
#Earth's Mass
def earthMass():
    print("Mass: 5.967 x 10^24 kg")
    return
#Earth's Surface
def earthSurf():
    print("Surface temperature: -50 to 50 degress Celsius")
    return

    
#MARS
def marsMenu():
    print("Mars Menu")
    (allOptions())
    marsIn=input("Enter your selection from the Mars menu:")   
    return marsIn
    while marsIn < "1" or marsIn > "4":
        marsIn=input("Try again:")
#Mars's average
def marsAv():
    print("Average distance from the sun: 227.9 million kilometers")
    return
#Mars's Mass
def marsMass():
    print("Mass: 0.6424 x 10^24 kg")
    return
#Mars's Surface
def marsSurf():
    print("Surface temperature: -140 to 20 degress Celsius")
    return



#Gets all the options       
def allOptions():
    print("1. Average distance from the sun")
    print("2. Mass")
    print("3. Surface temperature")
    print("4. Quit")

#Defines Main Menu
(mainMenu())
