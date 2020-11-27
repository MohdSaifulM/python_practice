# Code practice from codewars
# The aim of this exercise to learn the way python.
# May the Python be with you!!!

# Prompt:
# - Write a function called addList that accepts any quantity of numbers as arguments, adds them together and returns the resulting sum.
# - Assume all parameters will be numbers.
# - If called with no arguments, return 0 (zero).
# Examples:
# add(1) //=> 1
# add(1,50,1.23) //=> 52.23
# add(7,-12) //=> -5


def add():
    pass


# Write a function that totals the numbers inside of a list
# Or, subtracts the values if an optional "subtract" boolean is passed in
# this function should take two params one list and a do_subtraction
# by default do_subtraction should be set is set to false
def total():
    pass

# Sum digits
# sum_digits(10)  # returns 1
# sum_digits(101) # returns 2
# sum_digits(-32) # returns 5
def sum_digits(number):
    pass


# iq_test(numbers)
# iq_test('2 4 7 8 10') returns 3 which is the position of the odd number
# print(iq_test("1 2 2") returns 1 as 1 is the odd number


def iq_test(string_data):
    pass


# takes a string and returns the values below
# accum('abcd') returns  A-Bb-Ccc-Dddd
# accum("ZpglnRxqenU") returns Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu
def accum(s):
    pass


# Count the bits
# count_bits(0) returns 0
# count_bits(7) binary for 7 is 111 and the bits are 3 (counting the number of 1's). Answer should be 3.
# count_bits(10) binary for 10 is 1010 and the bits are 2(counting the number of 1). Answer should be 2
def count_bits(n):
    pass


count_bits(0)  # 0
count_bits(7)  # 3
count_bits(10)  # 2


# Likes
# likes([]) # must be "no one likes this"
# likes(["Peter"]) # must be "Peter likes this"
# likes(["Jacob", "Alex"]) # must be "Jacob and Alex like this"
# likes(["Max", "John", "Mark"]) # must be "Max, John and Mark like this"
# likes(["Alex", "Jacob", "Mark", "Max"]) # must be "Alex, Jacob and 2 others like this"
def likes(names):
    #your code here
    pass

# Maximum 69 Number
# Given a positive integer num consisting only of digits 6 and 9.
# Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).
# maximum69Number(9669) -> 9969
# maximum69Number(9996) -> 9999
def maximum69Number(num):
    pass



###--------------------######
# ------Champions ONLY------#
###-------------------#######

# checkPrinter
# checkPrinter(1) -> "one"
# checkPrinter(1000) -> "one thousand"
# checkPrinter(1234) -> "one thousand two hundred thirty four"
# checkPrinter(5432789) -> "five million four hundred thirty two thousand seven hundred eighty nine"

def checkPrinter(value):
    pass

# CountOccurences
# Given string of numbers, return a string of numbers representing the occurences of each number in sequence 
# countOccurences("111") -> 31
# countOccurences("111221") -> 312211
# countOccurences("1113213211") -> 31131211131221
# countOccurences("31131211131221") -> 13211311123113112211

def countOccurences(numbers):
    pass

# CountOccurences Part 2
# Given a number N, generate the string based on the Nth iteration of count and say
# countAndSay(1) -> 1
# countAndSay(2) -> 11
# countAndSay(3) -> 21
# countAndSay(4) -> 1211
# countAndSay(5) -> 111221 
# countAndSay(6) -> 312211
# countAndSay(7) -> 13112221
# countAndSay(8) -> 1113213211
# countAndSay(9) -> 31131211131221
# countAndSay(10) -> 13211311123113112211

def countAndSay(num):
    pass

