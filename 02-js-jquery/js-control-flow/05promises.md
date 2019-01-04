# Javascript Promises

A promise is an Javascript object that has a job: go get a particular value. A promise can be in one of three states:

* **Pending:** the promise is in the process of trying to retrieve the value
* **Fulfilled:** the promise has successfully retrieved the value
* **Rejected:** the promise was unable to retrieve the value

### Analogy
Imagine you are stuck at home with a sprained ankle, so you send your friend to the market to buy some pain medication. Your friend is the **promise**. Once your friend has left for the market, the promise is **pending**. If your friend returns from the market with medication, the promise is **fulfilled**. If your friend returns from the market _without_ medication, the promise is **rejected**. 

## Creating a Promise

When you create a new promise, you have to tell it what it's job is. Do this buy giving it a callback function.

```js
var myPromise = new Promise(myCallback)
```

The promise will pass 2 arguments into the callback:
**1.** a function to run if the value is successfully retrieved
**2.** a function to run if the value is not successfully retrieved

```js
function myCallback(resolve, reject) {
  console.log('pending...');
  if(valueToRetrieve) {
    resolve(valueToRetrieve);
  } else {
    reject('valueToRetrieve is falsey');
  }
}

var valueToRetrieve = "!!!";
var myPromise = new Promise(myCallback);
```

Once a promise is fulfilled, then the promise will represent the value it was sent to retrieve.

```js
console.log(myPromise);
```

## Consuming the Promise


## More Resources
* [Javascript Promises for Dummies](https://scotch.io/tutorials/javascript-promises-for-dummies)
* [cujoJS: Learning Promises](http://know.cujojs.com/tutorials/promises/)

