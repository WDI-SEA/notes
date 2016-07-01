#APIs with Ruby/Rails

## Objectives

* Review the purposes of APIs and why we call them on a server
* Use `rest-client` to interact with an API
* Use `foreman` to load API keys from a `.env file`

## What is an API?

API stands for **A**pplication **P**rogramming **I**nterface, and they provide a set of tools and methods for interacting with software. When we use an API, we generally interact with software by sending inputs. Once inputs are received, they're processed by the software, and we get output, or a response, from the software.

![API Graphic](http://www.programmableweb.com/wp-content/smart-file-small.jpg)

## Public APIS

We used public APIs during the JavaScript unit. Public APIs can be accessed openly without any authentication.

* http://www.reddit.com/search.json?q=kittens+nsfw:no
* https://itunes.apple.com/search?term=arcade%20fire

## APIs with Keys

Most robust APIs aren't completely open, in order to protect against abuse and/or malicious requests. Generally, an API will require keys to idenitfy who is connecting to the service. Google, Flickr, and Yelp are some companies that provide open APIs using keys.

When we use Flickr, we'll be given an API key and a secret key. Why two keys? Because math! Science! Security purposes! Here's some interesting explanations on why and how these keys are encrypted/decrypted:

* [API keys and Secret keys](http://stackoverflow.com/questions/2674445/how-do-api-keys-and-secret-keys-work)
* [Video on Public and Private keys](https://www.youtube.com/watch?v=3QnD2c4Xovk)

## Public APIs in Rails

Many web APIs work similarly to a Rails app. They support CRUD actions via a RESTful interface. Meaning, requests can be made over HTTP to get, post, update, and/or delete data.

### Clients for sending requests

* [rest-client](https://github.com/rest-client/rest-client)
  * great for simple requests
* [typhoeus](https://github.com/typhoeus/typhoeus)
  * great for sending multiple requests in parallel

### Implementing a Public API with iTunes

**Objective:** Display results from iTunes given a query.

Example call: https://itunes.apple.com/search?term=arcade%20fire

* create a new rails project
  * setup database
* create a new controller with index and show methods
* setup routes
* add the `'rest-client'` gem.
* on index, create a form for submitting a query
* on show, make a request to the API and show results

Of course, test along the way. Otherwise, you're living in the...

![Archer Danger Zone](http://www.eonline.com/eol_images/Entire_Site/2014013/rs_500x282-140113151420-92081-archer-danger-zone-gif-pnbv.gif)

## APIs w/keys in Rails

See [Environment Variables with Foreman](../../00-config-deployment/foreman/readme.md)
