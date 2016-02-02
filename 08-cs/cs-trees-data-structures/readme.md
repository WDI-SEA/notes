![General Assembly Logo](http://i.imgur.com/ke8USTq.png)

# Assorted CS Topics

## Trees

Trees are data structures that are similar to linked lists, but rely on nodes linking to many nodes in a tree-like fashion.

Trees consist of a top node, called the **root** of the tree, linking to **children** nodes below it.

![A tree](http://poj.org/images/1330_1.jpg)

So what's the point? Trees are used in many areas of computer science, including syntax parsers (determines if your parentheses and functions are correct).

### Binary Search Trees

The most common tree structure is known as a binary search tree. Each node has at most two children, and they provide a way to order elements. When inserting values, the value goes to the left child if less than the root node, and to the right child if greater than the root node.

![BST](http://cramster-image.s3.amazonaws.com/definitions/computerscience-5-img-1.png)

On average, insertion, deletion, and search take O(log(n)) with binary search trees. But there's a worst case scenario.

![BST worst case](http://interactivepython.org/runestone/static/pythonds/_images/skewedTree.png)

We just made a bloated linked list! There has to be a better way, and thanks to research, there is.

### Balanced Trees

To avoid the worst case scenario of a binary search tree, there are methods to create balanced trees, where we are **guaranteed** average and worst case runtimes of O(log(n)). A couple methods of doing this include rebalancing the tree based on subtree size and/or categorizing nodes.

### Tries

Tries are a special type of tree, usually implemented with strings as the data, where child nodes share a common prefix (as represented by the parent node).

![Trie](https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Trie_example.svg/400px-Trie_example.svg.png)

They're usually used for quick lookups, generally autocomplete fields and IP address lookups.

## Graphs

If we remove even more restrictions from trees, we end up with graphs, which are interconnected sets of nodes.

![Undirected graph](https://computersciencesource.files.wordpress.com/2010/05/dfs_1.png)
![Directed graph](https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Directed_acyclic_graph_2.svg/305px-Directed_acyclic_graph_2.svg.png)

Graphs can be directed (a path that has direction) or undirected. Graphs are essential in applications such as Facebook or Twitter, where showing relationships between users and groups is essential.

### Searching

There's a couple ways to search graphs.

#### Depth-First Search

Exploring the graph as far as possible, then backtracking.

#### Breadth-First Search

Exploring the graph close to the starting point, then slowly growing out.

[Some visualizations of these data structures and algorithms](http://visualgo.net/)

## Memory

### The Stack and Heap

* Out of Memory
* Stack overflow
* Heap overflow

The above are messages that you may encounter or have already encountered when working with programs. So what do they mean?

Whenever a program initialized (let's say, a Ruby program), the computer allocates a block of memory for the program to run in.

![Memory](http://www.cs.cornell.edu/courses/cs312/2004fa/lectures/memory%20layout.jpg)

The block of memory is separated into 3 sections: the stack, the heap, and the code.
The code required to run the program, and the stack/heap are for allocating new values. Note that the stack grows in one direction, while the heap grows in the other direction.
If one of these encroaches on the other, we run out of memory!

Ideally, this shouldn't happen, so we need to make sure that we only allocate memory when we absolutely need it. Web programmers occasionally encounter these problems, so it's good
to have a general idea of what's going on under the hood.

### Memory Hierarchy

![Memory Hierarchy](http://tjliu.myweb.hinet.net/COA_CH_6.files/image007.jpg)
