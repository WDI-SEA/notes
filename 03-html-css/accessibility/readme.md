# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Accessibility

## Lesson Objectives

After this lesson, you will be able to...

* Define accessibility in terms of web development
* Describe why accessibility is an important topic 
* Name a few ways to improve accessibility on a website 

## What is Accessibility in Terms of a Web Page?

You may hear the word "accessibility" and think of wheelchair ramps and wonder what that has to do with web development. In fact, an accessible website is one that anyone with a disability can use. This includes the obvious: people who are blind and depend on a screen-reader, but it also includes other disabilities such as:

* auditory
* cognitive
* visual (not just blindness)
* physical
* neurological
* speech

## Why Accessibility?

There are several ways to improve the accessibility of your website, but what about the greater question... why bother? You may note that most of the ways to improve accessibility include extra time and more typing. Why do that when there are deadlines looming and other shinier things that might make money?

Believe it or not, accessibility is totally a money issue. One reason is that you're excluding potential customers. If someone can't use your site, they won't buy your product or give you views or ad revenue. A perhaps less obvious reason is that companies do get sued over accessibility issues. In fact, [according to a recent study done by a law firm](https://www.adatitleiii.com/2019/01/number-of-federal-website-accessibility-lawsuits-nearly-triple-exceeding-2250-in-2018/), the number of lawsuits of website accessibility tripled between 2017 and 2018. Most sources expect that number to continue to rise. 

> In 2020, when we get new figures, please bug your instructor for an update!

Additionally, there is an issue of fairness, from which the ADA compliance laws stem. As put by the person who invented the internet:

