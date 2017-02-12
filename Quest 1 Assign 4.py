#Alisson Leiva Assignment 4 Question 1
#Function
def calculation(fatGramsIn,foodCalIn):
    if fatGramsIn and foodCalIn < 0:
        print ("Input less than 0")
    elif fatGramsIn and foodCalIn >0:
        perCalFat=(fatGramsIn*9)/foodCalIn
        print ("Percentage of calories from fat:",perCalFat,"%")
        if perCalFat < .30:
            print("Low Fat Intake!:",perCalFat,"%")
            return
    elif foodCalIn > fatGramsIn*9:
        print ("Number of calories cannot exceed fat grams * 9")
        
#Input
fatGramsIn=int(input("Enter number of fat grams:"))
foodCalIn=int(input("Enter calories in food item:"))

#Defining
(calculation(fatGramsIn,foodCalIn))
