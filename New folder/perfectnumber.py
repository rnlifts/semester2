def divisor():
 number=int(input("enter a number "))
 add=0
 for i in range(1,number):
    divisor=number%i
    if divisor==0 and i!=number:
     print("The divisor are",i)
     add=add+i

 print("The addition of divisor is",add)
 if add==number:
   print("Its a perfect number")
 else:
   print("The given number is not a perfect number")
divisor()
