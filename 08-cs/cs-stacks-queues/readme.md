#Stacks and Queues

##Objectives

* Understand arrays in the context of lower-level languages (C++, Java)
* Understand the concepts of LIFO and FIFO and how they apply to stacks and queues
* Use data structures to implement stacks and queues

##Memory and Arrays

So far, we've used arrays in JavaScript, which act as flexible containers for storing data. However, arrays in many lower-level languages (C++, Java) do not act like this. They are fixed in length, and we need to explicitly define the size on creation.

To understand why this is the case, let's look at how memory is stored in a computer.

![Memory](http://www.bernstein-plus-sons.com/.dowling/Prog_Lang_Module/images/lots.jpg)

Memory is stored in a block-like fashion, similar to city blocks. Each block has buildings with "addresses", and each block has a fixed length that can't be changed unless destroyed.

Memory in a computer is similar. When we allocate memory, we allocate "blocks". Each block has a fixed size, generally enough to store the type of data we're using. Each block has an address. And note that since the blocks are fixed and uniform, we can only have arrays of a specific data type in C++ and Java (no combining strings and integers in the same array).

###Does JavaScript do this?

JavaScript also allocates arrays as blocks of memory. However, since there's lots of flexibility, there is additional overhead in JavaScript, when it comes to **allocation** and **deallocation**. [This MDN article](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Memory_Management) is a great resource that goes into this in-depth.

##Stack

Arrays are the foundation for implementing a container called a **stack**. Stacks are special arrays where items can only be added and removed from the end. This is a LIFO (last in, first out) procedure.

![Stack](https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Data_stack.svg/2000px-Data_stack.svg.png)

Stacks are fairly simple to implement in Ruby and JavaScript. All that's needed are `pop` and `push` functions (included in both languages).

###Practical Applications for Stacks

* Bracket matching
* Undo/redo operations
* [Tower of Hanoi](https://en.wikipedia.org/wiki/Tower_of_Hanoi)

##Queue

A **queue** is another type of container generally implemented with a linked list, but can be implemented with arrays in JavaScript and Ruby. Items are only added to the end of a queue, and only removed from the beginning of the queue. This is a FIFO (first in, first out) procedure.

![Queue](https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Data_Queue.svg/300px-Data_Queue.svg.png)

Queues can be implemented with the `push` and `shift` functions in both JavaScript and Ruby.

###Practical Applications for Queues

* Representing a line
* Buffers for print jobs, or other tasks
