# Hash Tables

Also referred to as _hash maps_ or even simply just hashes.

## What is a hash table?

We've been using a very hash-table-like structure in both JavaScript and Python. The JavaScript `object` and the Python `dictionary` are both implementations of a hash table or hash map. **It is an array-like data structure in which every element is associated with a key.**

In JavaScript, everything is a hash table. MongoDB is essentially a distributed hash table. hash tables are used constantly in computer science, and provide
a flexible and fast way of storing and retrieving data. Why is this? To find out, we have to look at how a hash table is implemented.

A hash table always contains a hashing function that will take the key, hash and mod (%) it, and turn it into an internal index into which we will insert our item. When we want to access what we have inserted, we use the key and the hash table translates it into the index so it knows where to find the item we want.

## Data structure basics

Data structures are just collections of information, and there are four operations that you'll need to do with any data structure:

* Insertion - The data structure would be useless if you couldn't add things to it.
* Search - Finding an item when you don't initially know where it is
* Access - Accessing an item when you know it's location
* Deletion - You should be able to remove things from a data structure when you need to

In the most basic possible data structure, an unorganized array, insertion is easy as long as you store the length of the array. Just add something to the end. Lookup is hard. In the worst case, you go through
the entire array, and only find what you're looking for at the end. Deletion is similarly worse. You might have to go through the entire array, and then if you remove an item, you either leave gaps in your array,
which means degradation in performance over time, or you double your workload by resizing the array after you've made the deletion.

Things are slightly better in an ordered array, but the sort step, and the search step still aren't guaranteed to be fast, depending on the size. Hash Tables solve for many of these problems.

## Use Cases

Well, what have you been using objects and dictionaries for? We use them mostly in the same way as arrays but they are better for when we want a way to access the elements other than using an integer index. Arrays have inherent ordering; objects, dictionaries, and hash tables do not. Also, knowing the key always gives us constant-time search in addition to constant-time insertion and deletion - an advantage over arrays!

## Hash Table Concepts

### Sizing

At its heart, a hash table is yet another array. When we make a hash table, we create it with a certain size, just like an array in native languages. Typically, we choose the size to accomodate all the known data we have and then some room for growth. Resizing a hash table is a very involved operation so pick an appropriate number for your app's needs.

### Hashing Function

Arrays use integers as indices but we want to use keys, so we must find a way to translate a key into an index in our hash table's internal array. To do this we use a **hashing function**, a hallmark feature of hash tables. This function takes a key, hashes it (a type of mathematical encryption of sorts), and moduluses the result by the number of slots in the array. This computation will give us some index within the bounds of the array. By using the key and the hashing function, we can *access* elements in the hash table with the same efficiency as arrays but can *search* them even faster!

### Selecting keys

To get the keys to hash, we select some sort of key from the item we want to store in the table. For example, if we were storing users, we might use the email address as the key since it should be unique within our application. Database objects could use their `id` column values as the key since those are also generated to be unique. The more unique, the better!

### Hashing

Once we have the key, we hash it using one of the many hash libraries out there. In Python, we will be using a library called `hashlib` which will generate very good, consistent hashes from our keys. It generates a long identifier of alphanumeric characters. We take this long identifier, convert it to an integer, and compute the modulus with the number of slots in the hash table. This generates an index and we insert the item into that index.

## Collisions

In a perfect world, we'll always be able to hash our keys to perfectly unique hashes that map perfectly to unused indices in our hash table. Yeah, right! Even with the best hashing algorithms and key selection, given enough time and data, collisions will happen.

A collision occurs when an item is hashed to be in a slot already occupied by another item. We will learn of a couple of simple strategies to deal with this, however a collision resolution strategy can still break down under the increased collisions that come with a poor hashing function or poor key selection.

Imagine if we generated hashes based on the first letter of someone's name. Obviously there would be a ton of collisions as there are many names that start with the same letter. Even after hashing it and modding it we would still have a crushing number of collisions to deal with. The same would be true if we had an inadequate amount of space. Since extra steps must be taken to deal with a collision, if we get enough of them we lose the efficiency of the structure. Choosing a good hashing function, a good initial size, and a good collision resolution strategy are crucial for writing a good hash table.

## Collision Resolution Strategies

### Open Addressing or Probing

Probing is, quite simply, looking sequentially (or sometimes quadratically) for the next available open address. In linear probing, the algorithm simply iterates over the table until it finds an empty slot and then puts the item there. This can lead to clusters of elements forming which can reduce preformance if they get big enough so sometimes we look for open slots **quadratically**, a method where we increase the gap to the square of the next integer (e.g. first we look 1 slot ahead, then 4 (2*2), then 9 (3*3), then 16 (4*4), and so on.) This spreads out inserts over the table and helps maintain performance.

This means that our _search_ strategy now needs to involve locating an initial slot, checking the item there to see if it is the correct one, and if not, iterating over the next few until it finds an item that has a matching key.

This does definitely extend the lookups for some items but if we ammortize all the lookups we find that our average search time is far closer to constant than it would be in an array.

### Closed Addressing or Chaining

In the chaining strategy, each slot in the table is actually a bucket that holds multiple items and when a collision occurs, we simply add the new item as a new element in the bucket contained in that slot in the hash table. This makes insertions a bit faster than in the probing strategy since we don't need to iterate over an arbitrary number of elements to find an empty slot. Typically the bucket is implemented with a linked list but we will use a list (array) for simplicity. This will be our strategy.

## Hash Table Operations

The basic operations we will need are `search`, `insert`, and `remove`.

### search(key)

1. Pass in the key as a parameter
2. Hash the key to find the index
3. Look in the array at that index
4. Find the item in that bucket and return it

### insert(key, val)

1. Pass in the key and the value to be stored
2. Hash the key to get the index
3. Add the item to the end of the bucket at that index

### remove(key)

1. Pass in the key as a parameter
2. Hash the key to find the index
3. Look in the array at that index
4. Find the item in that bucket and delete it

## Test It!

"If you haven't tested it, it doesn't work."

Make sure you test every operation in every edge case you can think of. With data structures, it's good to test how functions behave when the structure contains:

* Zero items (edge case)
* One item (edge case)
* Many items (normal usage)
* Near capacity (edge case)
* Full cpacity (edge case)

Typically our code works fine in the "normal usage" cases when we first write it. It's the edge cases that usually cause problems so make sure you thoroughly test.

## Uses

MongoDB is essentially a distributed hashmap. Notice how every item you insert gets a big ugly string as an ID? That's basically a big number that's generated by it's internal hashing function. The
advantage is that we can split our hash buckets over a number of servers to distribute load more evenly, and make our system more fault-tolerant.

Everything is a hashmap in JavaScript. This makes it easy to add arbitrary values to objects without worrying about organization.

## Additional Resources

* [Basic Data Structures: Hash Tables](http://goodmath.scientopia.org/2013/10/20/basic-data-structures-hash-tables/)
* [Wikipedia's entry on Hash Tables](https://en.wikipedia.org/wiki/Hash_table)
* [Stack Overflow question on Hash Tables](http://stackoverflow.com/questions/730620/how-does-a-hash-table-work)
* [Generate a hash from a string in JavaScript](http://stackoverflow.com/questions/7616461/generate-a-hash-from-string-in-javascript-jquerya)