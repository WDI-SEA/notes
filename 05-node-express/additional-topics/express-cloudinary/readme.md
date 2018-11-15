#File / Image uploads

##Objectives

* Use and configure middleware to upload files from a form to a server
* Utilize a third party cloud service to upload, store, and retrieve images.

##Basic file uploads

Historically, file upload has been a fairly complex task, but with Node (and some 3rd party modules) it is incredibly simple. We'll be using **multer** along with **cloudinary** to upload images.

###Starter Code

We'll use the starter code here: https://github.com/WDI-SEA/express-cloudinary

###Process

* Create multipart form with a file field
* Install multer
* Create a post route to receive the file
* Configure middleware to upload the file to the server
* Upload file to cloudinary

####Creating a Multipart Form

To be able to upload files, you must use a multipart form. This is done by simply setting enctype to multipart/form-data. See this [StackOverflow response](http://stackoverflow.com/questions/4526273/what-does-enctype-multipart-form-data-mean) for more details on a form's `enctype`.

Also note, setting the input type to **file** will display a file picker.

```html
<form enctype="multipart/form-data" action="/" method="POST">
  <input type="file" name="myFile">
  <input type="submit" class="btn btn-primary">
</form>
```

####Creating the Route

Now, we'll need a route to catch the data from the file form. But in order to handle the file, we'll need a package called multer.

[https://www.npmjs.com/package/multer](https://www.npmjs.com/package/multer)
  
**Install Multer**

```
npm install --save multer
```

**add/configure multer**

```js
var multer = require('multer');
var upload = multer({ dest: './uploads/' });

app.post('/', upload.single('myFile'), function(req, res) {
  res.send(req.file);
});
```

For uploading multiple files, see the [Multer documentation](https://www.npmjs.com/package/multer).

Multer automatically handles the file upload and puts the file in the "uploads" directory based on what we set above in the middleware. The file can then be accessed from the request by accessing `req.file` or `req.files`

####Ephemeral file systems

Services like Heroku and AWS's EC2 use an ephemeral file system. This means that every time you deploy your project, all files are replaced with the latest version of your project (which means any user uploaded files will be removed).

To get around this, we need to copy uploaded files to a 3rd party service such as [Amazon S3](https://www.npmjs.com/package/s3) or [Cloudinary](http://cloudinary.com/). This ends up being beneficial because we can separate our image uploads and other assets to a separate server.

##Image processing with Cloudinary

###Process

* Create a Cloudinary account
* setup keys
* install npm module
* upload images
* generate image urls

[https://www.npmjs.com/package/cloudinary](https://www.npmjs.com/package/cloudinary)

####Create a Cloudinary account

In order to use Cloudinary, you'll need to create a Cloudinary account. This can be done by signing up on their website. Heroku also provides a Cloudinary addon, which also sets up a cloudinary account. 

https://cloudinary.com

####Setup Cloudinary Keys

On the Cloudinary dashboard, you'll want to find the environment variable called `CLOUDINARY_URL`. Copy/paste this URL into a `.env` file in your project. This will serve as the API key.

In **.env**

```
CLOUDINARY_URL=cloudinary://xxxx:xxxx@xxxxx
```

If you setup Cloudinary through the Heroku addon, the `CLOUDINARY_URL` and other environment variables can be obtained by running:

```
heroku config
```

####Install Cloudinary

```
npm install --save cloudinary
```

####Upload images to cloudinary

Uploading images to cloudinary can be done by requiring the cloudinary module and calling the `upload` function within cloudinary's uploader. Pass the path of the file that needs to be uploaded, then print the results in the callback. The result will have information regarding the cloudinary upload.

```js
//load module
var cloudinary = require('cloudinary');

//post route
app.post('/', upload.single('myFile'), function(req, res) {
  cloudinary.uploader.upload(req.file.path, function(result) {
    res.send(result);
  });
});
```

In the above example, cloudinary will automatically generate a URL to the image. While the image can be accessed with this URL, you'll want to save the **public_id** in your database in order to use Cloudinary's powerful image manipulation tools.

**Showing Images**

Cloudinary provides a simple method to manipulate images by generating image urls. To use it you simply pass in the public id of the image you want to load followed by an object containing the settings for manipulating the image.

```js
//using previously generated public id
var imgUrl = cloudinary.url("dysepgd0ucddso648bit", { width: 150, height: 150, crop: 'crop', gravity: 'face', radius: 'max' });
```

Read more here: [http://cloudinary.com/documentation/node_image_manipulation](http://cloudinary.com/documentation/node_image_manipulation)
