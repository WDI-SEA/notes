##Additional Topics

###Getting the Current User

We didn't use the `currentUser` function in our `Auth` service, but it's a great way to get the current user's data without making another request to the server, since it's already encoded in the token. This is also why we ensured that the password wasn't sent back to the server, since the hash could have been decoded and visible!

###Making Queries to other APIs

It's possible for an application to query multiple different APIs, such as a Node backend, a weather API, and a recipe API. In that case, we need to **alter our AuthInterceptor** so it doesn't send our authentication data to these other APIs! Not only would that be unwise in terms of security, but applications often give error messages when invalid tokens are passed.

We can adjust the `AuthInterceptor` by having a blacklist/whitelist of endpoints. Here's an example of `AuthInterceptor` with a blacklist.

```js
//...

.factory('AuthInterceptor', ['Auth', function(Auth) {
  // if querying other APIs, add URLs to this array
  var excludedEndpoints = [
    'https://swapi.co/api/films'
  ];

  return {
    request: function(config) {
      var token = Auth.getToken();
      var excludedEndpoint = excludedEndpoints.indexOf(config.url) > -1;
      if (token && !excludedEndpoint) {
        config.headers = config.headers || {};
        config.headers.Authorization = 'Bearer ' + token;
      }
      return config;
    }
  }
}])
```

Note that for a whitelist, we'd have to account for URLs that match a particular **pattern**, like `/api/recipes/1`, `/api/recipes/2`, etc. This would be a good application of regular expressions.

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions

###Making Alerts

Now that authentication has been set up, what about those cool Bootstrap alerts? Since authentication involves going from **controller to controller**, we'll need yet another **service** in order to add Bootstrap modals to our page. Here's an example service.

```js
//..

.factory('Alerts', [function() {
  var alerts = [];

  return {
    clear: function() {
      alerts = [];
    },
    add: function(type, msg) {
      alerts.push({type: type, msg: msg});
    },
    get: function() {
      return alerts;
    },
    remove: function(idx) {
      alerts.splice(idx, 1);
    }
  }
}])
```

Remember IIFEs (Immediately-Invoked Function Expressions)? In a sense, this factory acts like one! The `alerts` array is encapsulated and can only be altered through a set of endpoints:

* clear
* add
* get
* remove

Because `Alerts` is a service, a singleton, and able to be injected into controllers, `Alerts` will be our app-wide container for storing alerts.

**Let's try together:** Using the `Alerts` service provided above, incorporate alerts into the Secret Recipes app. Additionally, try to add **ng-show** and **ng-hide** directives for the links in the navbar. You'll need to keep a few things in mind:

* How will an alert be added after signup, login, and logout?
* How will the alerts be displayed? (May benefit to make an Alerts controller with a template, similar to the `NavCtrl`)
* Can we use UI Bootstrap to provide additional functionality?
