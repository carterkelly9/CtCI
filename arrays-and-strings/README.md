# Arrays and Strings

## Review

### Hash Tables

Maps keys to values for highly efficient lookup.  
This example uses an array of linked lists and a hash code function.

To insert a key/value pair:  
1. Compute the key's hash code (int/long)  
2. Map hash code to array index (hash(key) % array_length)  
3. Store in index's linked list  

A linked list is used to avoid collisions -- two different keys could have the same hash code, and two different hash codes could map to the same index.

#### Runtime

_Average case: O(1)_  
Worst case: O(N), where N is the number of keys -- many collisions

### ArrayList & Resizable Arrays

ArrayLists resize as needed.  
Can be implemented by doubling in size every time it gets full.

#### Runtime

_Insertion and access time: O(1)_  
Doubling takes O(n), but happens so rarely that the amortized insertion time is O(1).

### StringBuilder

Resizable array of strings.  
Faster and more efficient than manual concatenations.

## Assumptions

### Character Sets

_ASCII_: 128 characters as 7-bit integers  
_Extended ASCII_: 256 characters as 8-bit integers  
_