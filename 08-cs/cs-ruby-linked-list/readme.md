#Linked List Challenge

For this exercise, we will implement a simple version of a singly linked list. But first, let's learn what a linked list is, and **why you should care.**

##Linked List

A linked list a data structure, used for fast and memory efficient insertions and deletions. Unlike arrays, which are single objects, linked lists contain multiple 'node' objects that are linked together via references.

Linked lists can either be **singly** or **doubly** linked. We'll focus on singly linked lists for now.

#### Singly Linked List

If linked lists are multiple objects linked together, ideally we need a couple different objects.

1. A LinkedList object, which holds **all** of the objects in the list
2. A Node object, which contains the **data** for the element, as well as a **reference** to the next Node in the list.

![http://www.lisha.ufsc.br/teaching/sce/ine6511-2003-2/work/gp/lists_files/image001.gif](http://www.lisha.ufsc.br/teaching/sce/ine6511-2003-2/work/gp/lists_files/image001.gif)


## Getting Started

The best way to understand how linked lists work is to make one! Let's do so in Ruby. Here's the process.

1. Start by creating a `Node` Class. We will have attributes to represent the data (let's call this `data`) and the reference to the next Node (let's call this `next`).

2. Create a `LinkedList` class. This class will have one value `@head`. Initialize this to `nil` for now. We have an empty list!

3. Now for incorporating the two classes together. Create a method on the `LinkedList` class called `insert_node`. The challenge is to add an item to this list. This can be done by creating a new `Node`, then doing the following:

* If the `@head` is `nil`, set the `@head` to the newly created `Node`. This newly created `Node` doesn't have a `next` reference, because it's the only item left!
* If the `@head` is a `Node`, then we have some items in our list. But we want to insert the node to the end of the list, ideally. This can be done by taking a look at `@head`
  * If `@head.next` points to a Node (isn't `nil`), then we can "traverse" the list until we reach the end, perhaps with a loop
  * If `@head.next` is nil, then we're at the end of the list. But we're adding another item, so set `@head.next` to the `Node` we're adding to the list.

4. Create another method on the `LinkedList` called `to_s` in order to print the list to the console.

**BONUS:** Inserting nodes will take longer as the linked list becomes longer. To alleviate this, add a `@tail` instance variable so we can access the end of the list in constant time.
