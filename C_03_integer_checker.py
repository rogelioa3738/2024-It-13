
# checks that user enter an integer
# that is more than 13
while True:

    error = "Please enter and integer that is 13 or more."

    try:
        my_num = int(input("Enter an integer: "))

        # checks that the number is greater than / equal to 13
        if my_num < 13:
            print(error)
        else:
            print("Your number is ", my_num)

    except ValueError:
        print(error)
