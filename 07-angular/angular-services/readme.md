#Angular Services

##Objectives

* Create a service to provide a RESTful resource using $resource
* Describe the difference between a factory and a service

## What are Angular Services?

Each web application you build with Angular is composed of objects that collaborate to get stuff done. These objects need to be instantiated and wired together using [dependency injection](https://docs.angularjs.org/guide/di) for the app to work.

When you inject a dependency into a module, e.g.

```javascript
angular.module("StarWarsApp", ['ui.bootstrap']);
```

The injector service needs to know how it should insert these objects. It does this by using **recipes**.

