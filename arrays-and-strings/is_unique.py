# 1.1
# Is Unique: Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

# brute-force algorithm - O(n^2) time, O(1) space
def is_unique(str):
    if (len(str) > 128): # max number of unique characters
        return False

    for i in range(len(str) - 1):
        for j in range(i + 1, len(str) - 1):
            if str[i] == str[j]:
                return False

    return True

assert(is_unique("hello") == False)
assert(is_unique("world") == True)

# pre-sort string - O(nlogn), O(1) or more space
def is_unique2(str):
    if (len(str) > 128): # max number of unique characters
        return False

    sorted_str = sorted(str) # some nlogn sort

    for i in range(len(sorted_str) - 1):
        if sorted_str[i] == sorted_str[i + 1]:
            return False

    return True

assert(is_unique2("hello") == False)
assert(is_unique2("world") == True)

# using an additional data structure - O(n) time, O(1) space
def is_unique3(str):
    if (len(str) > 128): # max number of unique characters
        return False

    ascii_dict = {chr(i): False for i in range(129)}

    for i in range (0, len(str) - 1):
        if ascii_dict[str[i]]:
            return False
        ascii_dict[str[i]] = True
    
    return True

assert(is_unique3("hello") == False)
assert(is_unique3("world") == True)

print("Passed.")