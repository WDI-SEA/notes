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

**Test**:
```python
myList = LinkedList()
myList.insert_front('Taylor')
myList.insert_front('Dave')
myList.insert_front('Anna')
myList.insert_end('King')
print(myList)
print(len(myList))
```

```
[Anna -> Dave -> Taylor -> King]
4
```

### insert_after

Let's say we want to insert `Gavin` after `Anna` in the list. How would we do this? 

#### Find the reference node and store it
We would first certainly need a reference to the `Anna` node, which means we have to start at the `head` and iterate through the list until we find her! Once we find the `Anna` node, we'll store it in a holder variable called `temp`:

```python
	def insert_after(self, data, node_data):
		temp = None
		current = self.head
		while current:
			if current.data == node_data:
				temp = current
				break
			current = current.next
```

We should also handle the case in which we _didn't_ find the `Anna` node:

```python
	def insert_after(self, data, node_data):
		temp = None
		current = self.head
		while current:
			if current.data == node_data:
				temp = current
				break
			current = current.next
		if temp == None:
			return 'check your node_data, we couldn\'t find it!'
```

Assuming we _do_ find the node we're looking for, which should now be stored in `temp`, we can create the new node, make it point to the node that comes after `temp`, then reassign `temp` to point to the new node:

```python
	def insert_after(self, data, node_data):
		temp = None
		current = self.head
		while current:
			if current.data == node_data:
				temp = current
				break
			current = current.next
		if temp == None:
			return 'check your node_data, we couldn\'t find it!'
		newNode = Node(data, temp.next)
		temp.next = newNode
		self.size += 1
```

Test it!
```python
myList = LinkedList()
myList.insert_front('Taylor')
myList.insert_front('Dave')
myList.insert_front('Anna')
myList.insert_end('King')
myList.insert_after('Gavin', 'Anna')
myList.insert_after('Nick', 'King')
print(myList)
print(len(myList))
```

```
[Anna -> Gavin -> Dave -> Taylor -> King -> Nick]
6
```

### Bonus Challenge: insert_before

Try implementing an `insert_before` method!

