"Write a function that accepts a positive integer and determines if it is a prime number."
"The function should return true, if it is a prime number or false if it isn’t.)"




def task2(pos_num):  # defining a function
    pos_num = int(input("Enter a number"))  # convert input to an integar val
    for i in range(2, pos_num):  # for each number from 2 to input
        if pos_num % i == 0:  # if input mod (2 to (input-1)) = 0, false
            print("False")
            break  # break once condition is true
    else:
        print("True")


task2(pos_num)
