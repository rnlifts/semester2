number = [1, 5, 8, 4, 9, 6, 2, 3]

def findingreater():
    greater_num = number[0]
    for i in range(len(number)):
        for j in range(i+1, len(number)):
            if number[i] > number[j]:
                greater_num = number[i]
            else:
                greater_num = number[j]
            print(greater_num)

findingreater()
