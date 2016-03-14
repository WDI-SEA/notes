# Array Flatten

In Javascript we know that we can nest arrays inside of other arrays. For example, the following is a valid array in JavaScript

```js
[1, 2, [3, 4], [5, 6], 7]
```

but you can imagine a case when you'd like to flatten an array, decompose it into just an array of elements, so...

```js
[1, 2, [3, 4], [5, 6], 7]
```

would become

```js
[1, 2, 3, 4, 5, 6, 7]
```

##Challenge 1

Create a JavaScript file called `flatten.js` and implement the function below that flattens an array. For now, don't worry about arrays that are more than one level deep.

```js
var flatten = function(arr){
    //flatten the array here
    
    return arr;
}

var myArr = [1, 2, [3, 4], [5, 6], 7];

console.log(flatten(myArr));
//output: [1, 2, 3, 4, 5, 6, 7]
```

**HINT:** There might be something useful [in here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array).


##Challenge 2

As we know, arrays in JavaScript can be nested as deeply as we want. So the input could be...

```js
[1, 2, [3, 4], [5, [6]], 7]
```

or even something like...

```js
[1, [2, [3, [4, [5]]], 6, [7]]]
```

Therefore, our function needs to be able to handle an array of any depth. Create a new function called `flatten2` that flattens deeply nested arrays. So, both of the examples should be flattened to `[1, 2, 3, 4, 5, 6, 7]`.
