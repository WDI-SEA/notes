# Research AND Code

We'll be breaking up into groups. Each group will be assigned a component to research and briefly present to the class.

## Bcrypt

* What is bcrypt?
* How does bcrypt work?
* How do we use bcrypt in node?
* **Try it!** Implement code to use bcrypt to hash a plain text string AND then use `.compare()` to check it. This can be done in a **stand alone .js file** in a node app.

## Sequelize Validations

* What are different types of validations?
* Which ones could be useful?
* How do we use validations in sequelize?
* **Try it!** Implement a validation on BlogPulse to require submitted comments to be between `20` and `200` characters. Test that it works. Use .catch\(\) to send a message to the user. It can just use res.send\(\) for now if you want. If you have extra time, try to make the message render on the page.

## Sequelize Hooks

* What is a Sequelize hook?
* What are different types of Sequelize hooks? 
* How are hooks implemented in Sequelize?
* **Try it!** Use Sequelize hooks to convert all comments posted to your BlogPulse app to lowercase before they are created. The hook should be created in your model. If you have more time, try coming up with another use for a hook in the same project.

## Sessions

* What are sessions?
* What is the difference between sessions and cookies?
* How do we use sessions in express?

## Express Middleware

* What is middleware?
* What middleware have we used?
* How do we create our own express middleware?

