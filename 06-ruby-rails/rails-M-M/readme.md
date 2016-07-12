#Many to Many Associations

##Objectives

* Implement many to many relationships through models in Rails
* Understand the model ordering opinion used by Rails
* Use the `collection_check_boxes` form helper to display a collection of associated items

Today we'll add rangers to the national park app using a many to many relationship.

## Review: Relationships

![Database relationships](http://fms-itskills.ncl.ac.uk/db/ER.png)

##What we need

* Models
  * Park
  * Ranger
  * ParksRangers (join table)
* Association
  * Park <-> ParksRangers <-> Ranger
  * Park `has_and_belongs_to_many` Rangers
  * Ranger `has_and_belongs_to_many` Parks
* Views
  * parks#edit - add/remove rangers checkboxes
  * parks#new - add/remove rangers checkboxes
  * rangers#show
    * list all parks with a specific ranger

##Generating models

Review of **Parks**

```
rails g model park name description:text picture:text
```

**Rangers**

```
rails g model ranger name
```

**ParksRangers**

```
rails g model parks_rangers park:references ranger:references --force-plural
```

# IMPORTANT
The join table with the two models **must** be plural and in alphabetical order if you want to follow the Rails convention. Also, `--force-plural` is needed so that the table will never be pluralized.

Note that if you want to name your join table something different, you can specify your own join model with `through:`

##Setting up associations

When you do `:references` it automatically creates the `belongs_to` relations on the join table, but we need to manually add the `has_and_belongs_to_many` to the ranger and park models.

**models/park.rb**

```ruby
has_and_belongs_to_many :rangers
```

**models/ranger.rb**

```ruby
has_and_belongs_to_many :parks
```

#ALSO IMPORTANT
When creating the M:M associations, the name of the model is pluralized when adding the `has_and_belongs_to_many` method. In ParksRangers, the associations will be singular and generated for you.

##Adding rangers

```ruby
# assume the following:
park = Park.first
ranger = Ranger.first

# adding a ranger
park.rangers << ranger
```

##Removing rangers

```ruby
# assume the following:
park = Park.first
ranger = Ranger.first

# clear all of the park's rangers (leaves the rangers in the table)
park.rangers.clear

# removes a specific ranger from a park (leaves the ranger in the table)
c.rangers.delete(ranger)

# removes a specific ranger from a park (and deletes the ranger)
c.rangers.first.destroy
```


##Referencing and listing

Because Park and Ranger reference each other with `has_and_belongs_to_many` they can reference each other.

**Basic Examples**

```ruby
#lists all rangers
Ranger.all

#lists all parks
Park.all

#gets first park in the database
Park.first

#lists all rangers of first park
Park.first.rangers

#lists all parks of first ranger
Ranger.first.parks
```

**Advanced Examples / chaining**

```ruby
#All parks of the first ranger of the first park
Park.first.rangers.first.parks
```

## parks#new and parks#edit

* Add checkboxes to the form
```erb
<%= c.collection_check_boxes :ranger_ids, @rangers, :id, :name %>
```

1. `:ranger_ids` refers to the model's rangers
2. `@rangers` refers to all the rangers available (pass from the controller `Ranger.all`)
3. `:id` refers to the value of the checkbox
4. `:name` refers to the label of the checkbox

That's it! As far as assigning the rangers in the controller, we can modify the `Park` model to accept the `ranger_ids` array like so:

```ruby
def park_params
  params.require(:park).permit(:name, :description, :ranger_ids => [])
end
```

In order for the rangers to be assigned automatically, we can add the `accepts_nested_attributes_for` method to the `Park` model. You'll also want to add `inverse_of:` to the park's ranger association, in order to run any validations that may be on the `Ranger` model.

```ruby
class Park < ActiveRecord::Base
  has_and_belongs_to_many :rangers, inverse_of: :park
  accepts_nested_attributes_for :rangers
end
```

## rangers#show

When showing a specific ranger, display the ranger name and the list of parks associated with it.
