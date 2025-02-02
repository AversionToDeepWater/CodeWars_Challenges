"""
Write two functions that convert a roman numeral to and from an integer value. Multiple roman numeral values will
be tested for each function.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit
and skipping any digit with a value of zero. In Roman numerals:

1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC
2008 is written as 2000=MM, 8=VIII; or MMVIII
1666 uses each Roman symbol in descending order: MDCLXVI.
Input range : 1 <= n < 4000

In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").

EXAMPLES
to roman:
2000 -> "MM"
1666 -> "MDCLXVI"
  86 -> "LXXXVI"
   1 -> "I"

from roman:
"MM"      -> 2000
"MDCLXVI" -> 1666
"LXXXVI"  ->   86
"I"       ->    1

HELP
+--------+-------+
| Symbol | Value |
+--------+-------+
|    M   |  1000 |
|   CM   |   900 |
|    D   |   500 |
|   CD   |   400 |
|    C   |   100 |
|   XC   |    90 |
|    L   |    50 |
|   XL   |    40 |
|    X   |    10 |
|   IX   |     9 |
|    V   |     5 |
|   IV   |     4 |
|    I   |     1 |
+--------+-------+


"""

class RomanNumerals:
    num = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    sym = ["I", "IV","V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]

    i = 12 #this means that the code will loop from the largest num and sym (i.e., index 12)
    # this ensures that the algorithm will traverse the list from largest to smallest
    @staticmethod
    def to_roman(val : int) -> str:
        # roman = ''
        # if val >= 1000:
        #     mod = val % 1000
        #     for i in range(mod):
        #         roman += 'M'
        # elif

        return ''

    @staticmethod
    def from_roman(roman_num : str) -> int:
        return 0