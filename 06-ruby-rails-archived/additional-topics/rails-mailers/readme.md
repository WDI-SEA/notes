# Action Mailers - Password Reset

## Objectives

* Describe in details the concepts behind Action Mailers
* Identify situations where emails will need to be sent by your application
* Use Action Mailers to implement a password reset system

## Getting Started

https://github.com/WDI-SEA/rails-password-reset

Use this starter code in order to have an app with user authentication. We'll be building upon this app in order to add the ability to reset passwords.

## What are Action Mailers?

An Action Mailer is a class that allows you to send emails in Rails. They are very similar to controllers, where each mailer is a class with different methods. There are also views, which represent the content of the email.

Let's try creating a mailer and identify some components.

### Creating a Mailer

We'll be creating a mailer in order to send users a password reset link.

```
rails g mailer UserMailer password_reset
```

Note how the generator created layouts, views, test files, and a base class for all mailers. Each mailer class inherits from `ApplicationMailer`, and mailer classes have methods that represent different emails.

These mailers can be called from the console, but in development, we need to setup email delivery. Or, we can use a gem called `letter_opener` to view emails in the browser. Let's do that for now.

### Letter Opener

Install `letter_opener` to view emails in the browser. Add the gem to your gem file in the development group.

```ruby
group :development do
  gem 'letter_opener'
end
```

Configure `letter_opener` by going to your configuration and adding this line to your `config/environments/development.rb`. While we're at it, we'll also configure the email URLs (which must be done manually).

```ruby
config.action_mailer.delivery_method = :letter_opener
config.action_mailer.default_url_options = { host: 'http://localhost:3000' }
```

Now emails should appear in the browser. Right? Right. Try testing it by running `rails c` and call the mailer:

```ruby
# in rails console
UserMailer.password_reset.deliver_now
```

Now that we've verified the functionality of `letter_opener` and our mailer, let's make some routes and a controller to add password reset functionality.

## Create Routes and Controller

In **routes.rb**

```ruby
get 'reset' => 'passwords#new'
post 'reset' => 'passwords#create'
get 'reset/:code' => 'passwords#edit', as: :reset_code
put 'reset/:code' => 'passwords#update'
```

The latter two routes will handle our reset code. Then...

```
rails g controller passwords new edit
```

###Creating a Reset Password Form

In **views/passwords/new.html.erb**

```erb
<h1>Reset Password</h1>

<%= bootstrap_form_tag url: reset_path do |f| %>
  <%= f.email_field :email, placeholder: 'Enter your email' %>
  <%= f.primary 'Send Reset Email' %>
<% end %>
```

### Add Columns for a Reset Code and Expiration

```
rails g migration AddResetToUsers reset_code expires_at:datetime
```

Note that `Add<Attributes>To<Table Name>` will create the migration we need. All we need is to specify the columns.

Let's also add a method to our `User` model to set the password reset functionality. We'll do this by generating a reset code, setting an expiration date, and saving the user.

```ruby
def set_password_reset
  # this will ensure users with duplicate codes
  self.reset_code = loop do 
    code = SecureRandom.urlsafe_base64
    break code unless User.exists?(reset_code: code)
  end
  # set the expiration date with some handy date methods
  self.expires_at = 4.hours.from_now
  self.save
end
```
  
### Update the Password Controller

Make sure that we can find the user and set a reset code if found.

```ruby
def create
  user = User.find_by_email(params[:email])
  if user
    user.set_password_reset
    UserMailer.password_reset(user).deliver_now
  end
  flash[:warning] = 'Password reset sent if email exists'
  redirect_to root_path
end
```
  
### Alter the Password Reset Mailer

Lastly, we need to alter our mailer so it accepts a user and prints out the right information to our mailer view.

Alter the action in **app/mailers/user_mailer.rb**

```ruby
def password_reset(user)
  @user = user
  mail(to: user.email, subject: 'Password Reset')
end
```

Make sure to alter the views as well.

