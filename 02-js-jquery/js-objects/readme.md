### Objects

Objects, like arrays, store data, but objects are organized differently. Objects store `key: value` pairs, and instead of accessing a value by its index, we access a value by it's associate key. Thus, objects are not ordered like arrays are.

#### Creating

```js
var friend = {firstName: "Jane", lastName: "Doe"}
friend
```

#### Accessing

```js
friend.firstName
friend.lastName
```
or
```js
friend["firstName"]
friend["lastName"]
```

#### Adding Data

```js
friend.middleName = "Jersey"
```
or
```js
friend["middleName"] = "Jersey"
```

#### Modifying values

```js
friend.firstName = "John"
```
or
```js
friend["firstName"] = "John"
```

#### Deleting data
```js
delete friend.middleName
```
or
```js
delete friend['middleName']
```

### Exercise

1.) Represent the following values in an object:

````
"John", "Doe", 36, "1234 Park st".
````

2.) Once you've represented the above as an object, update John's address to `1234 Park ln`.

3.) Using a combination of Objects and Array, how would you represent the following data:

```
Moe, Doe, 31, 1234 Park st.
Larry, Doe, 36, 1234 Spark st.
Curly, Doe, 36, 1239 Park st.
Jane, Doe, 32, 1239 Spark st.
Emma, Doe, 34, 1235 Spark st.
Elizabeth, Doe, 36, 1234 Park st.
Elinor, Doe, 35, 1230 Park st.
Mary, Doe, 31, 1231 Park st.
Darcy, Doe, 32, 1224 Park st.
Grey, Doe, 34, 1214 Park st.
Lydia, Doe, 30, 1294 Park st.
Harriet, Doe, 32, 1324 Park st.
```

4.) Mary is taking to the road, so she no longer has an address. Delete her address!
