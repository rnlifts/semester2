#creating function named 'number to find the sum bewtween two given integer
def number(low_number, high_number):
    #checking if both value are integer or not and returning an error message if its not
    if not isinstance(low_number, int) or not isinstance(high_number, int):
        return "Invalid, Please eneter a integer"
    #checking if lowe no. is greater than high number or not and returning error message if it is.
    elif high_number < low_number:
        return "Invalid,number must be higher than lower number"
    elif low_number == high_number:
        return low_number
    #adding current low number to the sum of the rest of the number
    else:
        return low_number + number(low_number+1, high_number)
#taking input from the user 
low_number = input("Enter a low number: ")
high_number = input("Enter a high number: ")
#if the number is not integer it will raise value error exception.
try:
    low_number = int(low_number)
    high_number = int(high_number)
except ValueError:
    print("Invalid, Please eneter a integer")
else:
    #calling the number function to calculate the sum
    output = number(low_number, high_number)
    if isinstance(output, str):
        print(output)
    else:
        print(f"The sum of integers between {low_number} and {high_number} is {output}.")
