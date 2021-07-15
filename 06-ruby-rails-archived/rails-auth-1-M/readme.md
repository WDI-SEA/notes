#Rails Authentication and 1:M Associations

##Objectives

* Create users and store their passwords securely
* Enable the ability to authenticate users and store sessions once logged in
* Utilize filters and validations in Rails
* Establish 1:M relationships

Remember all that hassle of setting up authentication in Node? Rails makes it easy.

##Create a new project

You should know how to do this now. If not, see notes from Intro to Rails.

##Create a user model

We need to first start creating a user model that has a username/email field and a `password_digest`. Note that you **have** to name the field this.

```
rails g model user email password_digest
rake db:migrate
```

##Add some validations
[http://guides.rubyonrails.org/active_record_validations.html](http://guides.rubyonrails.org/active_record_validations.html)

**app/models/user.rb**

```ruby
validates :email,
presence: true,
uniqueness: {case_sensitive: false}
```

Note that we're only checking for presence and uniqueness of the email. Use [this gem](https://github.com/balexand/email_validator) if you'd like to actually validate the email address contents.

##Add password hashing

* Add `has_secure_password` to the user model
* uncomment `gem 'bcrypt'` on your Gemfile and run the bundler

###Test out a user
Now that we have `has_secure_password`, Rails gives out a password setter.

###Add Validations for User

```ruby
validates :password, length: { in: 8..72 }, on: :create
```

###Let's test a real user

```ruby
User.find_by_email('paul@gmail.com').try(:authenticate, '123')
```

This is nifty, but long. We can add a class method that will return true or false, based on the params from the controller.

###Add a helper method to the class

```ruby
def self.authenticate(params)
  User.find_by_email(params[:email]).try(:authenticate, params[:password])
end
```

###The finished User model

```ruby
class User < ActiveRecord::Base
  validates :email,
  presence: true,
  uniqueness: {case_sensitive: false}

  validates :password,
  length: { in: 8..72 },
  on: :create

  has_secure_password

  def self.authenticate(params)
    User.find_by_email(params[:email]).try(:authenticate, params[:password])
  end
end
```

##Add the login pages
Let's create a session controller to handle logging in/out. We'll organize this by calling the controller `sessions`, because in reality, we're creating and destroying sessions on login and logout.

```
rails g controller sessions new
```

add actions `create` and `destroy`

###Lets create some routes

```ruby
get "login" => "sessions#new"
post "login" => "sessions#create"
delete "logout" => "sessions#destroy"
```

### Lets generate a form

```erb
<h1>Login</h1>

<%= form_for :user do |f| %>
  <%= f.email_field :email, placeholder: "Enter your email" %>
  <%= f.password_field :password, placeholder: "Enter your password" %>
  <%= f.submit "Login" %>
<% end %>
```

Wait, why are we using the symbol? [See this StackOverflow answer](http://stackoverflow.com/questions/957204/instance-variable-vs-symbol-in-ruby-on-rails-form-for)

###Authenticate
Authenticate the user on `sessions#create`

```ruby
def create
  user = User.authenticate(user_params)

  if user
    session[:user_id] = user.id
    flash[:success] = "User logged in!!"
    redirect_to root_path
  else
    flash[:danger] = "Credentials Invalid!!"
    redirect_to login_path
  end
end

def destroy
  session[:user_id] = nil
  flash[:success] = "User logged out!!"
  redirect_to root_path
end

private

def user_params
  params.require(:user).permit(:email, :password)
end
```

###Add current User capabilities

```ruby
class ApplicationController < ActionController::Base
  # Prevent CSRF attacks by raising an exception.
  # For APIs, you may want to use :null_session instead.
  protect_from_forgery with: :exception

  before_action :current_user

  def is_authenticated
    unless current_user
      flash[:danger] = "Credentials Invalid!!"
      redirect_to login_path
    end
  end

  def current_user
    @current_user ||= User.find_by_id(session[:user_id])
  end
end
```

###Adding Flash Messages

The `flash` hash is accessible in every Rails controller and view. To access it, we'll need a way to iterate through the hash and print out the keys and values. The best way is to create a partial and include it on the layout (so it'll be on every page).

Partials have to start with an underscore in Rails. We can render the partial by using the `render` helper.

With a partial at **app/views/partials/_flash.html.erb**

```erb
<%= render "partials/flash" %>
```


**_flash.html.erb**

```erb
<% flash.each do |key, value| %>
  <div class="alert alert-<%= key %>">
    <%= value %>
  </div>
<% end %>
```

###Protect a controller

`before_action :is_authenticated` on the controller you want to protect

`@current_user` is now visible to all pages because the `current_user` function is invoked

##Adding 1:M relationships with another model

Let's first add another model to relate to the user. In order for the user to have many pets, we can create the model by including the model name and `references` as the type.

```
rails g model pet name user:references
```

This will make the following migration, which will include a userId in the pet model.

```ruby
class CreatePets < ActiveRecord::Migration
  def change
    create_table :pets do |t|
      t.string :name
      t.references :user, index: true, foreign_key: true

      t.timestamps null: false
    end
  end
end
```

Then, make sure to migrate and include the associations in each model.

```
rake db:migrate
```

**models/user.rb**
```ruby
class User < ActiveRecord::Base
  has_many :pets
  
  # ...
end
```

**models/pet.rb**
```ruby
class Pet < ActiveRecord::Base
  belongs_to :user
end
```

Now try testing in the Rails console

```ruby
User.first.pets

User.first.pets.create(name: 'Fido')

Pet.all

Pet.first

Pet.first.user
```
