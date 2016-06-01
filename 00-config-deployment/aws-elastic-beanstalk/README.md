# Amazon Web Services - Elastic Beanstalk

### Objectives
*After this lesson, students will be able to:*

- Describe AWS Elastic Beanstalk
- Build a web app and deploy to EB

### Preparation
*Before this lesson, students should already be able to:*

- Build a functioning full-stack application
- Explain what a virtual server is

## AWS - Amazon EB Intro (20 mins)

Amazon Elastic Beanstalk is an easy to use deployment system that will automatically allocate the necessary software needed such as EC2 instances and S3 buckets. EB comes coupled with a command-line tool that allows for quick code deployment.

[Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/)

While a little bit more in-depth than heroku, Elastic Beanstalk is helpful in that you can scale your app as you develop it. Meaning if you need more resources such as RAM you can change that on the fly.


You can access any apps you've deployed through the Elastic Beanstalk management console:

The EB portal can be used to manage our already created apps or to create new ones.

### Installing the eb-cli

```bash
$ brew install awsebcli
```

### Create a node app to deploy

```bash
mkdir app-name
cd app-name
npm init
npm install --save express
touch index.js index.html
```
Add a **Start** command to our scripts object in *package.json*:

```json
{
  "name": "custom-node-aws",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "start": "node index.js",
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "express": "^4.13.4"
  }
}
```

#### index.js
```javascript
var express = require('express');
var app = express();

app.get('/', function(req, res) {
  res.sendFile(__dirname + '/index.html');
});

app.listen(process.env.PORT || 3000);
```

#### index.html
```html
<!DOCTYPE html>
<html>
<head>
  <title>Test Page</title>
</head>
<body>

  <h1>You did it!!!</h1>

</body>
</html>
```

### Initialize your app for Elastic Beanstalk
```bash
$ eb init

Select a default region
1) us-east-1 : US East (N. Virginia)
2) us-west-1 : US West (N. California)
3) us-west-2 : US West (Oregon)
4) eu-west-1 : EU (Ireland)
5) eu-central-1 : EU (Frankfurt)
6) ap-southeast-1 : Asia Pacific (Singapore)
7) ap-southeast-2 : Asia Pacific (Sydney)
8) ap-northeast-1 : Asia Pacific (Tokyo)
9) ap-northeast-2 : Asia Pacific (Seoul)
10) sa-east-1 : South America (Sao Paulo)
11) cn-north-1 : China (Beijing)
(default is 3): 3

Select an application to use
1) [ Create new Application ]
(default is 1): 1

Enter Application Name
(default is "custom-node-aws2"):

Application custom-node-aws2 has been created.

It appears you are using Node.js. Is this correct?
(y/n): y

Do you want to set up SSH for your instances?
(y/n): n


```

### Create Environment on AWS

Now that our application is created we should see it show up in our EB console on aws.amazon.com.

![](http://res.cloudinary.com/du4thvcsa/image/upload/v1464736754/Screen_Shot_2016-05-31_at_4.18.54_PM_zozbfo.png)

Go ahead and click the ***Create one now*** link

Now you should be seeing the beginning of our Environment Creation page. Click the ***Create web server*** button

![](http://res.cloudinary.com/du4thvcsa/image/upload/v1464736928/Screen_Shot_2016-05-31_at_4.21.47_PM_ak1wo1.png)

For our **Predefined configuration** select **Node.js** from the dropdown and select **Single Instance** for the **Environment type**

The configuration will set up our server with Node.js and it's dependencies already installed. The two environment types are:

 - **Load balancing, auto scaling**: This setting is for if you know that your app will grow and you need to have some versatility to the hardware of your environment.
 - **Single instance**: This is primarily for if you are deploying a smaller app that won't have many requests or is for development, much more minimal.

![](http://res.cloudinary.com/du4thvcsa/image/upload/v1464737035/Screen_Shot_2016-05-31_at_4.23.45_PM_r1q5rn.png)

From here continue to click the ***Next*** button for each subsequent page until you are at the ***Review Information*** section. Once there, click the ***Launch*** button at the bottom.

At this point you should see a screen like this as your app platform is partitioned and setup by AWS. This portion will take several minutes so go grab some coffee!

![](http://res.cloudinary.com/du4thvcsa/image/upload/v1464737567/Screen_Shot_2016-05-31_at_4.32.31_PM_ucrg7r.png)

Eventually you'll get the green checkmark which means your environment has been created!

![](http://res.cloudinary.com/du4thvcsa/image/upload/v1464747889/Screen_Shot_2016-05-31_at_7.24.34_PM_qd6ayj.png)

Make note of your Environment Name located at the top: All Applications > application_name > environment name. Copy and paste that environment name and paste it into your ***config.yml*** for the Default environment:

```yml
branch-defaults:
  default:
    environment: <your_environment_name>
    group_suffix: null
global:
  application_name: custom-node-aws2
  default_ec2_keyname: null
  default_platform: Node.js
  default_region: us-west-2
  profile: eb-cli
  sc: null
```

Now you're ready to deploy! Go ahead and run this command in your app directory:

```bash
$ eb deploy
```