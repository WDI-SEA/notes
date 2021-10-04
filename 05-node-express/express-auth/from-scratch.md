# From Scratch

These notes get you started building an express app from scratch. Alternatively, you can start from the template available [here](https://gawdiseattle.gitbook.io/wdi/05-node-express/express-auth/practice).

## Part 1: Bare Bones

Utilize your step-by-step node/express app readme notes to do the following:

* Set up a new node/express app that incorporates ejs and express-ejs-layouts \(don't forgot you `.gitignore`!\)
* Set up your app to use environment variables \(don't forget the configuration in your entry point file!\)
* Stub out the following routes and place the ones that start with `/auth` in a `controllers/auth.js` file \(don't forget the middleware!\):
  * `GET /` \(home route\)
  * `GET /profile`
  * `GET /auth/signup`
  * `POST /auth/signup`
  * `GET /auth/login`
  * `POST /auth/login`
  * `GET /auth/logout`

## Part 2: Views

* Create your layout as well as the home and profile views
* Make views for your login and sign up forms in `views/auth`:
  * signup form should have Name, Email, and Password fields
  * check that your forms are posting to the right place by res.sending the form data \(did you remember the body parser middleware?\)

## Part 3: User Model

* Install sequelize and pg
* `sequelize init`, fix the `config.json` content, then `sequelize db:create`
* Create a user model based off the following table \(we will add the uniqueness and hashing later, so don't worry about those notes for now\)
* Migrate!
* Set up the `POST /auth/signup` route to post users to the db \(find or create based on email\)
* Set up the `POST /auth/login` to find the user from the db \(check both email and password\)

| Column Name | Data Type | Notes |
| :--- | :--- | :--- |
| id | Integer | Serial Primary Key, Auto-generated |
| name | String | Must be provided |
| email | String | Must be unique / used for login |
| password | String | Stored as a hash |
| createdAt | Date | Auto-generated |
| updatedAt | Date | Auto-generated |

```javascript
const express = require('express')
const router = express.Router()
const db = require('../models')

router.get('/login', (req, res)=>{
    res.render('auth/login')
})

router.post('/login', (req, res)=>{
    db.user.findOne({
        where: {
            email: req.body.email,
            password: req.body.password
        }
    })
    .then((foundUser)=>{
        res.send(`Logged in the following user: ${foundUser.name}`)
    })
    .catch((err)=>{
        console.log(err)
        res.send('There was an error logging in. Check console?')
    })
})

router.get('/signup', (req, res)=>{
    res.render('auth/signup')
})

router.post('/signup', (req, res)=>{
    db.user.findOrCreate({
        where: {email: req.body.email},
        defaults: {name: req.body.name, password: req.body.password}
    }).then(([user, wasCreated])=>{
        if(wasCreated) {
            res.send(`Created a new user profile for ${user.email}`)
        } else {
            res.send('Email already exists! Try logging in.')
        }
    })
})

router.get('/logout', (req, res)=>{
    res.send('loggin out')
})

module.exports = router
```

