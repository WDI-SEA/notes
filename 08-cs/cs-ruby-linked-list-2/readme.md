#Linked List Methods Challenge

Use the Linked List included in this document to implement the following methods.

####Find center

Finding the center element of a linked list is a classic interview problem. First, try to produce code that can get the right answer (regardless of efficiency). Then, try to get it done in O(n) time. You can assume that the list will be odd in length.

####Reverse

If you finish the find center method before we run out of time, try another classic problem, reversing a linked list.

This should be completed in O(n) time and needs to be done in place (shouldn't use any insert commands).

```rb
class Node
  attr_accessor :data, :next

  def initialize data
    @data = data
    @next = nil
  end

  def to_s
    output = @data.to_s
    output += ' > ' + @next.to_s unless @next.nil?
    output
  end
end


class LinkedList
  attr_accessor :head, :tail

  def initialize
    @head = nil
    @tail = nil
  end

  def insert_front data
    temp = @head
    @head = Node.new(data)
    @head.next = temp
    @tail = @head if @tail.nil?
  end

  def insert_end data
    temp = @tail
    @tail = Node.new(data)
    temp.next = @tail unless temp.nil?
    @head = @tail if @head.nil?
  end

  def to_s
    @head.to_s
  end

  def get_center
    #code solution for center here
  end

  def reverse
    #bonus - code solution for reverse here
  end
end

list = LinkedList.new

list.insert_front 1
list.insert_front 3
list.insert_front 5
list.insert_front 7
list.insert_front 9

#outputs: 9 > 7 > 5 > 3 > 1
puts list

#needs to output: 5
puts list.get_center.data

#needs to output: 1 > 3 > 5 > 7 > 9
list.reverse
puts list
```
