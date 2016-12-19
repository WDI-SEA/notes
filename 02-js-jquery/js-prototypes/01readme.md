#OOP with Prototypes

##Objectives

* Identify the downsides of object literal notation.
* Use constructor pattern to create multiple object instances.
* Discuss the basic premises behind object-oriented programming with prototypes in JavaScript.
* Define the difference between an instance and a class (or constructor function)
* Use constructors and prototypes to modularize code and keep code DRY.

##Object Oriented Programming

> Object-oriented programming (OOP) is a programming paradigm based on the concept of "objects", which are data structures that contain data, in the form of fields, often known as attributes; and code, in the form of procedures, often known as methods. A distinguishing feature of objects is that an object's procedures can access and often modify the data fields of the object with which they are associated (objects have a notion of "this"). In object-oriented programming, computer programs are designed by making them out of objects that interact with one another. - [wiki](http://en.wikipedia.org/wiki/Object-oriented_programming)

We've been encountering examples of object-oriented programming in JavaScript, but there's ways to make objects easier and more efficient to construct. Specifically, we'll be looking at **constructors** and **prototypes** in order to achieve these goals.
