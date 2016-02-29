#Asset Pipeline and Frontend in Rails

##Objectives

* Incorporate JavaScript, CSS, images, and other static files into a Rails application
* Understand the Asset Pipeline
* Utilize helper methods/tags for including static resources
* Use `gon` to pass data to the frontend
* Incorporate AJAX into a Rails application

We can work with JavaScript, CSS, and images in Rails just like we did in our frontend only projects. Rails uses the concept of an Asset pipeline to handle pre-processing and loading of static assets.

##Javascripts

To load javascript files in rails we simply create `.js` files in the `app/assets/javascripts` directory and rails will automatically load them in the head of the page using `<script>` tags.

To adjust the load order we just the `//=` lines at the bottom of `application.js`

####application.js

application.js is used to load other javascript files and allows us to change the load order of the files. You *CAN* put javascript code directly in that file

At the bottom of application.js there are a few lines that look like comments and start with `//=` these are used to specify which files to load and in what order. The last line (`//= require_tree .`) loads all of the files in the javascripts directory that aren't loaded explicitly above.

For example, if we had a file called `importantScript.js` in our javascripts directory and we needed it to be loaded first we could simply do something like this...

```js
//= require 'importantScript.js'
//= require jquery_ujs
//= require turbolinks
//= require_tree .
```

##Stylesheets

Rails uses SASS, which is a preprocessor for css that allows us to use some additonal features that standard css doesn't support. These files end with the `.scss` file extension and are processed on the server (backend) before they are sent to the user/browser as plain css.

Just like with javascript rails will auto-load any css or scss file that are in `app/assets/stylesheets`.

Also, similar to javascript we can adjust the load order by editing the bottom off `application.css`, and again we should avoid putting css directly in this file.


##Images

We can load images by placing them in `app/assets/images` and using the rails `image_tag` helper to load them for us.

####Images in views (erb)

If we have a file `app/assets/images/pic.jpg` we can display it in an erb file like this:

```html
<%= image_tag 'pic.jpg' %>
```

We can also get a string of the image url/path by calling `image_url` or `image_path`.

####Images in css (using sass/scss)

We also have access to a `image_url` helper method in `scss` (sass) files. It will be used in place of the standard css `url('/path/to/image.jpg')` format.

```css
.some-class{
  background-image: image_url('pic.jpg');
}
```

**NOTE:** make sure the file is named `scss` and not just `css`. The `css` files are served to the browser as-is (no pre-processing), but `scss` are run through the sass pre-proccessor first which will run the `image_url` method and insert the correct image path.


##Passing data to the frontend (gon)

We can pass data from a controller to frontend javascript using a gem called "gon" which allows us to easily pass any data from the backend to the frontend.

####gon setup

To use gon (just like any other gem) we need to add it to our `GemFile`. After adding it remember to run `bundle` and then restart your server with `rails s`

**in GemFile**

```ruby
gem 'gon`
```

Then we need to add a tag inside of our `<head>` tag that will load the backend values as javascript so we can use them in our frontend.

**in layouts/application.html.erb**

```html
<%= include_gon %>
```

Be sure to add this line BEFORE  `javascript_include_tag` that way the variables it defines will be available in your `.js` files.

####Using gon

gon is very simple to use. It exposes a varible called `gon` the controller. `gon` is a hash that we can add any values to and they will be available on the frontend automatically.

**In controller**

```ruby
def index
    gon.something="hello"
    gon.people = ['Lenny','Brian','Daniel']
    gon.tasks = Task.all
end
```

**In JS**

```javascript
console.log(gon.something);
//outputs: "hello"

console.log(gon.people);
//output: ['Lenny','Brian','Daniel']

console.log(gon.tasks);
//outputs: an array of objects for all tasks in the database
```

####Pitfalls

There is only one major "gotcha" with gon and that is that gon won't be defined in javascript unless you assign somethign to it in the controller.

Assume we didn't assign any values to gon in the controller...

**in JS**

```javascript
console.log(gon.taco);
```

This would throw an error because `gon` is undefined. To avoid this problem we just need to check it using `typeof`.

```javascript
if(typeof gon != 'undefined'){
    console.log('taco is', gon.taco);
}else{
    console.log('there is no gon (or taco)');
}
```

##AJAX

We can use jQuery to send AJAX calls to our server the same way we did it with other servers before. Of course, we also need to handle the backend code to make the server respond to the request apporpirately.

####AJAX Delete Example

Sometimes we want to perform actions without reloading the page. There are many AJAX strategies this is just one of them.

**In our view (erb)**

```html
<%= link_to 'delete', task, :class=>'js-delete-btn' %>
```

If we are doing anything that is using rails' built-in resource routing it is in our best interest to use the `link_to` helper to determine the delete url. We can simply add a class to this link which we can use in JS to override it's behavior.


**In our JS file**

```javascript
$('.js-delete-btn').on('click',function(e){
    e.preventDefault();
    var btn=$(this);
    $.ajax({
      url:  btn.attr('href'),
      method:'DELETE',
      dataType:'json'
    }).done(function(data){
      if(data){
        btn.closest('tr').remove();
      }
    })
});
```

Next, we listen for the click event, prevent it from doig it's default action (navigating to a url), make an AJAX call to the server, and then modify the view (through jQuery).

Notice that we're loading the URL from the href attribute of the link tag (allowing the rails `link_to` tag to tell us the url)


**In our controller (ruby)**

```rails
def destroy
  result = Task.destroy params[:id]
  # redirect_to :tasks
  respond_to do |format|
    format.html {redirect_to :tasks}
    format.json {render json: result}
  end
end
```

In our controller we need to use the `respond_to` method to tell rails to respond differently to different types of requests.

In this example we...
* redirect to the tasks index page for regular (html) requests.
* return json data for AJAX requests (which will be received by the `.done(function(data){ ... });` function in javascript.


##Additional Reading

* [Rails Guides - Assets Pipeline](http://guides.rubyonrails.org/asset_pipeline.html)
* [Rails API - Asset Tag Helpers](http://api.rubyonrails.org/classes/ActionView/Helpers/AssetTagHelper.html)
* [SASS documentation](http://sass-lang.com/documentation/file.SASS_REFERENCE.html)
* [gon gem](https://github.com/gazay/gon)
* [jQuery Docs - AJAX](http://api.jquery.com/jquery.ajax/)
