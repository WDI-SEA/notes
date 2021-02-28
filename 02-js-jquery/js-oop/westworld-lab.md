
<hr>
Title: OOP Westworld Lab<br>
Type: Lab<br>
Duration: 1 hr<br>
Creator: Thom Page<br>
Modified by: Kristyn Bryan, Taylor Darneille<br>
Topics: Object methods, Constructors<br>
<hr>

# OOP Westworld Lab

---

# WESTWORLD

![west world](https://i.imgur.com/WXmau06.png)

From Wikipedia:

> [Westworld] takes place in fictional Westworld, a technologically advanced, Western-themed amusement park populated completely by synthetic androids dubbed "hosts". 


## Make your own Westworld hosts

You are going to make some androids for the Westworld park!

#### Create a host

Make an object called `host` that has the following properties:

* name
* occupation

Give your `host` object a method called `saySpecs`.

The `saySpecs` method should output a message from the host listing the host's specifications -- the host's name and occupation:

```
=> "My name is Roget. My occupation is creator of Roget's Thesaurus."
```

<br>
<hr>

#### Create some basic hosts

Now let's make a **class** so that we can easily make many hosts.

Make a class called `BasicHost` that takes parameters for name and occupation.

```javascript
class BasicHost {
      constructor(name, occupation) {
	//stuff here
      }	
}
```

Make it so the `BasicHost` function will spit out a host object.

```javascript
var host1 = new BasicHost("Roget", "creator of Roget's Thesaurus"); 
```

```javascript
console.log(host1);
```

Output:

![](https://i.imgur.com/BSerF4b.png)


Make another instance with the BasicHost called `host2`.

<br>
<hr>

#### Augment your basic hosts

Give your class a `saySpecs` method that will log all of the specs of the instance. 

Create a few more basic host objects with your constructor.

Invoke the `saySpecs` function on those hosts.

<br>
<hr>

#### Populate the world with hosts

How many hosts can we make???? We are going to populate an array with host objects using a **for loop.**

We will need a pool of names to draw from. Make an array called `names`, and add in a few names. Here's one if you want to use it:

taken from http://listofrandomnames.com/

```javascript
const names = [
			       "Laila", "Jack", "Harley", "Hertha", "Darren", "Jolene", 
             "Loura", "Lona", "Davida", "Reena", "Leland", "Ta", "Jen", 
             "Linn", "Roslyn", "Margorie", "Rafaela", "Romona", "Shanel", "Stan"
            ];
```
  
Make an array called `occupations` and add in a few occupations. Here's one if you want to use it:

```javascript
const occupations = [
					         "Clerical assistant", "Leaflet distributor", "Landowner",
                   "Special constable", "Anaesthetist", "Park-keeper", "Butler",
                   "Choreographer", "Blacksmith", "Chef", "Legal secretary",
                   "Song writer", "Librarian", "Landscape gardener"
					        ];
```

<br>

Make an _empty_ array called `hostArray`. This is where we will store our host objects.


Write a **for loop** that will will run 100 times.
Inside the for loop, push a new BasicHost into the array:

```
hostArray.push(new BasicHost());
```

After the loop, console.log the hostArray.

We have 100 hosts, but they have no values for their attributes:

![](https://i.imgur.com/3IZ5Vmb.png)


FIGURE IT OUT

Make it so that when a new BasicHost is pushed into the array, that host will be assigned a **random name** and **random occupation** from the names and occupations arrays.

If it works, you should have an array of objects of a variety of different hosts.

hostArray:

![](https://i.imgur.com/BKqT6H6.png)

<br>
<hr>

Make a host speak.

`hostArray[55].saySpecs()`

![](https://i.imgur.com/TSJIUzN.png)

#### Bonus

Make your hosts more interesting by giving them random numerical values from 1-20 for personality traits (how ever many you would like):

* Empathy
* Loyalty
* Aggression
* Curiosity
* Bulk Apperception

Etc.
