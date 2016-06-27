#Many to Many Associations

##Objectives

* Implement many to many relationships through models in Rails
* Understand the model ordering opinion used by Rails
* Use the `collection_check_boxes` form helper to display a collection of associated items

Today we'll add tags to the bog app using a many to many relationship.

## Review: Relationships

![Database relationships](http://fms-itskills.ncl.ac.uk/db/ER.png)

##What we need

* Models
  * Tag
  * Creature
  * Creatures_Tags (join table)
* Association
  * tag <-> creatures_tags <-> creature
  * creature `has_and_belongs_to_many` tags
  * tag `has_and_belongs_to_many` creatures
* Views
  * creatures#edit - add/remove tags checkboxes
  * creatures#new - add/remove tags checkboxes
  * tag#show
    * list all creatures with a specific tag

##Generating models

Review of **Creatures**

```
rails g model creature name description:text
```

**Tags**

```
rails g model tag name
```

**Creatures_Tags**

```
rails g model creatures_tags creature:references tag:references --force-plural
```

# IMPORTANT
The join table with the two models **must** be plural and in alphabetical order if you want to follow the Rails convention. Also, `--force-plural` is needed so that the table will never be pluralized.

Note that if you want to name your join table something different, you can specify your own join model with `through:`

##Setting up associations

When you do `:references` it automatically creates the `belongs_to` relations on the join table (creatures_tags), but we need to manually add the `has_and_belongs_to_many` to the tag and creature models.

**models/creature.rb**

```ruby
has_and_belongs_to_many :tags
```

**models/tag.rb**

```ruby
has_and_belongs_to_many :creatures
```

#ALSO IMPORTANT
When creating the M:M associations, the name of the model is pluralized when adding the `has_and_belongs_to_many` method. In CreaturesTags, the associations will be singular and generated for you.

##Adding tags

```ruby
# assume the following:
creature = Creature.first
tag = Tag.first

# adding a tag
creature.tags << tag
```

##Removing tags

```ruby
# assume the following:
creature = Creature.first
tag = Tag.first

# clear all of the creature's tags (leaves the tags in the table)
creature.tags.clear

# removes a specific tag from a creature (leaves the tag in the table)
c.tags.delete(tag)

# removes a specific tag from a creature (and deletes the tag)
c.tags.first.destroy
```


##Referencing and listing

Because creature and tag reference each other with `has_and_belongs_to_many` they can reference each other.

**Basic Examples**

```ruby
#lists all tags
Tag.all

#lists all creatures
Creature.all

#gets first creature in the database
Creature.first

#lists all tags of first creature
Creature.first.tags

#lists all creatures of first tag
Tag.first.creatures
```

**Advanced Examples / chaining**

```ruby
#All creatures of the first tag of the first creature
Creature.first.tags.first.creatures
```

## creatures#new and creatures#edit

* Add checkboxes to the form
```erb
<%= c.collection_check_boxes :tag_ids, @tags, :id, :name %>
```

1. `:tag_ids` refers to the model's tags
2. `@tags` refers to all the tags available (pass from the controller `Tag.all`)
3. `:id` refers to the value of the checkbox
4. `:name` refers to the label of the checkbox

That's it! As far as assigning the tags in the controller, we can modify the `Creature` model to accept the `tag_ids` array like so:

```ruby
def creature_params
  params.require(:creature).permit(:name, :description, :tag_ids => [])
end
```

In order for the tags to be assigned automatically, we can add the `accepts_nested_attributes_for` method to the `Creature` model. You'll also want to add `inverse_of:` to the creature's tag association, in order to run any validations that may be on the `Tag` model.

```ruby
class Creature < ActiveRecord::Base
  has_and_belongs_to_many :tags, inverse_of: :creature
  accepts_nested_attributes_for :tags
end
```

## tag#show

When showing a specific tag, display the tag name and the list of creatures
associated with it.
