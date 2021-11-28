# Dino Blog Activity

## ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Lab: Dino Blog

Let's have some practice creating a React component from scratch. How about a blog post?

1. Change directories back into the main directory where you want to keep your lab code.
2. Referring to everything we've done up until now, create a new project using `create-react-app`. If you need to refresh your memory, refer to the Initial [Setup section](https://gasei.gitbook.io/sei/16-react/intro-react/setup) or view the official [React docs](https://reactjs.org/docs/create-a-new-react-app.html#create-react-app).

   > Note: If you are running something else on port 3000 - like a Node app or another React app, you may get prompted to use 3001 or specify a new port. You can do this or you can kill the process that's already running.

3. Create a `post` object in `src/index.js` that has the following properties:
   * `title`  \(example value: `"Dinosaurs are awesome"`\)
   * `author` \(example value: `"Stealthy Stegosaurus"`\)
   * `body` \(example value: `"Check out this body property!"`\)
   * `comments` \(example value: `["First!", "Great post", "Hire this author now!"]`\)
4. Render your `App` component with the information from your `post` object as its props values. For now, only include one of the comments, `comments[0]`. You decide how you want to display the title, author, body, and comment, or you can use the screenshot in the Solution section below as inspiration.
5. Optional: adjust the CSS of your index file body to align your text to the center of the document.

## Solution

Here's what the solution might look like:

![Solution for Project](https://res.cloudinary.com/briezh/image/upload/v1556226300/props_solution_wawthy.png)

## Going forward

Hang onto this code - we'll make some improvements to it so we can see all of the comments!

