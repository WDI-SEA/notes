![General Assembly Logo](http://i.imgur.com/ke8USTq.png)

#File / Image uploads

##Objectives

* Use and configure middleware to upload files from a form to a server
* Utilize a third party cloud service to upload, store, and retrieve images.

##Basic file uploads

Historically, file upload has been a fairly complex task, but with node (and some 3rd party modules) it is incredibly simple.

####Process

* Install multer
* Create post route to receive uploaded file
* Configure middleware for post route
* Create multipart form with file field

[https://www.npmjs.com/package/multer](https://www.npmjs.com/package/multer)
  
**Install Multer**

```
npm install --save multer
```

**add/configure middleware**

```js
//top of index.js
var upload = multer({ dest: './uploads/' });

//in post route
app.post('/', upload.single('myFile'), function(req, res) {
  res.send(req.file);
});
```

For uploading multiple files, see the [Multer documentation](https://www.npmjs.com/package/multer)

**multipart form**

To be able to upload files you must use a multipart form. This is done by simply setting enctype to multipart/form-data.

```html
<form enctype="multipart/form-data" action="/" method="post">
  <input type="file" name="myFile">
</form>
```

**receiving files**

Multer automatically handles the file upload and puts the file in the "uploads" directory based on what we set above in the middleware. The file can then be accessed from the request by accessing `req.file` or `req.files`

####Ephemeral file systems

Services like heroku use what is called a ephemeral file system. This means that every time you deploy your project all files are replaced with the latest version of your project (which means any user uploaded files will be removed).

To get around this we need to copy uploaded files to a 3rd party service such as [Amazon S3](https://www.npmjs.com/package/s3) or Cloudinary.

##Image processing with Cloudinary

####Process

* Load Cloudinary addon through Heroku
* install npm module
* setup .env
* upload images
* generate image urls

[https://www.npmjs.com/package/cloudinary](https://www.npmjs.com/package/cloudinary)

**Load cloudinary addon**

After creating a new heroku project `heroku create <app_name>` you can add the cloudinary add on from the command line.

```
heroku addons:create cloudinary
```

This enrolls you in the free tier of Cloudinary and sets the api credentials to your environment on heroku (run `heroku config` to check that it worked you should see a "CLOUDINARY_URL" value).

**install npm module**

```
npm install cloudinary --save
```

**Setting up .env**

Coudinary requires a cloudinary connection url which includes api credentials for using their service. This is generated automatically when you add the addon (above).

If you run `heroku config` you should see something like this

```
CLOUDINARY_URL: cloudinary://xxxx:xxxx@xxxxx
```

We simply need to copy this line in to our .env file and replace the ": " with an "=".

**.env file**

```
CLOUDINARY_URL=cloudinary://xxxx:xxxx@xxxxx
```

(remember to add .env to your .gitignore and to run nodemon using foreman)

**Upload images to cloudinary**

Uploading images to cloudinary is incredibly simple and works basically the same as the rename.

```js
//load module
var cloudinary = require('cloudinary');

//post route
router.post('/', upload.single('myFile'), function(req, res) {
  cloudinary.uploader.upload(req.file.path, function(result) {
    res.send(result);
    //store public_id from the result in database
    //redirect somewhere
  });
})
```

In the above example cloudinary will automatically generate a public_id.

**Showing Images**

Cloudinary provides a simple method to manipulate images by generating image urls. To use it you simply pass in the public id of the image you want to load followed by an object containing the settings for manipulating the image.

```js
//using previously generated public id
var imgUrl = cloudinary.url("dysepgd0ucddso648bit", { width: 150, height: 150, crop: 'crop', gravity: 'face',radius: 'max' });
```

Read more here: [http://cloudinary.com/documentation/node_image_manipulation](http://cloudinary.com/documentation/node_image_manipulation)
