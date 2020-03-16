# 1.3
# URLify: Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end to hold the additional characters,
# and that you are given the "true" length of the string.

# using an additional data structure - O(n) time, O(n) space
def URLify(input_str, n):
    url_string = ""

    for char in input_str:
        if (char == ' '):
            url_string += "%20"
        else:
            url_string += char

    return url_string

assert(URLify("Mr John Smith", 13) == "Mr%20John%20Smith")

# in-place - O(n) time, O(1) space
def URLify2(input_str, n):
    space_count = 0

    for i in range(n - 1, -1, -1):
        if (input_str[i] == ' '):
            space_count += 1

    shift = space_count * 2
    
    for i in range(n - 1, -1, -1):
        if (input_str[i] == ' '):
            input_str[i + shift] = '0'
            input_str[i + shift - 1] = '2'
            input_str[i + shift - 2] = '%'
            shift -= 2
        else:
            input_str[i + shift] = input_str[i]

    return input_str

# because Python strings are immutable, a list is inputted instead of a string
assert(URLify2(list("Mr John Smith    "), 13) == list("Mr%20John%20Smith")) 

print("Passed.")