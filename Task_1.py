"""Write a function that takes an array of positive integers.
The function should calculate the sum of all even and
odd integers and return an array containing the sums.
The first index in the returned array should hold the sum of the even integers
and the second index should hold the sum of the odd integers."""


def task1(num):  # defining the function
    even_sum = 0  # sum of even numbers
    odd_sum = 0  # sum of odd numbers
    for i in num:  # for each nunmer in array
        if i % 2 == 0:  # checking if it's an even or odd number using modulus
            even_sum += i  # if even add to even_sum
        else:
            odd_sum += i  #if odd add to odd_sum
    return [even_sum, odd_sum]


integar = [3, 5, 6, 9, 4]
array = task1(integar)
print(array)


