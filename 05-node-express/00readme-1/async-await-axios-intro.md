# Axios, Promises, async await

## Learning Objectives

* Understand the benefits of using Axios for making HTTP requests in Node.js
* Learn how to use Axios for GET requests and compare it to the built-in Fetch API
* Gain an understanding of `async/await` vs. ``.then` for handling asynchronous code
* Explore how to refactor code to avoid callback hell and improve readability using `async/await`
* Complete lab challenges that provide practice in refactoring Axios requests with `async/await` and `Promise.all`

## Using Axios for GET Requests

[`axios`](https://www.npmjs.com/package/axios) is a popular library for making HTTP requests in node (and javascript). Since there is no `window` in `Node.js`, we don't have access to `window.fetch` out of the box. `Node.js` does have a built in [requests](https://nodejs.org/api/http.html#class-httpclientrequest) module and support for [XMLHttpRequests](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest), they are quite clunky to use and `axios` is one of the most popular ways to make HTTP requests in node.

Here's a simple example of how to use `axios` to make a GET request:

```javascript
axios.get('https://jsonplaceholder.typicode.com/posts')
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.error(error);
  });
```


_Look, there is only one `.then`!_

![catbug happy](https://media4.giphy.com/media/3KYGq82Lb74TbVXLVc/giphy.gif?cid=ecf05e47i5po5dmlwgmem6aqndhkiyny3rrb5omes24bpote&rid=giphy.gif&ct=g)


One of the benefits of using `axios` over `fetch` is that it supports automatic transformation of response data. This is why only one `.then` is needed. For example, if the response data is JSON, axios will automatically parse it and return a JavaScript object. With fetch, you have to manually call `response.json()` to parse the response data.


Look in the `.then` to see another notable difference of using `axios` over fetch:

```javascript
  .then(response => {
    console.log(response.data);
  })
```

We have to dot into the `response` object to get the api reponse data. _Axios always puts the information sent back to us in a key called `data`_. Try `console.log`ing just the `response`. What is all that stuff in there?

Here's an example of how to use fetch to make the same GET request, for comparision:

```javascript
fetch('https://jsonplaceholder.typicode.com/posts')
  .then(response => {
    return response.json();
  })
  .then(data => {
    console.log(data);
  })
  .catch(error => {
    console.error(error);
  });
```

In this example, we're also making a GET request to the same endpoint, but we have to call `response.json()` to parse the response data before we can use it.

While fetch is built into modern browsers and has a simple API, axios provides a more comprehensive API with features such as automatic transformation of response data, support for request cancellation, and error handling. Ultimately, the choice between axios and fetch depends on the specific requirements of your project.

## `async/await` vs `.then`

`async/await` and `.then` are both ways to handle asynchronous code in JavaScript. `axios` supports both methods of handling asynchronous code, since axios requests return javascript [promise objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise). Here's an example of how to use async/await with axios.get:

```javascript
async function fetchData() {
  try {
    const response = await axios.get('https://jsonplaceholder.typicode.com/posts');
    console.log(response.data);
  } catch (error) {
    console.error(error);
  }
}
```

In this example, we're using the `async` keyword to define a function that fetches data from the https://jsonplaceholder.typicode.com/posts endpoint using axios.get. We're using `await` to wait for the response before continuing with the rest of the code. If there's an error, we catch it and log it to the console using the `try/catch` blocks, which act like `if/else` but only if an error is thrown. In javascript, `try/catch` can be used with any code, not just `async/await`.

```javascript=
try {
    // some code that might throw an error
    throw new Error('oops!') // uh-oh, something bad has happened!
} catch (err) {
    // phew! we 'caught' it
    console.log(err)
}
```

Here's the same example using .then:

```javascript
axios.get('https://jsonplaceholder.typicode.com/posts')
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    // .catch works exclusively with .then, unlike try/catch and async/await
    console.error(error); 
  });
```

The main difference between `async/await` and `.then` is in how they handle asynchronous code. `async/await` allows you to write asynchronous code that looks more like synchronous code, making it easier to read and understand. Originally `.then` syntax and promises where introduced to prevent [callback hell](http://callbackhell.com/), however nesting `.then`s can put you in a similar situation as callback hell, and `async/await` prevents this issue for the tradeoff of a little bit of boilerplate code.

`.then` is still useful, and shouldn't just tossed in the garbage bin. It is wise to consider the context of the code when you choose one method of handling asyncronous code over another. For example, It might not be worth it to go through the trouble of a setting up an `async` function with a `try/catch` for one simple promise. `.then` also lets you handle _each promise_ resolution with a `.catch` instead of having one catch block handle every error case, which can also be useful. 

### Callback hell

![going to hell](https://media3.giphy.com/media/3o6Mbu0rGDREDWrBsY/giphy.gif?cid=ecf05e471ok60eslztagm6t9ixywdzunefpg0deya0clnbom&rid=giphy.gif&ct=g)

#### Nesting `.then` can lead to callback hell 😵‍💫

```javascript
const axios = require('axios');

