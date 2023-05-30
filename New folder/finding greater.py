def taking_input():
    number=[]
    ask=int(input("how many number do you want to input??"))
    for i in range(ask):
        num=int(input("enter a number"))
        number.append(num)
    return number;

# number=[1,15,8,4,90,6,2,30] 
def findingreater(number):
    greater_num = number[0]
    for i in range(0,len(number)-1):
        for j in range(1,len(number)):
            if greater_num>number[j] :
                greater_num=greater_num
            else:
                greater_num=number[j]
                # return greater_num
            
    print("The greatesst number in the list is=",greater_num)   

def run():
    print("Hello, This program finds the greatest number from the list of number provided by user")
    number=taking_input()
    findingreater(number)

run()

            



