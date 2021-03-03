## Linked List in Python: node transactions

_(This lesson assumes you already have the code from the [basics lesson](https://gawdiseattle.gitbook.io/wdi/08-cs/intro/basics))_

In order to actually ***use*** our LinkedList class, we'd better have a way to add nodes to a list! Let's add the following methods:
* `insert_front`
* `insert_end`
* `insert_after`

### insert_front

In order to insert a node at the beginning of our list, we need to:
* create a new node
* insert the node (three cases)
* increment the length of the list

Note that there are three different possible cases:
* the list is currently empty
* the list has only one node
* the list has more than one node

```python
	# insert a new Node at the front of the list
	def insert_front(self, data):
		if self.size == 0: # list is empty
            # do something
		elif self.size == 1: # there is one node already in the list
            # do something else
		else:
            # do something else
		self.size += 1
```

What does inserting a new node at the beginning of the list look like for each of these cases?

```python
	def insert_front(self, data):
		if self.size == 0: # list is empty
			self.head = Node(data, None) # create a new node and make it the head
			self.tail = self.head # also set the tail to the same node
		elif self.size == 1:
			self.head = Node(data, self.tail)
		else:
			temp = self.head
			self.head = Node(data, temp)
		self.size += 1
```

Test it!

```python
myList = LinkedList()
myList.insert_front('Taylor')
myList.insert_front('Dave')
myList.insert_front('Anna')
```

```
[Anna -> Dave -> Taylor]
3
```

### Exercise: insert_end

Try writing an `insert_end` method that adds a new node to the **end** of a linked list.

##### Solution:
```python
	def insert_end(self, data):
		if self.size == 0:
			self.head = Node(data, None)
			self.tail = self.head
		else:
			temp = self.tail
			self.tail = Node(data, None)
			temp.next = self.tail
		self.size += 1
```