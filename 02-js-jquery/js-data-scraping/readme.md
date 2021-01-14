# Data Scraping

## Objectives

* Identify situations where data scraping would be beneficial
* Understand the methods and legality of data scraping
* Use modules such as Cheerio to scrape data from the web

## What is web scraping?

Scraping \(Screen Scraping, Web Data Extraction, Web Harvesting, etc\) refers to the process of requesting an HTML page and picking out relevant data from the document string. In other words, you can scrape content off of web pages by parsing the html.

#### Why scrape?

* no API available
* API is unreliable/unkept/etc.
* no fee or call limit \(unless a rate-limit is set up\)
* more anonymous than getting data through dev resources

#### Why not scrape?

* need to log into site in order to access desired data
* organization of data makes it hard/laborious to access
* web page structure frequently changes \(program that uses scraped data would need constant updates\)
* copywrite and other legal issues

**NOTE:** The legality of data scraping and using a site's data may depend on a site's terms of use. Scraping a site and using the data for profit may violate a site's terms of use, so be careful before scraping a site. This is not legal advice, and we are not lawyers, but we recommend that you contact a lawyer if you want to scrape data for a for-profit application.

## Getting Started: Scraping Seattle Neighborhoods

Let's try creating a program that will scrape neighborhood data from this site:

[https://visitseattle.org/partners/?frm=partners&ptype=visitors-guide&s=&neighborhood=Capitol+Hill](https://visitseattle.org/partners/?frm=partners&ptype=visitors-guide&s=&neighborhood=Capitol+Hill)

To get started, create a new folder, and initialize npm. We'll also want to install two modules:

* `request` - for accessing external resources via HTTP
* `cheerio` - essentially, this is server side jQuery. We will be using this to traverse the data we get back from our request.

### Step 1: Get the HTML document

There are multiple ways to get an HTML document, but we'll use the `request` module in this example. To scrape data from the site, we need to request the webpage. In a `getbusinesses.js` file, import `request`, then make a request to the Seattle Neigbhborhoods website.

```javascript
const request = require('request');
const URL = 'https://visitseattle.org/partners/?frm=partners&ptype=visitors-guide&s=&neighborhood=Capitol+Hill';

request(URL, (error, response, body) => {
    console.log(body);
});
```

Run the program and take a look at your output. What did the request return?

Look over the [Cheerio Documentation](https://cheerio.js.org/) - for more info about our next steps.

### Step 2: Parse the HTML

The request to the seattle neighborhoods url gave us the entire HTML document string - now we need to parse it in order to pick out the specific data we're looking for. This is where Cheerio comes in! Import Cheerio to your `getbusinesses.js`:

```javascript
const cheerio = require('cheerio');

```

Inside the callback function of request, we'll pass the html we got back into the `cheerio.load()` function. We store the result, which is a cheerio object, in the dollar sign variable because cheerio is designed to mimic jQuery selectors \(though technically, we could store it in any variable we'd like\).

```javascript
request(URL, (error, response, body) => {
  let $ = cheerio.load(body);
  console.log($);
});
```

Run the program and take a look at the `cheerio` object. How might we find the html again? Does the `cheerio` object contain a method for this?

### Step 3: Identify the content you want to scrape.

* First you have to identify what content you're looking to scrape and how to access it. Let's aim to scrape the names of all the busineses listed on this page of Capitol Hill businesses. Open the dev tools and inspect the page to see if you can pinpoint the elements that have the relvant information for each result.

Upon some inspection, we can see that the results live inside of a `search-results` `div`, which contains a `search-results-partner` `section` element. Inside *that* there is a `search-result-container` `div` that has a `search-result` `div` for each result.

Let's try to target the name of the first business. Inspect the first `search-result` `div` and identify exactly where the business name lives.

The business name can be found inside the `search-result-preview` `div` as both the `title` of the nested `a` tag, as well as the `h3` child of that anchor. 

First let's grab the first `search-result-preview` element. Cheerio uses [jQuery selectors](https://www.w3schools.com/jquery/jquery_ref_selectors.asp) to identify elements.

```javascript
request(URL, (error, response, body) => {
    let $ = cheerio.load(body);
    let result = $('.search-result-preview').html();
    console.log(result);
});
```

Now let's target the `title` attribute:

```javascript
request(URL, (error, response, body) => {
    let $ = cheerio.load(body);
    let result = $('.search-result-preview').find('a').attr('title');
    console.log(result);
});
```
Great! Now we know how to find the title of **one** business, but how do we get all of them?

### Step 4: Traverse the DOM \(scrape!\)

Cheerio actually gives us the option of selecting the *first* or *all* of the elements that match the selector. Let's take a closer look at `('.search-result-preview')` by getting it's `length`:

```javascript
request(URL, (error, response, body) => {
    let $ = cheerio.load(body);
    let result = $('.search-result-preview');
    console.log(result.length);
});
```
It looks like that result object actually contains all of the results on the page! Cheerio has iterators for traversing cheerio objects like this. Let's use the `each` iterator, which functions similarly to the javascript `Array.forEach()`:

```javascript
request(URL, (error, response, body) => {
    let $ = cheerio.load(body);
    let results = $('.search-result-preview');
    results.each((index, element)=>{
        console.log($(element).find('a').attr('title'));
    });
});
```

Logging to the console is great, but in practice, we'll likely want to store all of these titles in an an array-like cheerio object. We can use the built in `.map()` iterator to pull out *just* the titles and store them in their own cheerio object: 


```javascript
request(URL, (error, response, body) => {
    let $ = cheerio.load(body);
    let results = $('.search-result-preview');
    let resultTitles = results.map((index, element)=>{
        return $(element).find('a').attr('title');
    });
    console.log(resultTitles);
});
```

This still gives us a lot of gobbledy-gook we didn't ask for. Use the `.get()` function after `.map()` to see an array of exactly what we asked for \(see docs -&gt; traversing -&gt; get\):

```javascript
request(URL, (error, response, body) => {
    let $ = cheerio.load(body);
    let results = $('.search-result-preview');
    let resultTitles = results.map((index, element)=>{
        return $(element).find('a').attr('title');
    });
    console.log(resultTitles.get());
});
```

## Exercise:

What if we want more than just the name of the businesses? Let's modify our code to also store the URL for the image associated with the result:

```javascript
request(URL, (error, response, body) => {
    let $ = cheerio.load(body);
    let results = $('.search-result-preview');
    let filteredResults = results.map((index, element)=>{
        return {
            title: $(element).find('a').attr('title'),
            img: [ INSERT YOUR CODE HERE ]
        }
    });
    console.log(filteredResults.get());
});
```

### HINT
```javascript
 $(element).find('.image-container').attr('style');
```

Now you need to modify the string to isolate the url!

### SOLUTION

```javascript
request(URL, (error, response, body) => {
    let $ = cheerio.load(body);
    let results = $('.search-result-preview');
    let filteredResults = results.map((index, element)=>{
        let imgurl = $(element).find('.image-container').attr('style');
        imgurl = imgurl.substring(22, imgurl.length-15);
        return {
            title: $(element).find('a').attr('title'),
            img: imgurl
        }
    });
    console.log(filteredResults.get());
});
```

Now you need to modify the string to isolate the url!



## Some other resources on scraping

* [Scraping with Node](http://maxogden.com/scraping-with-node.html)
* [Web Scraping For Fun and Profit](https://blog.hartleybrody.com/web-scraping/)

