#Data Scraping with Cheerio

##Objectives

* Identify situations where data scraping would be beneficial
* Understand the methods and legality of data scraping
* Use modules such as Cheerio to scrape data from the web

Web scraping is a useful tool for extracting data from a webpage. It's a process that involves requesting a HTML page and picking out relevant data from the document.

**NOTE:** The legality of data scraping and using a site's data may depend on a site's terms of use. Scraping a site and using the data for profit may violate a site's terms of use, so be careful before scraping a site. This is not legal advice, and we are not lawyers, but we recommend that you contact a lawyer if you want to scrape data for a for-profit application.

##Getting Started: Scraping Seattle Neighborhoods

Let's try creating a file that will scrape Seattle neighborhoods from this site:

http://www.visitseattle.org/things-to-do/neighborhoods/

To get started, create a new folder, and initialize npm. We'll also want to install two modules:

* `request` - for accessing external resources via HTTP
* `cheerio` - essentially, this is server side jQuery. We will be using this to traverse the data we get back form `request`

```bash
mkdir seattle-neighborhoods
cd seattle-neighborhoods
npm init --yes
npm install --save request cheerio
```

## Getting the HTML document

To scrape data from the site, we need to request the webpage like so:

```js
var request = require('request');
var cheerio = require('cheerio');

request('http://www.visitseattle.org/things-to-do/neighborhoods/', function (error, response, data) {
  // code here
});
```

###Using Cheerio with the data

Inside the callback function of request, we'll pass the data along to Cheerio by calling `cheerio.load()`. The result can be stored in a variable, and then we can run jQuery-like selectors on the data.

Using `$` as the variable name will make this look like jQuery.

```js
var $ = cheerio.load(data);
```

Consult the [Cheerio Documentaiton](https://github.com/cheeriojs/cheerio) for most info.

###Traversing the DOM

* Neighborhoods on the page have the class `.text-medium-small`, so we'll select those elements using Cheerio's selector syntax
* Cheerio has its own `.map()` function, but it's slightly different in that the index comes first, then the element.
* Cheerio has `.text()`, which we'll call to get the element's text.
* The `.get()` function will correctly return the elements.

```js
var neighborhoods = $('.text-medium-small').map(function(index, element) {
  return {
    name: $(element).text(),
    link: $(element).closest('a').attr('href')
  };
}).get();

console.log(neighborhoods);
```

###Final Code
```js
var request = require('request');
var cheerio = require('cheerio');

request('http://www.visitseattle.org/things-to-do/neighborhoods/', function (error, response, data) {
  var $ = cheerio.load(data);

  var neighborhoods = $('.text-medium-small').map(function(index, element) {
    return {
      name: $(element).text(),
      link: $(element).closest('a').attr('href')
    };
  }).get();

  console.log(neighborhoods);
});
```

## Scraping multiple sites

By scraping this site, we were able to return an array of neighborhoods, complete with their name and a link to more information. Now, if we want to get neighborhood descriptions, we would need to make many more requests to retrieve additional webpages. Look at the notes for [async](../js-async/readme.md) for how to accomplish this task.

## Some other resources on scraping

[Scraping with Node](http://maxogden.com/scraping-with-node.html)
[Web Scraping For Fun and Profit](https://blog.hartleybrody.com/web-scraping/)
