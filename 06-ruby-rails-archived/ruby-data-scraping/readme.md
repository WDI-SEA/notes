# Data Scraping with Nokogiri

## Objectives

* Review `rest-client` and how it can be used to make HTTP requests
* Discuss the process and need for data scraping
* Use the Nokogiri parser and RestClient to obtain and parse data

Data scraping is the process of extracting data from a web site. This is used primarily when the data is not available from an existing API. Data is extracted by taking the HTML file and trying to extract certain blocks of text or data. We'll be using a Ruby gem called Nokogiri in order to scrape a page.

## Nokogiri

Nokogiri is a parser for HTML and XML. It allows us to process a HTML file (locally or on a remote server) and extract the data from it using CSS selectors. This is handy because the process is analagous to selecting data using jQuery or `querySelectorAll`.

[http://www.nokogiri.org/](http://www.nokogiri.org/)

In a new folder, let's install the Nokogiri and rest-client gems and try scraping a site.

**Gem Installation (or place into your Gemfile, if using Rails)**

```
gem install nokogiri
gem install rest-client
```

In a new file, we need to do the following:

* Get a HTML file (hint: 'rest-client')
* Give Nokogiri the HTML file
* Select data using CSS selectors

**In a file**

```rb
# require the gems we need
require 'rest-client'
require 'nokogiri'

#request data
response = RestClient.get("http://reddit.com/r/aww")
html = response.body

#give Nokogiri your file
data = Nokogiri::HTML(html)

#select data using CSS selectors
data.css('p.title a.title').each do |title|
  puts title.text
end
```

Let's analyze a few things we do here with Nokogiri

* We pass our HTML string into `Nokogiri::HTML`. `HTML` is a class inside of the `Nokogiri` module, and this class parses HTML files.
* To select specific DOM elements, we can take the parsed file and call the `.css` method. It's also possible to iterate through the results.
* Can you only get text? Nope! There's other methods associated with Nokogiri.
  * http://www.nokogiri.org/tutorials/searching_a_xml_html_document.html

## Using local data

When we are figuring out how to scrape a site we usually have to do a lot of trial and error. Which means reloading the data over and over. This could raise red flags with the site administrator and could possibly get your IP banned.

Luckily, we can avoid this by downloading the data for a page and using that file while we figure out how to scrape the data we need.

####Using cURL to download the data

We can use cURL to download HTML files and save them locally on our computers. By using the `-o` flag, we can specify the local file name and the URL we want to download.

```
curl -o reddit_aww.html https://www.reddit.com/r/aww
```

This example downloads data from `https://www.reddit.com/r/aww` and stores it in `reddit_aww.html`. Once the data has been downloaded, we'll want to include it in a different manner inside our Ruby file.

####Loading a local file

```rb
require 'nokogiri'

# open the file
reddit_html = File.open('reddit_aww.html')

# give Nokogiri the file
data = Nokogiri::HTML(reddit_html)
```

This opens the HTML file and stores the new file object to `reddit_html`. Then, we pass the file to Nokogiri, similar to before.
