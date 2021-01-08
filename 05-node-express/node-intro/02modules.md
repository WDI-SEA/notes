# Node Modules

## Creating, Exporting, and Importing Modules

Node's module system allows code written in one file to be exported, and then imported into other files. By importing a module \(i.e. a specified section of code\), we can then use that code as if it actually were written in the file we imported it to.

Let's try an example!

### 1. Create your module.

Inside the `my-first-node-project` folder, create a javascript file called `myModule.js`.

In Node, `module.exports` is an object that will hold the code to be exported. We can use dot-notation to add the code we want to export to this object.

Add the following code to your `myModule.js` file:

```javascript
module.exports.beBasic = () => console.log("That's so fetch!")
```

Now, our module.exports object has a key-value pair where the key is `beBasic` and the value is a function.

### 2. Import your module in `index.js`.

This is where the `require` function, specific to Node, comes into play. This function takes one argument: the path to the file that contains the module you are exporting.

In the `index.js` file, write the following code:

```javascript
const myModule = require('./myModule.js');

myModule.beBasic();
```

Run `index.js` via the command line:

`node index.js`

Voila! You've successfully created and imported a module!

Let's add some more code to our module. In `myModule.js`, add the following code:

```javascript
module.exports.beBasic = () => console.log("That's so fetch!")

const count = () => {
    for (let i = 0; i <= 10; i++) {
        console.log(i);
    }
}
```

Now call this new count function from `index.js`:

```javascript
const myModule = require('./myModule.js');

myModule.beBasic();
myModule.count();
```

Try running this code in the command line: `node index.js`

What happened? Why didn't this work?

_The exported module will only contain the code that is encapsulated in the_ `module.exports` _object!_

How do we get our `count` function to run? Make this happen.

Functions aren't the only things we can export! Try adding some other types of data to your module.

### Further Reading

To view a practical example of importing and exporting modules, read [this article](http://www.sitepoint.com/understanding-module-exports-exports-node-js/). You'll see that we can export multiple functions by assigning `module.exports` to an object. This is a pattern that we'll see frequently in Node.

## Using Built-In Modules

It's great to have the flexibility to create our own modules, but Node supplies us with some simple built-in modules \(aka core modules\) that are ready for us to import and use!

### Example: fs module

We will use the `fs` core module \(it stands for "file system"\) to read a text file.

Create a `story.txt` text file inside your project directory and write a short story inside it.

Core modules just need to be imported using the `require` function.

Write the following code to your entry point file:

```javascript
var fs = require('fs');

fs.readFile('story.txt', 'utf8', function(err, data){
    if(err) {
        console.log("There was a problem reading the file.");
    } else {
        console.log(data);
    }
});
```

Run `index.js` to read your story in the terminal!

For more on the `fs` module, see [w3schools](https://www.w3schools.com/nodejs/ref_fs.asp).

Try adding to your story using `fs.write()`.

### Exercise: HTTP core module

In this excercise, you will make a Hello World app from scratch by using the the HTTP core module to spin up an [HTTP server](https://www.quora.com/What-is-an-HTTP-Server-and-what-does-it-do).

![HTTP Request and Response Diagram](https://qph.fs.quoracdn.net/main-qimg-7cf2f16f34b9cdd2652abcf17f85555d)

1. Create a `hello-node` directory.
2. Initialize Node in this directory.
3. Create your entry point file.
4. Import the `http` module into your entry file. \(Hint: use the `require` function\)
5. Create an http server that listens to `port 8000` and writes `Hello, World!` to the client. \(Hint: look up the core http module on [w3schools](https://www.w3schools.com/nodejs/nodejs_http.asp)\)
6. Run the server using the command `node index.js`.
7. Check to see that your program is working by visiting `localhost:8000` in your browser.

<details><summary>SOLUTION</summary>
<p>

```js  
 const http = require('http')  
  
 http.createServer((req, res)=>{  
   res.write('Hello, World!')  
   res.end()  
 }).listen(8000)
 ```

</p>
</details>


