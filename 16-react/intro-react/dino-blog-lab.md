# Dino Blog Activity

## ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Lab: Dino Blog

Let's have some practice creating a React component from scratch. How about a blog post?

Here's our end game:

![](https://res.cloudinary.com/doc2wnnmb/image/upload/v1638206990/Screen_Shot_2021-11-29_at_9.29.01_AM_jakjnl.png)

1. Change directories back into the main directory where you want to keep your lab code.
2. Referring to everything we've done up until now, create a new project using `create-react-app` and call it `dino-blog`. If you need to refresh your memory, refer to the Initial [Setup section](https://gasei.gitbook.io/sei/16-react/intro-react/setup) or view the official [React docs](https://reactjs.org/docs/create-a-new-react-app.html#create-react-app).

   > Note: If you are running something else on port 3000 - like a Node app or another React app, you may get prompted to use 3001 or specify a new port. You can do this or you can kill the process that's already running.

3. Create a `post` object in `App.js` _**inside the function, but above the return statement**_ that has the following properties:
   * `title`  \(example value: `"Dinosaurs are awesome"`\)
   * `author` \(example value: `"Stealthy Stegosaurus"`\)
   * `body` \(example value: `"Check out this body property!"`\)
   * `comments` \(example value: `["First!", "Great post", "Hire this author now!"]`\)

```jsx
function App() {
  const post = {
    title: "Dinosaurs are awesome",
    author: "Stealthy Stegosaurus",
    body: "Check out this body property!",
    comments: ["First!", "Great post", "Hire this author now!"]
  }
  return (
```

4. Render a `Post` component inside `App.js` in place of the original app content (you can leave the main `App` div). Feed each of the values from your post object to the Home components as props. For now, only include one of the comments, `comments[0]`.
```jsx
  return (
    <div className="App">
      <Post 
        title={post.title} 
        author={post.author}  
        body={post.body}
        comments={comments}
      />
    </div>
  )
```

5. Create your **Post** component! You decide how you want to display the title, author, body, and comment, or you can use the screenshot in the Solution section below as inspiration. Make sure to import the component into `App.js`.

## Going forward

Hang onto this code - we'll make some improvements to it so we can see all of the comments!

