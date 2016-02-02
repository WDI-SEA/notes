![General Assembly Logo](http://i.imgur.com/ke8USTq.png)

# Test-Driven Development with Rspec

##Objectives

* Review the concepts behind TDD
* Setup rspec for running tests in Ruby
* Use a testing suite in the context of TDD

## Test-Driven Development (TDD)

Test-driven development (TDD) is a software development process that relies on the repetition of a very short development cycle: first the developer writes an (initially failing) automated test case that defines a desired improvement or new function, then produces the minimum amount of code to pass that test, and finally refactors the new code to acceptable standards. - [wiki](http://en.wikipedia.org/wiki/Test-driven_development)

## Process
1. Create / receive feature specification
2. Create test
3. Run tests (new test should fail)
4. Write code to try to make the test pass
5. Run tests (if fail return to step 4)
6. Refactor code if needed

## How to get started

Rspec is the testing framework we are going to be using for Ruby (including Rails). To get started:

```
gem install rspec
```

(you might have to `sudo` this depending on your machine settings)

Once you have successfully installed rspec, create a new project:

```
rspec --init 
# (this will create a .rspec and spec/spec_helper.rb file)
```

Inside your .rspec file make sure you have this text

```
--color
--require spec_helper
--format documentation
```

##Requiring files

###require
* This will load a ruby file ONCE and only once. All subsequent require statements will not reload the file.
* Doesn't need the .rb file extension, but won't hurt if it's there.

###require_relative
* Same as `require`, but will look for the file to require in the same directory

## Rspec matchers

```ruby
expect(actual).to be ___
expect(actual).to be_between(minimum, maximum).inclusive
expect(actual).to match(/expression/) # We will learn about this very soon!
expect(actual).to be true      # passes if actual == true
expect(actual).to be false     # passes if actual == false
expect(actual).to be_nil       # passes if actual is nil
expect(actual).to be_instance_of(Class)       # passes if actual is an instance of a certain Class
expect(actual).to exist        # passes if actual.exist? and/or actual.exists? are truthy
```

The rspec documentation is a great place to find more of these - you can find them [here](https://www.relishapp.com/rspec/rspec-expectations/v/3-1/docs/built-in-matchers)

### Writing your first test

Create a new file in the `spec` folder ending with `_spec`. In this example, we'll name our first test `tests_spec.rb`

Start with requiring `spec_helper`, then add a `describe` block, and inside an `it` statement as well

```ruby
require 'spec_helper'

describe "Some idea, variable or method" do
  it "is something or does something" do
    # expect...
  end
end
```

Let's start with some very simple tests

```ruby
describe "Random Tests" do
  it "should result in 5 equaling 5" do
    expect(5).to eq(5)
  end

  it "should result in 5 not equaling 3" do
    expect(5).to eq(3)
  end

  it "does something that is pending", pending: true do
    expect(5).to be < 3
  end

  xit "does something that is pending because we used xit" do
    expect(5).to be < 3 #this will be pending
  end
end
```

for more information see the [RSpec documentation](https://www.relishapp.com/rspec/rspec-core/docs/)

### I'm getting errors!

1. Make sure you have done `rspec --init` so that you have a .rspec file and a spec folder with a spec_helper.rb file
2. Did you mean to do `require_relative` instead of `require`?
3. If you do use `require_relative`, make sure you have the exact path



### Hooks

RSpec also supports before and after hooks which can be triggered before or after each example or once for the entire context (all things in a describe block). This is useful for doing things like initializing an instance of a class before testing it.

Here is a basic example using before

```ruby
describe Item do

  before(:context) do
    @item = Item.new("Generic Item",1.99)
  end

  describe "Initialization" do
    it "is an instance of the Item class" do
      expect(@item).to be_instance_of(Item)
    end
  end
end
```

More details [hooks in RSpec docs](https://www.relishapp.com/rspec/rspec-core/docs/hooks/before-and-after-hooks)