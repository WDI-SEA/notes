# Internet Fundamentals V2

## Lesson Objectives

1. Define what a server is
2. Diagram the request response cycle
3. Describe the different parts of a URL
4. Explain what Node.js is and why it's useful
5. Diagram how the internet works
6. Explain what DNS is
7. Describe what packets are and how they travel to servers

## Define what a server is

A server is just a computer that is always turned on and connected to the internet

## Diagram the request response cycle

![Request Response Cycle](https://cdn.zapier.com/storage/photos/9ec65c79de8ae54080c1b417540469a6.png)

There are four different types of requests we can make which correspond to four basic ways we can manipulate data

* POST \(Create data\)
* GET \(Read data\)
* PUT/PATCH \(Update data\)
* DELETE \(Destroy data\)

## Describe the different parts of a URL

URL stands for Uniform Resource Locator, and it's just a string of text characters used by Web browsers, email clients and other software to format the contents of an internet request message.

Let's breakdown the contents of a URL:

```text
    http://www.example.org:3000/hello/world/foo.html?foo=bar&baz=bat#footer
    \___/  \_____________/ \__/ \_________________/ \_____________/ \____/
  protocol  host/domain    port        path          query-string  hash/fragment
```

| Element | About |
| :--- | :--- |
| protocol | the most popular application protocol used on the world wide web is HTTP. Other familiar types of application protocols include FTP, SSH, GIT, FILE, HTTPS |
| host/domain name | the host or domain name is looked up in DNS to find the IP address of the host - the server that's providing the resource |
| port | a server can have multiple applications listening on multiple ports.  This allows users to access a different application on the same host |
| path | web servers can organize resources into what is effectively files in directories; the path indicates to the server which file from which directory the client wants |
| query-string | the client can pass parameters to the server through the query-string \(in a GET request method\); the server can then use these to customize the response - such as values to filter a search result |
| hash/fragment | this URL fragment is generally used by the client to identify some portion of the content in the response; interestingly, a broken hash will not break the whole link - it isn't the case for the previous elements |

## Explain what Node.js is and why it's useful

* Node is just a command line application that reads a JavaScript file and executes it within the context of the terminal
  * until recently, JavaScript could only be executed within a browsers
* Node allows JavaScript to become the first programming language that can be executed in both the browser and in a terminal application
  * Makes it easier to find a developer who can build all aspects of a web application
* Asynchronous
  * Uses event handlers \(just like click, hover, etc\) so you can tell an application to run code while waiting for other commands to finish executing
    * previously, long running commands like updating a database would have to finish before the application could continue running

## Diagram how the internet works

* [How the Internet Works in 5 Minutes](https://www.youtube.com/watch?v=7_LPdttKXPc)
* Request starts at local computer
* Goes to Router \(can have multiple computers hooked up to it, forming a Local Area Network\)
* Goes to Modem
* Goes ISP \(internet service provider\)
* ISP is connected to other ISPs and similar institutions
  * we're in the actual net at this point
* If the ISP isn't connected to the Network containing the final destination
  * it will ask the networks it is connected to if they are connected to the final destination's network
  * this process continues, building up a path to the final destination
    * each path to the final destination contains how many nodes it must visit to get to destination
    * can determine shortest path to final destination
* Once connection to final destination is made, it goes to final destination's network \(ISP\)
* From ISP it goes to the modem
* From the modem, it goes to the router
* From the router, it goes to the host computer

## Extra stuff

### HTTP Status Codes

When requests and responsese are made 2 things are sent

* headers
* body

Request/Response Headers   
 Always sent, which give details about the request/response. Things like:

* Accept: types of media allowed \(ie `text/plain`\)
* Date: the date
* Host: domain name of host

[A more complete list here](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields)

The other portion is the `body` of the request. The `body` may be empty, but generally includes the actual content being sent.

`Express` and our browser will be handling most of the details of our request/response headers.

However, we often will want to send HTTP Status Codes. The most common ones we encounter is propbably `404` Not Found.

We can get a sampling of codes, with memorable visuals [here](https://www.flickr.com/photos/girliemac/sets/72157628409467125/) or [here](https://httpstatusdogs.com/)   
 Or, [here is a link to the offical documents](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html)

### Explain what DNS is

Domain Name Servers help convert a domain \(example.com\) to an IP address. Similar to how people and places have phone numbers and you can use a phone book to look up the phone numbers. So rather than having to remember an arbitrary set of numbers, you can have a name for it that is easier to remember/ type.

#### What is the Resolution Process:

!\[DNS Resolution\]\([https://en.wikipedia.org/wiki/File:Tcp\_state\_diagram.png](https://en.wikipedia.org/wiki/File:Tcp_state_diagram.png)

* [DNS Explained](https://www.youtube.com/watch?v=72snZctFFtA)
* If computer can't find IP in cache, it asks The Resolving Name Server \(configured in OS\)
* If RNS doesn't have info in memory, it will ask the Root Name Servers
* Root Name Server know where TLD \(Top Level Domain\) servers are \(.com, .edu, .gov, etc\)
* TLDs know where Authoritative Name Servers are \(example.com\)
* Authoritative Name Servers knows the IP address of final destination
* Resolving Name Server gives IP to the operating system

#### How does the Authoritative Name Server know IP address?

1. When a domain is purchased
   * the registrar \(company that registers the domain name, e.g. godaddy\) is told which Authoritative Name Severs to use
   * The Authoritative Name Server is also told which IP address to use
2. The registrar then notifies the organization responsible for TLD name servers \(the registry\)
3. The registry tells the TLD name servers \(.com, .net, etc\) which Authoritative Name Servers to use for that new domain

### Describe what packets are and how they travel to servers

* [How Packet Travels in Network](https://www.youtube.com/watch?v=xIuBmOufbls) **Watch on your oqn**
* Everything you do on the Internet involves packets. For example, every Web page that you receive comes as a series of packets, and every e-mail you send leaves as a series of packets. Networks that ship data around in small packets are called packet switched networks. [Source](https://computer.howstuffworks.com/question525.htm)
* **Problem** 
  * If a problem occurs, data in transit is lost forever
  * Sender would have to send entire data all over again
    * think about resending an entire movie just because something dropped for a moment at the last second
* **Solution**
  * Break each transmission up into tiny chunks
  * Receiver reassembles the chunks as they are received
  * If one piece is missing, sender just resends that tiny chunk

_This lesson was adapted from_ [_SEIR-MAE_](https://git.generalassemb.ly/Software-Engineering-Immersive-Remote/SEIR-MAE-INSTRUCTORS/blob/master/unit_2/w09d1/instructor_notes/INTRO_TO_INTERNET.md)

