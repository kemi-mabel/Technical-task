"""Write a function that takes an array of positive integers
and calculates the standard deviation of the numbers.
The function should return the standard deviation."""

# standard_dev ={\sqrt {\frac {\sum(x_{i}-{\mu})^{2}}{N}}}
def stand_dev(array, array_size):
    average = sum(array) / array_size # add all numbers and divide by size of array
    n_a = []
    for number in array:  # for each number in array calculate calc
        calc = (number - average) ** 2
        n_a.append(calc)
    standard_dev = (sum(n_a) / array_size) ** 0.5
    print(standard_dev)  # printing standard deviation


numbers = [9, 2, 5, 4, 12, 7, 8, 11, 9, 3, 7, 4, 12, 5, 4, 10, 9, 6, 9, 4]
size = 20
stand_dev(numbers, size)
