# Setting up SASS with a Node/Express project

## What is SASS?

[SASS (Syntactically Awesome Style Sheets)](https://www.learnhowtoprogram.com/css/sass/what-is-sass) is a CSS preprocessor. This basically extends the features of CSS and helps us keep our CSS DRY. As the SASS website puts it SASS is "CSS with superpowers". Other popular preprocessors include Less and Stylus.

SASS has a couple different formats - SASS and SCSS. SASS format removes the semi-colons and curly braces and SCSS does not. Thus, SCSS is a little easier for most programmers to read, so that's what we'll use in this tutorial.

## Step-by-step

1. Set up your static files and folder structure.
    * Create `public` folder in top level folder
    * Put the following line of code in your index.js

        `app.use(express.static(__dirname + '/public/'));`

    * Inside the public folder, create a `css` folder.
    * Inside the css folder, create a `sass` folder.

2. Install some middleware that will compile the files for you

    `npm install -g node-sass`

3. Add to the scripts in your package.json

    `"sass": "node-sass css/sass/ -o css/"`

4. Create an SCSS file called `style.scss` in your sass folder

5. Put some code in it
    ```
    $my_favorite_color: #0f0;
    $my_second_favorite_color: #00f;

    h1 {
      color: $my_favorite_color;
      &:hover {
        color: $my_second_favorite_color;
      }
    }
    ```

6. Run the command `npm run-script sass` that we added to package.json earlier.

    * Check it out, you should have a style.css in the parent folder now!

7. Add your new `style.css` file to your layout.ejs file. See it in action!

## Neat. What else does it do?

Check out the [guide on the SASS website](https://sass-lang.com/guide) for an overview on what SASS can do. In a nutshell, we can use it to enable CSS to work with variables, nesting, inheritance, partials, mixins, and operators. 

| The thing  | What it does |
| -------- | ----------------------------------------------- |
|`Variables`| Declare something for use at a later time, like in our example above.|
|`Nesting`| We can put the relevant code inside the parent instead of having to write a long queryselector.|
|`Inheritance`| We can extend code from somewhere else.|
|`Mixins`| We can write blocks of CSS for later reuse.|
|`Partials`| We can include code snippets.|
|`Operators`| You can use +, -, *, /, and % for glorious, glorious math.|

# References
* [SASS website](https://sass-lang.com/)
* [node-sass NPM](https://www.npmjs.com/package/node-sass)
* [node-sass Github](https://github.com/sass/node-sass)
