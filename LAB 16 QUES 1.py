#Alisson Leiva LAB 16 Question #1
#Main Shapes Menu
def shapesMenu():
    print("Geometrical Shapes Menu:")
    print("1.Circle")
    print("2.Triangle")
    print("3.Rectangle")
    print("4.Quit")
    #Input for Main Shapes Menu
    shapeOption= input("Enter your selection:")
    
    #Loop to Check for selection
    while shapeOption < "1" or shapeOption > "4":
        print("Enter numbers from 1 through 4")
        shapeOption=input("Enter your selection:")
    return shapeOption
    
#CIRCLE
def printCircle():
    print("Circle Selected...")
#TRIANGLE
def printTriangle():
    print("Triangle Selected...")
#RECTANGLE
def printRectangle():
    print("Rectangle Selected...")
    
#Main Logic
repeatIn="y" or "Y"
if repeatIn== "y" or "Y":
    shapeOption=shapesMenu()
    if shapeOption == "1":
        opt=(printCircle())
    elif shapeOption == "2":
        (printTriangle())
    elif shapeOption == "3":
        (printRectangle())
    elif shapeOption == "4":
        quit()
    else:
        shapeOption=input("Enter numbers from 1 through 4")
    repeatIn=input("Repeat command? y/n:")







