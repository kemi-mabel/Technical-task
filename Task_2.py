"Write a function that accepts a positive integer and determines if it is a prime number."
"The function should return true, if it is a prime number or false if it isn’t.)"




def task2(pos_num):
    pos_num = int(input("Enter a number"))
    for i in range(2, pos_num):
        if pos_num % i == 0:
            print("False")
            break
    else:
        print("True")


task2(pos_num)
