# Internet Lab

## Answer and discuss the following questions with a partner:

* What does HTTP stand for?
* What is used to resolve a domain name to an IP address?
* How do clients compare to hosts?
* Compare different HTTP status codes.
* How does TCP ensure a reliable connection?
* What are the main five HTTP request types?
* Draw your own diagram of a request/response cycle and label where the following would come into play: client, host/server, URL, client-side languages, server-side languages, data
* T/F: HTTP headers can be changed by a user before executing a request.
* T/F: Every HTTP request has a domain and a path.
* T/F: Email uses the HTTP Protocol.

## Use the `ping` command to see how long it takes for servers to respond to your computer:

All requests sent from your computer must travel across the internet, going through various servers, in order to make the delivery. Using the `ping` command in the terminal window, try to find servers that respond quickly, and find some that take longer to respond. Hit `CTRL + C` if you need to exit `ping`. **What are the fastest and slowest sites you can ping?**

> University servers are usually hosted on their actual campuses. Use university servers to estimate how long it takes requests to travel around the world. Look up the distance between cities and calculate miles / time in milliseconds to calculate how fast these requests travel.

```text
# 4 miles away from GA campus
ping washington.edu
```

### Sample Output

```text
PING washington.edu (128.95.155.134): 56 data bytes
64 bytes from 128.95.155.134: icmp_seq=0 ttl=54 time=6.478 ms
64 bytes from 128.95.155.134: icmp_seq=1 ttl=54 time=8.162 ms
64 bytes from 128.95.155.134: icmp_seq=2 ttl=54 time=6.926 ms
^C
--- washington.edu ping statistics ---
3 packets transmitted, 3 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 6.478/7.189/8.162/0.712 ms

$ ping stanford.edu # 700 miles from Seattle
PING stanford.edu (171.67.215.200): 56 data bytes
64 bytes from 171.67.215.200: icmp_seq=0 ttl=247 time=26.922 ms
64 bytes from 171.67.215.200: icmp_seq=1 ttl=247 time=28.804 ms
64 bytes from 171.67.215.200: icmp_seq=2 ttl=247 time=28.702 ms
64 bytes from 171.67.215.200: icmp_seq=3 ttl=247 time=26.987 ms
^C

$ ping www.cam.ac.uk # Cambridge University in London: 4,757 miles from Seattle
$ ping www.u-tokyo.ac.jp # The University of Tokyo: 4,787 miles from Seattle, in the other direction!
$ ping sydney.edu.au # The University of Sydney in Australia: 7,757 miles from Seattle
$ ping www.hbc.ac.za # Helderberg College in Cape Town, South Africa: 10,217 miles from Seattle
```

Ping this specific IP address and see how long it takes the server to respond. Google this IP to find out what makes it unique. Be sure to use the Google homepage. IP addresses are hard to quick-search from your browser's location bar!

```text
ping 127.0.0.1
```

## Experiment with the traceroute command to see how internet traffic flows between your computer and servers:

```text
# the traceroute command will show which servers routed the traffic
traceroute washington.edu
```

### Sample Output

```text
traceroute: Warning: washington.edu has multiple addresses; using 128.95.155.135
traceroute to washington.edu (128.95.155.135), 64 hops max, 52 byte packets
 1  10.1.4.1 (10.1.4.1)  2.372 ms  2.008 ms  1.976 ms
 2  209.63.143.50 (209.63.143.50)  4.526 ms  4.797 ms  4.356 ms
 3  209.63.101.2 (209.63.101.2)  6.384 ms  5.994 ms
    209.63.101.6 (209.63.101.6)  6.123 ms
 4  six.tr-cps.internet2.edu (206.81.80.77)  11.866 ms  5.300 ms  5.357 ms
 5  ae-1.80.rtr.seat.net.internet2.edu (64.57.20.212)  4.118 ms  6.208 ms  4.382 ms
 6  198.71.47.6 (198.71.47.6)  4.226 ms  6.278 ms  6.259 ms
 7  ae0--4000.icar-sttl1-1.infra.pnw-gigapop.net (209.124.188.132)  6.270 ms  9.782 ms  9.148 ms
 8  ae0--4000.uwbr-ads-1.infra.washington.edu (209.124.188.133)  8.508 ms  5.471 ms  5.914 ms
 9  * * *
10  * * * (ignore asterisks and press CTRL+C to quit)
```

## Experiment with cURL and send requests to various web pages. Here are some useful flags you can use:

### Headers flag

```text
# -I returns the response headers only
curl -I http://www.google.com
```

### Sample Output

```text
HTTP/1.1 200 OK
Date: Sun, 27 Sep 2015 02:28:12 GMT
Expires: -1
Cache-Control: private, max-age=0
Content-Type: text/html; charset=ISO-8859-1
...
```

### Verbose mode

```text
# -v is verbose mode and returns the entire request and response (along with some additional info)
curl -v http://www.google.com
```

### Sample Output

```text
* Rebuilt URL to: http://www.google.com/
*   Trying 2607:f8b0:400a:806::2004...
* Connected to www.google.com (2607:f8b0:400a:806::2004) port 80 (#0)
...
```

## Using cURL and the `-I` flag, get the following response codes from some webpages:

* 2xx - examples include 200 \(OK\), 201 \(Created\)
* 3xx - examples include 301 \(Moved permanently\)
* 4xx - examples include 400 \(Bad request\), 404 \(Not found\)

