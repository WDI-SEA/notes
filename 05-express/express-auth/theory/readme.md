#Authentication in theory

##Objectives

* Utilize sessions to remember users between page loads
* Utilize bcrypt to hash passwords
* Utilize hooks and validations to hash passwords and verify data
* Utilize class/instance methods to authenticate users
* Utilize middleware to authorize users on each page request

Authentication is a complex concept that involves using many of the concepts you've already learned and several new concepts. An authentication system allows the registration / signup of new users and allows those users to sign in.

###Authentication vs. Authorization

* **Authentication:** Proving that a user is valid
  * Providing a username and password is a method of proving user validity
* **Authorization:** The rules that allow a user to perform actions
  * Admins may be authorized to delete users, while regular users cannot delete other users

###Creating Authentication

To facilitate creating an authentication system, we need to create the following:

* `GET /auth/signup`  - form where the user can register
* `POST /auth/signup`  - route to create a user in the database
* `GET /auth/login` - form where users can login
* `POST /auth/login` - validate the users e-mail and password
* A user model/table to store user data

All of the above we've already learned how to do in the past couple weeks.

Additionally, we need to:

* Hash the user's password
* Create a session to remember a user between page loads
* Create a way to easily check if the user is logged in
* Deny the user access to certain pages if they aren't logged in

To do this we need to learn some new concepts.
