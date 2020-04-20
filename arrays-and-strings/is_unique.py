# 1.1
# Is Unique: Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

# Brute-force Algorithm
# O(n^2) time - nested for loop
# O(1) space - no additional space is used
def is_unique(input_str):
    # check that the input string length does not exceed the max number of unique characters
    if (len(input_str) > 128):
        return False

    # for each character in the string, iterate through the rest of the string to check for duplicates
    for i in range(len(input_str)):
        for j in range(i + 1, len(input_str)):
            if input_str[i] == input_str[j]:
                return False

    return True

# Pre-Sort Algorithm
# O(nlogn) time - minimum sort time
# O(1) or more space - no additional space is explicitly used, but the built-in sorting algorithm might use some
def is_unique2(input_str):
    # check that the input string length does not exceed the max number of unique characters
    if (len(input_str) > 128):
        return False

    # pre-sort the string using some nlogn sort
    sorted_str = sorted(input_str)

    # for every character in the string, check if the following character is itself
    for i in range(len(sorted_str) - 1):
        if sorted_str[i] == sorted_str[i + 1]:
            return False

    return True

# Buffer Algorithm
# O(n) time
# O(1) space
def is_unique3(input_str):
    # check that the input string length does not exceed the max number of unique characters
    if (len(input_str) > 128):
        return False

    # create a bool ASCII dictionary
    ascii_dict = {chr(i): False for i in range(129)}

    # for every character in the string, check the ASCII dictionary to see whether or not it is unique
    for i in range(len(input_str)):
        if ascii_dict[input_str[i]]:
            return False
        ascii_dict[input_str[i]] = True
    
    return True