In **app/views/user_mailer/password_reset.html.erb**

```erb
<h1>Reset Password</h1>

<p>
  Hi <%= @user.name %>. You've requested a password reset. Go to this link to do so:
</p>

<%= link_to 'Password Reset', reset_code_url(@user.reset_code) %>
```

But what about the reset? Now we need an edit form and update action to handle the new password.

In **passwords_controller.rb**

```ruby
def edit
  @code = params[:code]
end

def update
  user = User.find_by_reset_code(params[:code])
  valid_code = user.expires_at > Time.now.utc
  if user && valid_code && params[:password]
    user.update(password: params[:password], reset_code: nil, expires_at: nil)
    flash[:success] = 'Reset successful, login!'
    redirect_to login_path
  else
    flash[:danger] = 'Invalid reset code and/or password'
    redirect_to root_path
  end
end
```

In **views/passwords/edit.html.erb**

```erb
<h1>Enter New Password</h1>

<%= bootstrap_form_tag url: reset_code_path(@code), method: :put do |f| %>
  <%= f.password_field :password %>
  <%= f.primary 'Reset Password' %>
<% end %>
```

### Sendmail

If you would like to test actually sending mail from your local machine, you can use a binary included with MacOSX/Linux called `sendmail`. In order to set up sendmail, you will need to set up some additional configuration in your project.

In your `config/environments/` folder, there are three environments files which are used for configuration depending on your current environment (dev/test for your machine or prod for deployment on, say, Heroku).

For now, we'll just edit the `development.rb` file. Append the following within the do block:

```rb
  config.action_mailer.delivery_method = :sendmail
  # Defaults to:
  # config.action_mailer.sendmail_settings = {
  #   location: '/usr/sbin/sendmail',
  #   arguments: '-i -t'
  # }
  config.action_mailer.perform_deliveries = true
  config.action_mailer.raise_delivery_errors = true
  config.action_mailer.default_options = {from: 'no-reply@example.com'}
```

You can see there are some additional parameters you can change, along with some comments on where the sendmail binary should be located, but the main gist of this config is the first line where we specify the sendmail binary as how our machine will send mail.

Simply calling `UserMailer.password_reset.deliver_now` will fire off an email to the address provided! Be sure to configure your from email address in `app/mailes/application_mailer.rb`.

### Heroku

Sendmail, however, is not present on Heroku and you will need to use some external service for sending mail. [More information can be found here.](https://devcenter.heroku.com/articles/smtp)

###Additional Notes

If you look in your console when you send an email, you'll notice a couple things. Sending the basic pre-generated email will display something like the following:

```
Sent mail to test@example.com (36.1ms)
Date: Wed, 13 Jul 2016 16:32:31 -0700
From: test@example.com
To: test@example.com
Message-ID: <5786cf8fe5adc_4fb3fed92d1901091979@my-macbook.local.mail>
Subject: test subject
Mime-Version: 1.0
Content-Type: multipart/alternative;
 boundary="--==_mimepart_5786cf8fe4ad1_4fb3fed92d1901091861";
 charset=UTF-8
Content-Transfer-Encoding: 7bit


----==_mimepart_5786cf8fe4ad1_4fb3fed92d1901091861
Content-Type: text/plain;
 charset=UTF-8
Content-Transfer-Encoding: 7bit

UserMailer#test_email

Hi, find me in app/views/user_mailer/test_email.text.erb

----==_mimepart_5786cf8fe4ad1_4fb3fed92d1901091861
Content-Type: text/html;
 charset=UTF-8
Content-Transfer-Encoding: 7bit

<h1>UserMailer#test_email</h1>

<p>
  Hi, find me in app/views/user_mailer/test_email.html.erb
</p>

----==_mimepart_5786cf8fe4ad1_4fb3fed92d1901091861--
```

Notice how the email has _both_ the plaintext and html sections? This is so the email client itself can determine what to display to the client. So if you edit your email, be sure to edit both the html and plain text file!
