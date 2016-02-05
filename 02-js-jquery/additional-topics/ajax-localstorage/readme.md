#AJAX w/JSON and Local Storage

##Objectives

* Utilize JSON files to separate data from logic
* Use AJAX to load data from JSON files in development and production environments
* Use local storage to store data (semi)-persistently on a user's browser

##Setting up a server

You'll notice the Bootstrap CDN urls start with `//`. This is a wildcard protocol, which means it will use whatever protocol your site is using (`http://` or `https://`). When we're loading a file locally, our protocol is `file:///`, meaning we're accessing a file on our harddrive. Therefore, the default CDN will look for the file on our computer (instead of on the CDN) and won't find it. To fix this we need to run a simple HTTP server.

This is also needed for running local AJAX calls (next section).

to set up the server shortcut edit your `zshrc`:

```
subl ~/.zshrc
```

insert this code near the bottom of the file:

###OSX

```
alias srv="_srv(){open \"http://localhost:\${1-8000}\" && python -m SimpleHTTPServer \$1}; _srv"
```

###Linux

```
alias srv="_srv(){xdg-open \"http://localhost:\${1-8000}\" && python -m SimpleHTTPServer \$1}; _srv"
```

Close and restart your terminal, or run `source ~/.zshrc` to reload the file.

Now you should be able to navigate to the folder of your project (the folder containing index.html), type `srv`, and hit enter. This will start a HTTP server and open your browser to that URL.

You can go back to the site at anytime by going to `http://localhost:8000`.

**NOTE:** The server must be running to access the site.

##AJAX w/JSON

We can load local files, such as JSON files, using AJAX/jQuery. All we need to do is use the local file name. As a security precaution modern browsers will only allow us to do this if we're running a HTTP server. This is to prevent sites from accessing files on our computer that we don't want them to have access to.

####Load data from local JSON file

**script.js**

```js
$.getJSON('data.json',function(data){
    console.log(data);
});
```

**data.json**

```js
{
    "key":"value",
    "number":5,
    "word":"taco",
    "other":[1,2,3,4,5]
}
```

The above code would load the data from `data.json` and console.log it. You can put whatever data you want in the data file. This can be useful if you have larger amounts of data that you don't want to hardcode in your js file.


##Local Storage

HTML5 introduced a feature called localStorage that allows us to store data on a local user's computer. The data is unique for a single person using a specific web site.

Local storage just a object that is retained even if the browser is reloaded. We can get and set values like any other object.

**Set value**

```js
localStorage.name = "Lenny";
```

**Get value**
```js
console.log(localStorage.name);
```


####Using JSON stringify / parse

We can use this to store any data, but it ONLY stores string data. Therefore, we have to use `JSON.parse` and `JSON.stringify` to convert complex data types such as collections into a string and back.

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

All we have to do now is put it together. We can store any javascript data structure (even highly nested objects / arrays) as a string by simply using stringify / parse.

**Saving data**

```js
var listValues = ['one','two','three','fidy'];
localStorage.myList = JSON.stringify(listValues);
```

**Loading data**

```js
var listValues = JSON.parse(localStorage.myList);
```

####Preventing errors

There is still one problem. If we run `JSON.parse` on something that isn't valid JSON it will throw an error and crash our entire site. There are two ways to avoid this.

####Option 1 - use an if statement to check the data

```js
if (localStorage.myList) {
  var listValues = JSON.parse(localStorage.myList);
}
```

Here we are just ensuring that `localStorage.myList` has something in it. It doesn't ensure it's valid JSON, but it will work in most situations (provided your code that does the saving is good).


####Option 2 - use try / catch (recommended)

```js
try {
  var listValues = JSON.parse(localStorage.myList);
  //do something with listValues here
  //other code in the try will only run if JSON.parse has no errors
} catch (err) {
  //optionally put code here to do something if it doesn't load
  
  //set default value (empty array)
  var listValues = [];
}
```

The way a `try / catch` works is that if any code inside of the try block (between the curly braces) causes an error it will jump to the code inside of the `catch` block. Any subsequent lines in the try block will be skipped.

This means if anything is wrong with the data in local storage it won't throw an error / crash. Instead we will "catch" the error and load a default value (or do nothing).

##Example

For more information about these topics, see the examples in this repository.
