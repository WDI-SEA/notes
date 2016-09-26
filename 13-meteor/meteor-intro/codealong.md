#Meteor Codealong

##To Start

We're going to be building an image-sharing board for our first application in Meteor. To begin, let's get Meteor installed on our computers:

```bash
curl https://install.meteor.com/ | sh
```

Next we'll jump to a place in our filesystem where we want the project and run this command:

```bash
meteor create image-board
cd image-board
meteor npm install
```

 * **meteor npm install** Another recent addition driven by community input has been the inclusion of **npm** support. Since there are so many great NPM packages out there and Meteor utilizes node, the community wanted a way to install those packages and utilize them. We'll cover packages more later.

This will automatically scaffold out a basic Meteor app for us. We can begin running the Meteor app right away by using the ```meteor``` command. It's best to actually leave the server running, much like nodemon and you'll see that Meteor takes care of building our code and even refreshing our browser, cool!

So just by running that command, we've setup a full-stack application complete with real-time DB interactions! 

Go to ```localhost:3000``` to see your app in action.

##File Structure

Here is a reference of a default Meteor file structure:

```bash
imports/
  startup/
    client/
      index.js                 # import client startup through a single index entry point
      routes.js                # set up all routes in the app
      useraccounts-configuration.js # configure login templates
    server/
      fixtures.js              # fill the DB with example data on startup
      index.js                 # import server startup through a single index entry point

  api/
    lists/                     # a unit of domain logic
      server/
        publications.js        # all list-related publications
        publications.tests.js  # tests for the list publications
      lists.js                 # definition of the Lists collection
      lists.tests.js           # tests for the behavior of that collection
      methods.js               # methods related to lists
      methods.tests.js         # tests for those methods

  ui/
    components/                # all reusable components in the application
                               # can be split by domain if there are many
    layouts/                   # wrapper components for behaviour and visuals
    pages/                     # entry points for rendering used by the router

client/
  main.js                      # client entry point, imports all client code

server/
  main.js 
```

Meteor apps have a few key folders that the platform looks for so that it knows where to execute code. The ```client``` folder is for client-side code and the ```server  ``` folder is for server-side code. The nice thing is that Meteor will automatically find our JS files where they live and execute them in the correct environment for us. This is known as **Isomorphic** code, meaning you write code that can be run on the client-side, server-side, or even both!

The next important directory is the ```imports``` directory. Any code in this directory is not executed until we **import** that module into another part of our client or server code.

