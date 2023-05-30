def taking_input():
    number=[]
    ask=int(input("how many number do you want to input in a list??"))
    for i in range(ask):
        num=int(input("enter a number"))
        number.append(num)
    return number;

def sum(number):
    output= 0
    
    for j in range(0,len(number)):
            output=output+number[j] 
    print("sum of list is=",output)

def main():
    print("this program prints the sum of number in the list provided by user")
    number=taking_input()
    sum(number)

main()
