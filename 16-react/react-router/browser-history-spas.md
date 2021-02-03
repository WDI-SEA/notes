## ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Browser History Mechanics and Single Page Applications


### Learning Objectives
*After this lesson, you will be able to:*
* Define old browser history mechanics
* Define routing
* Define Single Page Applications (SPAs)
* Understand why old browser history mechanics don't work for SPAs
* Describe modern browser history mechanics

## Browser History Mechanics

Browsers have built in history mechanics. You can go **back** and **forward**
between pages you've been been to and you can **reload** the page you're on.
- Browsers have built in buttons for users to do just that - go **back** and **forward** between pages the user has visited.
- These actions are also available to us in JavaScript.
  - We can write JavaScript programs that invoke `window.history.back()` and `window.history.forward()`.

This seems pretty straightforward, right?

However, the rise of recent approaches to websites - like React - broke old, traditional browser history mechanics and led to the introduction of new ways for websites to control what **back** and **forward** really mean.


## Exercise
Open a new tab in your browser and navigate to the Wikipedia article for
[Cafe Allegro](https://en.wikipedia.org/wiki/Cafe_Allegro) in Seattle.

* Hover over the link to the "Seattle" entry near the top of the article and look at the URL.
* Notice that the URL says `wikipedia.org/wiki/Seattle`. It does not include `Cafe_Allegro`, and there is no hashtag. This URL takes us to an entirely different page.
* Click the link to "Seattle" and notice how your browser goes blank and loads another page, which is also full of links to other articles.
* Click on several more links, paying attention to when the browser goes blank and loads a completely new page.
* Hold down your mouse on the **back** button. You'll see a drop down menu
  showing every page you've been on.

Holding down the back button to look at your browser history should show
something like this:

![Cafe Allegro to General Assembly](https://res.cloudinary.com/briezh/image/upload/v1556732364/allegro_to_GA_oneyhh.png)

Browser history mechanics are built for going **back** and **forward** between
different pages. Browsers have the back and forward buttons for users. These
actions are also available to us in JavaScript. We can write JavaScript programs
that invoke `window.history.back()` and `window.history.forward()`.

It's important to specifically note what a "page" is.
- A page is a whole HTML file that your browser downloads and displays. You know you're navigating between two different pages when you see your browser screen go blank then slowly load in a totally new page.

Pages can be all on the same site or on many different sites. A site is a domain, such as Yelp.com, IMDB.com, Google.com.

Browsing pages on one site is like viewing different articles on Wikipedia - you haven't left the Wikipedia site; you're just looking at different pages on it.

Browsing pages on different sites is like using a search engine to look up a restaurant, looking at Yelp's website, and then looking at a restaurant's official website. The
browser is still visiting different *pages* they're just on different *sites*.

We're going into detail about what a page is in order to draw contrast to how
modern web applications don't use multiple pages like they used to. Modern web
applications are now often what we call **Single Page Applications**.

Before we get into Single Page Applications, let's talk about URL routing.

## What is URL Routing?
**Routing** defines what content is displayed when someone visits a certain a
URL.
- If you go to `http://github.com/`, you expect to see GitHub's home page.
- If you go to `http://github.com/login`, you expect to see a log-in page.
These are two different pages on the same site, and each of these URLs is a **route**. Each
of these URLs is a **route**. A route pairs a URL with the content that should
be displayed for that URL. If you visit a webpage, copy the URL, and send it to a friend, your friend should end up viewing the same page.

Let's look at an example of how content is routed by URLs by looking at the
General Assembly homepage. Go to [General Assembly's Website](https://generalassemb.ly/). Interact with the menu in the top bar on the right.

You should see options for things like "On Campus," "Locations," and
"About." Click on the different links to pages and notice the URLs that you end
up at, or hover over the links to see their URL to save yourself from actually
navigating off the page, and specifically, look at their paths.

**What's a path?**
This table shows the **path** for each URL. The path of a URL is everything
after the domain name. In this case, the path is everything that appears after "https://generalassemb.ly" in the location bar of the browser. The `/` path is a special path called the root. It loads the homepage.

Compare the paths in the URLs and get a sense for how URLs are routed to
content. Websites URLs are general split into succinct, descriptive,
hierarchical categories. Notice how going to `/locations` takes you to a page
showing all campus locations, then each specific location falls in a hierarchy under that such as `/locations/london` and `/locations/singapore`.

| **URL Route**                       | **Content**                                              |
|-------------------------------------|----------------------------------------------------------|
| /                                               | Homepage                                     |
| /about                                          | General Information                          |
| /education                                      | Shows all local upcoming courses             |
| /education/web-development-immersive            | WDI course details                           |
| /education/user-experience-design-immersive     | UX course details                            |
| /locations                                      | Shows all global GA locations                |
| /locations/london                               | Shows London-specific location information   |
| /locations/singapore                            | Shows Singapore-specific location information|

You can see that URLs *route* users to content. When someone types in a URL
they are ultimately shown content associated with that URL.

Have you ever tried to send someone a link to what you're looking at on Google
Maps and then when they click on your link they end up looking at something
completely different? That's a great example of bad URL routing. (Google Maps
is actually much better about this these days.) URLs should represent the
main content of the page you're looking at!

Old websites:
- Spread their content across multiple pages.
- Use URLs to route users to different pages.
- Can use URLs with hashtags to take the user to different content on the same page.

For example - Open a new tab in your browser and navigate back to that Wikipedia article for
[Cafe Allegro](https://en.wikipedia.org/wiki/Cafe_Allegro) in Seattle.

* Hover over the "1. History" link in the Contents section
  ![History Link](assets/hover-over-history-link.png)
* Look in the lower-left corner of your browser to see the URL associated with the link.
* Notice the URL is `wikipedia.org/wiki/Cafe_Allegro#history`. Specifically note the hashtag `#history`.
* Click the history link and notice how it scrolls you down within the same page. This still counts as a route — it's navigating you to a new section on the same page.

## Modern Single Page Applications
Now, consider web pages where, depending on what you click, the actual content of the page dynamically changes - the page itself never reloads. Modern web apps serve up just one page and then change parts of its *contents*, without having to reload the entire page or send users to another page.

Websites that serve up only one page and change the content of the page dynamically without reloading it are called **single-page applications**.

Open your browser and navigate to Gmail (or whichever email site you use):

* When you load Gmail, you see your inbox.
* You can start instant messaging a friend in a sidebar.
* You can start to compose a new email to your manager to request time off.
* You can search for an email with flight information.
* You can browse through more emails to make sure you've talked your manager about getting time off and aren't just disappearing for a week.

This all happens on one page! The page never refreshes. The chat bar with your friend never disappears as you compose an email and search through your inbox.

Gmail fits the definition of a single-page application.
- Gmail loads one page just once.
- That page replaces content dynamically to show the user many different things.
- That single page changes its content dynamically without reloading or sending you to another page.

Consider the benefits of a single page application:
* It's fast. Users don't have to wait for a page to reload over and over.
* It's persistent. You can have a chat window open in one corner and keep
  talking to a friend as the rest of Gmail switches between showing you your
  inbox, an email, or email search results.

## Single Page Apps Break Old History Mechanics!
Now here's the catch, and why we went into such detail about browser history
mechanics and defining what exactly Single Page Applications (SPAs) are - Single Page Applications break the initial design of Browser History Mechanics.

Why is this? The **back** and **forward** actions were built specifically to go back and
forth between different pages. Since single page apps only change the content
of themselves without actually sending users to different web pages the notion
of **back** and **forward** is lost.

When users press the **back** button in a Single Page Application they go back
off the one page, completely out of the Single Page Application.

Luckily for us React-Router accounts for this! But it's always great to know what's going on underneath the hood!

## Introducing Modern Browser History Mechanics

So - developers need to have their fast loading web applications, but somehow still have the 'back' button work. For awhile, when SPAs were first coming into popularity users often experienced unexpected behavior. They'd feel like they were visiting "different" pages but they weren't really, so the back button took them to the previous website they were on rather than the previous "page".

Web Developers, browser vendors, and users (even if they don't know it) all love Single Page Applications; they're a great experience that the community is embracing. To facilitate these and still have things like the 'back' button work, a few years ago, people got together in committees and devised a way to upgrade the old
browser history mechanics to accommodate modern SPAs.

The modern HTML5 specification (published in October 2014) introduced new browser history mechanics that make it easy to browse "back" and "forward" in single-page applications, even while actually staying on the same page.

**How?**

HTML5 introduced:
- `.pushState()`  
- `.replaceState()`

These are functions that allow web pages to save custom history data to the browser.

Applications like Gmail can use
these functions to manually save custom browser history. For example, Gmail can use `.pushState` to put in the browser history that a user is on their search results page, so if they go into an email and click 'back', they get back to the search page - instead of off gmail.com completely.


A bit more technically, when someone goes from
their inbox to a specific email, Gmail can use `.pushState` to save in the browser information
about what the user is currently doing in the application. Now when the user
presses the 'back' button, the browser gives the saved information back to
Gmail and Gmail brings back the content the user was last looking at.


## Recap

Here's a summary of what we've learned so far for routing:

### Single Page Applications and Browser History Mechanics

* Single Page Applications are websites that serve only one web page, then
  change the content of that page dynamically, without refreshing.
* Old browser history mechanics support **back** and **forward** operations that
  traditionally keep track of history as users move between different pages.
* Since modern Single Page Applications keep the user on one page without
  refreshing old browser history **back** and **forward** mechanics don't work
  well with modern applications - so HTML5 changed the rules of how 'back' and 'forward' can work.
