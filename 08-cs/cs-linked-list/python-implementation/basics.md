# Linked List in Python

Here we'll use object-oriented programming to build a basic linked list in python. We'll need a `Node` class and a `LinkedList` class.

## Node

```python
class Node:
	# constructor
	def __init__(self, data, next):
		self.data = data
		self.next = next

	def __str__(self): # tell python how to print this node
		return str(self.data)
```

***Challenge:*** How would you modify this code to accomodate a doubly linked list? (This is currently only set up for a singly-linked list.)

## LinkedList

Properties and basic functionality we'll include:
* head
* tail
* length (how many nodes in the list)
* `__len__` (return the length of the list)
* `__str__` (return a string representation of the list)

```python
class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0
	
	# returns length of the list
	def __len__(self):
		return self.size
	
	def __str__(self):
		if self.size == 0:
			return '[]'

		current = self.head
		result = str(current) # what we return once we've concantenated all the nodes to it
		while current.next:
			result += f' -> {str(current.next)}'
			current = current.next
		return f'[{result}]'
```
