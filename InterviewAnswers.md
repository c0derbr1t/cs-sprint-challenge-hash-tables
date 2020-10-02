## Interview Questions

Be prepared to demonstrate your understanding of this week's concepts by answering questions on the following topics. You might prepare by writing down your answers beforehand.

1. Hashing functions
2. Collision resolution
3. Performance of basic hash table operations
4. Load factor
5. Automatic resizing
6. Various use cases for hash tables

We expect you to be able to answer questions in these areas. Your responses contribute to your Sprint Challenge grade.

## Interview Answers

1. Hashing functions take a keyword and turn it into a hard-to-break string. This makes a hash table more secure. It's used for personal information such as passwords.

2. Collision resolution is used when two values map to the same key in a hash table. A collision can be resolved by turning the values into a linked list!

3. Performance of basic hash table operations are mostly O(1)! A lot of operations in Python are O(log n) or O(n). Hash tables make things much more economical!

4. The Load Factor is how much of the hash table is used. For example, this week we used 0.2 and 0.7 (20% and 70%, respectivley) as the boundaries for resizing. This load factor takes into account how much is in the table vs what the capacity is.

5. Automatic resizing uses the load factor. It calculates it upon put (and sometimes delete) to determine if resizing is needed. If it goes beyond the bounds you set, it will run the resizing function.

6. There are so many use cases for hash tables! A hash table is a dictionary. Until now, I haven't made use of dictionaries very much. I like being able to store and look things up. That is such a powerful feature. I also like the sheer amount of data it can handle.