# 1.2
# Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.

# pre-sort string - O(nlogn), O(1) or more space
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

# efficient algorithm - O(n), O(1) space
def check_permutation2(str1, str2):
    if (len(str1) != len(str2)):  # permutations must have an equal number of characters
        return False
    
    str1_dict = {i: 0 for i in str1}
    
    for i in str1:
        str1_dict[i] += 1
    
    for i in str2:
        if i in str1_dict.keys():
            str1_dict[i] -= 1
            if (str1_dict[i] < 0):
                return False
        else:
            return False
    
    return True

assert(check_permutation2("hello", "hollow") == False)
assert(check_permutation2("hello", "world") == False)
assert(check_permutation2("silent", "listen") == True)

print("Passed.")