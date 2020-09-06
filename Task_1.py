"""Write a function that takes an array of positive integers.
The function should calculate the sum of all even and
odd integers and return an array containing the sums.
The first index in the returned array should hold the sum of the even integers
and the second index should hold the sum of the odd integers."""


def task1(num):
    even_sum = 0
    odd_sum = 0
    for i in num:  # for each nunmer in array
        if i % 2 == 0:  # comparing i modulus to 0
            even_sum += i
        else:
            odd_sum += i
    return [even_sum, odd_sum]


integar = [3, 5, 6, 9, 4]
array = task1(integar)
print(array)


