#Alisson Leiva LAB 16 Question #2
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
    print("Circle Menu")
    print("1.Area")
    print("2.Perimeter")
    print("3.Quit")
    optCircle=input("Enter numbers from 1 through 3:")
    while optCircle < "1" or optCircle > "3":
        optCircle=input("Enter numbers from 1 through 3 again:")
    return optCircle
def circleArea():
    
    radius=int(input("Enter radius of circle for Area calculation:"))
    import math
    area=radius*radius*math.pi
    print("Area of the circle is",area,".")
    
def circlePerimeter():
    radius=int(input("Enter radius of circle for Circumference calculation:"))
    import math
    circumference= 2*math.pi*radius
    print("Circumference of the circle is",circumference,".")   
#TRIANGLE
def printTriangle():
    print("Triangle Selected...")
    print("Triangle Menu")
    print("1.Area")
    print("2.Pythagorean Theorem")
    print("3.Quit")
    optTri=input("Enter numbers from 1 through 3:")
    while optTri < "1" or optTri > "3":
        optTri=input("Enter numbers from 1 through 3 again:")
    return optTri

def triangleArea():
    
    height=int(input("Input value for Height:"))
    base=int(input("Input value of the Base:"))
    area=height*base/2
    print("Area of Right Triangle is",area,".")
    
def triangleHy():
    import math
    height=float(input("Input value for Height:"))
    base=float(input("Input value of the Base:"))
    hy=math.sqrt((base*base)+(height*height))
    print("Hypotenuse:",hy,".")
    
    
#RECTANGLE
def printRectangle():
    print("Rectangle Selected...")
    print("Rectangle Menu")
    print("1.Perimeter")
    print("2.Area")
    print("3.Quit")
    optRec=input("Enter numbers from 1 through 3:")
    while optRec < "1" or optRec > "3":
        optRec=input("Enter numbers from 1 through 3 again:")
    return optRec
def recPeri():
    length=int(input("Enter Length:"))
    width=int(input("Enter Width:"))
    perimeter=2*(length+width)
    print("Perimeter of Rectangle:",perimeter,".")
        
def recArea():
    length=int(input("Enter Length:"))
    width=int(input("Enter Width:"))
    area=length*width
    print("Area of rectangle:",area,".")
    return area
       
#Main Logic
repeatIn="y" or "Y"
while repeatIn== "y" or "Y":
    shapeOption=shapesMenu()
    #Circle Menu
    if shapeOption == "1":
        optCircle=(printCircle())
        while optCircle== "1":
            (circleArea())
        while optCircle == "2":
            (circlePerimeter())
        while optCircle == "3":
            (shapesMenu())
    #Triangle Menu    
    elif shapeOption == "2":
        optTri=(printTriangle())
        while optTri == "1":
            (triangleArea())
        while optTri == "2":
            (triangleHy())
        while optTri == "3":
            (shapesMenu())
    #Rectangle Menu
    elif shapeOption == "3":
        optRec=(printRectangle())
        while optRec =="1":
            (recPeri())
        while optRec == "2":
            (recArea())
        while optRec == "3":
            (shapesMenu())
    #QUIT
    elif shapeOption == "4":
        quit()
    else:
        print("Options not done yet")
    repeatIn=input("Repeat? y/n")
