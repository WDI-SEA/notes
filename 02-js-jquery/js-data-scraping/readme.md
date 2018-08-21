# Data Scraping with Cheerio

## Objectives

* Identify situations where data scraping would be beneficial
* Understand the methods and legality of data scraping
* Use modules such as Cheerio to scrape data from the web

## What is web scraping?
Scraping (Screen Scraping, Web Data Extraction, Web Harvesting, etc) refers to the process of requesting an HTML page and picking out relevant data from the document string. In other words, you can scrape content off of web pages by parsing the html.

#### Why scrape?

* no API available
* API is unreliable/unkept/etc.
* no fee or call limit (unless a rate-limit is set up)
* more anonymous than getting data through dev resources

#### Why not scrape?

* need to log into site in order to access desired data
* organization of data is makes it hard/overly-laborious to access
* web page structure frequently changes (program that uses scraped data would need constant updates)
* copywrite and other legal issues

**NOTE:** The legality of data scraping and using a site's data may depend on a site's terms of use. Scraping a site and using the data for profit may violate a site's terms of use, so be careful before scraping a site. This is not legal advice, and we are not lawyers, but we recommend that you contact a lawyer if you want to scrape data for a for-profit application.

## Getting Started: Scraping Seattle Neighborhoods

Let's try creating a file that will scrape Seattle neighborhoods from this site:

http://www.visitseattle.org/things-to-do/neighborhoods/

To get started, create a new folder, and initialize npm. We'll also want to install two modules:

* `request` - for accessing external resources via HTTP
* `cheerio` - essentially, this is server side jQuery. We will be using this to traverse the data we get back form `request`

```bash
mkdir seattle-neighborhoods
cd seattle-neighborhoods
npm init --y
npm install request cheerio
```

#### Step 1: Get the HTML document

There are multiple ways to get an HTML document, but we'll use the ```request``` module in this example. To scrape data from the site, we need to request the webpage like so:

```js
var request = require('request');
var cheerio = require('cheerio');

request('http://www.visitseattle.org/things-to-do/neighborhoods/', function (error, response, body) {
  console.log(body);
});
```

Consult the [Cheerio Documentaiton](https://github.com/cheeriojs/cheerio) for most info.

### Step 2: Parse the HTML

The request to the seattle neighborhoods url gave us the entire HTML document string - now we need to parse it in order to pick out the specific data we're looking for. This is where Cheerio comes in! Inside the callback function of request, we'll pass the html we got back into the `cheerio.load()` function. We store the result, which is a cheerio object, in the dollar sign variable because cheerio is designed to mimic jQuery selectors (though technically, we could store it in any variable we'd like).

```js
request('http://www.visitseattle.org/things-to-do/neighborhoods/', function (error, response, body) {
  var $ = cheerio.load(data);
  console.log($);
});
```

### Step 3: Identify the content you want to scrape.

* First you have to identify what content you're looking to scrape and how to access it. Clicking on one of the neighborhoods displays a hidden div with information about that location. Each of these divs have both 1) the name of the 'hood and 2) a link to a page detailing the neighborhood. Let's say that we want to grab the name and the link to more info for each of the neighborhoods.
* Inspect that div- you'll see these hidden divs have a class `info-window-content`.
* So, we'll select those elements using Cheerio's selector syntax.

```js
// returns an cheerio object with a whole lot of info
 var neighborhoods = $('.info-window-content');
 console.log(neighborhoods);
```

### Step 4: Traverse the DOM (scrape!)

* Cheerio has its own `.map()` function to parse through a cheerio object, but it still returns another cheerio object
* (see docs -> traversing -> map)
* (for more on find/text/attr, etc, see docs)

```js
	var neighborhoods = $('.info-window-content').map(function(index, element) {
		// find() docs -> traversing -> find
	    return {
	        name: $(element).find('h4').text(),
	        link: $(element).find('a').attr('href')
	    };
	});
	console.log(neighborhoods);
```

This still gives us a lot of gobbledy-gook we didn't ask for. Use the get function after .map() to see an array of exactly what we asked for (see docs -> traversing -> get):

```js
	// add .get() to just get back what you asked for, instead of an entire cheerio object
	var neighborhoods = $('.info-window-content').map(function(index, element) {
	    return {
	        name: $(element).find('h4').text(),
	        link: $(element).find('a').attr('href')
	    };
	}).get();
	console.log(neighborhoods);
```

### Final Code

[cheerio-scraping-seattle-neighborhoods repo](https://github.com/WDI-SEA/cheerio-scraping-seattle-neighborhoods)

```js
var request = require('request');
var cheerio = require('cheerio');

request('http://www.visitseattle.org/things-to-do/neighborhoods/', function(error, response, data) {
    var $ = cheerio.load(data);

    var neighborhoods = $('.info-window-content').map(function(index, element) {
        return {
            name: $(element).find('h4').text(),
            link: $(element).find('a').attr('href')
        };
    }).get();

    console.log(neighborhoods);
});
```

## Scraping multiple sites

By scraping this site, we were able to return an array of neighborhoods, complete with their name and a link to more information. Now, if we want to get neighborhood descriptions, we would need to make many more requests to retrieve additional webpages. Look at the notes for [async](../js-async/readme.md) for how to accomplish this task.

## Some other resources on scraping

* [Scraping with Node](http://maxogden.com/scraping-with-node.html)
* [Web Scraping For Fun and Profit](https://blog.hartleybrody.com/web-scraping/)
