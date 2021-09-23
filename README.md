# SEI Seattle

![](https://res.cloudinary.com/briezh/image/upload/v1539805526/spaceneedle_ga_sea_ykjk40.jpg)


Welcome to GA Seattle! This is the notes repository for our Software Engineering Immersive (formerly known as Web Development Immersive). You can view the content in a more searchable/friendly format on [Gitbook](https://gawdiseattle.gitbooks.io/wdi/)!

![GA Logo](./_assets/ga_cog.png)

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
  * `git fetch upstream master` (get the changes from us)
  * `git merge upstream/master` (add those changes to your local machine's clone)
  * `git push origin master` (updates your fork on github)

## Contributing to the Notes

* All contributions can be done via pull requests
* Recommended process:
  * Make changes in your forked repository (use a separate branch)
  * Create a pull request and be sure to be very explicit about the changes you've made
  * Ask someone on the SEI team to look at your pull request

## Schedule

Notes below are organized by topic, but they are unordered. This is because we may at any point swap new material in or switch the order of the units.

Something to know is that some of the lessons here are more historical and haven't been used in at least a couple cohorts or years.

### Covid Era Remote Classroom Updates (2020)

| Unit | Tech | Weeks | Topics |
| ------------------------- | ----------------------- | ----------- | ----------- |
| Front-End Web Development | HTML/CSS/JS | 1 - 3 | Version control, DOM manipulation, (3rd party APIs/asynch JS may come in this unit or the next)|
| Full-Stack w/ Templates | Node/Express/PostgreSQL | 4 - 6 | Local auth, RESTful routing, ORMs, EJS |
| Front-End Framework | React/MongoDB (MERN) | 7 - 9 | JWT Token Auth, MongoDB | 
| Full-Stack Web Development | Python | 10 - 12 | Data Structures & Algorithms, Whiteboarding, Python fundamentals, (optional Django or Flask) |

### Connected Classroom Alteration (Fall 2018)

Connected classroom (SEA and DTLA) used Python/Django as unit 2 instead of unit 4. Also removed much of unit 4 computer science topics.

| Unit | Tech | Weeks | Topics |
| ------------------------- | ----------------------- | ----------- | ----------- |
| Front-End Web Development | HTML/CSS/JS | 1 - 3 | Version control, DOM manipulation, jQuery, AJAX, fundamentals |
| Full-Stack Web Development | Python/Django | 4 - 6 | Data Structures & Algorithms, Whiteboarding, Python fundamentals |
| Second Language Full-Stack Development | Node/Express/PostgreSQL | 7 - 9 | Local auth, RESTful routing, ORMs |
| Front-End Framework | React/Redux/Mongo (MERN) | 10 - 12 | JWT Token Auth, MongoDB | 


### Fall 2017-Current

Local market demand and the fact that Angular and Ruby content was not up to date led us to the conclusion we should switch from Angular to React, and from Ruby to Python. 

| Unit | Tech | Weeks | Topics |
| ------------------------- | ----------------------- | ----------- | ----------- |
| Front-End Web Development | HTML/CSS/JS | 1 - 3 | Version control, DOM manipulation, jQuery, AJAX, fundamentals |
| Full-Stack Web Development | Node/Express/PostgreSQL | 4 - 6 | Local auth, RESTful routing, ORMs |
| Front-End Framework | React/Redux/Mongo (MERN) | 7 - 9 | JWT Token Auth, MongoDB | 
| Second Language + Interview Prep | Python/Django | 10 - 12 | Data Structures & Algorithms, Whiteboarding, Python fundamentals |

### Early 2017

We began the transition from Angular to React. Some cohorts in this period may have learned either or both.

Additionally, much of the original Python material (locally) was developed at this time.

### 2016 and Before 

| Unit | Tech | Weeks | Topics |
| ------------------------- | ----------------------- | ----------- | ----------- |
| Front-End Web Development | HTML/CSS/JS | 1 - 3 | Version control, DOM manipulation, jQuery, AJAX, fundamentals |
| Full-Stack Web Development | Node/Express/PostgreSQL | 4 - 6 | Local auth, RESTful routing, ORMs |
| Front-End Framework | AngularJS (MEAN) | 7 - 9 | JWT Token Auth, MongoDB | 
| Second Language | Ruby/Rails | 10 - 12 | oAuth |

### Recommended Prework

* [GA Dash](https://dash.generalassemb.ly/)
* [WDI Fundamentals](http://fundamentals.generalassemb.ly/)
* [FreeCodeCamp](http://www.freecodecamp.com/)

### Front End Development

| Topic | Labs + Assignments |
| ----- | -------------- |
| [Internet Fundamentals][1] | [Internet Lab][1000] |
| [Command Line][2] <br><br> [Intro to Git][3] | [Command Line Murder Mystery][1001] <br><br> [Github 101][1026] |
| [HTML][5] <br><br> [CSS Selectors][6] |  |
| [CSS Box Model and Positioning][9] | [Recreate Instagram][1023] <br><br> [Recreate Airbnb][1024] |
| [JavaScript Primitives][4] | [Primitives Exercises][1003]  |
| [JavaScript Control Flow][7] | [Control Flow Problems][1004] <br><br> [Google Shopping][1002] |
| [JavaScript Functions][10] | [Functions Problem Set][1007] <br><br> [Google Shopping Functions][1006] |
| [DOM and Events][11] | [Reddit DOM][1008] <br><br> [Temperature Converter][1009] |
| [Callbacks and Iterators][12] | [Iterators Lab][1011] <br><br> [Iterators with Reddit][1012] |
| [Intro to jQuery][13] | [Random Quote Generator][1013] <br><br> [Todo List][1014] |
| [jQuery Plugins][14] | [jQuery UI Lab][1015] |
| [AJAX][15] | [AJAX Pokemons][1016] <br><br> [Reddit AJAX Slideshow][1017] |
| [Responsive CSS][16] | |
| [Bootstrap][17] | [Bootstrap Mockups][1018] |
| [User Stories and Wireframing][18] | [Wireframing: Build an Idea][1019] |
| [OOP with Constructors/Prototypes][19] <br><br> [Intro to TDD][20] | [Prototype Body Shop][1020] |
| [Scopes][21] | |
| [JavaScript Inheritance][22] | [Body Shop 2][1021] |

| Projects and Additional Topics |
| -------- |
| [Tic Tac Toe][1010] |
| [Project 1][1022] |
| [Code Review][1025] |

[1]: 09-other-topics/internet-fundamentals/readme.md
[2]: 01-workflow/command-line/01readme.md
[3]: 01-workflow/intro-git/readme.md
[4]: 02-js-jquery/js-primitives/readme.md
[5]: 03-html-css/html-review/readme.md
[6]: 03-html-css/css-selectors/readme.md
[7]: 02-js-jquery/js-control-flow/readme.md
[9]: 03-html-css/css-box-model/readme.md
[10]: 02-js-jquery/js-functions/readme.md
[11]: 02-js-jquery/js-dom-events/readme.md
[12]: 02-js-jquery/js-callbacks-iterators/readme.md
[13]: 02-js-jquery/jquery-intro/readme.md
[14]: 02-js-jquery/jquery-plugins/readme.md
[15]: 02-js-jquery/jquery-ajax/readme.md
[16]: 03-html-css/css-responsive-design/readme.md
[17]: 03-html-css/css-bootstrap/readme.md
[18]: 09-other-topics/user-stories-wireframing/readme.md
[19]: 02-js-jquery/js-prototypes/01readme.md
[20]: 02-js-jquery/js-tdd-intro/readme.md
[21]: 02-js-jquery/js-scopes/readme.md
[22]: 02-js-jquery/js-inheritance/01readme.md

[1000]: 09-other-topics/internet-fundamentals/internetlab.md
[1001]: https://github.com/WDI-SEA/command-line-murder-mystery
[1002]: https://github.com/WDI-SEA/google-shopping-conditionals-loops
[1003]: https://github.com/WDI-SEA/js-primitives
[1004]: https://github.com/WDI-SEA/js-control-flow
[1005]: https://github.com/WDI-SEA/css-selectors-animal-style
[1006]: https://github.com/WDI-SEA/google-shopping-functions
[1007]: https://github.com/WDI-SEA/js-functions
[1008]: https://github.com/WDI-SEA/selecting-reddit
[1009]: https://github.com/WDI-SEA/temperature-converter-dom
[1010]: https://github.com/WDI-SEA/tic-tac-toe
[1011]: https://github.com/WDI-SEA/js-callbacks-iterators
[1012]: https://github.com/WDI-SEA/iterators-reddit
[1013]: https://github.com/WDI-SEA/random-quote-jquery
[1014]: https://github.com/WDI-SEA/jquery-todo-list
[1015]: https://github.com/WDI-SEA/jquery-plugins
[1016]: https://github.com/WDI-SEA/jquery-ajax
[1017]: https://github.com/WDI-SEA/ajax-reddit-slideshow
[1018]: https://github.com/WDI-SEA/bootstrap-mockups
[1019]: 09-other-topics/user-stories-wireframing/exercise.md
[1020]: https://github.com/WDI-SEA/oop-prototype-car
[1021]: https://github.com/WDI-SEA/oop-inheritance-car
[1022]: 11-projects/project-1/readme.md
[1023]: https://github.com/WDI-SEA/css-positioning
[1024]: https://github.com/WDI-SEA/css-airbnb
[1025]: https://github.com/WDI-SEA/code-review
[1026]: https://github.com/WDI-SEA/github_101


### NodeJS/Express

| Topic                                                | Assignments                                                             |
| -----                                                | -----------                                                             |
| [Intro to Express][101]                              | [Daily Planet][1100]                                                    |
| [Organization and APIs][102] <br><br> [Foreman][114] | [OMDB Movie Search][1101]                                               |
| [Intro to SQL][103]                                  | [Apartment Lab][1102]                                                   |
| [Intro to SQL][103]                                  | [Carmen San Diego Lab](https://github.com/WDI-SEA/sql-carmen-san-diego)
| [Advanced SQL][104]                                  | [Booktown][1103]                                                        |
| [CRUD in Express](https://wdi_sea.gitbooks.io/notes/content/05-express/express-intro/05crudexpress.html) | [Cruddy Board Games](https://github.com/WDI-SEA/cruddy-board-games)
| [Full RESTful Routing w/AJAX][105]                   | [Hackathon Teams][1111] <br><br> [Daily Planet with AJAX (old)][1104]   |
| [Express with Databases via Sequelize][106]          | [Pokedex][1107] <br><br> [Link Shortener][1105]                         |
| [Sequelize 1:M][108]                                 | [Comments w/BlogPulse][1108]                                            |
| [Sequelize M:M][109]                                 | [Project Organizer][1109]                                               |
| [Express Testing with Mocha and Chai][112]           | [Starter code][113]                                                     |
| [Express Authentication Theory (Research/Code)][110] |                                                                         |
| [Express Authentication Practice (Codealong)][111]   | [Starter Template][1112]                                                |
| [Deploy Node to Heroku][107]                         | [Example App][1113]                                                     |

| Projects and Additional Topics |
| -------- |
| [Project 2][1106] |
| [oAuth][115] |
| [Realtime with Socket.io][117] |
| [Geocoding/Maps][116] |
| [Image Uploads with Cloudinary][118] |
| [Post Project 2][1110] |
| [Code Review][1025] |

[101]: 05-express/express-intro/01readme.md
[102]: 05-express/express-apis/01readme.md
[103]: 04-databases/sql-intro/readme.md
[104]: 04-databases/sql-advanced/readme.md
[105]: 05-express/express-ajax-crud/readme.md
[106]: 05-express/express-sequelize/readme.md
[107]: 00-config-deployment/deploy-node/readme.md
[108]: 05-express/express-1-to-many/readme.md
[109]: 05-express/express-many-to-many/readme.md
[110]: 05-express/express-auth/theory/readme.md
[111]: 05-express/express-auth/practice/readme.md
[112]: 05-express/express-mocha-testing/readme.md
[113]: https://github.com/WDI-SEA/mocha-chai-starter
[114]: 00-config-deployment/foreman/readme.md
[115]: 05-express/additional-topics/express-oauth/readme.md
[116]: 05-express/additional-topics/express-geocode/readme.md
[117]: 05-express/express-socket-io/readme.md
[118]: 05-express/additional-topics/express-cloudinary/readme.md

[1100]: https://github.com/WDI-SEA/express-daily-planet
[1101]: https://github.com/WDI-SEA/express-apis-omdb
[1102]: https://github.com/WDI-SEA/apartment-database
[1103]: https://github.com/WDI-SEA/booktown
[1104]: https://github.com/WDI-SEA/express-daily-planet-ajax
[1105]: https://github.com/WDI-SEA/link-shortener
[1106]: 11-projects/project-2/readme.md
[1107]: https://github.com/WDI-SEA/express-pokedex
[1108]: https://github.com/WDI-SEA/express-blogpulse
[1109]: https://github.com/WDI-SEA/express-project-organizer
[1110]: 11-projects/post-project-2/readme.md
[1111]: https://github.com/WDI-SEA/hackathon-teams
[1112]: https://github.com/WDI-SEA/express-authentication
[1113]: https://github.com/WDI-SEA/tacoapp

### Ruby on Rails

| Topic | Assignments |
| ----- | ----------- |
| [Intro to Ruby][201] | [Ruby Exercises][1201] <br><br> [Ruby Challenges][1202] |
| [Ruby Classes][202] |  |
| [Ruby Testing with Rspec][204] | [Rspec Testing][1204] |
| [Ruby Inheritance][203] | [Rio Grande][1205] |
| [Intro to Rails][205] | [National Parks][1206] |
| [APIs with Rest-Client][206] | |
| [Data Scraping with Nokogiri][216] | [Nokogiri CLI Tool][1207] |
| [Rails Asset Pipeline][207] | |
| [Rails Auth/1:M][208] | [Link Board][1209] |
| [Rails M:M][209] | [National Parks Part 2: Rangers][1211] |
| [Polymorphic Associations][210] | [Link Board Comments][1210] |

| Projects and Additional Topics |
| -------- |
| [Front End Hackathon][1208] |
| [Project 3][1200] |
| [Group Collaboration][215] |
| [oAuth][211] |
| [Mailers][212] |
| [Image Uploads with Cloudinary][213] |
| [Static Site Generators (Jekyll)][214] |
| [JS/jQuery Review][1212] |

[201]: 06-ruby-rails/ruby-intro/readme.md
[202]: 06-ruby-rails/ruby-classes/readme.md
[203]: 06-ruby-rails/ruby-inheritance/readme.md
[204]: 06-ruby-rails/ruby-rspec/readme.md
[205]: 06-ruby-rails/rails-intro/readme.md
[206]: 06-ruby-rails/rails-apis/readme.md
[207]: 06-ruby-rails/rails-assets-frontend/readme.md
[208]: 06-ruby-rails/rails-auth-1-M/readme.md
[209]: 06-ruby-rails/rails-M-M/readme.md
[210]: 06-ruby-rails/rails-polymorphism/readme.md
[211]: 06-ruby-rails/additional-topics/rails-oauth/readme.md
[212]: 06-ruby-rails/additional-topics/rails-mailers/readme.md
[213]: 06-ruby-rails/additional-topics/rails-cloudinary/readme.md
[214]: 06-ruby-rails/additional-topics/ruby-jekyll/readme.md
[215]: 01-workflow/group-collab/01readme.md
[216]: 06-ruby-rails/ruby-data-scraping/readme.md

[1200]: 11-projects/project-3/readme.md
[1201]: https://github.com/WDI-SEA/ruby-exercises
[1202]: https://github.com/WDI-SEA/ruby-challenges
[1203]: https://github.com/WDI-SEA/ruby-classes
[1204]: https://github.com/WDI-SEA/rspec-testing
[1205]: https://github.com/WDI-SEA/ruby-rio-grande
[1206]: https://github.com/WDI-SEA/rails-national-parks
[1207]: https://github.com/WDI-SEA/nokogiri-cli-tool
[1208]: https://github.com/WDI-SEA/front-end-hackathon
[1209]: https://github.com/WDI-SEA/link-board
[1210]: https://github.com/WDI-SEA/link-board/blob/master/part2.md
[1211]: https://github.com/WDI-SEA/rails-national-parks/blob/master/part2.md
[1212]: https://github.com/WDI-SEA/js-jquery-review

### Python
| Topic | Assignments |
| ----- | ----------- |
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
| ----- | ----------- |
| [Intro to Angular][301] | [Angular Calculator][1300] |
| [Directives and Filters][302] | [Fruits and Veggies][1301] |
| [Animation with ngAnimate][303] | |
| [Bootstrap Directives][304] | |
| [$http][305] | [(DEPRECATED) Reddit Dashboard][1303] <br><br> [Giphy Search][1302] |
| [Angular Services][306] | |
| [Angular Routing (UI Router)][307] | [Route Those Views][1305] |
| [Intro to MongoDB][309] <br><br> [Mongoose][310] |  |
| [JSON Web Tokens][311] | [RESTful API][1310] |
| [Angular + Express][313] <br><br> [Starter Code][314] | |
| [Angular Authentication][315] | [Starter Code][316] |
| [Custom Filters][319] | [Creating Filters][1313] |
| [Custom Directives][320] | [Creating Directives][1314] |
| [Angular Components][333] |                             |

### React

| Topic | Assignments + Labs |
| ----- | ------------------ |
| [Intro to ES6][1318] <br><br> [Let and Const][1319] <br><br> [Arrow Functions][1320] | [ES6 Overview][1321] |
| [Intro to ReactJS][] | [React Video (2m)][1322] <br><br> [React Video (8:30-16:30)][1323] <br><br> [Create React App][1324] |
| [React Components][1325] <br><br> [React Virtual DOM][1326] | [Virtual DOM Video][1327] |
| [React Props][1328] <br><br> [Multiple Props][1329] | [React Props][1330] <br><br> [React Nested Components][1331] <br><br> [LotR Lab][1332] |
| [React State][1334] | [React Films][1333] <br><br> [React Calculator][1335] <br><br> [React ATM][1336] |
| [React Router pt 1][1337] <br><br> [React Router pt 2][1338] | [Router Blog][1343] |
| [APIs][1340] <br><br> [Data Types][1341] | [Shakespeare Fetch][1342]  |
| [Unidirectional Flow][1344] | [Fetch the Weather][1345] |
| [Functional Components][1346] | [Functional Components Lab][1347] |
| [Redux Intro][1350] | [Lab 1][1351] [Lab 2][1352] |
| [React Native Set-Up][1353] <br><br> [React Native Lesson][1354] | [Navigators][1355] <br><br> [Deployment][1356] |



| Projects and Additional Topics |
| -------- |
| [Project 4][1304] |
| [MEAN/MERN Hackathon][1312] |
| [Interview Questions][1315]
| [ES6 Variables and Strings (Codepen)][1306] |
| [ES6 Arrow Functions (Codepen)][1307] |
| [Imperative vs Declarative][1339] |
| [Deploying React Apps][1348] |
| [React-Tac-Toe][1349] |


### Computer Science

| Topic | Assignments |
| ----- | ----------- |
| Recursion/Problem Solving | [Array Challenge][1308] |
| Binary Search <br><br> [Algorithm Complexity][308] | [Auto Guess][1309] |
| [Stacks and Queues][312] | [Bracket Matching][1311] |
| Linked Lists | [Singly Linked List][317] <br><br> [Linked List Methods][318] |
| Bucket Sort | [Bucket Sort: Sorting Papers][321] |
| [Bubble Sort][322] | |
| [Merge Sort][323] | |
| [Quick Sort][324] | |
| [Sorting Wrapup][325] | |
| [Hashmaps][326] | |
| [Trees and Other Topics][327] | N/A |


[301]: 07-angular/angular-intro/readme.md
[302]: 07-angular/angular-directives-filters/readme.md
[303]: 07-angular/angular-animation/readme.md
[304]: 07-angular/angular-bootstrap-directives/readme.md
[305]: 07-angular/angular-http/readme.md
[306]: 07-angular/angular-services/readme.md
[307]: 07-angular/angular-routing/readme.md
[308]: 08-cs/cs-algorithm-complexity/readme.md
[309]: 04-databases/mongo-intro/readme.md
[310]: 05-express/express-mongoose/readme.md
[311]: 05-express/express-jwt/readme.md
[312]: 08-cs/cs-stacks-queues/readme.md
[313]: 07-angular/angular-express/readme.md
[314]: https://github.com/WDI-SEA/fly-on-angular
[315]: 07-angular/angular-authentication/readme.md
[316]: https://github.com/WDI-SEA/angular-recipes
[317]: 08-cs/cs-ruby-linked-list/readme.md
[318]: 08-cs/cs-ruby-linked-list-2/readme.md
[319]: 07-angular/angular-custom-filters/readme.md
[320]: 07-angular/angular-custom-directives/readme.md
[321]: 08-cs/cs-ruby-bucket-sort/readme.md
[322]: 08-cs/cs-ruby-bubble-sort/readme.md
[323]: 08-cs/cs-ruby-mergesort/readme.md
[324]: 08-cs/cs-ruby-quicksort/readme.md
[325]: 08-cs/cs-sorting/readme.md
[326]: 08-cs/cs-hashmaps/readme.md
[327]: 08-cs/cs-trees-data-structures/readme.md
[328]: 10-react/react-intro/readme.md
[329]: 10-react/react-gulp-browserify/readme.md
[330]: 10-react/react-router/readme.md
[331]: https://github.com/WDI-SEA/react-omdb
[332]: 10-react/react-animations/readme.md
[333]: 07-angular/angular-components/readme.md

[1300]: https://github.com/WDI-SEA/angular-calculator
[1301]: https://github.com/WDI-SEA/fruits-and-veggies
[1302]: https://github.com/WDI-SEA/angular-giphy
[1303]: https://github.com/WDI-SEA/angular-reddit-dashboard
[1304]: 11-projects/project-4/readme.md
[1305]: https://github.com/WDI-SEA/angular-route-those-views
[1306]: http://codepen.io/bhague1281/pen/EKyMVz
[1307]: http://codepen.io/bhague1281/pen/aNZPrq
[1308]: 08-cs/teaser-js-array-flatten/readme.md
[1309]: 08-cs/teaser-ruby-binary-search/readme.md
[1310]: https://github.com/WDI-SEA/restful-api
[1311]: 08-cs/cs-ruby-bracket-stacks/readme.md
[1312]: 11-projects/mean-hackathon/readme.md
[1313]: https://github.com/WDI-SEA/angular-filters
[1314]: https://github.com/WDI-SEA/angular-directives
[1315]: https://github.com/WDI-SEA/interview-questions
[1316]: https://github.com/WDI-SEA/react-stopwatch
[1317]: https://github.com/WDI-SEA/react-yearbook
[1318]: https://github.com/WDI-SEA/react_es6_global/blob/master/01-es6.md
[1319]: https://github.com/WDI-SEA/react_es6_global/blob/master/02-es6-const-let.md
[1320]: https://github.com/WDI-SEA/react_es6_global/blob/master/03-es6-arrow.md
[1321]: https://github.com/WDI-SEA/react_es6_global/blob/master/05-es6-exercise.md
[1322]: https://generalassembly.wistia.com/medias/lr8idjxtx8
[1323]: https://www.youtube.com/watch?v=KVZ-P-ZI6W4&feature=youtu.be&t=510 
[1324]: https://github.com/WDI-SEA/react_intro_global/blob/master/02-initial-setup.md
[1325]: https://github.com/WDI-SEA/react_intro_global/blob/master/03-components.md 
[1326]: https://github.com/WDI-SEA/react_intro_global/blob/master/04-virtual-dom.md 
[1327]: https://www.youtube.com/watch?v=-DX3vJiqxm4
[1328]: https://github.com/WDI-SEA/react_intro_global/blob/master/05-props.md
[1329]: https://github.com/WDI-SEA/react_intro_global/blob/master/06-multiple-props.md
[1330]: https://github.com/WDI-SEA/react_intro_global/blob/master/07-props-challenge.md
[1331]: https://github.com/WDI-SEA/react_intro_global/blob/master/08-nested-components.md
[1332]: https://github.com/WDI-SEA/lotr-solution-code
[1333]: https://github.com/WDI-SEA/react_intro_global/blob/master/12-film-1-components.md
[1334]: https://github.com/WDI-SEA/react_state_exercises_global/blob/master/01_state.md
[1335]: https://github.com/WDI-SEA/react_state_exercises_global/blob/master/07_calculator_exercise.md
[1336]: https://github.com/WDI-SEA/react_atm_global
[1337]: https://github.com/WDI-SEA/react_router_global/blob/master/01-router-introduction.md
[1338]: https://github.com/WDI-SEA/react_router_global/blob/master/02-react-router-intro.md
[1339]: https://github.com/WDI-SEA/react_apis_heroku_global/blob/master/05-declarative-imperative.md
[1340]: https://github.com/WDI-SEA/react_apis_heroku_global/blob/master/01-APIs.md
[1341]: https://github.com/WDI-SEA/react_apis_heroku_global/blob/master/02-data-types.md
[1342]: https://github.com/WDI-SEA/react_apis_heroku_global/blob/master/03-fetch.md
[1343]: https://github.com/WDI-SEA/react_intro_global/blob/master/07-props-challenge.md
[1344]: https://github.com/WDI-SEA/react_es6_global/blob/master/08-unidirectional-flow.md
[1345]: https://github.com/WDI-SEA/react_apis_heroku_global/blob/master/04-fetch-project.md
[1346]: https://github.com/WDI-SEA/react_es6_global/blob/master/06-functional-components.md
[1347]: https://github.com/WDI-SEA/react_functional_components
[1348]: https://gawdiseattle.gitbooks.io/wdi/10-react/react-deploy/readme.html 
[1349]: https://github.com/WDI-SEA/react-tac-toe 
[1350]: https://git.generalassemb.ly/jamieking/redux-todo-list/tree/redux-impl
[1351]: https://git.generalassemb.ly/atl-wdi/wdi-curriculum/blob/master/instructor_notes/redux/state-management-and-intro-to-redux.md 
[1352]: https://git.generalassemb.ly/atl-wdi/wdi-curriculum/blob/master/instructor_notes/redux/react-with-redux.md
[1353]: https://git.generalassemb.ly/wdi-wc-march2018/warm-ups/blob/master/week-8/monday.md 
[1354]: https://git.generalassemb.ly/wdi-wc-march2018/react-native/blob/master/README.md
[1355]: https://reactnavigation.org/docs/en/hello-react-navigation.html
[1356]: https://docs.expo.io/versions/latest/guides/building-standalone-apps.html 

---

## Licensing
1. All content is licensed under a CC-BY-NC-SA 4.0 license.
2. All software code is licensed under GNU GPLv3. For commercial use or alternative licensing, please contact legal@ga.co.
