# Arrays and Strings

## Hash Tables

Maps keys to values for highly efficient lookup.

This example uses an array of linked lists and a hash code function.

To insert a key/value pair:

1. Compute the key's hash code (int/long)

2. Map hash code to array index (hash(key) % array_length)

3. Store in index's linked list

A linked list is used to avoid collisions -- two different keys could have the same hash code, and two different hash codes could map to the same index.

### Runtime

Average case: O(1)

Worst case: O(N), where N is the number of keys -- many collisions

## ArrayList & Resizable Arrays

ArrayLists resize as needed.

Can be implemented by doubling in size every time it gets full.

### Runtime

Insertion and access time: O(1)

Doubling takes O(n), but happens so rarely that the amortized insertion time is O(1).

## StringBuilder

Resizable array of strings.

Faster and more efficient than manual concatenations.