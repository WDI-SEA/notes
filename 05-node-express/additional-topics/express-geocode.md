# Geocoding and Google Maps

## Objectives

* Describe the reversable process of geocoding.
* Utilize geocoding with a geocoder and Sequelize hooks
* Use Google Maps to add geocoordinates to a map.

## Starter Code

We'll be using the starter code here \(fork and clone\): [https://github.com/WDI-SEA/express-geocode-maps-example](https://github.com/WDI-SEA/express-geocode-maps-example)

## Geocoding Addresses

**What is geocoding?** - The process of converting a description of a place to geographic coordinates. The relationship between the description and the place is a _mapping_ \(no pun intended\).

### Example:

"Seattle, WA" -&gt; **geocode** -&gt; {lat: 47.6062095, lng: -122.3320708}

### Using Geocoder

First lets install the package into our starter code. Note that we'll be using Google's geocoder API.

```text
npm install geocoder
```

### Try this in a separate file

We'll use this code in a file called `mapTest.js`

```javascript
var geocoder = require('geocoder');
geocoder.geocode('Seattle, WA', function(err, data) {
  console.log(data.results[0].geometry.location);
});
```

Note that once we type a location, the geocoder will lookup and give us coordinates for the location.

### Geocoding with a database model

In the starter code, we have a model called **place** that has a name, address, lat \(latitude\), and lng \(longitutde\) attributes.

If we want to take an address a user typed in, then determine the coordinates for the address, we can generate the coordinates using the `geocoder` library and a Sequelize `beforeCreate` hook. Let's try that in `place.js`.

At the top of the **place** model, import the geocoder.

```javascript
var geocoder = require('geocoder');
```

Then, add a hook below the `classmethods` object

```javascript
hooks: {
  beforeCreate: function(place, options, cb) {
    geocoder.geocode(place.address, function(err, data) {
      if (err) return cb(err, null);
      place.lat = data.results[0].geometry.location.lat;
      place.lng = data.results[0].geometry.location.lng;
      cb(null, place);
    });
  }
}
```

Now, try starting the app and entering a name/address. The geocoder will take the address and attempt to find the geocoordinates for the address. Check in the database to see if these results are generated.

## Using Google Maps

Google Maps is the most popular mapping app on the web. We'll be using it to display places on a map. In order to do so, we need **geocoordinates** of the places, which we already set up!

### Getting an API key

You'll need a Google/Gmail account first before setting up the API key. Once you've got that, head to the [Google developers console](https://console.developers.google.com/). You'll see a bunch of links to various APIs, and the only ones you care about right now are the Maps APIs.

Click on "Google Maps JavaScript API." Click "Enable." Use the API Manager pane on the left to navigate to "Credentials." Select "API Key" from the "Create credentials" drop down menu. Choose "Browser Key." Name the key something like "Google Maps Browser Key" and leave the referrers field blank. Now you have your browser key.

The two APIs you need to enable are the Google Maps JavaScript API, and the Google Maps Embed API. You might want to use the Google Maps Places API eventually, so go ahead and enable that too.

### Adding a map div

We already set up a map div in the `index.ejs` template, along with some CSS to set up the height. Take a look in order to familarize yourself. The CSS is important because if the div has no height, the map won't display.

**index.ejs\***

```markup
<div id="map"></div>
```

**style.css**

```css
#map {
  height: 500px;
}
```

### Link to Google Maps

In order to use Google Maps, you need to link to the maps script, along with the API key. These API keys are special browser keys, which don't need to be private \(and can't be private, since everything on the front end is visible\).

### Add a Map Script

Here's an example of adding the map script. Alternatively, you can find a walkthrough for including the Google Map script tag [here](https://developers.google.com/maps/documentation/javascript/tutorial). They also help out with automatically pasting your API key.

Let's add the script in **index.ejs** before our custom script.

```markup
<script async defer
  src="https://maps.googleapis.com/maps/api/js?key=<key here>&callback=initMap">
</script>
```

Note that there's a **callback** at the end of the script. This parameter defines the function that's called when the Maps API script is finished loading.

**REMEMBER TO CHANGE OUT THE KEY PARAMETER WITH YOU API KEY BEFORE CONTINUING**

Again, since the API key is front-end facing, and only really used for usage metrics, you don't need to be hide it. That said, it's good practice to include the key as an environment varaible, so that you can switch keys if they are expired or get reset.

**Example:**

```markup
<script async defer
  src="https://maps.googleapis.com/maps/api/js?key=<%= process.env.API_KEY_NAME %>&callback=initMap">
</script>
```

Now, let's define our `initMap` callback inside **script.js**. We'll be doing a series of operations inside this function.

* Creating a map attached to **map**, including a center point and zoom level
* If the browser supports geolocation, we'll ask the user their location and recenter the map if possible
* Add markers to the map by iterating across the array of markers \(currently empty, but we'll fill the array soon\)
  * Also, we'll bind a popup to each marker, displaying the location's name

```javascript
var initMap = function() {

  var map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: -34.397, lng: 150.644},
    zoom: 10
  });

  // if brower support available, ask user for location data and set the map view
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      var initialLocation = new google.maps.LatLng(
        position.coords.latitude,
        position.coords.longitude
      );
      map.setCenter(initialLocation);
    });
  }

  // for each marker passed through, add it to the map with a popup
  markers.forEach(function(marker) {
    console.log(marker);
    var position = new google.maps.LatLng(marker.lat, marker.lng);
    var googleMarker = new google.maps.Marker({
      position: position,
      title: marker.name,
      map: map
    });
    // Bind a popup to the marker
    googleMarker.addListener('click', function() {
      var infoWindow = new google.maps.InfoWindow({
        content: '<h3>' + marker.name + '</h3>'
      });
      infoWindow.open(map, googleMarker);
    });
  });
};
```

**IMPORTANT NOTES**

* It's important that you remember the async and defer attributes on the Google Maps script tag. This will wait until the page has loaded to start loading the Google Maps script.
* `initMap` is distinct from the `$(document).ready()` event. According to this Stack Overflow post, deferred scripts will execute before jQuery's `$(document).ready()` function.

[http://stackoverflow.com/questions/8638551/script-defer-and-document-ready](http://stackoverflow.com/questions/8638551/script-defer-and-document-ready)

### Setting up markers

Lastly, we need to get markers from our database and display them on the map. In order to do so, we'll add a `script` tag on the `index.ejs` template to show render points to the page. Note that it's **very** important to do this on a EJS template, otherwise, we can't use the EJS template tags.

**In index.ejs** before all the other scripts:

```markup
<script>
  var markers = <%- JSON.stringify(places) %>;
</script>
```

* `JSON.Stringify` will convert our data to JSON data that javascript can use.
* `<%- %>` syntax will display it exactly, and not escape it for html.

## Useful links

* [Google maps API reference](https://developers.google.com/maps/documentation/javascript/reference?hl=en)
* [Google developers console](https://console.developers.google.com/)

