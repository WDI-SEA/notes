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

Promises are generally _consumed_ by attaching a `.then().catch()`. 
**.then()** 
* triggered by the `resolve()` function
* handles what to do next with the retrieved data
**.catch()**
* triggered by the `reject()` function
* handles the error

```js
function consumePromise(){
	myPromise
		.then(function(retrievedValue){ // will run if resolve() is called
			console.log("fulfilled! retrievedValue is:", retrievedValue);
		}).catch(function(err){ // will run if reject() is called
			console.log("wah wah :( Error:", err);
		})
}

var valueToRetrieve = "!!!";
var myPromise = new Promise(myCallback);
consumePromise();
```

Run this code to see the `.then()` callback run. Change `valueToRetrieve` to a falsey value to see the `.catch()` in action!

## Chaining Promises

You can chain multiple promises together using the `.then()` function. In the callback function of the `.then()`, just return the next promise you want to run:

```js
function consumeTwoPromises(){
	myPromise
		.then(function(firstRetrievedValue){
			return new Promise(function(resolve, reject){
				console.log("first retrived value: "+firstRetrievedValue);
				if(firstRetrievedValue){
					resolve(firstRetrievedValue+"???")
				} else {
					reject("firstRetrievedValue is falsey");
				}
			})
		})
		.then(function(secondRetrievedValue){ // will run if resolve() is called
			console.log("second retrieved value is:", secondRetrievedValue);
		}).catch(function(err){ // will run if reject() is called
			console.log("wah wah :( Error:", err);
		})
}

var valueToRetrieve = "!!!";
var myPromise = new Promise(myCallback);
consumeTwoPromises();
```

## Asyncronicity

Note that promises are asynchronous. If we add the following `console.log()` statements, they wont necessarily run in the order we'd expect. Try it out!

```js
function consumeTwoPromises(){
	console.log("before promises")
	myPromise
		.then(function(firstRetrievedValue){
			return new Promise(function(resolve, reject){
				console.log("first retrived value: "+firstRetrievedValue);
				if(firstRetrievedValue){
					resolve(firstRetrievedValue+"???")
				} else {
					reject("firstRetrievedValue is falsey");
				}
			})
		})
		.then(function(secondRetrievedValue){ // will run if resolve() is called
			console.log("second retrieved value is:", secondRetrievedValue);
		}).catch(function(err){ // will run if reject() is called
			console.log("wah wah :( Error:", err);
		})
	console.log("after promises");
}
```

How would you edit this code so that the final `console.log` statement runs _after_ the promises are fulfilled?

## More Resources
* [Javascript Promises for Dummies](https://scotch.io/tutorials/javascript-promises-for-dummies)
* [cujoJS: Learning Promises](http://know.cujojs.com/tutorials/promises/)

