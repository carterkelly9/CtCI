# 1.2
# Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.

# pre-sort string - O(nlogn) time, O(1) or more space
def check_permutation(str1, str2):
    if (len(str1) != len(str2)):  # permutations must have an equal number of characters
        return False
    
    str1_sorted = sorted(str1) # some nlogn sort
    str2_sorted = sorted(str2) # some nlogn sort

    if (str1_sorted != str2_sorted):
        return False
    
    return True

assert(check_permutation("hello", "hollow") == False)
assert(check_permutation("hello", "world") == False)
assert(check_permutation("silent", "listen") == True)

# efficient algorithm - O(n) time, O(1) space
def check_permutation2(str1, str2):
    if (len(str1) != len(str2)):  # permutations must have an equal number of characters
        return False
    
    ascii_dict = {chr(i): 0 for i in range(129)}
    
    for i in str1:
        ascii_dict[i] += 1
    
    for i in str2:
        if i in ascii_dict.keys():
            ascii_dict[i] -= 1
            if (ascii_dict[i] < 0):
                return False
        else:
            return False
    
    return True

assert(check_permutation2("hello", "hollow") == False)
assert(check_permutation2("hello", "world") == False)
assert(check_permutation2("silent", "listen") == True)

print("Passed.")