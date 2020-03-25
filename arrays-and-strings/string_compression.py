# 1.6
# String Compression: Implement a method to perform basic string compression using the counts of repeated characters.
# For example, the string aabcccccaaa would become a2b1c5a3.
# If the "compressed" string would not become smaller than the original string, your method should return the original string.
# You can assume the string has only uppercase and lowercase letters (a - z).

# using an additional data structure - O(n) time, O(n) space
def string_compression(input_str):
    compressed_str = []
    char_count = 0

    for i in range(len(input_str)):
        char_count += 1

        if (i + 1 >= len(input_str) or input_str[i + 1] != input_str[i]):
            compressed_str += input_str[i]
            compressed_str += str(char_count)
            char_count = 0

    return ''.join(compressed_str) if len(compressed_str) < len(input_str) else input_str

assert(string_compression("aabcccccaaa") == "a2b1c5a3")
assert(string_compression("abc") == "abc")

print("Passed.")