[Application Structure Doc](https://guide.meteor.com/structure.html)

##Replace Default Code

Next we're going to start building our own code into the default app, which means wiping out the code that is presently there.

First lets create our **imports** folder and then a sub folder called **ui**
where we'll put our separate components.

```bash
mkdir imports
mkdir imports/ui
mkdir imports/ui/body
touch imports/ui/body/body.html imports/ui/body/body.js
```

In our **body.html** file we'll put this code:

```html
<body>
  <div class="container">
    <header>
      <h1>Image Board</h1>
    </header>
 
    <ul>
      {{#each images}}
        {{> image}}
      {{/each}}
    </ul>
  </div>
</body>
 
<template name="image">
  <li><img src={{url}}></li>
</template>
```

The curly braces should seem familiar to our Angular lessons. The template system we're actually using however is the **Blaze** templating system built into Meteor. Later we'll learn how to swap to Angular.

Now our **body.js** file:

```javascript
import { Template } from 'meteor/templating';
 
import './body.html';
 
Template.body.helpers({
  images: [
    { url: 'http://img.memecdn.com/fat-cats-are-cannibals_fb_3338377.jpg' },
    { url: 'http://orig10.deviantart.net/3c0f/f/2014/287/a/d/funny_fat_cats_with_guns_300x300_by_felicaviris-d82s263.jpg' },
    { url: 'http://www.vmirocks.com/wp-content/uploads/2012/05/fat-cat-rnr-300x300.png' },
  ],
});
```

and then finally an import in our **client.js**

```javascript
import '../imports/ui/body.js';
```

So what we've done here is remove the default client code and instead started utilizing Meteor's imports folder and a component based structure. Each component typically has a view file (.html) and view logic (.js), similar to how we coupled Angular components.

Finally we'll add some css to **main.css**

```css
body {
  font-family: sans-serif;
  background-color: #315481;
  background-image: linear-gradient(to bottom, #315481, #918e82 100%);
  background-attachment: fixed;
 
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
 
  padding: 0;
  margin: 0;
 
  font-size: 14px;
}
 
.container {
  max-width: 600px;
  margin: 0 auto;
  min-height: 100%;
  background: white;
}
 
header {
  background: #d2edf4;
  background-image: linear-gradient(to bottom, #d0edf5, #e1e5f0 100%);
  padding: 20px 15px 15px 15px;
  position: relative;
}
 
#login-buttons {
  display: block;
}
 
h1 {
  font-size: 1.5em;
  margin: 0;
  margin-bottom: 10px;
  display: inline-block;
  margin-right: 1em;
}
 
form {
  margin-top: 10px;
  margin-bottom: -10px;
  position: relative;
}
 
.new-task input {
  box-sizing: border-box;
  padding: 10px 0;
  background: transparent;
  border: none;
  width: 100%;
  padding-right: 80px;
  font-size: 1em;
}
 
.new-task input:focus{
  outline: 0;
}
 
ul {
  margin: 0;
  padding: 0;
  background: white;
}
 
.delete {
  float: right;
  font-weight: bold;
  background: none;
  font-size: 1em;
  border: none;
  position: relative;
}
 
li {
  position: relative;
  list-style: none;
  padding: 15px;
  border-bottom: #eee solid 1px;
}
 
li .text {
  margin-left: 10px;
}
 
li.checked {
  color: #888;
}
 
li.checked .text {
  text-decoration: line-through;
}
 
li.private {
  background: #eee;
  border-color: #ddd;
}
 
header .hide-completed {
  float: right;
}
 
.toggle-private {
  margin-left: 5px;
}
 
@media (max-width: 600px) {
  li {
    padding: 12px 15px;
  }
 
  .search {
    width: 150px;
    clear: both;
  }
 
  .new-task input {
    padding-bottom: 5px;
  }
}
```

Notice when we make changes to files, our app automatically refreshes. When we make changes to client code, it'll just rebuild that code and refresh the browser. But when we make changes to the server code it'll restart our entire application.

##Using MongoDB for data

So far we've only wired up static data in our client-side code. Now lets swap that out with an actual DB collection for our images.

First we need to create a new folder in imports and then create a file in that folder:

```bash
mkdir imports/api
touch imports/api/images.js
```

**images.js** is where we'll be instantiating our MongoDB collection to store urls in. Here is the code:

```javascript
import { Mongo } from 'meteor/mongo';
 
export const Images = new Mongo.Collection('images');
```

then we need to import this collection on the server-side in **server/main.js**:

```javascript
import '../imports/api/images.js';
```

and then import the collection in our client code as well in **body.js**:

```javascript
import { Template } from 'meteor/templating';
 
import { Images } from '../api/images.js';
 
import './body.html';
 
Template.body.helpers({
  images() {
    return Images.find({});
  },
});
```

Now instead of returning a static array in our helper, we're returning a MongoDB query, which will return the data from the collection. By importing the collection on both the client and the server we've made the collection code **isomorphic** which is how we facilitate our **latency-compensation**.

Next up we'll utilize mongo shell commands to instantiate data in our collection and then move that to a form on our client.

##Using Meteor mongo command

A handy feature of Meteor is that it's tied directly to MongoDB and we can automatically connect to our apps DB using the ```meteor mongo``` command in our app directory!

Once we're in the mongo shell we can start adding data to our **images** collection:

```bash
> db.images.insert([{ url: 'http://img.memecdn.com/fat-cats-are-cannibals_fb_3338377.jpg', createdAt: new Date()},{ url: 'http://orig10.deviantart.net/3c0f/f/2014/287/a/d/funny_fat_cats_with_guns_300x300_by_felicaviris-d82s263.jpg', createAt: new Date() },{ url: 'http://www.vmirocks.com/wp-content/uploads/2012/05/fat-cat-rnr-300x300.png', createAt: newDate() }])
```

What will happen is when the collection changes, LiveQuery will send a message to our client over DDP, the client will update it's Minimongo, and the UI will update to reflect that data. Cool!