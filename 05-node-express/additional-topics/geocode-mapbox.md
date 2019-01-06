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
Search for `'Seattle, WA'` and check out the GeoJSON feature collection that is returned!

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
