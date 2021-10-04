# Deploy - S3 Static Sites

### Objectives

_After this lesson, developers will be able to:_

* Describe S3 storage usages
* Utilize S3 to store files and host website and Route53 for domain routing
* Create and upload static content for a website

### Preparation

_Before this lesson, developers should already be able to:_

* Describe the difference between static and dynamic websites
* Write HTML, CSS, JS to build a functioning website

## S3 - Simple Storage Service Intro \(20 mins\)

Amazon S3, or Simple Storage Service, is an implementation of cloud storage offered by Amazon. Using S3 you can store large amounts of static content needed for websites and apps. Files, or **Objects** as they are referred to in Amazon docs, are stored in seperate **Buckets** that can reach sizes of up to 5 Terabytes.

![S3 Buckets](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/AWS_Simple_Icons_Storage_Amazon_S3_Bucket_with_Objects.svg/1024px-AWS_Simple_Icons_Storage_Amazon_S3_Bucket_with_Objects.svg.png)

Each file/object in the bucket receives a unique **Key** from the user when added to the bucket. Think of it like a folder in your file system. When you try to have two files with the same name you are given the choice of either replacing the old file or giving the new file a new name. S3 buckets work in a similar way.

#### But what does it mean?!

This means S3 is basically a big file system where you can keep and access content!

## Creating a static website \(15 mins\)

One of the major uses of S3 is hosting a static website. S3 now has functionality built in to help with domain mapping which even allows you to use your custom domain name. S3 stands as a nice alternative to BitBalloon and other dropbox-esque services due to it's speed and custom nature.

