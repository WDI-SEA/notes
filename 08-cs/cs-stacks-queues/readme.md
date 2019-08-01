# Stacks and Queues

## Objectives

* Describe arrays in the context of lower-level languages* (C, C++)
* Memorize the acronyms LIFO and FIFO and how they apply to stacks and queues
* Use data structures to implement stacks and queues

*Note: what we mean here is a high-level language that required you to know a lot about what was going on under the hood - not assembly or a similarly low-level language

## Memory and Arrays

So far, we've used arrays in JavaScript, which act as flexible containers for storing data - like a bag of effectively infinite holding. However, arrays in many lower-level languages* do not act like this. They are fixed in length, and we need to explicitly define the size on creation. If we need to a seemingly simple task, like adding a new element, it's time to create an entirely new array of size + 1, copy the old array over, and then deallocate the other array. The other option is to create an array bigger than you need and then you may or may not use all of it. Neither are attractive options. Many times people will combine these two for a bit of middle ground.

To understand why this is the case, let's look at how memory is stored in a computer.

![Memory](http://www.bernstein-plus-sons.com/.dowling/Prog_Lang_Module/images/lots.jpg)

Memory is stored in a block-like fashion, similar to city blocks. Each block has buildings with "addresses", and each block has a fixed length that can't be changed unless destroyed.

Memory in a computer is similar. When we allocate memory, we allocate "blocks". Each block has a fixed size, generally enough to store the type of data we're using. Each block has an address. And note that since the blocks are fixed and uniform, we can only have arrays of a specific data type in C++ and Java (no combining strings and integers in the same array).

### Does JavaScript do this?

JavaScript also allocates arrays as blocks of memory. However, since there's lots of flexibility, there is additional overhead in JavaScript, when it comes to **allocation** and **deallocation**. [This MDN article](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Memory_Management) is a great resource that goes into this in-depth.

## Stack

![Stack](https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Data_stack.svg/2000px-Data_stack.svg.png)

A **Stack** is an array-like structure. You can think of it as a vertical stack with elements piled on top of each other. It has only two operations built into it:

* **push**: This function adds the argument passed in to the top of the stack.
* **pop**: This function removes the top element from the stack and returns it.

**Note:** You may recall that these two methods exist on any JavaScript array. They originated from the Stack data struct but because an array and a stack are so close structure-wise, JavaScript decided to build those onto its Array so you could use them as stacks.

That's it! There is only one end of the stack that we ever do anything with: the top. Because of this, we call it a `Last In, First Out` data structure, or `LIFO`. If you want a real world example, think of the trays or plates in the wells at a buffet. You can only ever place new trays or plates on the top and if you take one, it can only be the top one that you take.

### Practical Applications for Stacks

What is this good for, apart from simulating a buffet line? It turns out that stacks are fantastic at keeping track of when things start and stop and what happens in between. The relationship of the items in our stack is very similar to how elements are nested in HTML tags, or how function calls in recursive algorithms nest inside each other. Because of this, many programming language compilers and interpreters use stacks for parsing language syntax, specifically for detecting when you open a code block and then when that code block is closed. We call this "bracket matching" and it is probably one of the biggest use cases for stacks. But, of course, you can use a stack for anything where new things must be dealt with before older things can be resolved:

* Bracket matching
* Undo/redo operations
* [Tower of Hanoi](https://en.wikipedia.org/wiki/Tower_of_Hanoi)

## Queue

A **queue** is another type of container generally implemented with a linked list, but can be implemented with arrays in JavaScript and Python. Items are only added to the end of a queue, and only removed from the beginning of the queue. This is a FIFO (first in, first out) procedure.

![Queue](https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Data_Queue.svg/300px-Data_Queue.svg.png)

The queue is a **first in, first out** (or FIFO) data structure which means that the first element added to the queue will be the first one removed and processed. It implements only two functions:

* **enqueue**: This function works like `push`. It takes one parameter and it inserts it into the queue in the last place position.
* **dequeue**: This one works like `pop`. It takes no parameters. It removes and returns the element in the first place position.

While these two methods don't exist in our JavaScript arrays, we can use others to affect the same result:

* **push** will add on to the end and **shift** will remove from the front
* Or you could go the reverse direction with **unshift** and **pop**

### Practical Applications for Queues

It's much easier to think of what a queue would be used for. In any situation where you must process data items in the order they came in, a queue is the perfect solution. It is used in event systems like in our web apps. You may also have heard of a print queue that documents go into to wait their turn to be printed. This is the same sort of structure. It keeps the data organized so that no matter how many new ones come in or how long each one takes to process, they will always be done in the order they came in.

* Representing a line
* Buffers for print jobs
* Web event processing
