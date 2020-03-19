# 1.5
# One Away: There are three types of edits than can be performed on strings:
# insert a character, remove a character, or replace a character.
# Given two strings, write a function to check if they are one edit (or zero edits) away.
# The palindrome does not need to be limited to just dictionary words.

# using an additional data structure - O(n) time, O(1) space
def one_away(str1, str2):    
    if ((len(str1) > len(str2) + 1) or (len(str1) < len(str2) - 1)):
        return False
    
    if (str1 == str2):
        return True

    if ((len(str1) == len(str2) + 1) or (len(str1) == len(str2))):
        bigger_str = str1
        smaller_str = str2
    else:
        bigger_str = str2
        smaller_str = str1

    one_different = False
    j = 0

    for i in range(len(smaller_str)):
        if (bigger_str[j] != smaller_str[i]):
            if (one_different):
                return False
            one_different = True
            if (len(bigger_str) != len(smaller_str)):
                j += 1
        j += 1
    
    return True
 
assert(one_away("hello", "big world") == False)
assert(one_away("hello", "hello") == True)
assert(one_away("pale", "bake") == False)
assert(one_away("pale", "bale") == True)
assert(one_away("pale", "ple") == True)
assert(one_away("pales", "pale") == True)
assert(one_away("ple", "pale") == True)
assert(one_away("pale", "pales") == True)

print("Passed.")