##Password Protection

For password protection we'll use bcrypt. Bcrypt creates highly secure salted passswords. Learn more about bcrypt: [bcrypt wiki](http://en.wikipedia.org/wiki/Bcrypt). Note that bcrypt hashes passwords in an extremely secure way. It differs from other hashing methods like MD5 by putting a roadblock in the way between the hash and the infiltrator. **Time.** Let's see how this works.

To use bcrypt in node we need to install / use the bcrypt npm module.

**Install bcrypt**

```
npm install bcrypt --save
```

**Encrypt (hash) password**

```js
//example
bcrypt.hash("myPassword", 10, function(err, hash) {
  //hash = encrypted password (using salt)
});
```

**bcrypt.hash() takes 3 parameters**

* Password to encrypt -- self explanitory
* Rounds -- Number of rounds of processing when generating the salt. The higher the number the more secure the hash.
* Callback function (called when the hashing completes)

**Note about rounds:** The higher the number, the longer it will take for a potential hacker to crack the password via brute-force. HOWEVER, it also takes longer to create the password. The default value of 10 takes less than a second. A value of 13 will take about a second. 25 will take about an hour and 30 will take DAYS to complete. The default value of 10 is perfectly fine for now.

[More info about bcrypt module](https://www.npmjs.com/package/bcrypt)
