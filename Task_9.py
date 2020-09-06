"""Write a function that takes a string and determines if the string is a palindrome.
A palindrome is a word, number, phrase, or other sequence of characters
which reads the same backward as forward, such as madam, race car.
The function should return “Yes” if the word is a palindrome and “No” if it isn’t.
You are not to use the programming language’s existing function or method, if any."""

string = input("Please enter your own String : ")  # input the string
reverse = ""  # create an empty string

for i in string:  # for each letter in the string(input)
    reverse = i + reverse  # keep adding i to reverse(hand: h, a+h, n+ah, d + nah)
if string == reverse:  # comparing string to palindrome
    print("Yes, This is a Palindrome")
else:
    print("No, this is Not a Palindrome")
