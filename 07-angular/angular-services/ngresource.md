#Resources

A handy module for interacting with RESTful APIs is `ngResource`. Instead of using `$http` over and over again, we can use `ngResource` to define an endpoint with HTTP verbs.

###Illustrating $resource

Before we dive into the service, let's see a simple example of using `ngResource`.

```js
var resourceObject = $resource('http://localhost:3000/api/airplanes/:id');
```

We'll be showing a more complete example in a moment, but notice that we can create a resource by using the `$resource` service. By providing a URL with a spot for an `id` parameter, this object will provide us the following methods:

```js
resourceObject.get([params], [success], [error]) //GET :id
resourceObject.save([params], postData, [success], [error]) //POST
resourceObject.query([params], [success], [error]) //GET all
resourceObject.remove([params], postData, [success], [error]) //DELETE :id
```

Woah, a RESTful interface for working with a RESTful API.
