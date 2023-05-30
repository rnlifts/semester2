def number():
    low_number=int(input("enter a number(a lower number)"))
    high_number=int(input("enter a number(a higher number)"))
    while high_number<low_number:
     high_number=int(input("enter a number(a higher number)"))
    if low_number<high_number:
       sum=low_number
       for i in range(low_number,high_number):
            low_number=low_number+1
            a=low_number
            sum= sum+a
        
    print(sum)
       

number()