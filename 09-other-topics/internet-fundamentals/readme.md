# How the Internet works

### Objectives

- Explain the difference between a client and server
- Explain the difference between an HTTP request and an HTTP response.
- Identify the difference between the Internet and the World Wide Web
- Describe the purpose of an Internet Protocol (IP) address
- Summarize how data travels through the internet
- Breakdown the components of a URL: protocol, subdomain, domain, extension, resources
- Identify the most common HTTP request/response headers

##How the Internet Works in 5 Minutes

<iframe width="100%" height="590" src="https://www.youtube.com/embed/7_LPdttKXPc" frameborder="0" allowfullscreen></iframe>

https://www.youtube.com/watch?v=7_LPdttKXPc

## Server, Client, Request, HTTP

The internet as you know comes down to requests and responses - you send information out to the web, and based on the info you send, you get information back.

#### HTTP 101

HTTP stands for "Hyper Text Transfer Protocol" - because it's a protocol, it allows for communication between a variety of different computers and supports a ton of different network configurations. To make this possible, it assumes very little about a particular system, and does not keep state between different message exchanges.

Read this as: "HTTP makes it easy for many different computers to talk to each other."

This makes HTTP a stateless protocol.

Let's define the following vocabulary:

- **Host** - a computer or other device connected to a computer network; host may offer information resources, services, and applications (via computer code!) to users or other computers on the network
  - Ex: servers and web services
- **Client** - the requesting program in the client/host relationship; the client initiates an HTTP request message, which is serviced through a HTTP response message in return
  - Ex: browsers, terminals, SQL clients

To sum it up, communication between a host and a client occurs via a request/response pair. The client initiates an HTTP request message, which is serviced through a HTTP response message in return. We will look at this fundamental message-pair in the next section.

Now, we're making this really simple, just to give you the big idea - there are a ton of intricacies that go into getting your request message to the right place and delivering the information you requested.  We'll go into more detail today and over the rest of the course.


