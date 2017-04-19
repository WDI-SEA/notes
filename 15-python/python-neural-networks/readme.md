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

### Neural Networks using Iris Data

For this code-along we'll go through the example found [here](https://www.tensorflow.org/get_started/tflearn).