![S3 Static Website](http://docs.aws.amazon.com/gettingstarted/latest/swh/images/AWS_StaticWebsiteHosting_Architecture_4b.png)

To get our static site up and running we're going to be using not only S3 but also two other Amazon services. We'll also use Route53 for DNS resolution.

First we'll create our S3 buckets. We're going to be creating 3 different buckets for our site. Two will be linked to our domain and the 3rd will be for logs that S3 produces. This structure is recognized and utilized by S3 for static sites. **Important** Be sure to name the buckets the same name as your domain, whatever that may be!

![Static Site Buckets](http://docs.aws.amazon.com/gettingstarted/latest/swh/images/AWS_StaticWebsiteHosting_Architecture_1.png)

By creating the buckets this way, Amazon will generate a URL according to that name:

* [http://example.com.s3-website-us-east-1.amazonaws.com/](http://example.com.s3-website-us-east-1.amazonaws.com/)

Lets jump into the [S3 management console](https://console.aws.amazon.com/s3/) and click the "Create Bucket" button.

![Create Bucket](https://dl.dropboxusercontent.com/u/111919248/Screenshots/Screen%20Shot%202016-03-07%20at%206.44.07%20AM.png) ![Name Bucket](https://dl.dropboxusercontent.com/u/111919248/Screenshots/Screen%20Shot%202016-03-07%20at%206.49.39%20AM.png)

Rinse and repeat bucket creation process for **www.domainname.com** and **logs.domainname.com**

Next we'll setup permissions for our buckets. Since this is a website we'll need parts of it to be accessible to clients. First, from the management console, click on the root domain bucket and click Properties.

![Bucket Properties](https://dl.dropboxusercontent.com/u/111919248/Screenshots/Screen%20Shot%202016-03-07%20at%206.52.59%20AM.png)

Click **Permissions** and then **Add Bucket Policy** to change who can access files. Next we're going to input some config options into the popup editor. Go ahead and copy and paste this JSON code into that popup:

```javascript
{
  "Version":"2012-10-17",
  "Statement": [{
    "Sid": "Allow Public Access to All Objects",
    "Effect": "Allow",
    "Principal": "*",
    "Action": "s3:GetObject",
    "Resource": "arn:aws:s3:::example.com/*"
  }
 ]
}
```

**Make sure to change the domain in the Resource value to match your bucket name!!!**

![Bucket Policy](https://dl.dropboxusercontent.com/u/111919248/Screenshots/Screen%20Shot%202016-03-07%20at%206.57.34%20AM.png)

Next enable logging from your root domain bucket. Click **Logging** in your bucket properties and edit the values like this:

![Logging](http://docs.aws.amazon.com/gettingstarted/latest/swh/images/AWS_StaticWebsiteHosting_ConfigureLogging.png)

### Finally adding some content

By now we should have our buckets set up and ready for static content, so let's upload some!

First we're going to create two files on our computers to be uploaded, **index.html** and **error.html**.

index.html

```markup
<!DOCTYPE html>
<html>
  <body>
    <p>Hello, World!</p>
  </body>
</html>
```

error.html

```markup
<!DOCTYPE html>
<html>
  <body>
    <p>This is an error page.</p>
  </body>
</html>
```

Save those files somewhere on your local computer. Both of these files are recognized by S3 when we enable Static Web Hosting.

Next we're going to upload these files to our root domain bucket. From the management console click the **Actions** dropdown and select **Upload**. You can then either drag and drop or select the two files to upload.

![Uploading files](http://docs.aws.amazon.com/gettingstarted/latest/swh/images/AWS_StaticWebsiteHosting_HostingStaticWebsite_1.png)

After you find the files and click **Start upload** it should look like this:

![Upload complete](http://docs.aws.amazon.com/gettingstarted/latest/swh/images/AWS_StaticWebsiteHosting_HostingStaticWebsite_2.png)

Finally we need to configure one more aspect of our bucket, enabling Static Website Hosting. Back at the S3 management console open your root domain bucket and open Properties. Then open the Static Website Hosting section. Check the **Enable website hosting** option and enter in the information for your two files as such:

![Static site settings](http://docs.aws.amazon.com/gettingstarted/latest/swh/images/AWS_StaticWebsiteHosting_ConfigureAmazonS3Website_1.png)

Click Save and you're done! You've just hosted a static website on S3, nice job!

## Independent Practice \(20 minutes\)

## Front end \(Javascript\) Libraries

| purpose | home page | demos |
| :--- | :--- | :--- |
| Drawing / visual | [http://svgjs.com/](http://svgjs.com/) | obvious on homepage |
| Drawing / visual | [http://paperjs.org/](http://paperjs.org/) | [nyan](http://paperjs.org/examples/nyan-rainbow/), [Other demos](http://paperjs.org/examples) |
| Data Visualization | [http://d3js.org/](http://d3js.org/) | obvious on homepage |
| Physics | [http://wellcaffeinated.net/PhysicsJS/](http://wellcaffeinated.net/PhysicsJS/) | on homepage |
| 2D | [http://cutjs.org/](http://cutjs.org/) | obvious on homepage |
| 3D | [http://threejs.org/](http://threejs.org/) | [rubicks cube](https://www.google.com/logos/2014/rubiks/rubiks.html) / [more demos](http://threejs.org/examples/#webgl_kinect) |
| 2D Game engine | [http://www.html5quintus.com/](http://www.html5quintus.com/) | obvious on site |
| Voice recognition | [https://www.talater.com/annyang/](https://www.talater.com/annyang/) | homepage is demo |
| Audio generator / visualization | [https://github.com/jeromeetienne/webaudiox](https://github.com/jeromeetienne/webaudiox) | [visualization](http://jeromeetienne.github.io/webaudiox/examples/analyser2canvas.html), [audio generator](http://jeromeetienne.github.io/webaudiox/examples/jsfx.html) |
| Typography | [http://letteringjs.com/](http://letteringjs.com/) | links on homepage |

Need more? [http://www.javascripting.com/](http://www.javascripting.com/)

> _**Note:**_ _This can be a pair programming activity or done independently._

Now that you have static content being served out to clients let's add some flavor to it! For this exercise go ahead and pick one frontend technology to add to your site to make it more robust. It can be anything you like but some popular ideas:

* Angular
* Jquery
* D3
* Phaser

Using that technology go ahead and try and code something simple but brand new. Then upload it to S3 and test it out! Now get those fingers moving!!

