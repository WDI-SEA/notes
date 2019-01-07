# Geocoding with Mapbox

## Objectives
* Describe geocoding
* Use Mapbox geocoder to forward and reverse geocode

## Geocoding

**What is geocoding?** - The process of converting a description of a place to geographic coordinates. The relationship between the description and the place is a *mapping* (no pun intended).

### Example:

"Seattle, WA" -> **geocode** -> {lat: 47.6062095, lng: -122.3320708}

### Mapbox
We'll use the [Mapbox Geocoding API](https://www.mapbox.com/api-documentation/#geocoding). Mapbox is a system of geolocation-related APIs, similar to the Google Maps API. Lyft, the Weather Channel, and many other large companies use Mapbox to incorporate maps into their apps. 

## Get Geocoding

### Using Mapbox
* Head to the [mapbox sign up page](https://www.mapbox.com/signup/?route-to=%22/account/%22) and make an account.
* Locate your Access Token - this will be the same for all Mapbox APIs

### Set up
* Create a new node project called `geocode-example`.
* Install the [@mapbox/mapbox-sdk](https://github.com/mapbox/mapbox-sdk-js) node module via `npm`.
* In `mapTest.js` file, import the geocoder from the mapbox module and set up a geocoding client using your access token [docs](https://www.mapbox.com/api-documentation/?language=JavaScript#geocoding).

```js
const mbxGeocoding = require('@mapbox/mapbox-sdk/services/geocoding');
const geocodingClient = mbxGeocoding({ accessToken: 'your-access-token' });
```

### Forward Geocode

Search for `'Seattle, WA'` and check out the GeoJSON feature collection that is returned. [docs](https://www.mapbox.com/api-documentation/?language=JavaScript#search-for-places) 

**mapTest.js**
```js
geocodingClient
  .forwardGeocode({
    query: 'Seattle, WA'
  })
  .send()
  .then(response => {
    const match = response.body;
    console.log(match);
  });
```

The coordinates are listed under the `center` field of each object.

```js
geocodingClient
  .forwardGeocode({
    query: 'Seattle, WA'
  })
  .send()
  .then(response => {
    const match = response.body;
    console.log(match.features[0].center);
  });
```

### Reverse Geocode

Now copy the coordinates that you just found and reverse geocode them! [docs](https://www.mapbox.com/api-documentation/?language=JavaScript#retrieve-places-near-a-location)

```js
geocodingClient
  .reverseGeocode({
    query: [ -122.3301, 47.6038 ]
  })
  .send()
  .then(response => {
    const match = response.body;
    console.log(match);
  });
```

## Exercise/Lab: City Search
You're going to set up an app that allows users to search for a city and add their favorite cities to a database.

### Set up the front end.

* Install `express`, `ejs`, and `express-ejs-layouts`.
* Set up an `express` app that listens to port `8000`.
* Add `ejs`, `express-ejs-layouts`, and `body-parser` middleware.
* Create your `views` folder that has your `layout.ejs`.


### Views

### Routes

## More Resources
* [Geocoding](https://www.mapbox.com/help/how-geocoding-works/#how-geocoding-works)
