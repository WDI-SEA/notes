# Linked List Beginner Exercises
Here are some problems designed to help you practice manipulating linked lists.
Each problem has two lines. The first line shows how the list starts. The second
line shows how the linked list should end.

Your job is to write code that manually manipulates the given start list so it
ends up like the end list.
* You may create new nodes with `Node.new(data)`
* You may create temporary variables to refer to nodes,
  like `current = root` or `current = root.next`
* You may reassign the `.next` value of any node
* Your solution will be in the format of several small lines of code
  manipulating the list.

Here are some example solutions to get you started.

## Example 1

Add a node to an empty list

```
root -> nil
root -> 43 -> nil
```

Solution:

```
root = Node.new 43
```

## Example 2

Add a node at the beginning of the list

```
root -> 2 -> 3 -> 4 -> nil
root -> 1 -> 2 -> 3 -> 4 -> nil
```

Solution:

```
node = Node.new 1
node.next = root
root = node
```

## Problem 1
Add a node in the second place
```
root -> 1 -> 3 -> 4 -> nil
root -> 1 -> 2 -> 3 -> 4 -> nil
```

## Problem 2
Add a node to the end
```
root -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> nil
root -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> nil
```

## Problem 3
Add a node second to the end
```
root -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 8 -> nil
root -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> nil
```

## Problem 4
Delete the first node from the list.
```
root -> 1 -> 2 -> 3 -> nil
root -> 2 -> 3 -> nil
```

## Problem 5
Delete everything from the list.
```
root -> 34 -> 45 -> 78
root -> nil
```

## Problem 6
Manually stutter an existing list (make each item appear twice)
```
root -> 23 -> 17 -> 8 -> nil
root -> 23 -> 23 -> 17 -> 17 -> 8 -> 8 -> nil
```

## Problem 7
Manually reverse an existing linked list

```
root -> 3 -> 4 -> 5 -> 6 -> nil
root -> 6 -> 5 -> 4 -> 3 -> nil
```

# Iterating Over Linked Lists
Now that you're familiar with manually manipulating linked lists try to write
methods that act generally on linked lists.

## Contains

Write a method called `contiains` that accepts a linked list and a value. The method should iterate
over the list and return true if the value exists as data at a node in the list,
or otherwise return false.

```ruby
def contains(ll, value)

end
```

## Get Second-To-Last
Write a method that returns the second to last node in a list. You can assume
the list has at least two element in it, or more. You can not assume you know
the size of the list. You must use a while loop to iterate through the entire
list and find out if a `.next` property on a node points to `nil` to find the end
of the list.

```
def second_to_last(ll)

end
```
