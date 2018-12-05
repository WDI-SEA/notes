# Fetch

`fetch` is a built-in Javascript function that allows us to make API requests using Javascript.

The basic syntax for `fetch` is as follows:

```js
fetch(requestURL)
	.then(function(responseData){
		// Fetch will package the response into an object with some methods that allow us to do some useful things with the response.
		// Use the .json() method to return the data in JSON format
			return responseData.json();
	})
	.then(function(jsonData){
		// whatever we return in the first .then promise will be passed into this callback function
		// do some stuff with the jsonData here
	})
	.catch(function(error){
		// any errors encountered in the request or the .then promises above will be passed into this callback
		console.log("Oh no, there's been an error!", error);
	})
```

---

## Example

In this example, we'll display a list of random people using fetch and the [Random User API](https://randomuser.me/)

**index.html**
```html
<h1>People</h1>
<ul id="people"></ul>
```

### First let's look at our data in the console

**script.js**
```js

fetch(requestUrl)
	.then(function(responseData){
		return responseData.json();
	})
	.then(function(jsonData){
		// the above .then passed our returned data into this callback
		console.log(jsonData);
		// now we can see that the data we want is nested under an inner 'results'
		console.log(jsonData.results)
	})
	.catch(function(error){
		// If any error is sent back, you will have access to it here.
		console.log("error!!!:", error);
	});

```

### Now let's get some of this data rendering on the page!

**script.js**
```js
document.addEventListener("DOMContentLoaded", function(){
	
	const ul = document.getElementById("people");
	const requestUrl = "https://randomuser.me/api/?results=10";

	function addPerson(person) {
		let li = document.createElement("li");
		li.textContent = person.name.first, person.name.last;
		ul.appendChild(li);
	}

	fetch(requestUrl)
		.then(function(responseData){
			// Fetch will package the response into an object with some methods that allow us to do some useful things with the response.
			// Use the .json method to return the data in JSON format
			return responseData.json();
		})
		.then(function(jsonData){
			// the above .then passed our returned data into this callback
			console.log(jsonData);
			// now we can see that the data we want is nested under an inner 'results'
			console.log(jsonData.results)
			// store this array of objects in a 'people' variable
			let people = jsonData.results;
			people.forEach(addPerson);
		})
		.catch(function(error){
			// If any error is sent bac, you will have access to it here.
			console.log("error!!!:", error);
		});
});

```

### Exercise

Add to the above code so that we see a photo along with the random user.


