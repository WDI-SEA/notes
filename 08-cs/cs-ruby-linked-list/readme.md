#Linked List Challenge

For this exercise, we will implement a simple version of a singly linked list.

A linked list a data structure, used for fast and memory efficient insertions and deletions.

It does this because items in a linked list are connected by reference to each other, vs being contained inside of 1 object.


#### Singly Linked List

A singly linked list each node in the list stores the contents of the node and a pointer or reference to the next node in the list.

![http://www.lisha.ufsc.br/teaching/sce/ine6511-2003-2/work/gp/lists_files/image001.gif](http://www.lisha.ufsc.br/teaching/sce/ine6511-2003-2/work/gp/lists_files/image001.gif)


##Getting Started
We will be creating 2 data structures for this.

1. Start by creating a `Node` Class. This will be initialized with a value. We will have attributes for both this value (`item`)and place holder for pointing to another object(`next`).

2. Create a `LinkedList` class. This class will initialize with two values. `@head` and `@tail`. Each of these will initially be `nil`

3. Create a method on `LinkedList` class called `insert_front`. The challenge is to add an item to this list. This can be done by creating a new `Node`, and changing the `next` value to point to the item in the list.
