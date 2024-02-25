def checkNeon (x) :
    # storing the square of x
    sq = x * x
    # calculating the sum of digits
    # of sq
    sum_digits = 0
    while (sq != 0) :
        sum_digits = sum_digits + sq % 10
        sq = sq // 10
     
    return (sum_digits == x)

while True:
    try:
        user_input = int(input("Enter a number: "))
        if (checkNeon(user_input)) :
            print("The number is a neon number.")
        else :
            print("The number is not a neon number.")
        print("To terminate the program, press Ctrl + C.")
    except ValueError:
        print("Please enter a valid integer.")

