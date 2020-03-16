# 1.1
# Is Unique: Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

# brute-force algorithm - O(n^2) time, O(1) space
def is_unique(input_str):
    if (len(input_str) > 128): # max number of unique characters
        return False

    for i in range(len(input_str)):
        for j in range(i + 1, len(input_str)):
            if input_str[i] == input_str[j]:
                return False

    return True

assert(is_unique("hello") == False)
assert(is_unique("world") == True)

# pre-sort string - O(nlogn) time, O(1) or more space
def is_unique2(input_str):
    if (len(input_str) > 128): # max number of unique characters
        return False

    sorted_str = sorted(input_str) # some nlogn sort

    for i in range(len(sorted_str) - 1):
        if sorted_str[i] == sorted_str[i + 1]:
            return False

    return True

assert(is_unique2("hello") == False)
assert(is_unique2("world") == True)

# using an additional data structure - O(n) time, O(1) space
def is_unique3(input_str):
    if (len(input_str) > 128): # max number of unique characters
        return False

    ascii_dict = {chr(i): False for i in range(129)}

    for i in range(len(input_str)):
        if ascii_dict[input_str[i]]:
            return False
        ascii_dict[input_str[i]] = True
    
    return True

assert(is_unique3("hello") == False)
assert(is_unique3("world") == True)

print("Passed.")