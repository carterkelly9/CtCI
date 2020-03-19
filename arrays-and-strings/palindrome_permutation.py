# 1.4
# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards as backwards.
# A permutation is a rearrangement of letters.
# The palindrome does not need to be limited to just dictionary words.

# using an additional data structure - O(n) time, O(1) space
def palindrome_permutation(input_str):    
    ascii_dict = {chr(i): 0 for i in range(129)}
    
    for i in input_str:
        ascii_dict[i] += 1
    
    one_odd = False

    for i in ascii_dict.keys():
        if (ascii_dict[i] % 2 == 1):
            if (one_odd):
                return False
            one_odd = True
    
    return True
 
assert(palindrome_permutation("hello") == False)
assert(palindrome_permutation("even") == False)
assert(palindrome_permutation("odd") == True)
assert(palindrome_permutation("evenvn") == True)

print("Passed.")