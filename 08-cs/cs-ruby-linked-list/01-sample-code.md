# Sample Node and LinkedList Class

## Example Usage
Use these classes to create lists like this:

```ruby
list = LinkedList.new
list.insert_end 1
list.insert_end 2
list.insert_end 3
list.insert_end 4

puts list.to_s
```

## Sample Classes
```ruby
class Node
  attr_accessor :data, :next

  def initialize data
    @data = data
    @next = nil
  end

  def to_s
    output = @data.to_s
    if @next != nil
    end
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
end
```
