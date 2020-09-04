"""Write a method to count the number of 3s that appear in all the numbers between 0 and n (inclusive).
 It should return an object containing the count of the number of 3s that appear
 and an array of the numbers that have 3s in them
Example:
Input: 35
Output: { count: 10, numbers: [3, 13, 23, 30, 31, 32, 33, 34, 35] }"""


class Counter3:
    def count3(self):
        count = 0  # number of 3
        numbers_3 = []  # numbers with 3
        all_numbers = []  # list of all numbers from 0 to self
        for number in range(0, self + 1):  # 
            all_numbers.append(str(number))
        for number in all_numbers:
            if "3" in number:
                numbers_3.append(number)
                count += number.count('3')

        print("count: {} numbers:{}".format(count, numbers_3))


Counter3.count3(35)
