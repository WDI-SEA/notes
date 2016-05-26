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

#### Wait, why not use arrays instead?

In lower level languages, arrays are allocatd in **blocks.** Therefore, arrays are static in size and can only hold a specific data type. Linked lists store data in the **heap,** meaning that the data can be stored in an unorganized manner. Since each node points to the next one, it's still possible to maintain the list structure.

## Getting Started

The best way to understand how linked lists work is to make one! Let's do so in Ruby. Here's the process.

1. Start by creating a `Node` Class. We will have attributes to represent the data (let's call this `@data`) and the reference to the next Node (let's call this `@next`).

2. Create a `LinkedList` class. This class will have two values, `@head` and `@tail`. These will represent the beginning and end of the list. Initialize both to `nil` for now. We have an empty list!

3. Now for incorporating the two classes together. Create a method on the `LinkedList` class called `insert_front`. The challenge is to add an item to the beginning of the list. This can be done by creating a new `Node`, then doing the following:

* Store the value of `@head` into a temp variable
* Set the `@head` to the newly created `Node`. Note that currently, its `next` reference is `nil`.
* Think about what we would need to do if we're adding a new item to the beginning of a linked list. Consult the diagram (hint: we'll have to do something with the new node's `next` reference)
* Lastly, handle the special case of the `@tail`. `@tail` should always be the last `Node` in the linked list.

4. Create another method on the `LinkedList` or `Node` called `to_s` in order to print the list to the console.

## Iterating Over Linked Lists

Use while loops to iterate over a linked lists. While loops are better than for
loops here because Linked Lists don't have a length property. Instead of iterating
`for` a certain number of times, we simply iterate `while` our `current` pointer is
not `nil`.

Create a a local variable called `current` that starts off pointing to the list's
root node. Inside the loop you can do two things:

1. access the value of the current node at `current.data`
2. point the current variable to the next item with `current = current.next`

```ruby
list = LinkedList.new
list.insert_front 23
list.insert_front 82
list.insert_front 33
list.insert_front 97

current = list.root
while current.next != nil
	puts current.data
	current = current.next
end
```

**BONUS:** Create an `insert_end` method to add nodes to the end of the list.

**SUPER BONUS:** Create a more versatile `insert` method to add a node anywhere in the linked list, providing an index for the new item.
