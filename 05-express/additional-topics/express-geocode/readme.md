#Geocoding with Node and Google Maps

## Objectives

* Understand the reversable process of geocoding.
* Utilize geocoding with a geocoder and Sequelize hooks
* Use Google Maps to add geocoordinates to a map.

## Geocoding Addresses

**What is geocoding?** - The process of converting a description of a place to geographic coordinates.

### Example:

"Seattle, WA" -> **geocode** -> {lat: 47.6062095, lng: -122.3320708}

### Using Geocoder
First lets install the package into a new folder. Note that we'll be using Google's geocoder API.

```
mkdir geocode_example
cd geocode_example

npm init
npm install --save geocoder
```

### Try this in a separate file:

```js
var geocoder = require('geocoder');
geocoder.geocode("Space Needle", function(err, data) {
  console.log(data.results[0].geometry.location);
});
```

### Geocoding with a database model

Lets create a model where that we can use to setup some map content.

```
npm install --save sequelize pg pg-hstore

sequelize init
sequelize model:create --name place --attributes name:string,address:string,lat:float,lng:float
```

We have added fields for latitude and longitude. We've added them to our
model, because we will be using the `geocoder` npm model to have the
fields automatically fillled in when creating new entries.

Geocoder will be used on our model, we need to include it on the `place.js` model.

```js
var geocoder = require('geocoder');
```

and add a hook below `classmethods`

```js
hooks: {
  beforeCreate: function(place, options, fn) {
    geocoder.geocode(place.address, function(err, data) {
      if (err) return fn(err, null);
      place.lat = data.results[0].geometry.location.lat;
      place.lng = data.results[0].geometry.location.lng;
      fn(null, place);
    });
  }
}
```

Once your database configuration is setup, run database migrations. Then, let's create a simple Express app with a form for inputting a place and address.

##Using Google Maps
Google Maps is the most popular mapping app on the web. We'll be using it to display points on a map.

### Getting an API key
You'll need a Google/Gmail account first before setting up the API key. Once you've got that, head to the [Google developers console](https://console.developers.google.com/). From there, click on "Use Google APIs". You'll see a bunch of links to various APIs, and the only ones you care about right now are the Maps APIs.

The two APIs you need to enable are the Google Maps JavaScript API, and the Google Maps Embed API. You might want to use the Google Maps Places API eventually, so go ahead and enable that too.

###Add a map div

In the page you want to embed a map in, set up a div like this:

```html
<div id='map'></div>
```

and set a height in your css...

```css
#map {
  height: 500px;
}
```

And that's really all you need. The map will automatically scale to the size of the container you give it.

### Link to Google Maps

In order to use Google Maps, you need to link to the maps script.

You can find a walkthrough for including the Google Map script tag [here](https://developers.google.com/maps/documentation/javascript/tutorial).

### Add a Map Script
Notice that the URL for the Maps script includes a parameter besides your API key called "callback".

`https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&<b>callback=initMap</b>`

This parameter defines the callback that's used when the Maps API script is finished loading.

**REMEMBER TO CHANGE OUT THE KEY PARAMETER WITH YOU API KEY BEFORE CONTINUING**

Since the API key is front-end facing, and only really used for usage metrics, you don't need to be hide it. That said, it's good practice to include the key as an environment varaible, so that you can switch keys if they are expired or get reset.

`https://maps.googleapis.com/maps/api/js?key=<%= process.env.YOUR_API_KEY %>&<b>callback=initMap</b>`

Now, let's define our `initMap` callback

```js
var initMap = function() {

  var map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: -34.397, lng: 150.644},
    zoom: 8
  });

  // if brower support available, ask user for location data and set the map view
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      initialLocation = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
      map.setCenter(initialLocation);
    });
  }

  // for each marker passed through, add it to the map with a popup
  markers.forEach(function(marker) {
    console.log(marker);
    var latLng = new google.maps.LatLng(marker.lat, marker.lng);
    var googleMarker = new google.maps.Marker({
      position: latlng,
      title: marker.name,
      map: map
    });
    // Bind a popup to the marker
    googleMarker.addListener("click", function() {
      var infoWindow = new google.maps.InfoWindow({content: "<h3>"+marker.name+"</h3>"});
      infoWindow.open(map, marker);
    });
  });
};
```

**IMPORTANT NOTES**

* It's important that you remember the async and defer attributes on the Google Maps script tag. This will wait until the page has loaded to start loading the Google Maps script.
* `initMap` is distinct from the document ready event. According to this Stack Overflow post...

http://stackoverflow.com/questions/8638551/script-defer-and-document-ready

...deferred scripts will execute before jQuery's docready, but you can't be totally sure of that.

###On your route that needs a map

Add a `script` tag to show render points to the page.

```html
<script>
  var myPoints = <%- JSON.stringify(places) %>;
</script>
```

* `JSON.Stringify` will convert our data to JSON data that javascript can use.
* `<%- %>` syntax will display it exactly, and not escape it for html.

## Useful links

* [Google maps API reference](https://developers.google.com/maps/documentation/javascript/reference?hl=en)
* [Google developers console](https://console.developers.google.com/)
