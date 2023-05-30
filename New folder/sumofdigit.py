
number= int(input("enter a number"))
sum=0
while number>0:
 remainder=number%10;
 number=int(number/10)
 sum=sum+remainder
print("sum of digit is=",sum)

