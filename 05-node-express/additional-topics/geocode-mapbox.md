# Geocoding and Mapbox

# TODO INSTRUCTIONS: set up a mapbox account and get access token

We'll use the [@mapbox/mapbox-sdk](https://github.com/mapbox/mapbox-sdk-js) node module.

## Objectives

* Describe the reversable process of geocoding.
* Utilize geocoding with a geocoder and Sequelize hooks
* Use Google Maps to add geocoordinates to a map.

## Geocoder

**What is geocoding?** - The process of converting a description of a place to geographic coordinates. The relationship between the description and the place is a *mapping* (no pun intended).

### Example:

"Seattle, WA" -> **geocode** -> {lat: 47.6062095, lng: -122.3320708}

## Geocoder

**1.** Set up a new node project called `geocode-example`.

**2.** Install `@mapbox/mapbox-sdk` via `npm`.

**3.** In a file called `mapTest.js`, import the geocoder from the mapbox module and set up a geocoding client using your access token.

```js
const mbxGeocoding = require('@mapbox/mapbox-sdk/services/geocoding');
const geocodingClient = mbxGeocoding({ accessToken: 'your-access-token' });
```
