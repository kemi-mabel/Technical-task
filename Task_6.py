"""Write a function that takes two parameters, an array and some number.
The function should determine whether any three numbers in the array add up to the number.
If it does, the function should return the numbers as an array. If it doesn’t, the function should return -1.
Example
Input: [1, 2, 3, 4, 5, 6], 6
Output: [1, 2, 3]"""


def find3Numbers(A, arr_size, sum):
    # Fix the first element as A[i]
    for i in range(0, arr_size - 2):
        # Fix the second element as A[j]

        for j in range(i + 1, arr_size - 1):
            # Now look for the third number
            for k in range(j + 1, arr_size):
                if A[i] + A[j] + A[k] == sum:
                    print("Triplet is", A[i], ", ", A[j], ", ", A[k])


    # If we reach here, then no
    # triplet was found
    else:
        print(-1)


A = [1, 4, 45, 5, 10, 2]
sum = 22
arr_size = len(A)
find3Numbers(A, arr_size, sum)
