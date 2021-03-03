# Sample Node and LinkedList Class

## Sample Usage

```js
var list = new LinkedList();
list.add(1);
list.add(2);
list.add(3);
list.add(4);

console.log(list.toString());
```

## Sample Classes
```js
function Node(data) {
  this.data = data;
  this.next = undefined;
}

function LinkedList() {
  this.root = undefined;
}

LinkedList.prototype.add = function(data) {
  var node = new Node(data);

  // if the list is empty then set the root equal to the new node.
  if (root === undefined) {
    root = node;
  } else {
    // traverse to the end of the list.
    var current = root;
    while (current.next != undefined) {
      current = current.next;
    }

    // add the new node as a reference from the very end of the list.
    current.next = node;
  }
};

LinkedList.prototype.toString = function() {
  var current = this.root;
  var result = "";
  while (current !== undefined) {
    result += " " + current.data;
    current = current.next;
  }

  return result;
};
```
