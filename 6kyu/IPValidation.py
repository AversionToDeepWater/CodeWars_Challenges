'''
Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.

Valid inputs examples:
Examples of valid inputs:
1.2.3.4
123.45.67.89
Invalid input examples:
1.2.3
1.2.3.4.5
123.456.78.90
123.045.067.089
Notes:
Leading zeros (e.g. 01.02.03.04) are considered invalid
Inputs are guaranteed to be a single string


'''
example1 = '123.456.78.90' #should be false
example2 ='123.45.67.89'


def is_valid_ip(string) -> bool:
    # Splits our ip address into a list of strings. Our ip address is split at the '.'
    split_ip = string.split('.')

    #Checks that there are four octets (we should have four items in our list)
    if len(split_ip) != 4:
        return False

    #Make a new list with the first character of each item in split_ip. If any of those are zero ('0' as we are working with strings), return False.
    is_zero = [x[0] for x in split_ip]
    for item in is_zero:
        # 0 by itself would be valid, so check if there are leading zeros
        if len(item) > 1 and item == '0':
            return False

    # Changed to check if a criteria is *not* met, otherwise the first true item it encounters returns True and breaks the loop
    for items in split_ip:
        if not 0 < int(items) < 255:
            return False

    #If it passes all the checks then return True
    return True

test = is_valid_ip(example2)
print(test)


# UNCOMMENT THIS FOR BETTER UNDERSTANDING OF HOW CODE WORKS
# s = example1.split('.')
# print(s) #-> prints list of split string
# y = [x[0] for x in s] #returns first character from each item in list of strings
# print(y)