# Cloudinary Uploads

## Objectives

* Discuss the benefits and drawbacks of using cloud-based storage
* Use Cloudinary to upload images in Rails

##Basic file uploads

In Rails, file uploads can be done via the standard form helper or bootstrap form helper.

#### View

```rb
<%= form_for @person do |f| %>
  <%= f.text_field :name %>
  <%= f.file_field :picture %>
  <%= f.submit %>
<% end %>
```

Just by adding a file_field to a form in rails it automatically converts it to a multi-part form and handles the file upload.

#### Controller

In your controller you can access it like any other param. In this example it would be `params[:person][:picture]`.

The value in that param will be a UploadFile object which has several methods we can use to interact with the file. For cloudinary we only need the `path` method which will give us the path to the newly uploaded file.

[Details about UploadedFile object](http://api.rubyonrails.org/classes/ActionDispatch/Http/UploadedFile.html)

## Cloudinary

Cloudinary can be setup by either adding it via a Heroku addon...

```
heroku addons:create cloudinary
```

This will sign you up for a free cloudinary account and should create a config value with the cloudinary credentials. Or signup on Cloudinary's website and grab the config value from the Cloudinary dashboard.

http://cloudinary.com/

Either way, your config value should look like this in your .env file:

```
CLOUDINARY_URL=cloudinary://xxxxx:xxxxx@xxxxxxx
```

#### Setting up the gem

Add the `cloudinary` gem to your Gemfile. The gem automatically looks for the `CLOUDINARY_URL` environment variable. As long as you have your .env file set up correctly, it will "just work™".

In **Gemfile**

```
gem 'cloudinary'
```

Run `bundle install` as well.

#### Processing the upload

The `Cloudinary::Uploader.upload` method is used to upload a file. All we have to pass in to it is the path to the image that was uploaded to the server.

The method returns a hash with some various information about the upload including file size, dimensions, format, url, and public_id. The `public_id` is what we need to store to display the image in the future.

```rb
uploaded_file = params[:person][:picture].path
cloudnary_file = Cloudinary::Uploader.upload(uploaded_file)

#store this public_id value to the database
#cloudnary_file['public_id']

render json: cloudnary_file
```

#### Displaying the image

To display the image we just need to use the `cl_image_tag` helper and pass it the (previously stored) `public_id`. This works exactly like the standard `image_tag` helper, but loads images from Cloudinary instead of images in the assets folder.


```erb
<%= cl_image_tag(@person.picture) %>
```

You can also pass in settings for width, height, etc to manipulate the image on the fly.

```erb
<%= cl_image_tag(@person.picture,
      :width => 400, :height => 400,
      :crop => :fill, :gravity => :face)
      %>
```


## Additional Resources


* [Cloudinary Rails docs](http://cloudinary.com/documentation/rails_integration)
* [Cloudinary image manipulation](http://cloudinary.com/documentation/image_transformations)
* [Rails file field form helper](http://guides.rubyonrails.org/form_helpers.html#uploading-files)
* [Details about UploadedFile object](http://api.rubyonrails.org/classes/ActionDispatch/Http/UploadedFile.html)
