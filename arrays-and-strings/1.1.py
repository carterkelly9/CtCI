# 1.1
# Is Unique: Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

# brute-force algorithm - O(n^2)
def check_unique(some_string):
    for i in range(0, len(some_string) - 1):
        for j in range(i + 1, len(some_string) - 1):
            if some_string[i] == some_string[j]:
                return False

    return True

# test
assert(check_unique("hello") == False)
assert(check_unique("world") == True)

print("hello - " + str(check_unique("hello")))
print("world - " + str(check_unique("world")))

# pre-sort string - O(nlogn)
def check_unique2 (some_string):
    sorted_string = sorted(some_string) # some nlogn sort

    for i in range(0, len(sorted_string) - 1):
        if sorted_string[i] == sorted_string[i + 1]:
            return False

    return True

assert(check_unique2("hello") == False)
assert(check_unique2("world") == True)

print("hello - " + str(check_unique2("hello")))
print("world - " + str(check_unique2("world")))

# using an additional data structure - O(n)