# Third Party APIs

## API: Application Program Interface

This term, _API_ is thrown around quite a bit in talk about web applications, but what exactly is an API? It is an application-to-program _interface_, meaning it is the part of a program that specifies how outside applications can interact with it. APIs are integral to the HTTP request-response proccess; they facilitate the response!

---

## Real-world Analogy
Think of the API as the postal service worker you interact with when you go to the post office to pick up a package. You're the client, the server is that big room full of unclaimed packages. 

**The Request**: You hand the paper with the package information on it to the postal worker (the API). 

**API**: The postal worker locates the package you're looking for, checks your id, maybe gets a signature.

**The Response:** The postal worker(the API) then hands you the package!

---

## Example: Yelp & Google Maps

Visit the [yelp](https://www.yelp.com/) page and search for restaurants in Seattle. Notice the map view of the search results. Let's look at the interaction that happened here:

**Request #1:** You browser, the client, made a request to the Yelp server.

**Request #2:** The Yelp server (the client, in this request), made a request to the Google Maps API for data.

**Response #1:** The Google Maps API sent maps data back to the yelp server.

**Response #2:** The Yelp server integrated this data into it's files and then responded to your browser with the files that it used to build the webpage before you.

---

## Internal vs. Third Party APIs

Companies will often break up their software between multiple different servers, in which case those servers may be making API calls to each other in order to work together.

In the case above, a Yelp server is making an API request to a _third party_ server from Google.

--

## Looking at API response data

Your browser can also make API requests directly, but remember that a browser is only equipped to render HTML. Since HTTP requests can only send text back and forth, response data general comes in JSON format (or similar).

It is important to spend time reading the documentation for an API, which will tell you the base URL for the request, and how to format endpoints to get the data you want. The documentation will also (usually) show you examples of the data you will receive so you are prepared to navigate that data.

**Non-auth Examples:** 

Many APIs require you to sign up for a personalized key that you will need to add to the request URL. This allows them to regulate the incoming requests.

**Examples (no key required)**
* [Random Quotes API](https://talaikis.com/random_quotes_api/)

* [iTunes API](https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/)

**Examples (key required)**

* [NASA](https://api.nasa.gov/)

* [Spotify](https://developer.spotify.com/documentation/web-api/)

* [NYT Bestsellers](http://developer.nytimes.com/)

* [Youtube](https://developers.google.com/youtube/v3/getting-started)

* [Pretty much anything API you might want from google](https://console.developers.google.com/apis/)
