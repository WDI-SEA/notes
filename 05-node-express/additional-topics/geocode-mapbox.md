# Geocoding with Mapbox

## Objectives

* Describe geocoding
* Use Mapbox geocoder to forward and reverse geocode

## Geocoding

**What is geocoding?** - The process of converting a description of a place to geographic coordinates. The relationship between the description and the place is a _mapping_ \(no pun intended\).

### Example:

"Seattle, WA" -&gt; **geocode** -&gt; {lat: 47.6062095, lng: -122.3320708}

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

```javascript
const mbxGeocoding = require('@mapbox/mapbox-sdk/services/geocoding');
const geocodingClient = mbxGeocoding({ accessToken: 'your-access-token' });
```

### Forward Geocode

Search for `'Seattle, WA'` and check out the GeoJSON feature collection that is returned. [docs](https://www.mapbox.com/api-documentation/?language=JavaScript#search-for-places)

**mapTest.js**

```javascript
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

```javascript
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

```javascript
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

## More Resources

* [Geocoding](https://www.mapbox.com/help/how-geocoding-works/#how-geocoding-works)

## Exercise/Lab: City Search

You're going to set up an app that allows users to search for a city and add their favorite cities to a database.

### Set up the front end.

* Install `express`, `ejs`, `express-ejs-layouts`, and `method-override`.
* Set up an `express` app that listens to port `8000`.
* Add `ejs`, `express-ejs-layouts`, `body-parser`, and `method-override` middleware.
* Create your `views` folder that has your `layout.ejs`.

### Set up the database.

* install `pg` and `sequelize` via npm
* initialize  `sequelize`
* configure `config.json`
* create a `place` model with `city`, `state`, `lat`, and `long` fields
* run migration

### Views

#### city-search

* form with two text inputs, one for city and one for state
* form should submit a GET request to `/search`
* "View My Favorites" button links to  `/favorites` view

#### search-results

* header that says "search results for  "
* list search results \(include the name and coordinates of each result, along with an "add to favorites" button\)
* each list item should include a form with four hidden fields \(city, state, lat, long\) so the favorites button actually submits a `POST` request to `/add`
* include a "back to search" button that links back to the search page

#### favorites

* lists all saved favorite cities
* each list item should have a "remove from favorites" button that deletes that city from the `places` table and redirects back to the favorites page
* "remove from favorites" button will need to be a `POST` form with a submit button that utilizes `method-override`

### Routes

#### GET '/'

* render `city-search` view

#### GET '/search'

* use forward geocoding to search for cities in the US \(_hint: use the `type` and `countries` fields in addition to `query`_\)
* render `search-results` page, passing through the searched data as well as the results

#### POST '/add'

* use `findOrCreate` to post to the database of favorites

#### GET '/favorites'

* pull all favorited cities from the database and pass them into the view

#### DELETE '/remove'

* deletes city from `place` table and redirects to _favorites_ view

