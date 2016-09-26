#Introduction to Meteor

##Objectives

* Discuss the parts of a Meteor app
* Install Meteor CLI
* Build ToDo app using Meteor

##Meteoric Development

Meteor is a full-stack Javascript development platform meant to be a complete solution for hitting both web and mobile devices while having a single codebase. Or in their words:

Meteor is a full-stack JavaScript platform for developing modern web and mobile applications. Meteor includes a key set of technologies for building connected-client reactive applications, a build tool, and a curated set of packages from the Node.js and general JavaScript community.

##Parts of a Meteor App

![Meteor Structure](http://image.slidesharecdn.com/meteor-intro-2015-rev1-150710171349-lva1-app6891/95/meteor-intro2015-17-638.jpg?cb=1436552556)

Meteor's true power comes from a few different key technologies that, when brought together, allow for real-time, native-like interactions.

###No REST for the wicked

Up until this point we've been building purely RESTful backends that connect to a DB. With Meteor we're leaving the slower **Request/Response** cycle behind and instead utilizing some other tech to facilitate data transfer.

####Database: MongoDB
Let's start at the database level. Currently Meteor utilizes good 'ol MongoDB for all it's persistent data storage. This means that all the stuff about Mongo that we've been learning is completely applicable and you'll see that we'll be crafting queries in a very similar way to previous work.

There are plans in the works to utilize SQL DB's with Meteor as well, but nothing is out of beta stages.

####LiveQuery
Now for our first piece awesome Meteor tech. Baked into each Meteor app is something called LiveQuery. LiveQuery allows you to make a subscription to certain subsets of your DB. What this means on a basic level is that the data in your DB is watched by LiveQuery and whenever something changes, LiveQuery will alert the rest of the app about the change!

####DDP
Next up on our list of cool Meteor tech is our data transfer protocol, DDP or Distributed Data Protocol. This is a client/server protocol created by the Meteor development group. Built on top of websocket functionality, DDP allows consistent connections between the server and any connected clients. When LiveQuery detects a change on the DB it will send a message to the connected clients via DDP.

DDP utilizes a **Publish and Subscribe** system that we will see in action later.

####Minimongo - Client-Side Cache
While having the LiveQuery watch the DB and send messages to each connected client is helpful and extremely quick, there will be times where the changes just aren't appearing quick enough on a client's device. This is due to **latency** between when the client changes the DB and when the message gets to the other connected clients.

Meteor's answer to this issue is to utilize a client-side storage mechanism called **Minimongo**. Like the name implies, Minimongo is a smaller version of the MongoDB that is being utilized on the backend. It is created on the client's device and stores a copy of the data that a client is subscribed to.

So when a client makes changes to the data, Meteor will do two things. First is send off the message to the server over DDP. Next it makes the change right away to the Minimongo to make the client UI change. Once the message reaches the server and actual DB, any differences in the data are corrected. This process is called **latency compensation**

####Front-End Framework
The final piece of our Meteor app is the front-end framework. For it's initial release, Meteor came bundled with a custom framework called **Blaze**. This framework was built primarily for Meteor and therefore had it's unique structure in mind. As of Meteor version 1.2 however, support for Angular and React was introduced. Now it is up to the developer which front-end framework they want to work with, making Meteor that much more accessible.

####The Full Picture
![Data Transfer](http://image.slidesharecdn.com/meteor-intro-2015-rev1-150710171349-lva1-app6891/95/meteor-intro2015-14-638.jpg?cb=1436552556)

##Reactive Programming
A quick note about coding with Meteor. Since it functions as a real-time app, most of the code we will be writing will be **Reactive**. This means we write a piece of code to react to a certain event. We've already experienced this a bit with DOM event-handlers.

##Enough Talk

While discussing the tech is always worthwhile, lets get our hands dirty and actually build a Meteor app! If you'd like to read up some more on Meteor and what it can do, check out the API docs:

[Meteor API Docs](http://docs.meteor.com/)
