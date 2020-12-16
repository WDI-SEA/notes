# Use data to populate the DOM

Here is a rolodex with people's names and addresses:

![](https://i.imgur.com/TtermqB.png)

We would like to run a function that will populate our page with names and addresses from an **array of objects**

### Data

* Add the **array of objects**

```javascript
const data = [
  { name: "Megatron", address: "Cybertron" },
  { name: "Some guy", address: "Some street" },
  { name: "Grace Hopper", address: "Arlington, Virginia" },
  { name: "Ching Shih", address: "The High Seas" },
  { name: "Slimer", address: "The Library" },
  { name: "Umbra", address: "The Void" },
  { name: "Hypatia", address: "The Neoplatonic school at Alexandria" },
  { name: "Matt Huntington", address: "Remote" },
  { name: "Ronald McDonald", address: "Casa del McDonalds" },
  { name: "Jem", address: "Starlight Music" }
];
```

What we want to do is **populate** our page with data from the array. If, in the future, we change the data in the array, the page can be **re-populated**.

* Write a loop that iterates over the array

```javascript
for (let i=0; i < data.length; i++) {
	console.log(data[i]);
}
```

* We will now be interacting with the DOM so wrap the code in the `DOMContentLoaded` event listener.

* Create a container that will house each name and address. Give it a class we can adjust later

```javascript
document.addEventListener('DOMContentLoaded', () => {

  for (let i=0; i < data.length; i++) {
    console.log(data[i])
    const infoContainer = document.createElement('div')
    infoContainer.classList.add('info-container')
  }

})
```

* Add in the name div, whose text comes from the array. Give it a class we can adjust later.

```javascript
    const nameDiv = document.createElement('div')
    nameDiv.classList.add('name')
    nameDiv.innerText = data[i].name
```

And the address div, whose text comes from the array. Give it a class we can adjust later.

```javascript
    const addressDiv = document.createElement('div')
    addressDiv.classList.add('address')
    addressDiv.innerText = data[i].address
```

* Append the divs to the container div

Finished result

```javascript
document.addEventListener('DOMContentLoaded', () => {

    for (let i=0; i < data.length; i++) {
        const infoContainer = document.createElement('div')
        infoContainer.classList.add('info-container')
        const nameDiv = document.createElement('div')
        nameDiv.classList.add('name')
        nameDiv.innerText = data[i].name
        const addressDiv = document.createElement('div')
        addressDiv.classList.add('address')
        addressDiv.innerText = data[i].address
        infoContainer.appendChild(nameDiv)
        infoContainer.appendChild(addressDiv)
        document.querySelector('body').appendChild(infoContainer)
    }
  
  })
```

### CSS

Give the body a nicer font

```css
body {
  font-family: Verdana;
}
```

Give the info container some color, border, margin, padding

```css
.info-container {
  background-color: azure;
  border: 1px solid grey;
  margin-bottom: 5px;
  padding: 20px;
}
```

Last, give each name and address classes a display of inline-block, some margin, padding, and a border

```css
.name, .address {
  border: 1px solid grey;
  display: inline-block;
  margin-right: 20px;
  padding: 5px;
}
```

### Write in a function that will 'populate' the page

```javascript
const populateData = () => {
    for (let i=0; i < data.length; i++) {
        const infoContainer = document.createElement('div')
        infoContainer.classList.add('info-container')
        const nameDiv = document.createElement('div')
        nameDiv.classList.add('name')
        nameDiv.innerText = data[i].name
        const addressDiv = document.createElement('div')
        addressDiv.classList.add('address')
        addressDiv.innerText = data[i].address
        infoContainer.appendChild(nameDiv)
        infoContainer.appendChild(addressDiv)
        document.querySelector('body').appendChild(infoContainer)
    }
}
```

Now we can move the function out of the window onload, and just invoke the function within the `DOMContentLoaded` listener.

```javascript
document.addEventListener('DOMContentLoaded', () => {
    populateData()
})
```

### Adding data

* Write a function that will push new data in to the array.
* The function should take `name` and `address` as parameters
* The function should then run the `populateData` function


```javascript
const addData = (name, address) => {
    data.push({name, address})
    populateData()
}

document.addEventListener('DOMContentLoaded', () => {
    populateData()
    addData('Taylor', 'Seattle')
})
```

The function 'doubles' the information. To fix this, we should clear out the old information before it populates.

```javascript
const addData = (name, address) => {
    data.push({name, address})
    const body = document.querySelector('body')
    while(body.firstChild) {
        body.removeChild(body.firstChild)
    }
    populateData()
}

document.addEventListener('DOMContentLoaded', () => {
    populateData()
    addData('Taylor', 'Seattle')
})
```

### Activity

See if you can figure out how to create a removeData function that takes a name of a person you want to remove, removes them from the `data` array, then refreshes the rolodex.