_"The power of the Web is in its universality. Access by everyone regardless of disability is an essential aspect."_ -Tim Berners Lee ([Source](https://www.w3.org/WAI/fundamentals/accessibility-intro/))

In other words, our usage of the web is so pervasive, that you couldn't really live a normal life if you weren't able to use it.

One last reason to make your website accessible (if you weren't convinced already) is that an accessible website is often good for people without a disability too. Think about how we increasingly use smaller or embedded devices, or the fact that people can have "temporary" or even "situational" disabilities, like a broken arm or inability to read a screen in bright sunlight. Because of its emphasis on logical ordering, it can also be useful for people with slow internet connections who may not get the benefit of your fancy CSS and JavaScript.

In conclusion, we care about accessibility for the following reasons:

* It's costing real money
* It's a matter of fairness
* It also benefits non-disabled people

## How Do We Accomplish Accessibility?

Okay, it's important, but where do we even start?

The first thing we should know about are the official standards that are cited in the above mentioned lawsuits, the [Web Content Accessibility Guidelines](https://www.w3.org/WAI/WCAG21/quickref/?versions=2.0). However, these docs can be a bit dense for those of us who aren't super into reading technical documents. Here's a couple of [important highlights modified from this blog](https://juiceboxinteractive.com/blog/accessibility-checklist/).

### Alt Text

All of your image tags are required to have alternate (alt) text attribute. That looks something like this in your HTML:

```html
<img src="https://media.giphy.com/media/C9ttWNVgNj4Qw/giphy.gif" alt="Kitten falling over">
```

> Tip: If an image is _purely_ decorative, you can provide an empty value to the alt attribute to indicate to a screen reader it should be ignored. (i.e., `alt=""`)

### Link Text

Make your link text as descriptive as possible. Try to avoid text like "Click Here".

*YES:*

```html
Read more on <a href="mysistersblog.com">my sister's website</a>
```

*NO:*

```html
<a href="mysistersblog.com">Read more</a> on my sister's website!
```

### Header Heirarchy

Your site should have properly nested headers. This means, you have just one `<h1>` tag and the second level headers are `<h2>`, and so on. You wouldn't skip from `<h2>` to `<h4>` without also using an `<h3>` in between.

*YES:*

```html
<h1>Main Page Title</h1>
<h2>Super Important Topic</h2>
<h3>Sub-Topic 1</h3>
<h3>Sub-Topic 2</h3>
<h4>Details about sub-topic 2</h4>
<h3>Sub-Topic 3</h3>
<h2>Another Super Important Topic</h2>
<h3>Sub-Topic</h3>
```

*NO:*

```html
<h1>Main Heading</h1>
<h1>Another Main Heading</h1>
<h1>Everything I Say Is Super Important??</h1>
<h4>Except this apparently</h4>
<h1>Another Main Heading!</h1>
```

*ALSO NO:*

```html
<h1>Main Page Title</h1>
<h6>Well, I like to use the headings to size my text, even though that's what CSS is for</h6>
```

### Text Contrast

Can your text be easily read? UX Designers you work with may be able to get technical about contrast ratios, but the bottom line is don't put text on a background that is too close in hue to its background color. This is even more important for small text.

### Use Headers Without a Mouse

Can all your header links and dropdown items be accessed without a mouse (by keyboard alone)? Are you sure? If you used a CSS framework's blueprint for a header the answer is probably yes, but if you just made one yourself... double-check!

### Skip to Main Content

Speaking of headers, you've likely been on a website that has 60 or 70 links in a huge header with lots of dropdowns and sub-menus. If you've got to press "tab" 70 times to get to the main content, that isn't exactly accessible. Include a skip to main content link to further down on your page.

### ARIA

ARIA stands for Accessible Rich Internet Application. It's used to denote the purpose of things like sliders, tooltips, and tab panels that otherwise wouldn't be able to be understood simply by looking at the HTML alone.

[MDN's ARIA page](https://developer.mozilla.org/en-US/docs/Web/Accessibility/An_overview_of_accessible_web_applications_and_widgets) describes the following issue. How would you know that the following described a tab list and tab panel? (Particularly if the developer had chosen poor naming conventions?)

```html
<!-- This is a tabs widget. How would you know, looking only at the markup? -->
<ol>
  <li id="ch1Tab">
    <a href="#ch1Panel">Chapter 1</a>
  </li>
  <li id="ch2Tab">
    <a href="#ch2Panel">Chapter 2</a>
  </li>
  <li id="quizTab">
    <a href="#quizPanel">Quiz</a>
  </li>
</ol>

<div>
  <div id="ch1Panel">Chapter 1 content goes here</div>
  <div id="ch2Panel">Chapter 2 content goes here</div>
  <div id="quizPanel">Quiz content goes here</div>
</div>
```

The answer is basically, you wouldn't have any way of knowing. That's where ARIA comes in. Here's an example of the same thing, but properly labelled.

```html
<!-- Now *these* are Tabs! -->
<!-- We've added role attributes to describe the tab list and each tab. -->
<ol role="tablist">
  <li id="ch1Tab" role="tab">
    <a href="#ch1Panel">Chapter 1</a>
  </li>
  <li id="ch2Tab" role="tab">
    <a href="#ch2Panel">Chapter 2</a>
  </li>
  <li id="quizTab" role="tab">
    <a href="#quizPanel">Quiz</a>
  </li>
</ol>

<div>
  <!-- Notice the role and aria-labelledby attributes we've added to describe these panels. -->
  <div id="ch1Panel" role="tabpanel" aria-labelledby="ch1Tab">Chapter 1 content goes here</div>
  <div id="ch2Panel" role="tabpanel" aria-labelledby="ch2Tab">Chapter 2 content goes here</div>
  <div id="quizPanel" role="tabpanel" aria-labelledby="quizTab">Quiz content goes here</div>
</div>
```

### Semantic Tags

Semantic tags are descriptive of using the HTML tags in a way that conveys their purpose. So for example, using an `<h1>` as a first-level heading and not just a way to make your text big. Another example of a non-semantic usage is using a `<p>` tag to create extra space, as opposed to making a paragraph text like it is supposed to.

> Generally using tags to create space is bad. Remember to make CSS do its job!

Semantic tags, particularly HTML5 additions, often tend to highlight sections of your website, so they are very, very helpful for screen readers. Otherwise a screen reader doesn't necessarily know what order to consume information.

Common semantic tags include:

* nav
* main
* footer
* section
* aside
* summary
* details

### Labels (in Forms)

That `<label>` tag you are likely tired of typing in your forms has a purpose. Your form will be accessible!

### Accessible Names for Icons

Somewhat related to alt text for images, there should be accessible names for every visual component. You might not think twice about using an icon for an edit button or a delete button or something else, but how is a screen reader supposed to know how to deal with it?

[Font Awesome Icons Accessibility Page](https://fontawesome.com/how-to-use/on-the-web/other-topics/accessibility) describes a great way to use a car icon:

```html
<i aria-hidden="true" class="fas fa-car" title="Time to destination by car"></i>
<span class="sr-only">Time to destination by car:</span>
<span>4 minutes</span>
```

As you can see, the icon has a title and a name that describes it ("fa-car" where "fa" just stands for "Font Awesome"). Additionally there is a span tag with "sr-only" (screen reader only, not for display - this is a class defined in the Bootstrap CSS framework) to describe verbally what a seeing user would understand from the icon or picture.

### Captioned Videos

You didn't think so much about vision impairment that you forgot about hearing impairment did you? All videos with sound should be captioned or should be provided with a transcript!

### No Strobe Lights!

Though it may be tempting, your pages shouldn't contain any quick flashing!

![The Cheat Lightswitch Rave](https://thumbs.gfycat.com/AdvancedKlutzyCopperbutterfly-small.gif)

## Conclusion and Resources

Remember, this is far from an exhaustive list! All of the above examples were just some highlights we picked out to discuss. Feel free to dive deeper with these as a starting point:

* [W3C](https://www.w3.org/WAI/fundamentals/accessibility-intro/)
* [Web Content Accessibility Guidelines 2.1](https://www.w3.org/WAI/WCAG21/quickref/?versions=2.0)
* [MDN's Intro to ARIA](https://developer.mozilla.org/en-US/docs/Web/Accessibility/An_overview_of_accessible_web_applications_and_widgets)
* [WAI-ARIA Docs](https://www.w3.org/TR/wai-aria-1.1/#introstates)
* [ADA Lawsuits Source](https://www.adatitleiii.com/2019/01/number-of-federal-website-accessibility-lawsuits-nearly-triple-exceeding-2250-in-2018/)
* [Accessibility Checklist](https://juiceboxinteractive.com/blog/accessibility-checklist/)
