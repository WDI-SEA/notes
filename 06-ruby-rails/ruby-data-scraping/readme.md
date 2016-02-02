![General Assembly Logo](http://i.imgur.com/ke8USTq.png)

#Data Scraping with Nokogiri

##Objectives

* Review the process and need for data scraping
* Use the Nokogiri parser and RestClient to obtain and parse data

Data scraping is the process of extracting data from a web site. This is used primarily when the data is not available from an existing API.

##Nokogiri

Nokogiri is a parser for html and xml. It allows us to process an html file (locally or on a remote server) and extract the data from it.

[http://www.nokogiri.org/](http://www.nokogiri.org/)

**Gem Installation**

```
gem install nokogiri
```

**In rails (Gemfile)**

```ruby
gem 'nokogiri'
```

##Loading html from server

```
#top of file (or in gemfile for rails)
require 'rest-client'

#request data
response = RestClient.get("http://reddit.com/r/aww")
html = response.body
```

##Using local data

When we are figuring out how to scrape a site we usually have to do a lot of trial and error. Which means reloading the data over and over. This could raise red flags with the site administrator and if you're using any loops could result in requesting pages too quickly and getting your IP banned.

Luckily, we can avoid this by downloading the data for a page and using that file while we figure out how to scrape the data we need.

####Using wget to download the data

There is a command line tool (terminal) called wget that can download data for us. We pass it a url and a file to store the data in and it will download it as an html file that we can use to test.

```
wget -O reddit_aww.html "http://reddit.com/r/aww"
```

Downloads data from `http://reddit.com/r/aww` and stores it in `reddit_aww.html`. The -O flag (capital o) tells it the ouput file to store the data.

####Installing wget

What if wget doesn't work?? Just install wget with brew.

```
brew install wget
```

####Loading local file data in ruby

```
#top of file
require 'open-uri'


#local file (previously downloaded with wget or something)
html = open("reddit_aww.html")
```

This loads the html contents of the file into the `html` variable in ruby.


##Parsing the data

Before we can parse data we need to require nokogiri at the top of the file like this

```ruby
require 'nokogiri'
```

then we can use nokogiri to process the data loaded with the open command (above).

```ruby
#load url data in to nokogiri
data = Nokogiri::HTML(html)

#output the name of the sub reddit
puts data.css('span.pagename').text
#outputs: "aww"
```

You can also retrive a collection of items and loop through them in the same way we would loop through any array.

```ruby
data.css('p.title a.title').each do |title|
    puts title.text
end
```
