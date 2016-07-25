#Recipes

The main recipe that the injector needs to inject something into a module is called the **provider** recipe. However, on top of that, there are five other types of recipes which the injector uses to "cook" the recipe slightly differently. These recipes are:

1. **Factory**
2. **Service**
3. **Provider**
4. **Constant**
5. **Value**

Each of these create a new object when they are used. They also follow a couple different properties:

####Service Properties

Angular [services](https://docs.angularjs.org/guide/services) are:

- **Lazily instantiated** – Angular only instantiates a service when it is needed. If we never use the service, it's never instantiated.
- **Singletons** – Each component dependent on a service gets a reference to the single instance. If we use a service in multiple controllers, each controller refers to the **same instance**
- **Persistent** - Once instantiated, unlike a controller, it persists throughout the lifetime of our app.

If your app needs data from an API or database, we probably don't want to keep loading that same data every time we change routes. Fetching that data once and holding it in a service makes a lot of sense.

Also, because services are persistent singletons, they provide a mechanism to **share data between controllers.**

### Factory vs service?

Factory and Service are the most commonly used recipes. However, if factories and services are so similar, what's the difference? They look quite similar:

```js
angular.service('myService', myServiceFunction);
angular.factory('myFactory', myFactoryFunction);
```

Well here's the difference:

**Service**

Services are instantiated by the injector using the `new` keyword. Therefore, it's like a constructor, and we need to attach properties to `this`.

```js
app.service('myService', ['$http', function($http) {
  this.get = function() {};
}]);
```

**Factory**

Factories are instantiated by being called like functions. Therefore, it's like a function, and we need to return something.

```js
app.factory('myFactory', ['$http', function($http) {
  return {
    get: function() {}
  }
}]);
```

For the most part, we'll use the factory. Why? **A service is called like a constructor, therefore it always returns an object** Factories give us more flexibility, because the factory can return an object, a function reference, or any value at all.
