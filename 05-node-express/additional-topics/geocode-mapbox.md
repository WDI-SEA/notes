# Geocoding and Mapbox

* Describe geocoding
* Use Mapbox geocoder to forward and reverse geocode

# TODO INSTRUCTIONS: set up a mapbox account and get access token

We'll use the [@mapbox/mapbox-sdk](https://github.com/mapbox/mapbox-sdk-js) node module.

**1.** Set up a new node project called `geocode-example`.

**2.** Install `@mapbox/mapbox-sdk` via `npm`.

## Geocoder

**What is geocoding?** - The process of converting a description of a place to geographic coordinates. The relationship between the description and the place is a *mapping* (no pun intended).

### Example:

"Seattle, WA" -> **geocode** -> {lat: 47.6062095, lng: -122.3320708}

## Geocoder

**3.** In a file called `mapTest.js`, import the geocoder from the mapbox module and set up a geocoding client using your access token [docs](https://www.mapbox.com/api-documentation/?language=JavaScript#geocoding).

```js
const mbxGeocoding = require('@mapbox/mapbox-sdk/services/geocoding');
const geocodingClient = mbxGeocoding({ accessToken: 'your-access-token' });
```

**4.Forward Geocode!**

Search for `'Seattle, WA'` and check out the GeoJSON feature collection that is returned. [docs](https://www.mapbox.com/api-documentation/?language=JavaScript#search-for-places) 

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

**5.Reverse Geocode!**

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

## Embedding a Map

Now we're going to embed a map into a web page so our user can interact with it on the front end.

**6.** Set up the front end.

* Install `express` and `ejs`.
* Set up an `express` app that uses `ejs` as its view engine and listens to port `8000`.
* Write a home route that renders a `map` view.

**7.** Copy Example Code

The [Mapbox Examples] page has all the examples plus source code you could ever want! Let's copy the source code from the [Draw GeoJSON points](https://www.mapbox.com/mapbox-gl-js/example/geojson-markers/) example and do some tweaking to make it our own.

**8.** Put our own marker on the map

By default, there are two GeoJSON markers on the map, one in San Francisco and one in DC. Let's get the coordinates for General Assembly Seattle and add it to our list of markers that display on load.

## More Resources
* [Geocoding](https://www.mapbox.com/help/how-geocoding-works/#how-geocoding-works)
