![General Assembly Logo](http://i.imgur.com/ke8USTq.png)

#Data Scraping with Cheerio

##Objectives

* Identify situations where data scraping would be beneficial
* Understand the methods and legality of data scraping
* Use modules such as Cheerio to scrape data from the web

Web scraping is a useful tool for extracting data from a webpage. 

##Getting Started
The first steps to getting started is to make a new project folder. We must work inside of a project folder, in order to leverage the `package.json` file

we can either make a package.json file in a few ways
* run `npm init`
* create a file called `package.json` with `{}` inside as the contents.
* Or this line liner: `echo "{}" >> package.json`


##Necessary Modules
We will be using `request` and `cheerio`

* `request` is a module for open remote resources
* `cheerio` is essentially server side jquery. We will be using this to traverse the data we get back form `request`

##HackerNews Scraping
In this HackerNews Scraping example, we will use request to just open the data from the webpage. We can use also use the `request` to open up `json` related urls.

```js
request('https://news.ycombinator.com/', function (error, response, data) {
})
```

We will introduce the concept of a callback. In an asynchronous call, we must only refer the result inside the closure of the callback function.


###Using Cheerio with the data
Inside the callback function of request, we want to set `$` the to the actuall page's data.

We can use 

```js
var $ = cheerio.load(data);
```
From now on we can any selectors and most jquery related functions to grab data form the page.

Consult the [Cheerio Documentaiton](https://github.com/cheeriojs/cheerio) for most info.


###Traversing the DOM

```js
var links = $('.title a').map(function(index, element) {
  return {link: $(this).text(), url: $(this).attr("href")}
}).get();

console.log(links);
```

###Final Code
```js
var request = require('request');
var cheerio = require('cheerio');

request('https://news.ycombinator.com/', function (error, response, data) {
  if (!error && response.statusCode == 200) {
    var $ = cheerio.load(data);

    // $('.title a').each(function(index, element) {
    //   console.log($(element).attr("href"))
    // })

    var links = $('.title a').map(function(index, element) {
      return {link: $(this).text(), url: $(this).attr("href")}
    }).get();

    console.log(links);

  }
});

```

## Some other resources on scraping
[Scraping with Node](http://maxogden.com/scraping-with-node.html)
[Web Scraping For Fun and Profit](https://blog.hartleybrody.com/web-scraping/)
