#Local Storage

HTML5 introduced a feature called `localStorage` that allows us to store data on a local user's computer. The data is unique for a single person using a specific web site.

Local storage is an object that is retained even if the browser is reloaded. We can get and set values like any other object.

**Set value**

```js
localStorage.name = 'Lenny';
```

**Get value**
```js
console.log(localStorage.name);
```

####Using JSON stringify / parse

Local storage can only store strings. Therefore, we have to use `JSON.parse` and `JSON.stringify` to convert complex data types such as collections into a string and back.

[JSON MDN Documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON)

**stringify** - converts object to string

```js
JSON.stringify({a:1,b:2});
//returns a json string: '{"a":1,"b":2}'
```

**parse** - converts string to object

```javascript
JSON.parse('{"a":1,"b":2}');
//returns a json object {a:1,b:2}
```

####Using with JSON data

All we have to do now is put it together. We can store any JavaScript data structure (even highly nested objects / arrays) as a string by using `JSON.stringify` and `JSON.parse`.

**Saving data**

```js
var listValues = ['taco', 'burrito', { name: 'Brian' }];
localStorage.myList = JSON.stringify(listValues);
```

**Loading data**

```js
var listValues = JSON.parse(localStorage.myList);
```

####Preventing errors

There is still one problem. If we run `JSON.parse` on something that isn't valid JSON, it will throw an error and prevent some of our JavaScript from running! We can avoid this by using a **try...catch** statement.

A **try..catch** statement will "try" running a block of code that is prone to throw an error. If the code throws an error, the error won't be thrown to the console. Instead, it will be handled gracefully by the "catch" block, where we can set a default value for our values.

```js
try {
  // Code that is prone to errors (if invalid JSON is parsed)
  var listValues = JSON.parse(localStorage.myList);
} catch (err) {
  // If an error occurs, catch the error and handle it gracefully, such as
  // setting a default value (empty array)
  var listValues = [];
}
```

[MDN Documentation: try...catch statements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch)