_Text From [Tuts +](http://code.tutsplus.com/tutorials/http-the-protocol-every-web-developer-must-know-part-1--net-31177)_


####Exercise

Pair up in groups of 2, and have one person be the client, one person be the server. Initiate requests and responses by crumbling paper with a request (a web address) and throwing them back and forth.

#### How to reach a specific server

All computers on the internet have a unique numeric address composed of four bytes of data, separated by periods. This is the way computers find "each other" when communicating. You may recognize the format below - it's an IP address:

```
123.123.123.123
```

#### IP Addresses to domains

Of course, these numbers are hard to remember, and are not really human-friendly. Can you imagine if website addresses had to be given this way? Instead of commercials on the radio saying "go to OurWebsite.com", they'd be saying "go to 12.14.142.231" and repeating it five times just to make sure everyone got it!

So what was needed was a way to translate real names in to those numbers. This is why we have domain registrars - basically, you reserve the name, and at the domain registrar, your domain name is pointed to the server's particular unique address.

When you type a website domain in to your web browser (or other internet capable app), what happens is a "DNS Lookup" of that particular domain's IP address, so your computer can actually connect to it.  DNS stands for "Domain Name System", and it's the way that Internet domain names are located and translated into Internet Protocol addresses.

| Domain Name  | IP Address    |
|--------------|---------------|
| apple.com    | 17.172.224.47 |
| facebook.com | 31.13.65.1    |
| google.com   | 216.58.192.46 |

Your internet provider has a nice little cached list of all of the registered domains - and their respective IP addresses - so when you go to apple.com, your browser asks the DNS server "what is the IP address of apple.com?" The DNS server responds with "17.172.224.47", and the browser can then connect to 17.172.224.47.

In real world terms, it's like how we use street addresses for finding a house, rather than using Latitude and Longitude coordinates - they're easier to remember and to read.

#### Client and server communication

All client-server protocols operate in the application layer. The application-layer protocol defines the basic patterns of the dialogue.

A server may receive requests from many different clients in a very short period of time. Because the computer can perform a limited number of tasks at any moment, it relies on a scheduling system to prioritize incoming requests from clients in order to accommodate them all in turn. To prevent abuse and maximize uptime, the server's software limits how a client can use the server's resources. Even so, a server is not immune from abuse. A denial of service attack exploits a server's obligation to process requests by bombarding it with requests incessantly. This inhibits the server's ability to respond to legitimate requests.

#### Example

*When a bank customer accesses online banking services with a web browser (the client), the client initiates a request to the bank's web server. The customer's login credentials may be stored in a database, and the web server accesses the database server as a client. An application server interprets the returned data by applying the bank's business logic, and provides the output to the web server. Finally, the web server returns the result to the client web browser for display.
In each step of this sequence of client--server message exchanges, a computer processes a request and returns data. This is the request-response messaging pattern. When all the requests are met, the sequence is complete and the web browser presents the data to the customer.*


*Taken from [Wikipedia](https://en.wikipedia.org/wiki/Client%E2%80%93server_model)*

## What Is the Difference Between the Internet and the Web?

#### The Internet is a Big Collection of Computers and Cables

The Internet is named for "interconnection of computer networks". It is a massive hardware combination of millions of personal, business, and governmental computers, all connected like roads and highways.

No single person owns the Internet. No single government has authority over its operations. Some technical rules and hardware/software standards enforce how people plug into the Internet, but for the most part, the Internet is a free and open broadcast medium of hardware networking.

#### The Web Is a Big Collection of HTML Pages on the Internet

The World Wide Web, or "Web" for short, is a massive collection of digital pages: that large software subset of the Internet dedicated to broadcasting content in the form of HTML pages. The Web is viewed by using free software called web browsers. Born in 1989, the Web is based on hypertext transfer protocol, the language which allows you and me to "jump" (hyperlink) to any other public web page. There are over 65 billion public web pages on the Web today."

- Taken from [About Tech](http://netforbeginners.about.com/od/i/f/What-Is-The-Internet.htm)


#### Elements of a URL

URL stands for Uniform Resource Locator, and it's just a string of text characters used by Web browsers, email clients and other software to format the contents of an internet request message.

Let's breakdown the contents of a URL:



```
    http://www.example.org/hello/world/foo.html?foo=bar&baz=bat#footer
    \___/  \_____________/ \__________________/ \_____________/ \____/
  protocol  host/domain name        path         querystring     hash/fragment
```

Element | About
------|--------
protocol | the most popular application protocol used on the world wide web is HTTP. Other familiar types of application protocols include FTP, SSH, HTTPS
host/domain name | the host or domain name is looked up in DNS to find the IP address of the host - the server that's providing the resource
path | web servers can organise resources into what is effectively files in directories; the path indicates to the server which file from which directory the client wants
querystring | the client can pass parameters to the server through the querystring (in a GET request method); the server can then use these to customise the response - such as values to filter a search result
hash/fragment | the URI fragment is generally used by the client to identify some portion of the content in the response; interestingly, a broken hash will not break the whole link - it isn't the case for the previous elements




_The Schema above is from [Tuts +](http://code.tutsplus.com/tutorials/http-the-protocol-every-web-developer-must-know-part-1--net-31177)_


When someone types `http://google.com` in a web browser, a new cycle resulting in an HTTP  Request/ Response is initiated.  Essentially, your browser is saying:

_"Hey, give me the information located at the web address 'google.com'"_

When the user press enter in the url input in a web browser , a `GET request` will start, this is what this request will look like:

![http request CLI](https://i.imgur.com/58nCl0e.png)


Note, the webpage being requested is:

`http://www.google.co.uk/?gfe_rd=cr&ei=WkvPVabgC-HH8gfWjoCIAw`

Anything after the `?` is considered a parameter - information you're also giving to that web address in the querystring.

In the response, the HTTP version is provided, which in this case is 1.1.

The rest of the lines are HTTP headers, which do things like: tell the webserver what website to retrieve, based on the domain (Host:); report the user-agent and acceptable encoding and language; and other browser-specific options.

## Responding to a request - Intro


Once this request reaches the server, then this server will return a response to the request emitter.

HTTP responses are similar to HTTP requests in the way that they are text based and contain HTTP headers and status. Look on the first line above, again - the HTTP response returns the HTTP status code. This code is very useful for developers working with request/response cycles.

They come as three digit numbers and dictate whether a specific HTTP requests has been successfully completed. Responses are grouped in five classes, with the first digit determining the higher-level categorization:

- 1xx Informational
- 2xx Success
- 3xx Redirection
- 4xx Client Error
- 5xx Server Error


After the status code, some server headers are sent, including information about the type of server and software it's running. Next, the body of the response contains the data we requested, which is generally HTML, CSS, Javascript, or binary data like an image or PDF.

Since HTTP is a text-based protocol, it's easy to make HTTP requests manually


_Some text taken from [One Month](http://learn.onemonth.com/understanding-http-basics)_


####Exercise

Pair up in the same groups, and have one person be the client, one person be the server. Initiate requests and responses by crumbling paper with a request and throwing them back and forth.

* The client should write out the host, path, and any data being sent to the server.
* The server should write out a response (404, 401, 500, 200, etc.);


#### Server-side vs. Client-side

Once the request <--> response cycle has been executed, the web browser is in charge of interpreting the data received and showing it to the user.  Looking more closely at the types of computer languages and markup that's involved:

![](http://image.slidesharecdn.com/html-css-presentation-131023112801-phpapp02/95/html-csspresentation-7-638.jpg?cb=1383133015)

The server contains code - Ruby, C, Java, even JavaScript - that processes your request.  Depending on the contents of your request, the server will execute different files, containing code, and return a particular set of information and data.

The information and data received received is usually packaged in an HTML document with some CSS and JavaScript files. You may also get a PDF, image, or some other type of content. The location of the resource is specified by the user using a URI (Uniform Resource Identifier).

The way the browser interprets and displays HTML files is specified in the HTML and CSS specifications. These specifications are maintained by the W3C (World Wide Web Consortium) organization, which is the standards organization for the web.


_Taken from  [HTML5Rocks](http://www.html5rocks.com/en/tutorials/internals/howbrowserswork/)_


## Conclusion

The foundational concepts taught in this lesson will be important for the duration of the course because we will use the internet everyday, and if you are struggling with how the data is received on the server, please come back to this lesson and ask questions to your instructional team.
