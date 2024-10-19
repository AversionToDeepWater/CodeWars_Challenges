'''
Write a function that accepts a string, and returns the same string with all even indexed characters in each word
upper case, and all odd indexed characters in each word lower cased. The indexing just explained is zero based,
so the zero-ith index is even, therefore that character should be upper case, and you need to start over for each word.

The passed in string will only consist of alphabetical characters and spaces(' ').
Spaces will only be present if there are multiple words. Words will be separated by a single space(' ').

Examples:
"String" => "StRiNg"
"Weird string case" => "WeIrD StRiNg CaSe"

'''

string = "Hello"

def to_weird_case(words:str) -> str:
    len_words = len(words) #no. of characters in words
    separated = words.split(" ") # split string at any white space and give you back string as list

