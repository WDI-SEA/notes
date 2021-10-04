# DOM Review Lab

Title: 'Vanilla' DOM commands  
 Type: Lab   
 Duration: 45 - 60 mins  
 Creator: Karolin Rafalski   
 Original Inspiration by : Thom Page Topics: DOM intro with Vanilla JS  
 Adapted by: Taylor Darneille

## JS DOM commands

This is an exercise to get you familiar with the concept of the DOM and the pattern of how we interact with it.

At the bottom of the DOM Review notes is an appendix of vanilla DOM commands; use that and your notes from lecture to complete the following

## Setup Part 1

1. Make a new directory called `vanilla_dom_practice` that contains three files: `index.html`, `dom_practice.js`, and `readme.md`
2. Make `vanilla_dom_practice` a git repo by running `git init` in the terminal **MAKE SURE YOU'RE IN THE CORRECT FOLDER BEFORE RUNNING GIT INIT**. Then to go [github.com](https://github.com/) and create a new remote repository called `vanilla_dom_practice`. Follow the instructions to push your recently created local repo to this new remote repo.

```text
git add . (or git add -A)
git commit -m "initial commit"
git remote add origin git@github.com:TaylorDarneille/vanilla_dom_practice.git
git push -u origin master
```

_after this last part, you'll always be able to just run `git push` to push committed changes to github \(wihtout the -u flag\)_

### Throughout this whole lab, make a commit after you complete each step!!! This will allow us to grade it properly.

1. Load your `index.html` file for this lab into the browser and make sure that the proper js file is connected.

## Setup Part 2

#### Make a web page for your hometown

Include:

* html boilerplate
* a link to your js file
* an `h2` tag with a `welcome to` and the name of your hometown
* an image of your hometown
* an `h4` tag that says `Featuring`
* an `ol` tag \(ordered list\) that has
  * 2 - 5 `li` elements that have text of things in your town
* two other html elements of your choice, they can be anywhere in your HTML's `body` \(maybe a `div` or `footer` if you are short for ideas\)
* give one element an id
* give at least two elements a class

**Note:** The focus of this lab is the DOM so don't spend more than 10 minutes on the set up and don't do any extra HTML, skip the CSS for now, CSS is the Hungry for More, if you have time at the end

## How to Check Your Work

**Check the results of your commands in the Elements tab and in the Console** \(some divs won't have text, etc. but you can see the element appearing in the DOM in the elements tab.\)

Remember: to see it in the **console**, you will need to either log the JS code or save the code to a variable and log the variable. Save your file and the refresh your browser.

## ⌘R

⌘R in your browser, or Command-R will **reload** your webpage after you have made changes to your html, css, or js files \(if your OS has focus on the browser\).

## Part 1 Draw the DOM tree structure

* Based on your HTML, draw the tree of your elements, starting with the `document` as the root and branch off from there
* You can do this on paper and take a photo and [upload it to the `readme.md`](https://guides.github.com/features/mastering-markdown/#) to have a record; you can also use a drawing program if you are more comfortable doing that
* Think about which elements are children, which are siblings, which are 'leaves' or the end of the tree. Can you branch off of text?

## Part 2 Manipulate the DOM

### Notes

Use `document.querySelector()` to find your an element

Use `document.querySelectorAll()` to find a collection of elements in the DOM.

Refer back to the instructor notes \(and the appendix at the bottom\) - for more details/syntax checks

### Activity

#### Query and change some elements

🔵 Get the element with the id you assigned and save it to a variable . Console.log that variable.

**Make sure** you get the element logged in the console:

![](https://i.imgur.com/1ocG4tc.png)

🔵 Get the `h2` element and save it to a variable `h2`. Console.log that variable.

🔵 Using JavaScript, change the innerText of your `h2` to have 3 exclamation points at the end

🔵 Get all of the elements with the class you assigned and save them to a variable. Console.log that variable.

**Make sure** you get an array:

![](https://i.imgur.com/Ahh8J0C.png)

And **not this** \(a single element\)

![](https://i.imgur.com/2YLSvzd.png)

Why?

🔵 Change the style/color of the text of your ONE of your `li` elements to your [favorite html color](https://htmlcolorcodes.com/color-names/)

🔵 Change the innerText of one of your list items to 'Jamboree sandwich at the Jambo-ree'

#### Create an element and append it

🔵 Create a new `img` element using `document.createElement()`

🔵 Add an attribute for the source url of your new image using `.setAttribute()`

🔵 Append it to your page, somewhere, using `.appendChild()`

🔵 Check that your image has appeared

BONUS:

Change the style/color of the text of your ALL of your `li` elements to another [favorite html color](https://htmlcolorcodes.com/color-names/)

#### Remove an element:

🔵 Select any element using `querySelector` and save it to a variable

🔵 and remove it from your page using `.remove()`

* if you would like your element to stay, just comment this line of code out - so you have it as a reference

## Submitting:

Slack your homework grader with the link to the github repo you made for this assignment!

### Hungry for More

* Now would be a good time to get a little extra CSS practice
* Go ahead and style your page with some CSS

### Wildly Ravenous for Even More

* Build an image carousel that scrolls through 2-4 images every 2-3 seconds

