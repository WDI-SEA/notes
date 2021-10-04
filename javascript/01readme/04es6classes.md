# ES6 Inheritance

Other languages, such as C++ and Java, handle inheritance in a different way. Most OOP languages follow a **class** pattern, which contains the constructor and any methods shared across objects, as opposed to attaching methods to the prototype.

ES6, short for ECMAScript 6, is the latest update coming to JavaScript. ES6 provides a different way for implementing constructors and inheritance. An example is shown below. See resources such as [this one](http://javascriptplayground.com/blog/2014/07/introduction-to-es6-classes-tutorial/) for more details.

```javascript
class Person {
  constructor(name) {
    this.name = name;
  }

  greet() {
    return "Hello, my name is " + this.name;
  }
}

class Student extends Person {
  constructor(name, course) {
    super(name);
    this.course = course;
  }
}
```

Note that the parent/superclass constructor is called using the `super` keyword. Also, since ES6 isn't implemented across all platforms, this code won't work in many browsers. In order to write ES6 code now while still supporting older systems, we can use [Babel](https://babeljs.io/) to compile this code into ES5-friendly code.

