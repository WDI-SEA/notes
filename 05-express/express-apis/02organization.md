#Organizing an Express App

## Layouts

Another layout option is to create a layout and have a body that is replaced with content (more similar to Rails, with a predetermined header/footer). In order to do this, another module must be installed.

### Example

**Step 1:**
Install `express-ejs-layouts` via
```
npm install --save express-ejs-layouts
```

**Step 2:**
Require the module and add it to the app.
```js
var ejsLayouts = require("express-ejs-layouts");
app.use(ejsLayouts);
```

**Step 3:**
In the root of the views folder, add a layout called `layout.ejs`

**layout.ejs**
```html
<!DOCTYPE html>
<html>
<head>
  <title>Page</title>
</head>
<body>
  <%- body %>
</body>
</html>
```

This layout will be used by all pages, and the content will be
filled in where the `<%- body %>` tag is placed.


## Controllers

We have been placing all routes into `index.js` when creating a Node/Express app, but this can get cumbersome when dealing with many routes. The solution is to separate routes into separate files and attach the routes to the Express router.

**index.js**
```js
var peopleCtrl = require("./controllers/people")
app.use("/people", peopleCtrl);
```

**controllers/people.js**
```js
var express = require("express");
var router = express.Router();

router.get("/", function(req, res) {

});

module.exports = router;
```
