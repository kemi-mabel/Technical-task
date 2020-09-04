"""Write a function that accepts an array of positive integers
and returns an array of all prime numbers from the given array. ."""


def task3():
    number_list = []
    n = int(input("Enter the list size : "))

    for i in range(0, n):
        print("Enter number at index", i, ":")
        number = int(input())
        number_list.append(number)

    prime_numbers = []

    for e_number in number_list:  # for each number in the list
        for i in range(2, e_number):  # for each number between the range of 2 to that number
            if e_number % i == 0:  # if number/2......  = 0 stop the loop
                break
        else:
            prime_numbers.append(e_number) # add the number to prime number list
    print(prime_numbers)


task3()
