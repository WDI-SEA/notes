# Nested Components

### Learning Objectives

_After this lesson, you will be able to:_

* Diagram nested components
* Render components within another component
* Pass props to a nested component

![](https://res.cloudinary.com/briezh/image/upload/v1556226718/nested-components-we-need-to-go-deeper_pt62rf.jpg)

## The Problem: Redundant, Unflexible Code

In your blog, a section of your `Post.js` `render` function currently looks like this:

```markup
<h3>Comments:</h3>
<p>{this.props.comments[0]}</p>
```

While you can certainly display more comments with `<p>{this.props.comments[1]}</p>`, `<p>{this.props.comments[2]}</p>`, etc, do you think this is the best way?

It would be a pain to have to explicitly define every comment when rendering `<Post />`, especially if each comment had multiple properties. This would also require us to add code each time a new comment is posted or one is deleted, which isn't sustainable. We need a dynamic approach!

To solve this problem, we will:
1. Create a generic `Comment` component that receives the comment content as a prop.
2. **nest** an instance of a Comment component within the `Post` component _for each_ comment in the `comments` prop array.

Refer back to this diagram as needed:

![component and content diagram](https://res.cloudinary.com/doc2wnnmb/image/upload/v1638206990/Screen_Shot_2021-11-29_at_9.29.01_AM_jakjnl.png)

## Modularize Comments: Nest Comment components inside of Post components

In your Dino Blog code, create a `Comment` component:

```jsx
import React, {Component} from 'react';

class Comment extends Component {
  render () {
    return (
      <div>
          <p>{this.props.content}</p>
      </div>
    )
  }
}

export default Comment
```

Now, give your Post component access to the Comment component by importing it inside `src/Post.js`:

```javascript
import React, { Component } from 'react';
import './App.css';

// Load in Comment component
import Comment from './Comment.js';
```

Change your Post JSX to render a Comment component instead of directly rendering a paragraph.  Make sure you send through the `content` prop that the `Comment` component class needs:

```javascript
<Comment content={this.props.comments[0]} />
```

Let's reflect on what just happened. We rendered a component _inside another component_. Technically, we just **nested** components. Very much like how we imported `Post` into `App.js` and rendered a Post inside `App`, we've imported `Comment` from `Comment.js` into `Post.js` and rendered a Comment. **APP>POST>COMMENT**

## Make it dynamic: Render a Comment component for each comment in the array

`<Comment content={this.props.comments[0]} />` passed just the first object in the `comments` prop array. Let's render all of them!

#### Here's how to nest a dynamic number of components inside another:

1. Use `map` to generate a new array called `allComments` that holds Comment _components_ for each of the comments, instead of just the comment content. Do this _**inside the render but above the return**_.
2. Render `allComments` in Post, where we want the comments to appear.


```jsx
class Post extends Component {
    render() {
        let allComments = this.props.comments.map((c)=>{
            return <Comment content={c} />
        })
        return (
            <>
                <h1>{this.props.title}</h1>
                <h2>{this.props.author}</h2>
                <p>{this.props.body}</p>
                <hr></hr>
                <h3>Comments:</h3>
                {allComments}
            </>
        )
    }
}
```

