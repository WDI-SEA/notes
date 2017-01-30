class ListNode:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

  def __str__(self):
    return str(self.data)
    
class LinkedList:
    root = None
    size = 0
    
    # Create a new LinkedList. The list will default to being
    # empty, or data can be passed in.
    def __init__(self, data=None):
      if data is not None:
        self.root = ListNode(data)
        self.size = 1
        
    def __len__(self):
      return self.size
        
    def __str__(self):
      if self.is_empty():
        return "[]"
    
      current = self.root
      result = str(current)
      while current.next is not None:
        result += f' -> {str(current.next)}'
        current = current.next
      return f'[{result}]'
      
    def __iter__(self):
      current = self.root
      while current is not None:
        yield current
        current = current.next
      return
      
    def is_empty(self):
      if self.root is None:
        return True
      return False
      
    # Insert a new piece of data at the front of the list.
    # This is O(1) because it always does a constant number of operations
    # no matter how long the list is. The entire benefit of linked lists
    # is that elements point to each other by reference and don't have to
    # be rearranged.
    def insert_in_front(self, data):
      # create a new node to hold the data.
      node = ListNode(data)
      
      # if the list is empty then make the new node the root.
      if self.root is None:
        self.size += 1
        self.root = node
        return node
        
      # otherwise, make the new node first point to the current root
      # then reset the root so it points to the new node. The order
      # here is important. If you point the root to the new node before
      # pointing the new node to the root then the entire list is lost.
      node.next = self.root
      self.root = node
      self.size += 1
      
    # Remove and return the first node in the list.
    def remove_front(self):
      if self.is_empty():
        return False
        
      # save a reference to the node at root
      node = self.root
      # make root equal to what it used to reference
      self.root = self.root.next
      self.size -= 1
      return node
      
    # Append a piece of data to the end of the list.
    # This is O(N) because it has to look at all N nodes.
    def insert_at_end(self, data):
      # create a new node to hold the data.
      node = ListNode(data)
      
      # if the list is empty then make the new node the root.
      if self.root is None:
        self.size += 1
        self.root = node
        return self.root
        
      # make a temporary variable that starts pointing to the root
      current = self.root
      
      # step through the list until you find a node that is not pointing
      # to another node.
      while current.next is not None:
        current = current.next
        
      # make the last node point to the new node.
      self.size += 1
      current.next = node
      return node
      
    def remove_last(self):
      # can't remove anything from an empty list
      if self.root is None:
        return False
        
      # A special case for when there's only one thing in the list.
      if self.root.next is None:
        node = self.root.next
        self.root = None
        self.size -= 1
        return node
        
      # create a temporary variable and step through the list one at a time
      # until getting to the node second-from-last so we can bump it's
      # next reference over the last node and have it point to none.
      #                   v----gotta stop current at this one.
      # root -> 0 -> 1 -> 2 -> 3 -> None
      current = self.root
      while current.next.next is not None:
        current = current.next
    
      # We're at the second-to-last node in the list. Save a reference to it's
      # next node. Change it's next reference so it points to None. Return the
      # node reference we saved.
      node = current.next
      current.next = None
      
      # make sure the node that was removed doesn't point to the rest
      # of the list anymore
      node.next = None
      self.size -= 1
      return node
      
    # insert a new node at the specified index.
    # index defaults to zero, where inserts are always fast O(1)
    def insert_at_index(self, data, index=0):
      # use our already-built insert_in_front method if the node is being
      # added at zero.
      if index == 0:
        return self.insert_in_front(data)
        
      # create a new node to hold the data.
      # create a temporary variable to iterate through the list.
      # create a temporary varaible to count how many nodes we've seen
      node = ListNode(data)
      current = self.root
      count = 0
      
      while (count < index and current is not None):
        if (count + 1 == index):
          node.next = current.next
          current.next = node
          self.size += 1
          return True
        # increment the count at every step.
        current = current.next
        count += 1
        
      # the user must have specified an out-of-bounds index.
      return False
      
    # Remove and return a node at a specific index. The index defaults
    # to zero if no value is provided.
    def remove_at_index(self, index=0):
      if self.is_empty():
        return False
        
      if (index == 0):
        return self.remove_front()
        
      count = 0
      current = self.root
      while count < index and current.next is not None:
        if count + 1 == index:
          node = current.next
          current.next = current.next.next
          self.size -= 1
          return node
            
        current = current.next
        count += 1
      return False
      
