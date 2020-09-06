"""Write a function that takes a string. The function should calculate the character in the string
with the most occurrences and return that character. If more than one character has the most occurrence,
return those characters as an array.
Example
Input: “afhuusnimr443o0sggg”
Output: “g”"""


def most_occur(string):
    counts = dict()
    # adding each letter to the dictionary and populating their count
    for letter in string:
        if letter in counts:
            counts[letter] = countsletter] + 1
        else:
            counts[letter] = 1
    print(counts)
    # Find item with Max Value in Dictionary
    max_value = max(counts.items(), key=lambda x: x[1]) # max(iterable, *[, key, default])
    print('Maximum Value in Dictionary : ', max_value[1])
    list_Of_Keys = list()
    # Iterate over all the items in dictionary to find keys with max value
    for key, value in counts.items():
        if value == max_value[1]:
            list_Of_Keys.append(key)
    print('Keys with maximum Value in Dictionary : ', list_Of_Keys)



ppp = "afhuusnimmmr443o0sggg"
most_occur(ppp)



