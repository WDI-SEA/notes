# Neural Networks and Tensor Flow

## Objectives
* Describe a neural network as a high-level concept
* Use the TensorFlow library for linear regression
* Train a simple neural network based on an existing data set
* Test your neural network on new sample data

## Intro activity

Form groups of 2 or 3 with the people sitting closest to you. Answer the following questions together:
* What is a neural network?
* Why might you hear the distinction `artificial` neural network?
* In what way can a neural network be modeled on a computer?
* What practical, real-world applications might this be used for?

## What is a neural network?

`"a computer system modeled on the human brain and nervous system."`

At the microscopic level the human brain (or any other animal's brain) is made up of [neurons](https://en.wikipedia.org/wiki/Neuron) which are highly interconnected with each other. The synapse of each neuron is where each neuron will fire or not fire. If it fires, then the connected neuron is activated.

![Neuron](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Neuron.svg/300px-Neuron.svg.png)

The brain, as it learns, changes the weight or cost of connections, or the likelihood of the neuron actually firing. The more something works, the stronger the path to get there becomes. 

### What are neural networks used for?

When we make models for a computer that mimic a biological neural network, it is called an [Artificial Neural Network](https://en.wikipedia.org/wiki/Artificial_neural_network). These are used for a number of things, but some common themes found in real-world applications include:

* Function approximation or regression analysis, including time series prediction, fitness approximation and modeling.
* Classification, including pattern and sequence recognition, novelty detection and sequential decision making.
* Data processing, including filtering, clustering, blind source separation and compression.
* Robotics, including directing manipulators, prosthesis.
* Control, including computer numerical control.

#### ...And More

To explore further, you can read about [Machine Learning for Predicting Heart Attacks](http://www.digitaltrends.com/health-fitness/ai-algorithm-heart-attack/), [How Self-Driving Cars Work](http://fortune.com/2015/10/16/how-tesla-autopilot-learns/), [Uses of Machine Learning in Online Advertising](https://ozcontent.com/blog/3-surprising-ways-machine-learning-is-being-used-in-advertising/), or if you're not into the world-changey sort of stuff, you can read about a guy who created an optimal strategy for [Finding Waldo](https://www.wired.com/2015/02/created-perfect-wheres-waldo-strategy-machine-learning/)

With the variety of problems that neural networks can be applied to, it's easy to see why this is such a hot topic and why the workplace you enter may well be thinking about using them in some way.

### Practically speaking

Let's watch this video for a visual example of how an artificial neural network is modeled https://www.youtube.com/watch?v=DG5-UyRBQD4

## TensorFlow

Now that you're aware at a high-level of what artificial neural networks are used for, let's use a Python library called TensorFlow that provides a lot of functionality for using these concepts in real-life scenarios.

Run the following commands in your terminal to install TensorFlow on a Mac. If you are not using a mac, visit the [install page](https://www.tensorflow.org/install) for specific instructions.

```
pip3 install --upgrade virtualenv 

virtualenv --system-site-packages .

pip3 install --upgrade tensorflow 
```

### Linear Regression

It's been a little while since math class for most of us, but as a reminder, [linear regression](https://en.wikipedia.org/wiki/Linear_regression) is the process of calculating a function to represent the relationship between a set of data points - usually it measures an independent variable in relation to one or more dependent variables. In short, you're creating a line of best fit for your data set. A [loss function](https://en.wikipedia.org/wiki/Loss_function) is a measure of how far off the real data your calculation was, and is found by summing the squares of the difference between the calculated data and the actual data. Basically, it's a measure of how good your guess is.

![Regression Line](http://www.biostathandbook.com/pix/regressionlollipop.gif)

### Using TensorFlow 

In order to learn some basics about TensorFlow, we'll follow the [getting started example](https://www.tensorflow.org/get_started/get_started) on their website. In this example, we'll be using TensorFlow to model linear regression as well as calculate our loss.

#### The Basics

A tensor is a generic term for vector (in the mathematical sense). A tensor's `rank` is the number of dimensions. You can think of these as levels of depth in your arrays.

![Ranks](http://res.cloudinary.com/briezh/image/upload/v1492641274/Screen_Shot_Ranks_liqan7.png)

Let's first create a test file to play around with called `test.py`. Import TensorFlow at the top the the file. Then create a couple of constants an try printing them out.

```
import tensorflow as tf

node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0) # also tf.float32 implicitly
print(node1, node2)
```

Your output might have looked similar to this:

```
Tensor("Const:0", shape=(), dtype=float32) Tensor("Const_1:0", shape=(), dtype=float32)
```

The zero refers to the rank (see above), because a constant (also known as a scalar value) has a rank of 0. Notice also that there is no value within the Tensors. In fact, you will not see the values until you explicitly run them within a session to evaluate them. Let's change our code so that we create and run a session to evaluate the nodes. Replace the print statement in the code above with the following:

```
sess = tf.Session()
print(sess.run([node1, node2]))
```

Now you should see the values printed out as you originally expected.

```
[3.0, 4.0]
```

Let's get a little more complex and add our two tensor nodes together. Comment out the last line of your code (with the session.run statement) and add the following.

```
node3 = tf.add(node1, node2)
print("sess.run(node3): ",sess.run(node3))

# prints:
# sess.run(node3):  7.0
```

![Simple Add Graph](http://res.cloudinary.com/briezh/image/upload/v1492641238/Screen_Shot_2017-04-19_at_3.29.45_PM_ddbvar.png)

#### Next level

So far, our code is not terribly exciting because all of our data is hard-coded and no external input is going in. We can accept external input by declaring placeholders. Note that a + b is a shortcut for tf.add(a, b).

```
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a + b 

print(sess.run(adder_node, {a: 3, b:4.5}))

# prints: 7.5
```

Now, we can actually run this on an array of input as well. Try the following:

```
print(sess.run(adder_node, {a: [1, 3, 5], b: [2, 4, 6]}))

# prints: [3. 7. 11.]
```

We can do further computations on the input before printing it out, for example, if we wanted to add and then triple the value.

```
add_and_triple = adder_node * 3.
print(sess.run(add_and_triple, {a: [1, 3, 5], b: [2, 4, 6]}))

# prints: [9. 21. 33.]
```

In TensorFlow, we differentiate between placeholders and variables. Think of placeholders as representing the data coming in, and variables as trainable parameters. These are the things that your graph will adjust on each iteration.

#### Back to Linear Regression

Let's create a new python file called `regression.py`. In this file we'll teach our model to fit a set of data points. We're going to be guessing the values of the variables m and b in the equation for a line `mx + b` where m and b are variables, and x is the input value. Initially we'll assign random or default initial values to m and b and then we'll train it from there. Start with the following code:

```
import tensorflow as tf

m = tf.Variable([.3], tf.float32)
b = tf.Variable([-.3], tf.float32)
x = tf.placeholder(tf.float32)
linear_model = m * x + b

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
print(sess.run(linear_model, {x:[1,2,3,4]}))

# prints: [ 0. 0.30000001  0.60000002  0.90000004]
```

If we were to graph this data, it would look like the following:

| x | y |
|-------|-----------|
| 1 | 0 |
| 2 | 0.30000001 |
| 3 | 0.60000002 |
| 4 | 0.90000004 |

![Linear Model](http://res.cloudinary.com/briezh/image/upload/v1492643860/Screen_Shot_2017-04-19_at_4.17.10_PM_ezx2qk.png)

Now that we have a model, we need actual data to compare it to. Let's say the actual y values are 
`[0, -1, -2, -3]`. Knowing that, we can now calculate our 'loss', or how far off we were from the actual values. We do this by taking the difference between each point, squaring that number, then adding all of those numbers together.

| y-actual | y-calculated | difference | squared |
|-----------|-----------|-----------|-----------|
| 0 | 0 | 0 | 0|
| -1 | 0.3 | -1.3 | 1.69 |
| -2 | 0.6 | -2.6 | 6.76 |
| -3 | 0.9 | -3.9 | 15.21 |

Take the sum of all the numbers in the last column. This yields us a loss value of `23.66`. Let's now have TensorFlow do the heavy lifting to calculate this number for us. Add the following code to `regression.py`.

```
y = tf.placeholder(tf.float32)
squared_deltas = tf.square(linear_model - y)
loss = tf.reduce_sum(squared_deltas)
print(sess.run(loss, {x:[1,2,3,4], y:[0,-1,-2,-3]}))
```

In an ideal scenario, we can tweak the values of the two variables until the loss is 0. TensorFlow provides optimizer functions that slowly tweak the values of the variables to minimize the loss. The simplest optimizer is called `gradient descent`. This is how we use it:

```
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)
sess.run(init) # reset values to incorrect defaults.
for i in range(1000):
  sess.run(train, {x:[1,2,3,4], y:[0,-1,-2,-3]})

print(sess.run([W, b]))
```

Sweet! Notice it got close to the perfect values of 1 and -1 minus some rounding errors.

### Neural Networks using Iris Data

For this code-along we'll go through the example found [here](https://www.tensorflow.org/get_started/tflearn).

## Further reading

* [Modelling Linear Regression - Many Resources](http://www.dataschool.io/linear-regression-in-python/)
* [Bayesian Networks](https://en.wikipedia.org/wiki/Bayesian_network)

