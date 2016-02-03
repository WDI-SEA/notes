#Cloudinary upload

This will outline how to setup rails to upload files to cloudinary.


##Basic file uploads

In rails basic file uploads are very simple using the standard form helper or bootstrap form helper.

####View

```
<%= form_for @person do |f| %>
  <%= f.text_field :name %>
  <%= f.file_field :picture %>
  <%= f.submit %>
<% end %>
```

Just by adding a file_field to a form in rails it automatically converts it to a multi-part form and handles the file upload.

####Controller

In your controller you can access it like any other param. In this example it would be `params[:person][:picture]`.

The value in that param will be a UploadFile object which has several methods we can use to interact with the file. For cloudinary we only need the `path` method which will give us the path to the newly uploaded file.

[Details about UploadedFile object](http://api.rubyonrails.org/classes/ActionDispatch/Http/UploadedFile.html)


##Cloudinary

####Set up the Heroku addon

Make sure your project is a heroku project (run `heroku create` before you do this) and you can add the cloudinary addon

```
heroku addons:create cloudinary
```

This will sign you up for a free cloudinary account and should create a config value with the cloudinary credentials (remember to add addons you need to have a credit card number on file).

It will look something like this.

```
heroku config

CLOUDINARY_URL: cloudinary://xxxxx:xxxxx@xxxxxxx
```

To test locally you'll need to copy this information in to your .env file (just replace the ": " with an "=" symbol like this

**.env** file

```
CLOUDINARY_URL=cloudinary://xxxxx:xxxxx@xxxxxxx
```

(note make sure you copy the whole thing if the data is word-wrapped in terminal it's easy to miss part of the string when copying it)


####Setting up the gem

All you have to do to set this up is add the gem to the `Gemfile`. The gem automatically looks for the `CLOUDINARY_URL` env variable so as long as you have your .env file set up correctly it will "just work™".

```
gem 'cloudinary'
```

####Processing the upload

The `Cloudinary::Uploader.upload` method is used to upload a file. All we have to pass in to it is the path to the image that was uploaded to the server.

The method returns a hash with some various information about the upload including file size, dimensions, format, url, and public\_id. The public\_id is what we need to store to display the image in the future.

```
uploaded_file = params[:person][:picture].path
cloudnary_file = Cloudinary::Uploader.upload(uploaded_file)

render json: cloudnary_file

#store this public_id value to the database
#cloudnary_file['public_id']
```

####Displaying the image

To display the image we just need to use the cl\_image\_tag helper and pass it the (previously stored) public\_id. This works exactly like the standard image\_tag helper, but loads images from cloudinary instead of images in the assets folder.


```
<%= cl_image_tag(@person.picture) %>
```

You can also pass in settings for width, height, etc to manipulate the image on the fly.

```
<%= cl_image_tag(@person.picture,
      :width => 400, :height => 400,
      :crop => :fill, :gravity => :face)
      %>
```


##Additional Resources


* [cloudinary rails docs](http://cloudinary.com/documentation/rails_integration)
* [cloudinary image manipulation](http://cloudinary.com/documentation/image_transformations)
* [Rails file field form helper](http://guides.rubyonrails.org/form_helpers.html#uploading-files)
* [Details about UploadedFile object](http://api.rubyonrails.org/classes/ActionDispatch/Http/UploadedFile.html)
