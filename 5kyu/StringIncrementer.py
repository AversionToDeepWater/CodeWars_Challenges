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

foobar099 -> foobar100

fo99obar99 -> fo99obar100

Attention: If the number has leading zeros the amount of digits should be considered.
'''

# I think I should try and use re library bc that seems to make the most sense
# def increment_string(string):
#     # start at one as we want to increase the number at the end by 1, or add 1 at the end if there isn't a number at the end of the text
#     numbers = []
#     text = ""
#     for i in string: # this only adds one to the first digit it encounters in the string
#         if i.isdigit() or string.endswith(i, i.isdigit()):
#             numbers.append(i)
#         else:
#             text += i
#
#     # string = text + str(numbers)
#
#     return numbers








##### TESTING ####
# example1 = "foo1"
# example2 = "foobar"
# example3 = "foobar099"
# example4 = "fo99obar99"
#
# # test_output1 = increment_string(example1)
# # test_output2 = increment_string(example2)
# test_output3 = increment_string(example3)
# test_output4 = increment_string(example4)
# # print(test_output1)
# # print(test_output2)
# print(test_output4)




#Articles I looked at

# https://www.w3schools.com/python/python_regex.asp
# https://www.geeksforgeeks.org/python-splitting-text-and-number-in-string/

# Code below only works if there is a space between the word and the numbers in the string
# i.e., can split 12 in 'foo 12' but NOT in 'foo12'
# example = 'foo12'
# num = [int(n) for n in example.split() if n.isdigit()]
#
# print(num)

