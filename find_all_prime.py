lower_value = int(input("Please, Enter Lowest Range Value: "))
upper_value = int(input("Please, Enter Upper Range Value: "))
print("the prime number in the range are: ".capitalize())
for number in range(lower_value,upper_value+1):
    if number > 1: 
        for i in range(2,number):
            if (number % i) == 0:
                break
        else:
            print(number)
