#OAuth with OmniAuth

## Objectives

* Review the concepts behind using OAuth
* Use a third-party gem in order to implement authentication strategies
* Use environment variables to hide sensitive data when implementing OmniAuth strategies


##Starter Code

This lesson uses starter code, provided here: https://github.com/WDI-SEA/oh-auth-example

##Review

For a review of OAuth, look back at our experience using OAuth with Passport in Express

![OAuth from Oracle](https://docs.oracle.com/cd/E50612_01/doc.11122/oauth_guide/content/images/oauth/oauth_overview.png)

##Setting Up OAuth

In this example, a sample application is setup for you, with a main controller and an index page. Look at the structure of the application and **understand the components.**

Now, we're going to setup the user model we'll need for this app.

###Generate the user model

```
rails g model user provider provider_id provider_hash email name
```

* `provider_hash` - the hash we get from the OAuth provider (such as Facebook, Twitter, etc.)
* `provider` and `provider_id` - the Oauth provider name and id we're using

Note that in this example, we're only providing OAuth for one provider. If we wanted to support multiple providers, we would need a separate `provider` model with a one-to-many association with the user.

###Create the database and table

```
rake db:create
rake db:migrate
```

###Quickly test your model

Make sure your user can be queried.

```rb
rails c
User.all
```

####Add OmniAuth

Similar to how Passport had a core package and different "strategies" to implement, Rails has a gem called OmniAuth with different strategies to implement. Note that in this case, OmniAuth is used as middleware. So let's install the gems we need!

We'll be adding OAuth with Facebook, so in Gemfile, add `omniauth` and the strategy gem for each oauth provider you want to support. [Full list of supported strategies](https://github.com/intridea/omniauth/wiki/List-of-Strategies).

**Gemfile**

```rb
gem 'omniauth'
gem 'omniauth-facebook'
```

After updating the Gemfile, remember to run `bundle`.

###Init OmniAuth

Create a new file in config folder of the Rails application called `omniauth.rb`

```
config/initializers/omniauth.rb
```

Add an initializer for each strategy/provider you want to support.

```rb
Rails.application.config.middleware.use OmniAuth::Builder do
  provider :facebook, ENV['FACEBOOK_KEY'], ENV['FACEBOOK_SECRET']
end
```

Any additional providers would go under the `OmniAuth::Builder` block.

##Create apps with providers

Now you need to go to Facebook and create an app. This will allow you to get the key/secret for each service which you can set in your environment variable. When using Facebook, don't forget to set the **Site URL** in settings as `http://localhost:3000`

Again, the workflow for including keys/secrets:
* store keys locally in a `.env` file.
* Run your app using `foreman run rails s`
* access keys via the `ENV` array (for example, `ENV['FACEBOOK_KEY']`)

**NOTE:** remember to add `.env` to your `.gitignore` file to avoid exposing your keys on github.

**Quicklinks for API key creation**

* [Facebook](https://developers.facebook.com/apps/)
* [Twitter](https://apps.twitter.com/)
* [Google](https://console.developers.google.com/project)

###Create auth routes

Like many things in rails OmniAuth uses convention over configuration so it has pre-defined routes that you are expected to use.

* `/auth/:provider`
  * login route, created for us, redirects user to the appropriate provider.
* `/auth/failure`
  * user is sent here on authentication failure
* `/auth/:provider/callback`
  * callback url. This is where the user is redirected after they come back from the provider.

Let's set these routes up.

**add to `config/routes.rb`**

```rb
get 'auth/logout' => 'auth#logout'
get 'auth/failure' => 'auth#failure'
get 'auth/:provider/callback' => 'auth#callback'
```

Now that we have routes, we can create the `auth` controller and start implementing the `callback`, `logout`, and `failure` controller actions. Also, we don't have to implement the `/auth/:provider` route explictly, because OmniAuth does that for us.

Note that since we're still using session authentication, the logout method be nearly the same. The failure method, for now, will just render an error message as text. Therefore, we really need to worry about the implementation of the `callback` method.

###Callback method

The callback method will perform the following operation:

* Obtain the provider information from Facebook
* Find or create a user with the provider and provider id
  * Add the name, email, and hash of the user (the hash being the token from the provider user)
* Create a session (same as before)
* Redirect


```rb
class AuthController < ApplicationController

  def callback
    provider_user = request.env['omniauth.auth']

    #find create a user
    user = User.find_or_create_by(provider_id: provider_user['uid'], provider: params[:provider]) do |u|
      u.provider_hash = provider_user['credentials']['token']
      u.name = provider_user['info']['name']
      u.email = provider_user['info']['email']
    end

    session[:user_id] = user.id
    redirect_to root_path
  end

  def logout
    session[:user_id] = nil
    redirect_to root_path
  end

  def failure
    #TODO: display error page
    render plain: "this is a failure"
  end

end
```

> [What is request.env?](http://blogofchirag.blogspot.com/2008/09/variables-in-request-env-ruby-on-rails.html)

Lastly, make sure to setup your `@current_user` variable inside the `ApplicationController`. We included a `before_action` for you.

```rb
class ApplicationController < ActionController::Base
  # Prevent CSRF attacks by raising an exception.
  # For APIs, you may want to use :null_session instead.
  protect_from_forgery with: :exception

  def current_user
    @current_user ||= User.find_by_id(session[:user_id])
  end
end
```

Now test your code and verify that you can login.

##Conclusion

Adding OAuth via OmniAuth to your application is similar to implementing Passport with Express. A summary of the steps we took:

* Create a user model with the provider attributes
* Add the OmniAuth middleware and strategies
* Configure API keys (if necessary)
* Define routes and controller methods
* Apply a before_action to make the current user available on specific pages
