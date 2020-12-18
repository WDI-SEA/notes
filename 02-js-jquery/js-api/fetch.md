# Fetch

`fetch` is a built-in Javascript function that allows us to make API requests using Javascript.

The basic syntax for `fetch` is as follows:

```javascript
fetch(requestURL)
    .then((responseData)=>{
        // Fetch will package the response into an object with some methods that allow us to do some useful things with the response.
        // Use the .json() method to return the data in JSON format
            return responseData.json();
    })
    .then((jsonData)=>{
        // whatever we return in the first .then promise will be passed into this callback function
        // do some stuff with the jsonData here
    })
    .catch(function(error){
        // any errors encountered in the request or the .then promises above will be passed into this callback
        console.log("Oh no, there's been an error!", error);
    })
```

## Fetching from Reddit

Let's use fetch to see how we could get the kittens search query data from reddit inside of our javascript. This will allow us to retrieve that data and then do whatever we want with it without disturbing the user experience of our web-page.

* Create a basic Hello World app called `fetch practice` using html, css, and javascript.
* Once your app is up and running, add the following fetch call to the javascript:

```javascript
console.log('Script is running');

fetch('https://www.reddit.com/search.json?q=kittens') 
  .then((responseData)=>{
    return responseData.json();
  })
  .then((jsonData)=>{
    console.log("Here is the data:", jsonData);
  })

console.log('Just fired AJAX request!');
```

What order will the `console.log`s appear in? Why?

This is all fine and dandy, but why would we do this? How do we incorporate API data into our webpage, once we have it? DOM Manipulation, of course! Let's look at another example.

## Random User Example: Displaying data to the page

In this example, we'll display a list of random people using fetch and the [Random User API](https://randomuser.me/)

**index.html**

```markup
<h1>People</h1>
<ul id="peopleList"></ul>
```

### First let's set up our fetch call and look at our data in the console

Look through the documentation and experiment in your browser to see if you can find the proper endpoint that returns data about one random user.

**script.js**

```javascript

const requestUrl = 'https://randomuser.me/api/'

fetch(requestUrl)
    .then((responseData)=>{
        return responseData.json();
    })
    .then((jsonData)=>{
        // the above .then passed our returned data into this callback
        console.log(jsonData);
        // now we can see that the data we want is nested under an inner 'results'
        console.log(jsonData.results)
    })
    .catch((error)=>{
        // If any error is sent back, you will have access to it here.
        console.log("error!!!:", error);
    });
```

Now look through the documentation again and figure out which endpoint you need to ping to get 10 random users back, instead of just one! Change the `requestUrl` accordingly.

### Now let's get some of this data rendering on the page!

Write an `addPerson` function that takes a `person` argument (a single random user from the API data), creates a new list item that contains the person's first and last name, then adds that list item to the existing unordered `peopleList` list.

**script.js**

```javascript
document.addEventListener("DOMContentLoaded", ()=>{

    const requestUrl = "https://randomuser.me/api/?results=10";

    const addPerson = (person)=>{
        let li = document.createElement("li");
        li.textContent = person.name.first, person.name.last;
        peopleList.appendChild(li);
    }

    fetch(requestUrl)
    .then((responseData)=>{
        // Fetch will package the response into an object with some methods that allow us to do some useful things with the response.
        // Use the .json method to return the data in JSON format
        return responseData.json();
    })
    .then((jsonData)=>{
        // the above .then passed our returned data into this callback
        console.log(jsonData);
        // now we can see that the data we want is nested under an inner 'results'
        console.log(jsonData.results)
        // store this array of objects in a 'people' variable
        let people = jsonData.results;
        people.forEach(addPerson);
    })
    .catch((error)=>{
        // If any error is sent bac, you will have access to it here.
        console.log("error!!!:", error);
    });
});
```

### Exercise

Add to the above code so that we see a photo for reach random user too!

## Building query from user input

Let's let the app user determine how many random people they want to display.

Add a form to the html:
```html
<body>
    <h1>People</h1>
    <form id="form">
        <input id="input" type="number" min=1 value=1>
        <input type="submit">
    </form>
    <ul id="peopleList"></ul>
    <script src="app.js"></script>
</body>
```

Now add an event listener to the form that listens for the form submission event and prints the user's input:
```javascript
    form.addEventListener('submit', (e)=>{
        e.preventDefault()
        console.log("user input is:", input.value)
    })
```

Great! Now that we have the user input, once the form is submitted, let's move our fetch call *into* the form submission event listener, so random users are only added to the list when the form is submitted. How do you need to modify the `requestUrl` and fetch call to make this happen?

```javascript
const requestUrl = "https://randomuser.me/api/?results=";

document.addEventListener("DOMContentLoaded", ()=>{

    form.addEventListener('submit', (e)=>{
        e.preventDefault()
        fetch(requestUrl+input.value)
        .then((responseData)=>{
            return responseData.json();
        })
        .then((jsonData)=>{
            // console.log(jsonData);
            // console.log(jsonData.results)
            let people = jsonData.results;
            people.forEach(addPerson);
        })
        .catch((error)=>{
            console.log("error!!!:", error);
        });
    })

    const addPerson = (person)=>{
        let li = document.createElement("li");
        li.textContent = person.name.first, person.name.last;
        peopleList.appendChild(li);
    }

});
```

### Bonus Exercises:
* Clear the original list each time the form is submitted (that way it's not just creating a longer and longer list each time)
* Refactor this code so the fetch call happens in a function called `fetchPeople` that takes an `endpoint` argument.
