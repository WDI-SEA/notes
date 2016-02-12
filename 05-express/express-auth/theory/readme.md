#Authentication in theory

##Objectives

* Utilize sessions to remember users between page loads
* Utilize bcrypt to encrypt passwords
* Utilize hooks and validations to encrypt and verify passwords
* Utilize class/instance methods to authenticate users
* Utilize middleware to load the current user on each request

Authentication is a complex concept that involves using many of the concepts you've already learned and several new concepts. An authentication system allows the registration / signup of new users and allows those users to sign in.

To facilitate that we need to create the following:

* `GET /signup`  -form where the user can register
* `POST /signup`  -route to create a user in the database
* `GET /login` -form where users can login
* `POST /login` -validate the users e-mail and password
* A user model/table to store user data

All of the above we've already learned how to do in the past couple weeks.

Additionally, we need to:

* Encrypt the user's password
* Create a session to remember a user between page loads
* Create a way to easily check if the user is logged in
* Deny the user access to certain pages if they aren't logged in

To do this we need to learn some new concepts.
