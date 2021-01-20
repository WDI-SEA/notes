# Passwords

For password protection we'll use bcrypt. Bcrypt creates highly secure salted hashed passswords. Learn more about bcrypt on the [bcrypt wiki](http://en.wikipedia.org/wiki/Bcrypt), and maybe read about [the difference between encoding, encrypting, and hashing](https://medium.com/swlh/the-difference-between-encoding-encryption-and-hashing-878c606a7aff#:~:text=%2D%20Encryption%20is%20a%20process%20to,into%20a%20fixed%2Dlength%20string.) while you're at it! Note that bcrypt hashes passwords in an extremely secure way. It differs from other hashing methods like MD5 by putting a roadblock in the way between the hash and a hacker \(specifically, time\). Let's see how this works.

To use bcrypt in node we need to install / use the bcrypt npm module.

**Install bcrypt**

```text
npm i bcrypt
```

**Hash password**

```javascript
//example
bcrypt.hash('myPassword', 10).then(hashedPassword=>{
  console.log(`\'myPassword\' became ---> ${hashedPassword}`)
});
```

**bcrypt.hash\(\) takes 3 parameters**

* Password to hash -- self explanitory
* Rounds -- Number of rounds of processing when generating the salt. The higher the number, the longer it takes to generate the hash, and the more secure the hash. More on salting and hashing [here](https://medium.com/swlh/introduction-to-salted-hashed-passwords-d19bd6f92480).
* Callback function \(called when the hashing completes\)

**Note about salt rounds:** The higher the number, the longer it will take for a potential hacker to crack the password via brute-force. HOWEVER, it also takes longer to create the password. The default value of 10 takes less than a second. A value of 13 will take about a second. 25 will take about an hour and 30 will take DAYS to complete. The default value of 10 is perfectly fine for now.

[More info about bcrypt module](https://www.npmjs.com/package/bcrypt)

### Hash the password in a sequelize hook

Read more about hooks [here](https://sequelize.org/master/manual/hooks.html). We want the password to be hashed before the CRUD (specifically the C in this case) happens, so use a `beforeCreate` hook to replace the password that the user entered with a hash!

```javascript
  user.addHook('beforeCreate', async (pendingUser, options)=>{
    await bcrypt.hash(pendingUser.password, 10)
    .then(hashedPassword=>{
      console.log(`${pendingUser.password} became ---> ${hashedPassword}`)
      pendingUser.password = hashedPassword
    })
  })
```

**OR** There's also a synchronous version of this function called `hashSync`. Read more about async vs. sync hashing [here](https://www.npmjs.com/package/bcrypt#why-is-async-mode-recommended-over-sync-mode).

```javascript
  user.addHook('beforeCreate', (pendingUser, options)=>{
    let hashedPassword = bcrypt.hashSync(pendingUser.password, 10)
    console.log(`${pendingUser.password} became ---> ${hashedPassword}`)
    pendingUser.password = hashedPassword
  })
```

