# Timing Functions

Many built in javascript functions take callback functions. For example, `setInterval` and `setTimeout` both take a function and run it at a specific time.

## setTimeout & setInterval

`setTimeout` takes two arguments:

* the function to be run
* how long to wait \(in milliseconds\) before running that function

```javascript
const alarm = () => {
    console.log("Wake up!");
}

setTimeout(alarm, 10000)
```

`setInterval` also takes two arguments:

* the function to be run
* how often to run the function \(in milliseconds\)

```javascript
const = annoy => () {
  console.log('Are we there yet?');
}

setInterval(annoy, 1000);
```

You may want to have multiple instances of these timing events going, so you can differentiate between the instances by assigning the functions to variables.

```javascript
const alarm = () => {
    console.log("Wake up!");
}

const firstAlarm = setTimeout(alarm, 3000);
const secondAlarm = setTimeout(alarm, 6000);
```

```javascript
const annoy = () => {
    console.log('Are we there yet?');
}

const shutDown = () => {
    console.log('No!')
}

const kids = setInterval(annoy, 1000);
const parents = setInterval(shutDown, 3200);
```

You can disable an interval using `clearInterval`:

```javascript
const annoy = () => {
    console.log('Are we there yet?');
}
const hush = () => {
    clearInterval(kids);
}
const kids = setInterval(annoy, 1000);
setTimeout(hush, 10000)
```

And you can disable your `setTimeout` before the function fires using `clearTimeout`:

```javascript
const alarmRing = () => {
    console.log('RRRIIINNNGGGGG');
}

const turnOffSnooze = () => {
    console.log("turning snooze off now");
    clearTimeout(snoozeAlarm);
}

const snoozeAlarm = setTimeout(alarmRing, 5000);

const snoozeOff = setTimeout(turnOffSnooze, 3000)
```

### Exercises:

_**1.**_ Use `setInteral` and `setTimeout` to write a program that prints the following:

\(This should mimic a countdown, so each line will print after a one second delay.\)

```bash
10
9
8
7
6
5
4
3
2
1
Blast off!
```

_**2.**_ How could you mimic the `setInterval` functionality using `setTimeout`? Use `setTimeout` to recreate the `const kids = setInterval(annoy, 1000);` functionality.

