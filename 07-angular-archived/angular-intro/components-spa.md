#Angular Components and SPA

##Angular Components

![angular_components](https://cloud.githubusercontent.com/assets/25366/8970275/a1ab2ee2-35fd-11e5-8b23-65f4159ff7d6.jpg)

#### Modules

Modules are containers for related code.  The concept of *modules* is prevalent throughout programming, and here, it's considered to be a container for our app.

#### Config & Routes

Each AngularJS module has a *config* method that allows us to provide code that runs when a module is loaded.  The *config* method is used most commonly to setup routing, which allows your app to have multiple views.

#### Controller

Controllers in AngularJS serve two primary purposes:

* Initialize the data used for the view they are attached to
* Contain the primary code to respond to user events, such as when a user clicks on a button

A controller is a JS constructor function that is instantiated by the _ng-controller_ directive.

#### Services & Factories

Services provide a way to organize related code and data that can be shared by controllers and even other services. Unlike controllers, which are instantiated and destroyed as the views they are attached to come into and out of view, services are created once (singletons) and persist for the life of the application.

Services should be used to hold the bulk of your application's logic and data, thus keeping controllers focused on what they are responsible for.

#### Directives

Directives are "markers" in HTML - most commonly as attributes and custom element tags. When processed by AngularJS's HTML compiler, they attach behavior to DOM elements or even transform them and/or their children.


#### Filters

Filters are used to transform data. They are very flexible and can be used for formatting text in a view, such as making it all uppercase, or used to filter and sort an array of items.

#### The AngularJS Mindset

Programming a web app with AngularJS requires a different mindset. To use AngularJS effectively, it helps to think of your application being driven by data - you change data, the app responds. We naturally think more procedurally when coding, we attach an event handler and write code to respond.

Let's look at an example of the different approaches.  Say we want an edit form to show when a button is clicked:

* Procedurally, we would attach an event handler to the button. The handler code would select the element and set its display property to something besides "none".
* Using AngularJS, we declare a click handler on the button element.  The handler could set a variable named editMode equal to true, and the view would respond automatically.
* Remember, drive your application using data - your data model is the single source of truth!

##SPA Architecture

Single Page Applications (SPA) are all the rage today. A misconception is that a SPA has only a single view - this is far from the truth!  The single page aspect of a SPA refers to a single page coming from the server, such as our _index.html_ page.  Once loaded, the SPA changes views by using _client-side_ routing, which loads partial HTML snippets called templates.

![spa_architecture](https://cloud.githubusercontent.com/assets/25366/8970635/896c4cce-35ff-11e5-96b2-ef7e62784764.png)

Client-side routing requires something known as a _router_.  A router in AngularJS, at a minimum, is used to define our routes, specify the template for that route, and specify which controller to attach to that view.

Notice that it's possible to recreate this SPA architecture using jQuery, but it would be cumbersome and hard to organize.
