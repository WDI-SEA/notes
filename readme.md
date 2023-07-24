# Intro to SEI

![](https://res.cloudinary.com/briezh/image/upload/v1539805526/spaceneedle_ga_sea_ykjk40.jpg)

Welcome to GA Seattle! This is the notes repository for our Software Engineering Immersive \(formerly known as Web Development Immersive\). You can view the content in a more searchable/friendly format on [Gitbook](https://gawdiseattle.gitbooks.io/wdi/)!

![GA Logo](.gitbook/assets/ga_cog.png)

## Setting up the Notes locally

This is totally optional. If you choose to do this, please update every 3-6 months to get any additions/updates changes we make to the local Seattle curriculum!

* Fork this repository
* Clone your fork to your development machine
* Setup a remote for your fork
  * On your terminal, run `git remote add upstream git@github.com:WDI-SEA/notes.git`
* Install the Gitbook CLI tool by running `npm install -g gitbook-cli`
* Preview the Gitbook by running `gitbook serve`

#### Updating your local repo

* On your terminal, run:
  * `git fetch upstream master` \(get the changes from us\)
  * `git merge upstream/master` \(add those changes to your local machine's clone\)
  * `git push origin master` \(updates your fork on github\)

## Contributing to the Notes

* All contributions can be done via pull requests
* Recommended process:
  * Make changes in your forked repository \(use a separate branch\)
  * Create a pull request and be sure to be very explicit about the changes you've made
  * Ask someone on the SEI team to look at your pull request

## Schedule

Notes below are organized by topic, but they are unordered. This is because we may at any point swap new material in or switch the order of the units.

Something to know is that some of the lessons here are more historical and haven't been used in at least a couple cohorts or years.

### Covid Era Remote Classroom Updates \(2020\)

| Unit | Tech | Weeks | Topics |
| :--- | :--- | :--- | :--- |
| Front-End Web Development | HTML/CSS/JS | 1 - 3 | Version control, HTML/CSS, Javascript, Programming fundamentals, DOM manipulation, HTTP, 3rd party APIs/async JS  |
| Full-Stack w/ Templates | Node/Express/PostgreSQL | 4 - 6 | Local auth, RESTful routing, ORMs, EJS, node, Express, 3 tier web applications, Relational data modeling, CI/CD |
| Front-End Framework | React/MongoDB \(MERN\) | 7 - 9 | JWT Token Auth, MongoDB, React, Hooks, SPAs |
| Full-Stack Web Development | Python | 10 - 12 | Data Structures & Algorithms, Whiteboarding, Python fundamentals, OOP, \(optional Django or Flask\) |

### Connected Classroom Alteration \(Fall 2018\)

Connected classroom \(SEA and DTLA\) used Python/Django as unit 2 instead of unit 4. Also removed much of unit 4 computer science topics.

| Unit | Tech | Weeks | Topics |
| :--- | :--- | :--- | :--- |
| Front-End Web Development | HTML/CSS/JS | 1 - 3 | Version control, DOM manipulation, jQuery, AJAX, fundamentals |
| Full-Stack Web Development | Python/Django | 4 - 6 | Data Structures & Algorithms, Whiteboarding, Python fundamentals |
| Second Language Full-Stack Development | Node/Express/PostgreSQL | 7 - 9 | Local auth, RESTful routing, ORMs |
| Front-End Framework | React/Redux/Mongo \(MERN\) | 10 - 12 | JWT Token Auth, MongoDB |

### Fall 2017-Current

Local market demand and the fact that Angular and Ruby content was not up to date led us to the conclusion we should switch from Angular to React, and from Ruby to Python.

| Unit | Tech | Weeks | Topics |
| :--- | :--- | :--- | :--- |
| Front-End Web Development | HTML/CSS/JS | 1 - 3 | Version control, DOM manipulation, jQuery, AJAX, fundamentals |
| Full-Stack Web Development | Node/Express/PostgreSQL | 4 - 6 | Local auth, RESTful routing, ORMs |
| Front-End Framework | React/Redux/Mongo \(MERN\) | 7 - 9 | JWT Token Auth, MongoDB |
| Second Language + Interview Prep | Python/Django | 10 - 12 | Data Structures & Algorithms, Whiteboarding, Python fundamentals |

### Early 2017

We began the transition from Angular to React. Some cohorts in this period may have learned either or both.

Additionally, much of the original Python material \(locally\) was developed at this time.

### 2016 and Before

| Unit | Tech | Weeks | Topics |
| :--- | :--- | :--- | :--- |
| Front-End Web Development | HTML/CSS/JS | 1 - 3 | Version control, DOM manipulation, jQuery, AJAX, fundamentals |
| Full-Stack Web Development | Node/Express/PostgreSQL | 4 - 6 | Local auth, RESTful routing, ORMs |
| Front-End Framework | AngularJS \(MEAN\) | 7 - 9 | JWT Token Auth, MongoDB |
| Second Language | Ruby/Rails | 10 - 12 | oAuth |

### Recommended Prework

* [GA Dash](https://dash.generalassemb.ly/)
* [SEI Fundamentals](http://fundamentals.generalassemb.ly/)
* [FreeCodeCamp](http://www.freecodecamp.com/)

### Front End Development

| Topic | Labs + Assignments |
| :--- | :--- |
| [Internet Fundamentals](09-other-topics/internet-fundamentals/) | [Internet Lab](09-other-topics/internet-fundamentals/internetlab.md) |
| [Command Line](01-workflow/01readme/)    [Intro to Git](01-workflow/intro-git/) | [Command Line Murder Mystery](https://github.com/WDI-SEA/command-line-murder-mystery)    [Github 101](https://github.com/WDI-SEA/github_101) |
| [HTML](03-html-css/html-review.md)    [CSS Selectors](03-html-css/css-selectors.md) |  |
| [CSS Box Model and Positioning](https://github.com/WDI-SEA/notes/tree/5537c491fcc61eb363b9c34cc82a02076abf9fc7/03-html-css/css-box-model/readme.md) | [Recreate Instagram](https://github.com/WDI-SEA/css-positioning)    [Recreate Airbnb](https://github.com/WDI-SEA/css-airbnb) |
| [JavaScript Primitives](javascript/js-primitives.md) | [Primitives Exercises](https://github.com/WDI-SEA/js-primitives) |
| [JavaScript Control Flow](javascript/js-control-flow/) | [Control Flow Problems](https://github.com/WDI-SEA/js-control-flow)    [Google Shopping](https://github.com/WDI-SEA/google-shopping-conditionals-loops) |
| [JavaScript Functions](https://github.com/WDI-SEA/notes/tree/5537c491fcc61eb363b9c34cc82a02076abf9fc7/02-js-jquery/js-functions/readme.md) | [Functions Problem Set](https://github.com/WDI-SEA/js-functions)    [Google Shopping Functions](https://github.com/WDI-SEA/google-shopping-functions) |
| [DOM and Events](https://github.com/WDI-SEA/notes/tree/5537c491fcc61eb363b9c34cc82a02076abf9fc7/02-js-jquery/js-dom-events/readme.md) | [Reddit DOM](https://github.com/WDI-SEA/selecting-reddit)    [Temperature Converter](https://github.com/WDI-SEA/temperature-converter-dom) |
| [Callbacks and Iterators](https://github.com/WDI-SEA/notes/tree/5537c491fcc61eb363b9c34cc82a02076abf9fc7/02-js-jquery/js-callbacks-iterators/readme.md) | [Iterators Lab](https://github.com/WDI-SEA/js-callbacks-iterators)    [Iterators with Reddit](https://github.com/WDI-SEA/iterators-reddit) |
| [Intro to jQuery](jquery/jquery-intro/) | [Random Quote Generator](https://github.com/WDI-SEA/random-quote-jquery)    [Todo List](https://github.com/WDI-SEA/jquery-todo-list) |
| [jQuery Plugins](jquery/jquery-plugins.md) | [jQuery UI Lab](https://github.com/WDI-SEA/jquery-plugins) |
| [AJAX](https://github.com/WDI-SEA/notes/tree/5537c491fcc61eb363b9c34cc82a02076abf9fc7/02-js-jquery/jquery-ajax/readme.md) | [AJAX Pokemons](https://github.com/WDI-SEA/jquery-ajax)    [Reddit AJAX Slideshow](https://github.com/WDI-SEA/ajax-reddit-slideshow) |
| [Responsive CSS](03-html-css/css-responsive-design/) |  |
| [Bootstrap](03-html-css/css-bootstrap.md) | [Bootstrap Mockups](https://github.com/WDI-SEA/bootstrap-mockups) |
| [User Stories and Wireframing](09-other-topics/user-stories-wireframing/) | [Wireframing: Build an Idea](09-other-topics/user-stories-wireframing/exercise.md) |
| [OOP with Constructors/Prototypes](javascript/javascript-oop/01readme/)    [Intro to TDD](javascript/js-tdd-intro.md) | [Prototype Body Shop](https://github.com/WDI-SEA/oop-prototype-car) |
| [Scopes](javascript/js-scopes.md) |  |
| [JavaScript Inheritance](javascript/01readme/) | [Body Shop 2](https://github.com/WDI-SEA/oop-inheritance-car) |

| Projects and Additional Topics |
| :--- |
| [Tic Tac Toe](https://github.com/WDI-SEA/tic-tac-toe) |
| [Project 1](11-projects/project-1.md) |
| [Code Review](https://github.com/WDI-SEA/code-review) |

### NodeJS/Express

| Topic | Assignments |
| :--- | :--- |
| [Intro to Express](https://github.com/WDI-SEA/notes/tree/5537c491fcc61eb363b9c34cc82a02076abf9fc7/05-express/express-intro/01readme.md) | [Daily Planet](https://github.com/WDI-SEA/express-daily-planet) |
| [Organization and APIs](https://github.com/WDI-SEA/notes/tree/5537c491fcc61eb363b9c34cc82a02076abf9fc7/05-express/express-apis/01readme.md)    [Foreman](00-config-deployment/deploy-rails/foreman.md) | [OMDB Movie Search](https://github.com/WDI-SEA/express-apis-omdb) |
| [Intro to SQL](04-databases/sql-intro.md) | [Apartment Lab](https://github.com/WDI-SEA/apartment-database) |
| [Intro to SQL](04-databases/sql-intro.md) | [Carmen San Diego Lab](https://github.com/WDI-SEA/sql-carmen-san-diego) |
| [Advanced SQL](04-databases/sql-advanced.md) | [Booktown](https://github.com/WDI-SEA/booktown) |
| [CRUD in Express](https://wdi_sea.gitbooks.io/notes/content/05-express/express-intro/05crudexpress.html) | [Cruddy Board Games](https://github.com/WDI-SEA/cruddy-board-games) |
| [Full RESTful Routing w/AJAX](https://github.com/WDI-SEA/notes/tree/5537c491fcc61eb363b9c34cc82a02076abf9fc7/05-express/express-ajax-crud/readme.md) | [Hackathon Teams](https://github.com/WDI-SEA/hackathon-teams)    [Daily Planet with AJAX \(old\)](https://github.com/WDI-SEA/express-daily-planet-ajax) |
| [Express with Databases via Sequelize](https://github.com/WDI-SEA/notes/tree/5537c491fcc61eb363b9c34cc82a02076abf9fc7/05-express/express-sequelize/readme.md) | [Pokedex](https://github.com/WDI-SEA/express-pokedex)    [Link Shortener](https://github.com/WDI-SEA/link-shortener) |
| [Sequelize 1:M](https://github.com/WDI-SEA/notes/tree/5537c491fcc61eb363b9c34cc82a02076abf9fc7/05-express/express-1-to-many/readme.md) | [Comments w/BlogPulse](https://github.com/WDI-SEA/express-blogpulse) |
| [Sequelize M:M](https://github.com/WDI-SEA/notes/tree/5537c491fcc61eb363b9c34cc82a02076abf9fc7/05-express/express-many-to-many/readme.md) | [Project Organizer](https://github.com/WDI-SEA/express-project-organizer) |
| [Express Testing with Mocha and Chai](https://github.com/WDI-SEA/notes/tree/5537c491fcc61eb363b9c34cc82a02076abf9fc7/05-express/express-mocha-testing/readme.md) | [Starter code](https://github.com/WDI-SEA/mocha-chai-starter) |
| [Express Authentication Theory \(Research/Code\)](https://github.com/WDI-SEA/notes/tree/5537c491fcc61eb363b9c34cc82a02076abf9fc7/05-express/express-auth/theory/readme.md) |  |
| [Express Authentication Practice \(Codealong\)](https://github.com/WDI-SEA/notes/tree/5537c491fcc61eb363b9c34cc82a02076abf9fc7/05-express/express-auth/practice/readme.md) | [Starter Template](https://github.com/WDI-SEA/express-authentication) |
| [Deploy Node to Heroku](00-config-deployment/deploy-node.md) | [Example App](https://github.com/WDI-SEA/tacoapp) |

| Projects and Additional Topics |
| :--- |
| [Project 2](11-projects/project-2.md) |
| [oAuth](https://github.com/WDI-SEA/notes/tree/5537c491fcc61eb363b9c34cc82a02076abf9fc7/05-express/additional-topics/express-oauth/readme.md) |
| [Realtime with Socket.io](https://github.com/WDI-SEA/notes/tree/5537c491fcc61eb363b9c34cc82a02076abf9fc7/05-express/express-socket-io/readme.md) |
| [Geocoding/Maps](https://github.com/WDI-SEA/notes/tree/5537c491fcc61eb363b9c34cc82a02076abf9fc7/05-express/additional-topics/express-geocode/readme.md) |
| [Image Uploads with Cloudinary](https://github.com/WDI-SEA/notes/tree/5537c491fcc61eb363b9c34cc82a02076abf9fc7/05-express/additional-topics/express-cloudinary/readme.md) |
| [Post Project 2](11-projects/post-project-2.md) |
| [Code Review](https://github.com/WDI-SEA/code-review) |

### Ruby on Rails

| Topic | Assignments |
| :--- | :--- |
| [Intro to Ruby](https://github.com/WDI-SEA/notes/tree/5537c491fcc61eb363b9c34cc82a02076abf9fc7/06-ruby-rails/ruby-intro/readme.md) | [Ruby Exercises](https://github.com/WDI-SEA/ruby-exercises)    [Ruby Challenges](https://github.com/WDI-SEA/ruby-challenges) |
| [Ruby Classes](https://github.com/WDI-SEA/notes/tree/5537c491fcc61eb363b9c34cc82a02076abf9fc7/06-ruby-rails/ruby-classes/readme.md) |  |
| [Ruby Testing with Rspec](https://github.com/WDI-SEA/notes/tree/5537c491fcc61eb363b9c34cc82a02076abf9fc7/06-ruby-rails/ruby-rspec/readme.md) | [Rspec Testing](https://github.com/WDI-SEA/rspec-testing) |
| [Ruby Inheritance](https://github.com/WDI-SEA/notes/tree/5537c491fcc61eb363b9c34cc82a02076abf9fc7/06-ruby-rails/ruby-inheritance/readme.md) | [Rio Grande](https://github.com/WDI-SEA/ruby-rio-grande) |
| [Intro to Rails](https://github.com/WDI-SEA/notes/tree/5537c491fcc61eb363b9c34cc82a02076abf9fc7/06-ruby-rails/rails-intro/readme.md) | [National Parks](https://github.com/WDI-SEA/rails-national-parks) |
| [APIs with Rest-Client](https://github.com/WDI-SEA/notes/tree/5537c491fcc61eb363b9c34cc82a02076abf9fc7/06-ruby-rails/rails-apis/readme.md) |  |
| [Data Scraping with Nokogiri](https://github.com/WDI-SEA/notes/tree/5537c491fcc61eb363b9c34cc82a02076abf9fc7/06-ruby-rails/ruby-data-scraping/readme.md) | [Nokogiri CLI Tool](https://github.com/WDI-SEA/nokogiri-cli-tool) |
| [Rails Asset Pipeline](https://github.com/WDI-SEA/notes/tree/5537c491fcc61eb363b9c34cc82a02076abf9fc7/06-ruby-rails/rails-assets-frontend/readme.md) |  |
| [Rails Auth/1:M](https://github.com/WDI-SEA/notes/tree/5537c491fcc61eb363b9c34cc82a02076abf9fc7/06-ruby-rails/rails-auth-1-M/readme.md) | [Link Board](https://github.com/WDI-SEA/link-board) |
| [Rails M:M](https://github.com/WDI-SEA/notes/tree/5537c491fcc61eb363b9c34cc82a02076abf9fc7/06-ruby-rails/rails-M-M/readme.md) | [National Parks Part 2: Rangers](https://github.com/WDI-SEA/rails-national-parks/blob/master/part2.md) |
| [Polymorphic Associations](https://github.com/WDI-SEA/notes/tree/5537c491fcc61eb363b9c34cc82a02076abf9fc7/06-ruby-rails/rails-polymorphism/readme.md) | [Link Board Comments](https://github.com/WDI-SEA/link-board/blob/master/part2.md) |

| Projects and Additional Topics |
| :--- |
| [Front End Hackathon](https://github.com/WDI-SEA/front-end-hackathon) |
| [Project 3](11-projects/project-3/) |
| [Group Collaboration](01-workflow/01readme-1/) |
| [oAuth](https://github.com/WDI-SEA/notes/tree/5537c491fcc61eb363b9c34cc82a02076abf9fc7/06-ruby-rails/additional-topics/rails-oauth/readme.md) |
| [Mailers](https://github.com/WDI-SEA/notes/tree/5537c491fcc61eb363b9c34cc82a02076abf9fc7/06-ruby-rails/additional-topics/rails-mailers/readme.md) |
| [Image Uploads with Cloudinary](https://github.com/WDI-SEA/notes/tree/5537c491fcc61eb363b9c34cc82a02076abf9fc7/06-ruby-rails/additional-topics/rails-cloudinary/readme.md) |
| [Static Site Generators \(Jekyll\)](https://github.com/WDI-SEA/notes/tree/5537c491fcc61eb363b9c34cc82a02076abf9fc7/06-ruby-rails/additional-topics/ruby-jekyll/readme.md) |
| [JS/jQuery Review](https://github.com/WDI-SEA/js-jquery-review) |

### Python

| Topic | Assignments |
| :--- | :--- |
| Intro to Python | [Intro to Python](https://github.com/WDI-SEA/intro-python) |
| Python Exercises | [Python Exercises](https://github.com/WDI-SEA/python-exercises) |
| Python Challenges | [Python Challenges](https://github.com/WDI-SEA/python-challenges) |
| Arrays and For Loops | [Convert JS to PY](https://github.com/WDI-SEA/python-arrays-and-for-loops) |
| File Processing | [Renobet](https://github.com/geluso/renobet) |
| Python Unit Tests | [Python Unit Tests](https://github.com/WDI-SEA/python-unit-tests) |
| Python Class Examples | [Python Class Examples](https://github.com/WDI-SEA/python-class-examples) |
| Recursion | [Python Recursion](https://github.com/WDI-SEA/python-recursion) |
| Binary Search | [Python Binary Search](https://github.com/WDI-SEA/python-binary-search) |
| Linked Lists | [Python Linked Lists](https://github.com/WDI-SEA/python-linked-lists) |
| Binary Trees | [Python Recursion](https://github.com/WDI-SEA/python-binary-trees) |
| Graphs | [Python Graph](https://github.com/WDI-SEA/python-graph-data-structure) |
| Sorting | [Python Sorting Algorithms](https://github.com/WDI-SEA/python-sorting-algorithms) |

### AngularJS 1.x and APIs

| Topic | Assignments |
| :--- | :--- |
| [Intro to Angular](https://github.com/WDI-SEA/notes/tree/5537c491fcc61eb363b9c34cc82a02076abf9fc7/07-angular/angular-intro/readme.md) | [Angular Calculator](https://github.com/WDI-SEA/angular-calculator) |
| [Directives and Filters](https://github.com/WDI-SEA/notes/tree/5537c491fcc61eb363b9c34cc82a02076abf9fc7/07-angular/angular-directives-filters/readme.md) | [Fruits and Veggies](https://github.com/WDI-SEA/fruits-and-veggies) |
| [Animation with ngAnimate](https://github.com/WDI-SEA/notes/tree/5537c491fcc61eb363b9c34cc82a02076abf9fc7/07-angular/angular-animation/readme.md) |  |
| [Bootstrap Directives](https://github.com/WDI-SEA/notes/tree/5537c491fcc61eb363b9c34cc82a02076abf9fc7/07-angular/angular-bootstrap-directives/readme.md) |  |
| [$http](https://github.com/WDI-SEA/notes/tree/5537c491fcc61eb363b9c34cc82a02076abf9fc7/07-angular/angular-http/readme.md) | [\(DEPRECATED\) Reddit Dashboard](https://github.com/WDI-SEA/angular-reddit-dashboard)    [Giphy Search](https://github.com/WDI-SEA/angular-giphy) |
| [Angular Services](https://github.com/WDI-SEA/notes/tree/5537c491fcc61eb363b9c34cc82a02076abf9fc7/07-angular/angular-services/readme.md) |  |
| [Angular Routing \(UI Router\)](https://github.com/WDI-SEA/notes/tree/5537c491fcc61eb363b9c34cc82a02076abf9fc7/07-angular/angular-routing/readme.md) | [Route Those Views](https://github.com/WDI-SEA/angular-route-those-views) |
| [Intro to MongoDB](04-databases/mongo-intro/)    [Mongoose](https://github.com/WDI-SEA/notes/tree/5537c491fcc61eb363b9c34cc82a02076abf9fc7/05-express/express-mongoose/readme.md) |  |
| [JSON Web Tokens](https://github.com/WDI-SEA/notes/tree/5537c491fcc61eb363b9c34cc82a02076abf9fc7/05-express/express-jwt/readme.md) | [RESTful API](https://github.com/WDI-SEA/restful-api) |
| [Angular + Express](https://github.com/WDI-SEA/notes/tree/5537c491fcc61eb363b9c34cc82a02076abf9fc7/07-angular/angular-express/readme.md)    [Starter Code](https://github.com/WDI-SEA/fly-on-angular) |  |
| [Angular Authentication](https://github.com/WDI-SEA/notes/tree/5537c491fcc61eb363b9c34cc82a02076abf9fc7/07-angular/angular-authentication/readme.md) | [Starter Code](https://github.com/WDI-SEA/angular-recipes) |
| [Custom Filters](https://github.com/WDI-SEA/notes/tree/5537c491fcc61eb363b9c34cc82a02076abf9fc7/07-angular/angular-custom-filters/readme.md) | [Creating Filters](https://github.com/WDI-SEA/angular-filters) |
| [Custom Directives](https://github.com/WDI-SEA/notes/tree/5537c491fcc61eb363b9c34cc82a02076abf9fc7/07-angular/angular-custom-directives/readme.md) | [Creating Directives](https://github.com/WDI-SEA/angular-directives) |
| [Angular Components](https://github.com/WDI-SEA/notes/tree/5537c491fcc61eb363b9c34cc82a02076abf9fc7/07-angular/angular-components/readme.md) |  |

### React

| Topic | Assignments + Labs |
| :--- | :--- |
| [Intro to ES6](https://github.com/WDI-SEA/react_es6_global/blob/master/01-es6.md)    [Let and Const](https://github.com/WDI-SEA/react_es6_global/blob/master/02-es6-const-let.md)    [Arrow Functions](https://github.com/WDI-SEA/react_es6_global/blob/master/03-es6-arrow.md) | [ES6 Overview](https://github.com/WDI-SEA/react_es6_global/blob/master/05-es6-exercise.md) |
| \[Intro to ReactJS\]\[\] | [React Video \(2m\)](https://generalassembly.wistia.com/medias/lr8idjxtx8)    [React Video \(8:30-16:30\)](https://www.youtube.com/watch?v=KVZ-P-ZI6W4&feature=youtu.be&t=510)    [Create React App](https://github.com/WDI-SEA/react_intro_global/blob/master/02-initial-setup.md) |
| [React Components](https://github.com/WDI-SEA/react_intro_global/blob/master/03-components.md)    [React Virtual DOM](https://github.com/WDI-SEA/react_intro_global/blob/master/04-virtual-dom.md) | [Virtual DOM Video](https://www.youtube.com/watch?v=-DX3vJiqxm4) |
| [React Props](https://github.com/WDI-SEA/react_intro_global/blob/master/05-props.md)    [Multiple Props](https://github.com/WDI-SEA/react_intro_global/blob/master/06-multiple-props.md) | [React Props](https://github.com/WDI-SEA/react_intro_global/blob/master/07-props-challenge.md)    [React Nested Components](https://github.com/WDI-SEA/react_intro_global/blob/master/08-nested-components.md)    [LotR Lab](https://github.com/WDI-SEA/lotr-solution-code) |
| [React State](https://github.com/WDI-SEA/react_state_exercises_global/blob/master/01_state.md) | [React Films](https://github.com/WDI-SEA/react_intro_global/blob/master/12-film-1-components.md)    [React Calculator](https://github.com/WDI-SEA/react_state_exercises_global/blob/master/07_calculator_exercise.md)    [React ATM](https://github.com/WDI-SEA/react_atm_global) |
| [React Router pt 1](https://github.com/WDI-SEA/react_router_global/blob/master/01-router-introduction.md)    [React Router pt 2](https://github.com/WDI-SEA/react_router_global/blob/master/02-react-router-intro.md) | [Router Blog](https://github.com/WDI-SEA/react_intro_global/blob/master/07-props-challenge.md) |
| [APIs](https://github.com/WDI-SEA/react_apis_heroku_global/blob/master/01-APIs.md)    [Data Types](https://github.com/WDI-SEA/react_apis_heroku_global/blob/master/02-data-types.md) | [Shakespeare Fetch](https://github.com/WDI-SEA/react_apis_heroku_global/blob/master/03-fetch.md) |
| [Unidirectional Flow](https://github.com/WDI-SEA/react_es6_global/blob/master/08-unidirectional-flow.md) | [Fetch the Weather](https://github.com/WDI-SEA/react_apis_heroku_global/blob/master/04-fetch-project.md) |
| [Functional Components](https://github.com/WDI-SEA/react_es6_global/blob/master/06-functional-components.md) | [Functional Components Lab](https://github.com/WDI-SEA/react_functional_components) |
| [Redux Intro](https://git.generalassemb.ly/jamieking/redux-todo-list/tree/redux-impl) | [Lab 1](https://git.generalassemb.ly/atl-wdi/wdi-curriculum/blob/master/instructor_notes/redux/state-management-and-intro-to-redux.md) [Lab 2](https://git.generalassemb.ly/atl-wdi/wdi-curriculum/blob/master/instructor_notes/redux/react-with-redux.md) |
| [React Native Set-Up](https://git.generalassemb.ly/wdi-wc-march2018/warm-ups/blob/master/week-8/monday.md)    [React Native Lesson](https://git.generalassemb.ly/wdi-wc-march2018/react-native/blob/master/README.md) | [Navigators](https://reactnavigation.org/docs/en/hello-react-navigation.html)    [Deployment](https://docs.expo.io/versions/latest/guides/building-standalone-apps.html) |

| Projects and Additional Topics |
| :--- |
| [Project 4](11-projects/project-4.md) |
| [MEAN/MERN Hackathon](11-projects/mean-hackathon/) |
| [Interview Questions](https://github.com/WDI-SEA/interview-questions) |
| [ES6 Variables and Strings \(Codepen\)](http://codepen.io/bhague1281/pen/EKyMVz) |
| [ES6 Arrow Functions \(Codepen\)](http://codepen.io/bhague1281/pen/aNZPrq) |
| [Imperative vs Declarative](https://github.com/WDI-SEA/react_apis_heroku_global/blob/master/05-declarative-imperative.md) |
| [Deploying React Apps](https://gawdiseattle.gitbooks.io/wdi/10-react/react-deploy/readme.html) |
| [React-Tac-Toe](https://github.com/WDI-SEA/react-tac-toe) |

### Computer Science

| Topic | Assignments |
| :--- | :--- |
| Recursion/Problem Solving | [Array Challenge](08-cs/teaser-js-array-flatten.md) |
| Binary Search    [Algorithm Complexity](08-cs/cs-algorithm-complexity.md) | [Auto Guess](08-cs/teaser-ruby-binary-search.md) |
| [Stacks and Queues](08-cs/cs-stacks-queues.md) | [Bracket Matching](08-cs/cs-ruby-bracket-stacks.md) |
| Linked Lists | [Singly Linked List](https://github.com/WDI-SEA/notes/tree/5537c491fcc61eb363b9c34cc82a02076abf9fc7/08-cs/cs-ruby-linked-list/readme.md)    [Linked List Methods](https://github.com/WDI-SEA/notes/tree/5537c491fcc61eb363b9c34cc82a02076abf9fc7/08-cs/cs-ruby-linked-list-2/readme.md) |
| Bucket Sort | [Bucket Sort: Sorting Papers](08-cs/cs-sets/cs-ruby-bucket-sort.md) |
| [Bubble Sort](08-cs/cs-sets/cs-ruby-bubble-sort.md) |  |
| [Merge Sort](08-cs/cs-sets/cs-ruby-mergesort.md) |  |
| [Quick Sort](08-cs/cs-sets/cs-ruby-quicksort.md) |  |
| [Sorting Wrapup](08-cs/cs-sets/cs-sorting.md) |  |
| [Hashmaps](https://github.com/WDI-SEA/notes/tree/5537c491fcc61eb363b9c34cc82a02076abf9fc7/08-cs/cs-hashmaps/readme.md) |  |
| [Trees and Other Topics](08-cs/cs-trees-data-structures.md) | N/A |

## Licensing

1. All content is licensed under a CC-BY-NC-SA 4.0 license.
2. All software code is licensed under GNU GPLv3. For commercial use or alternative licensing, please contact legal@ga.co.
