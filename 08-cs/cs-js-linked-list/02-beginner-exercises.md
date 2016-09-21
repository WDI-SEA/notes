function Node(data) {
  this.data = data;
  this.next = undefined;
}

function LinkedList() {
  this.root = undefined;
}

LinkedList.prototype.toString = function() {
  var current = this.root;
  var result = "";
  while (current !== undefined) {
    result += " " + current.data;
    current = current.next;
  }

  return result;
}


// problem 1
// 1 3 4
// 1 2 3 4
var list1 = makeList([1, 3, 4]);
console.log(list1.toString());

// your manipulations here

console.log(list1.toString());
console.log();


// problem 2
// 1 2 3 4 5 6 7
// 1 2 3 4 5 6 7 8
var list2 = makeList([1, 2, 3, 4, 5, 6, 7]);
console.log(list2.toString());

// your manipulations here

console.log(list2.toString());
console.log();


// problem 3
// 1 2 3 4 5 6 8
// 1 2 3 4 5 6 7 8
var list3 = makeList([1, 2, 3, 4, 5, 6, 8]);
console.log(list3.toString());

// your manipulations here

console.log(list3.toString());
console.log();


// problem 4
// 1 2 3
// 2 3
var list4 = makeList([1, 2, 3]);
console.log(list4.toString());

// your manipulations here

console.log(list4.toString());
console.log();

// problem 5
// 34 45 78
// undefined
var list5 = makeList([34, 45, 78]);
console.log(list5.toString());
// your manipulations here
list5.root = undefined;

console.log(list5.toString());
console.log();

// problem 6
// 23 17 8
// 23 23 17 17 8 8
var list6 = makeList([23, 17, 8]);
console.log(list6.toString());

// your manipulations here

console.log(list6.toString());
console.log();

// problem 7
// 3 4 5 6
// 6 5 4 3
var list7 = makeList([3, 4, 5, 6]);
console.log(list7.toString());

// your manipulations here

console.log(list7.toString());
console.log();


// DO NOT MODIFY!!
// Helper functions to set up lists for each problem.

function makeList(a) {
  var list = new LinkedList();
  list.root = new Node(a[0]);

  var current = list.root;
  for (var i = 1; i < a.length; i++) {
    current.next = new Node(a[i]);
    current = current.next;
  }

  return list;
}

