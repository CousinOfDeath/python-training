import calendar


# 1. Write a Python function is_even that takes as input the parameter number (an integer)
# and returns True if number is even
# and False if number is odd. Hint: Apply the remainder operator to n (i.e., number % 2) and compare to zero.


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


print(f"is_even(4) {is_even(4)}")
print(f"is_even(3) {is_even(3)}")
print("")


# 2. Write a Python function is_lunchtime that takes as input the parameters
# hour (an integer in the range [1, 12][1, 12]) and is_am (a Boolean "flag" that
# represents whether the hour is before noon). The function should return True when the
# input corresponds to 11am or 12pm (noon) and False otherwise.


def is_lunchtime(hour, is_am):
    if hour == 11 and is_am or hour == 12 and not is_am:
        return True
    else:
        return False


print(f"is_lunchtime(9, True) {is_lunchtime(9, True)}")
print(f"is_lunchtime(11, True) {is_lunchtime(11, True)}")
print(f"is_lunchtime(11, False) {is_lunchtime(11, False)}")
print(f"is_lunchtime(12, False) {is_lunchtime(12, False)}")
print(f"is_lunchtime(12, True) {is_lunchtime(12, True)}")
print("")


# 3. Write a Python function is_leap_year that take as input the parameter year and returns
# True if year (an integer) is a leap year according to the Gregorian calendar and False otherwise.

def is_leap_year(year):
    if calendar.isleap(year):
        return True
    else:
        return False


print(f"is_leap_year(2019) {is_leap_year(2019)}")
print(f"is_leap_year(2019) {is_leap_year(2020)}")
print(f"is_leap_year(2019) {is_leap_year(2021)}")
print(f"is_leap_year(2019) {is_leap_year(2022)}")
print(f"is_leap_year(2019) {is_leap_year(2023)}")
print(f"is_leap_year(2019) {is_leap_year(20124)}")
print("")


# 4. Write a Python function name_and_age that take as input the parameters name (a string)
# and age (a number) and returns a string of the form '% is % years old.' where the percents
# are the string forms of name and age. The function should include an error check for the case
# when age is less than zero. In this case, the function should return the string 'Error: Invalid age'.

def name_and_age(name, age):
    if age < 0:
        return "Error: Invalid age."
    else:
        return f"{name} is {age} years old."


output = name_and_age("John", 30)
print(f"name_and_age(\"John\", 30) {output}")
output = name_and_age("Pete", 0)
print(f"name_and_age(\"Pete\", 0) {output}")
output = name_and_age("Unborn", -1)
print(f"name_and_age(\"Unborn\", -1) {output}")
print("")


# 5. Write a Python function print_digits that takes an integer number in the range [0,100)[0,100)
# and prints the message 'The tens digit is %, and the ones digit is %.'
# where the percents should be replaced with the appropriate values. The function should
# include an error check for the case when number is negative or greater than or equal to 100.
# In those cases, the function should instead print 'Error: Input is not a two-digit number.'.


def print_digits(number):
    if 9 < number < 100:
        return f"The tens digit is {str(number)[:1]}, and the ones digit is {str(number)[1:]}."
    else:
        return "Error: Input is not a two-digit number."


print(f"print_digits(9) {print_digits(9)}")
print(f"print_digits(10) {print_digits(10)}")
print(f"print_digits(99) {print_digits(99)}")
print(f"print_digits(100) {print_digits(100)}")


# 6. Pig Latin is a language game that involves altering words via a simple set of rules.
# Write a Python function pig_latin that takes a string word and applies the following rules to generate
# a new word in Pig Latin. If the first letter in word is a consonant, append the consonant plus 'ay' to the end
# of the remainder of the word. For example, pig_latin('pig') would return 'igpay'. If the first letter in word
# is a vowel, append 'way' to the end of the word. For example, pig_latin('omelet') returns 'omeletway'.
# You can assume that word is in lower case.


# 7. Given numbers a, b, and c, the quadratic equation ax^2 + bx + c = 0 can have zero, one or two real solutions
# (i.e; values for x that satisfy the equation). The quadratic formula x_1 = -b+sqrt(d) / 2a, x_2 = -b-sqrt(d) / 2a
# can be used to compute these solutions, where d = b^2 - 4ac, the discriminant associated with the equation.
# If the discriminant is positive, the equation has two solutions. If the discriminant is zero,
# the equation has one solution.
# Finally, if the discriminant is negative, the equation has no solutions. Write a
# Python function get_smaller_root that takes an input the numbers a, b and c and returns the smaller
# solution to this equation if one exists. If the equation has no real solutions, print the message
# 'Error: No real solutions.' and simply return.


