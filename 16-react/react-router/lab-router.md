## ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) React Router Recap and Exercise

## Recap
What have we learned so far?
* Single Page Applications have specific URLs that are routed to display
  different content.
* React Router is a third-party library that we can install and use with React.
* Since React Router isn't built in to React, we must import its components.
* React Router makes it easy for us to route URLs to components.
* React Router automatically manipulates modern browser history mechanics.

Now let's put that to the test!

## You Do: Implement Router

Let's continue our blog project.

Your blog needs to have five pages:
- Homepage
- Main blog
- Favorite movie
- Favorite food
- About page

You already have the "Main blog" page, which renders the `Post` component! One down, four to go.

Task:

- Each page is a component - we're learning to use React Router here!
- Create a navigation menu of list items that Route to each page.
  - These pages don't need to have much content — just the header at the top saying what the page is and a paragraph description of your choosing.

_Fun Note:_ There's no reason you can't change the CSS, if you'd like! The CSS file that you'll change is `App.css`. If you'd like, you can grab ours [here](https://git.generalassemb.ly/education-product/React-Exercise-Solutions/blob/master/projects/project-04-router/solution-code/src/App.css).
 - Thought exercise: Why is that the only CSS file you need to change?

**Hint**: You'll need multiple `.js` files

**Hint**: Do you have `react-router-dom` installed for this project?

**Hint**: You can instantiate a component with `props` inside of a `<Route>` element. An example is below:


```js
<Route path="/blog" component={
    () => (<Blog title={post.title}
              author={post.author}
              body={post.body}
              comments={post.comments} />
)}/>
```


## Solution

Your solution should look something like as follows:

![Solution for Project](https://github.com/WDI-SEA/react_router_global/blob/master/assets/router-solution.png)
