# Post Project 2

## Fix up your project

### Home page description

On the home page, include a description of what your app is.

### Site Contact Info

Have a proper about section on the page, along with a link to the Github repository, in order to have recruiters and people contact you.

### Validation and Error handling

* All fields taken by the user should have validation
* All models should have validations on critical fields, like uniqueness for email/username, and password lengths
* All fields and routes should be able to handle unexpected input, and empty values.
  * All incorrect urls should be handled with 404 pages, and not crash your app. Example: `/home/asldkfjalsdf` or `/user/a342` will not result in a crash.
  * Regardless of what you type in any field, your app should check for bad values and inputs. 
  * Display error and flash messages everywhere on the site.
* As the ultimate test, try to have others use your site and see if they can break it.

### Visual Styling and Usability

* All page content should fit within bounds on desktop and mobile. This means no content should overflow outside of its container.
* Maps should not zoom with mouse scrolls.
* Overall, make your application responsive, and test it on your phone. Don't forget the viewport meta tag!

### Code Quality

* All code should be properly indented.
* Make sure all variables, routes, and views have descriptive names. A new developer should know how your app works and where data is being sent.
  * Get rid of variables like `data` and translate it to things like `usersData`
* Make sure `.env` files are not stored on github.

## Ruby

We will be returning to Ruby when we get back. But before then, you can check out these resources before we deep dive into when we get back. To get ready, we're going to re-do the Google Shopping assignment using Ruby.

Link to Google Shopping: [https://github.com/WDI-SEA/google-shopping-ruby](https://github.com/WDI-SEA/google-shopping-ruby)

### Ruby Resources

* [Codeschool Ruby](https://www.codeschool.com/courses/try-ruby)
* [Learn Ruby the hard way by Zed Shaw](http://learnrubythehardway.org/book/)