axios.get('https://swapi.dev/api/people/1/')
  .then(response => {
    const homeworldURL = response.data.homeworld;

    axios.get(homeworldURL)
      .then(response => {
        const population = response.data.population;

        axios.get(`https://swapi.dev/api/planets/?search=${response.data.name}`)
          .then(response => {
            const residentsURLs = response.data.results[0].residents;

            axios.all(residentsURLs.map(url => axios.get(url)))
              .then(responses => {
                const residents = responses.map(res => res.data.name);

                console.log(`Name: ${response.data.name}`);
                console.log(`Homeworld Population: ${population}`);
                console.log(`Residents: ${residents.join(', ')}`);
              })
              .catch(error => {
                console.log('Error fetching residents', error);
              });
          })
          .catch(error => {
            console.log('Error fetching planet', error);
          });
      })
      .catch(error => {
        console.log('Error fetching homeworld', error);
      });
  })
  .catch(error => {
    console.log('Error fetching character', error);
  });
```

#### `async/await` to the rescue! 🙌

```javascript
const axios = require('axios');

async function fetchCharacterInfo() {
  try {
    const response = await axios.get('https://swapi.dev/api/people/1/');
    const homeworldURL = response.data.homeworld;
    
    const homeworldResponse = await axios.get(homeworldURL);
    const population = homeworldResponse.data.population;
    
    const planetResponse = await axios.get(`https://swapi.dev/api/planets/?search=${homeworldResponse.data.name}`);
    const residentsURLs = planetResponse.data.results[0].residents;
    
    const residentsResponses = await axios.all(residentsURLs.map(url => axios.get(url)));
    const residents = residentsResponses.map(res => res.data.name);
    
    console.log(`Name: ${response.data.name}`);
    console.log(`Homeworld Population: ${population}`);
    console.log(`Residents: ${residents.join(', ')}`);
  } catch (error) {
    console.log('Error fetching data', error);
  }
}

fetchCharacterInfo();
```

## Lab: Challenge Problems for Refactoring Axios

For the following challenges, refactor these requests to use `async/await` syntax instead of `.then`. You will need to create a new npm project and install the [axios](https://www.npmjs.com/package/axios) package.

### Single Requests

```javascript 
axios.get('https://swapi.dev/api/films/1/')
  .then(response => {
    console.log(response.data.title);
    console.log(response.data.director);
    console.log(response.data.release_date);
  })
  .catch(error => {
    console.log(error);
  });
```

```javascript
axios.get('https://swapi.dev/api/planets/?page=1')
  .then(response => {
    response.data.results.forEach(planet => {
      console.log(planet.name);
      console.log(planet.climate);
      console.log(planet.terrain);
    });
  })
  .catch(error => {
    console.log(error);
  });
```

### `.then` Chaining

```javascript
axios.get('https://swapi.dev/api/films/1/')
  .then(filmResponse => {
    console.log(filmResponse.data.title);
    return axios.get(filmResponse.data.characters[0]);
  })
  .then(characterResponse => {
    console.log(characterResponse.data.name);
    return axios.get(characterResponse.data.homeworld);
  })
  .then(homeworldResponse => {
    console.log(homeworldResponse.data.name);
  })
  .catch(error => {
    console.log(error);
  });
```

### Nested `.then`

```javascript
axios.get('https://swapi.dev/api/planets/2/')
  .then(response => {
    console.log(response.data.name);
    axios.get(response.data.residents[0])
      .then(residentResponse => {
        console.log(residentResponse.data.name);
	  })
      .catch(error => {
        console.log(error);
      });
  })
  .catch(error => {
    console.log(error);
  });
```

### Bonus: using `Promise.all`

Research how `Promise.all` works before working on these. [MDN's](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all) article might a be good place to start.

```javascript
axios.get('https://swapi.dev/api/species/3/')
  .then(speciesResponse => {
    console.log(speciesResponse.data.name);
    return Promise.all(speciesResponse.data.people.map(personUrl => axios.get(personUrl)));
  })
  .then(personResponses => {
    personResponses.forEach(personResponse => {
      console.log(personResponse.data.name);
    });
  })
  .catch(error => {
    console.log(error);
  });
```

```javascript
const starshipIds = [2, 9, 10];

const promises = starshipIds.map(id => axios.get(`https://swapi.dev/api/starships/${id}`));

Promise.all(promises)
  .then(responses => {
    responses.forEach(response => {
      console.log(response.data.name);
      Promise.all(response.data.pilots.map(pilotUrl => axios.get(pilotUrl)))
        .then(pilotResponses => {
          pilotResponses.forEach(pilotResponse => {
            console.log(`- ${pilotResponse.data.name}`);
          });
        })
        .catch(error => {
          console.log(error);
        });
    });
  })
  .catch(error => {
    console.log(error);
  });
```
