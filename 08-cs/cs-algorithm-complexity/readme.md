#Algorithm Complexity

##Objectives

* Explain what algorithms are
* Understand the need to analyze algorithms and their complexity in terms of time and space
* Explain why asymptotic behavior is observed
* Use Big-O to explain the complexity of different algorithms

##What are Algorithms

An algorithm is a procedure or formula for solving a problem. Specifically, it is a step-by-step set of operations to be performed. We've been creating algorithms, in one form or another, throughout this class.

##What is Algorithm Complexity?

Whenever we create algorithms, we need to be aware that they run on computers, and computers have limits in terms of time and space. Even though most of the algorithms we've written seem to run instantaneously, when dealing with concepts like scalability, that "instant" algorithm can possibly take minutes or days to run if there's too much data provided to it.

What we need to do is analyze the complexity of the algorithm so we can estimate how efficient it is. This is done in terms of:

* Runtime (processing time, via the CPU)
* Runspace (how much memory does it take up)

The most common way to express the efficiency/complexity of an algorithm is using what is called Big-O Notation

##Big-O Notation

> In computer science, big O notation is used to classify algorithms by how they respond (e.g., in their processing time or working space requirements) to changes in input size. -- Wikipedia

Since a big issue when discussing algorithms and data structures is their efficiency in the face of certain tasks, we want to use a common language to discuss such (in)efficiencies. Normally, we are interested in how much memory or processing time is needed to complete the task depending on the size of the input. We often let n represent the input size.

Note that when we use Big-O notation, we're only worried about the **asymptotic** behavior. In other words, the behavior as we approach some type of limit. Therefore, we don't worry too much about coefficients in Big-O notation (You'll rarely see an algorithm analyzed as O(3n). It simplifies down to just O(n)).

###Common Notations

An algorithm that is O(1), is said to be "Big O of 1" or **constant**, and does not vary depending on the size of the input. This is good. This is fast even for very large values of n.

####Example

```js
function constantRuntime(x) {
  var result = x * 2;
  return result;
}
```

An algorithm that is O(n), is said to be "Big O of n" or **linear**, and this indicates that the resources required grow proportionally to the size of the input. This is reasonable performance.

####Example

```js
function linearRuntime(x) {
  for (var i = 0; i < x; i++) {
    console.log(i);
  }
}
```

An algorithm that is O(n^2), is said to be "Big O of n squared" or **quadratic**, and it means the resources grow in proportion to the square of the input. This is **slow**. Think of really big numbers and then think of them squared.

####Example

```js
function quadraticRuntime(x) {
  for (var i = 0; i < x; i++) {
    for (var j = 0; j < x; j++) {
      console.log(i * j);
    }
  }
}
```

An algorithm that is O(log(n)), is said to be "Big O of log n" or **logarithmic**, and it means the resources grow to the inverse of exponential growth. This is **fast!** Algorithms that grow this slow are great!

####Example

```
function binarySearch(search) {
    var min = 0;
    var max = this.length - 1;
    var index;
    var elem;
 
    while (min <= max) {
        index = (min +  max) / 2 | 0;
        elem = this[index];
 
        if (elem < search) {
            min = index + 1;
        }
        else if (elem > search) {
            max = index - 1;
        }
        else {
            return index;
        }
    }
 
    return -1;
}
```

See the [Cheat Sheet](http://bigocheatsheet.com/) for some other common time (processing time) and space (memory) complexities and their notations.
