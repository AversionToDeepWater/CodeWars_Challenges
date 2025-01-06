'''
Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.
Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.
'''

def increment_string(string):
    # start at one as we want to increase the number at the end by 1, or add 1 at the end if there isn't a number at the end of the text
    numbers = 1
    text = ""
    for i in string:
        if i.isdigit():
            numbers += int(i)
        else:
            text += i

    string = text + str(numbers)

    return string

example1 = "foo1"
example2 = "foobar"

test_output1 = increment_string(example1)
test_output2 = increment_string(example2)
print(test_output1)
print(test_output2)


#Article I looked at
# https://www.geeksforgeeks.org/python-splitting-text-and-number-in-string/

# Code below only works if there is a space between the word and the numbers in the string
# i.e., can split 12 in 'foo 12' but NOT in 'foo12'
# example = 'foo12'
# num = [int(n) for n in example.split() if n.isdigit()]
#
# print(num)

