# Internet Fundamentals

#### Answer and discuss the following questions with a partner:

- What does HTTP stand for?
- Which protocol is used to resolve a domain name to an IP address?
- How do clients compare to hosts?
- Compare different HTTP status codes.
- Draw your own diagram of a request/response cycle and label where the following would come into play: client, host/server, URL, client-side languages, server-side languages, data
- T/F: HTTP headers can be changed by a user before executing a request.
- T/F: Every HTTP request has a domain and a path.
- T/F: Email uses the HTTP Protocol.

#### Experiment with cURL and send requests to various web pages. Here are some useful flags you can use:
```
# -I returns the response headers only
curl -I http://www.google.com

HTTP/1.1 200 OK
Date: Sun, 27 Sep 2015 02:28:12 GMT
Expires: -1
Cache-Control: private, max-age=0
Content-Type: text/html; charset=ISO-8859-1
...


# -v is verbose mode and returns the entire request and response (along with some additional info)
curl -v http://www.google.com
* Rebuilt URL to: http://www.google.com/
*   Trying 2607:f8b0:400a:806::2004...
* Connected to www.google.com (2607:f8b0:400a:806::2004) port 80 (#0)
...
```

#### Using cURL and the `-I` flag, get the following response codes from some webpages:

- 2xx - examples include 200 (OK), 201 (Created)
- 3xx - examples include 301 (Moved permanently)
- 4xx - examples include 400 (Bad request), 404 (Not found)

