# Promises

A promise is an Javascript object that has a job: go get a particular value. A promise can be in one of three states:

* **Pending:** the promise is in the process of trying to retrieve the value
* **Fulfilled:** the promise has successfully retrieved the value
* **Rejected:** the promise was unable to retrieve the value

### Analogy

“Imagine you are a kid. Your mom promises you that she’ll get you a new phone next week.”

You don’t know if you will get that phone until next week. Your mom can either really buy you a brand new phone, or she doesn’t, because she is not happy :\(.

That is a promise. A promise has 3 states. They are:

* **Pending**: You don’t know if you will get that phone
* **Fulfilled**: Mom is happy, she buys you a brand new phone
* **Rejected**: Mom is unhappy, she doesn’t buy you a phone

_This example scenario is adapted from_ [_Javascript Promises for Dummies_](https://www.digitalocean.com/community/tutorials/javascript-promises-for-dummies)

## Creating a Promise

When you create a new promise, you have to tell it what it's job is. Do this by giving it a callback function.

```javascript
const myPromise = new Promise(myCallback)
```

So, in our phone example:

```javascript
const newPhonePromise = new Promise(checkMomsMood);
```

The promise will pass 2 arguments into the callback: **1.** a function to run if the value is successfully retrieved \(_resolve_\) **2.** a function to run if the value is not successfully retrieved \(_reject_\)

```javascript
const isMomHappy = true

const checkMomsMood = (resolve, reject) => {
  console.log('pending...');
  if (isMomHappy) {
      const phone = { brand: 'Samsung', color: 'black' }
      resolve(phone)
  } else {
      const reason = new Error('mom is not happy')
      reject(reason)
  }
}

const newPhonePromise = new Promise(checkMomsMood)
```

Once a promise is fulfilled, then the promise will represent the value it was sent to retrieve.

```javascript
console.log(newPhonePromise)
```

Try changing `isMomHappy` to a `false` - what changes?

## Consuming the Promise

Promises are generally _consumed_ by attaching a `.then().catch()`. **.then\(\)**

* triggered by the `resolve()` function
* handles what to do next with the retrieved data

  **.catch\(\)**

* triggered by the `reject()` function
* handles the error

```javascript
const isMomHappy = true

const checkMomsMood = (resolve, reject) => {
  console.log('pending...');
  if (isMomHappy) {
      const phone = { brand: 'Samsung', color: 'black' }
      resolve(phone)
  } else {
      const reason = new Error('mom is not happy')
      reject(reason)
  }
}

const newPhonePromise = new Promise(checkMomsMood)

const willIGetNewPhone = () => {
  newPhonePromise
  .then(newPhone => {
    console.log("look at this sweet new phone:", newPhone)
  })
  .catch(err => {
    console.log("did NOT get a new phone :(")
    console.log(err)
  })
}

willIGetNewPhone()
```

Run this code to see the `.then()` callback run. Change `isMomHappy` to `false` to see the `.catch()` in action!

## Chaining Promises

You can chain multiple promises together using the `.then()` function. In the callback function of the `.then()`, just return the next promise you want to run:

```javascript
const isMomHappy = true

const checkMomsMood = (resolve, reject) => {
  console.log('pending...');
  if (isMomHappy) {
      const phone = { brand: 'Samsung', color: 'black' }
      resolve(phone)
  } else {
      const reason = new Error('mom is not happy')
      reject(reason)
  }
}

// 1st promise
const newPhonePromise = new Promise(checkMomsMood)

// 2nd promise (we don't need a reject because we know it will only run if we got a new phone)
const showOff = phone => {
    const message = 'Hey friend, I have a new ' +
                phone.color + ' ' + phone.brand + ' phone'
    return Promise.resolve(message)
}

const willIGetNewPhone = () => {
  newPhonePromise
  .then(newPhone => {
    console.log(showOff(newPhone))
  })
  .catch(err => {
    console.log("did NOT get a new phone :(")
    console.log(err)
  })
}

willIGetNewPhone()
```

## Asyncronicity

Note that promises are asynchronous. If we add the following `console.log()` statements, they wont necessarily run in the order we'd expect. Try it out!

```javascript
const willIGetNewPhone = () => {
  console.log("before promises")
  newPhonePromise
  .then(newPhone => {
    console.log(showOff(newPhone))
  })
  .catch(err => {
    console.log("did NOT get a new phone :(")
    console.log(err)
  })
  console.log("after promises")
}
```

How would you edit this code so that the final `console.log` statement runs _after_ the promises are fulfilled?

### Exercise:

Imagine you are stuck at home with a sprained ankle, so you send your friend to the market to buy some pain medication. Your friend makes a **promise** to return with some pain medication for you. Once your friend has left for the market, the promise is **pending**. If your friend returns from the market with medication, the promise is **fulfilled**. If your friend returns from the market _without_ medication, the promise is **rejected**.

Write code with promises to represent this scenario!

_**EVERYTHING BELOW THIS LINE IS ESSENTIALLY THE SAME CODE AS ABOVE, JUST GENERIC VERSIONS FOR FURTHER REVIEW IF DESIRED**_

## Creating a Promise

When you create a new promise, you have to tell it what it's job is. Do this buy giving it a callback function.

```javascript
var myPromise = new Promise(myCallback)
```

The promise will pass 2 arguments into the callback: **1.** a function to run if the value is successfully retrieved \(_resolve_\) **2.** a function to run if the value is not successfully retrieved \(_reject_\)

```javascript
const myCallback = (resolve, reject)=>{
  console.log('pending...');
  if(valueToRetrieve) {
    resolve(valueToRetrieve);
  } else {
    reject('valueToRetrieve is falsey');
  }
}

let valueToRetrieve = "";
let myPromise = new Promise(myCallback);
```

Once a promise is fulfilled, then the promise will represent the value it was sent to retrieve.

```javascript
console.log(myPromise);
```

Try changing `valueToRetrieve` to a falsey value - what changes?

## Consuming the Promise

Promises are generally _consumed_ by attaching a `.then().catch()`. **.then\(\)**

* triggered by the `resolve()` function
* handles what to do next with the retrieved data

  **.catch\(\)**

* triggered by the `reject()` function
* handles the error

```javascript
const myCallback = (resolve, reject)=>{
  console.log('pending...');
  if(valueToRetrieve) {
    setTimeout(()=>{resolve(valueToRetrieve)}, 2000);
  } else {
    setTimeout(()=>{reject('valueToRetrieve is falsey')}, 3000);
  }
}

const consumePromise = () => {
    myPromise
    .then((retrievedValue)=>{ // will run if resolve() is called
        console.log("fulfilled! retrievedValue is:", retrievedValue);
    }).catch((err) =>{ // will run if reject() is called
        console.log("wah wah :( Error:", err);
    })
}

let valueToRetrieve = "!!!";
let myPromise = new Promise(myCallback);
consumePromise()
```

Run this code to see the `.then()` callback run. Change `valueToRetrieve` to a falsey value to see the `.catch()` in action!

## Chaining Promises

You can chain multiple promises together using the `.then()` function. In the callback function of the `.then()`, just return the next promise you want to run:

```javascript
const consumeTwoPromises = () => {
    myPromise
    .then((firstRetrievedValue)=>{
      return new Promise((resolve, reject)=>{
          console.log("first retrived value: "+firstRetrievedValue);
          if(firstRetrievedValue){
            resolve(firstRetrievedValue+"???")
          } else {
            reject("firstRetrievedValue is falsey");
          }
      })
    })
    .then((secondRetrievedValue)=>{ // will run if resolve() is called
        console.log("second retrieved value is:", secondRetrievedValue);
    })
    .catch((err)=>{ // will run if reject() is called
        console.log("wah wah :( Error:", err);
    })
}

let valueToRetrieve = "!!!";
let myPromise = new Promise(myCallback);
consumeTwoPromises()
```

## Asyncronicity

Note that promises are asynchronous. If we add the following `console.log()` statements, they wont necessarily run in the order we'd expect. Try it out!

```javascript
const consumeTwoPromises = () => {
    console.log("this is the console.log before promises")
    myPromise
    .then((firstRetrievedValue)=>{
      return new Promise((resolve, reject)=>{
          console.log("first retrived value: "+firstRetrievedValue);
          if(firstRetrievedValue){
            resolve(firstRetrievedValue+"???")
          } else {
            reject("firstRetrievedValue is falsey");
          }
      })
    })
    .then((secondRetrievedValue)=>{ // will run if resolve() is called
        console.log("second retrieved value is:", secondRetrievedValue);
    })
    .catch((err)=>{ // will run if reject() is called
        console.log("wah wah :( Error:", err);
    })
    console.log("this is the console.log written after promises")
}
```

How would you edit this code so that the final `console.log` statement runs _after_ the promises are fulfilled?

## More Resources

* [Javascript Promises for Dummies](https://scotch.io/tutorials/javascript-promises-for-dummies)
* [cujoJS: Learning Promises](http://know.cujojs.com/tutorials/promises/)

