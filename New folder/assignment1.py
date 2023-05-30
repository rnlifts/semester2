#Basal Metabolic rate


#creating function for determining exercise level
def exercise_level(BMR):
    print("Please select exercise code base on the following activity-")
    print()
    print("0:Little to no exercise")
    print("1:Light exercise(1-3 days per week)")
    print("2:Moderate exercise(3-5 days per week)")
    print("3:Heavy exercise(6-7 days per week)")
    print("4:Very heavy exercise(twice per day,extra heavy workouts)")

    while True:  #if user inputs string value then repeteady ask user for correct integer value
      try:
       exercise =int(input("Enter your exercise level(0-4)"))
       break
      except:
       print("enter valid data")

    print()
    while exercise>4: #if user inputs  value greater than 4 repeteady ask user for value within range
     while True:    #if user inputs string value then repeteady ask user for correct integer value
      try:
       exercise =int(input("Invalid selection,Enter your exercise level(0-4)"))
       break
      except:
        print("invalid data")
    #checking which exercise level code user have choose and determining calorie intake according to that
    if exercise==0:
        calorie_intake=BMR*1.2
    elif exercise==1:
        calorie_intake=BMR*1.375
    elif exercise==2:
        calorie_intake=BMR*1.55
    elif exercise==3:
        calorie_intake=BMR*1.725
    elif exercise==4:
        calorie_intake=BMR*1.9
    print("Your Daily Calorie Requirement Is:"+str(calorie_intake)+" "+"Kcal")
    return calorie_intake
    

# function that take user input on weight,height,age and calculates BMR and return BMR to user(For Men)
def for_men():
 while True:
    try:
     weight=int(input("Enter your weight in kilogram(KG)"))
     height=float(input("Enter your height in centimeter(cm)"))
     age=int(input("Enter your age in years"))
     BMR= 88.362+(13.397*weight)+(4.799*height)-(5.677*age) 
    except:
       print("enter valid data")
       
    print()
    print(f"Your BMR is {BMR}")
    exercise_level(BMR)
    break
    
# function that take user input on weight,height,age and calculates BMR and return BMR to user(For Women)
def for_women():
   while True:
    try:
      weight=int(input("Enter your weight in kilogram(KG)"))
      height=float(input("Enter your height in centimeter(cm)"))
      age=int(input("Enter your age in years"))
      BMR= 447.593+(9.247*weight)+(3.098*height)-(4.330*age)
      break
    except:
     print("enter valid data")
    
    print()
    print(f"Your BMR is {BMR}")
    print()
    exercise_level(BMR)
    break


    
#function that takes gender as input from user in string
def main_calculation():
 gender=input("enter your gender(m/f) ")
 while gender !='m' and gender!='f':
   gender=input("invalid,enter your gender(m/f) ")

 if gender =='m' or gender =='M':
    for_men() #if gender is male calls the for_men() function
 elif gender =='f' or gender =='F':
    for_women() #if gender is female calls the for_women() function

main_calculation()
 






       
       

    

