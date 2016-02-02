![General Assembly Logo](http://i.imgur.com/ke8USTq.png)

#Static Sites with Jekyll

##Objectives

* Identify and apply different frameworks to different problems
* Compare and contrast full-stack web applications with static site generators
* Identify the various components that are incorporated by Jekyll
* Use Jekyll to create a portfolio/blog

##Choosing Frameworks

So far, we've utilized various different frontend and backend frameworks. Why so many? Why can't there be just one?

Each framework has its benefits and drawbacks, and it's your job as a developer to choose the framework that's right for the job.

**Think about it:** What are some cases where we'd want to use Rails over Express? How about something unfamiliar, like Wordpress, over Express?

##Static Site Generators

[What is a Static Website?](http://nilclass.com/courses/what-is-a-static-website)

Fairly often, the dynamic complexity of Rails or Express may be overkill for the project at hand. For example, most blogs and portfolios at a small scale do not **need** a database. In these cases, we can use static site generators.

Static site generators are frameworks that take content, usually in the form of text/markup, pass the content to a template engine, then render HTML pages for viewing.

We'll be using **Jekyll** to create a static portfolio/blog. Jekyll uses **Markdown** and the **Liquid** template engine, along with HTML/CSS/JavaScript, in order to generate a static site.

Markdown -> Liquid (templating) + HTML + CSS + JS -> HTML pages

##Setting up and Using Jekyll

[Jekyll Home Page](http://jekyllrb.com/)

To get started with jekyll, install it as a gem.

```
gem install jekyll
```

To create a new site, run the `jekyll new` command.

```
jekyll new my-portfolio
```

**Note:** If you happen to get an error that says `uninitialized constant Psych::Nodes (NameError)`, run `gem clean`, then try creating the site again.

`cd` into the new directory created, and you'll see some files and folders that Jekyll pre-built for you.

###Folders

* `_includes` - Liquid partials, such as headers and footers
* `_layouts` - page layouts that utilize partials from `_includes`. Jekyll can utilize many different layouts, which is handy for displaying different content
* `_posts` - Jekyll is used often for blogging, so this folder provides some organization for your content. These files are written in Markdown and contain metadata at the top of each file, written in YAML, known as **front matter**
* `_sass` - Jekyll supports SASS out-of-the-box, so add SASS files here
* `_css` - Contains the main SASS file, which contains any variables and imports files from the `_sass` folder


###Files

* `.gitignore`
* `_config.yml` - this configuration file is YAML markup with site-wide settings, such as the name, email, description, URL, and other data
* `about.md, index.html` - by default, Jekyll provides two pages. The first one is a Markdown file, and the second one is a HTML file. Note that you can use either extension for your blog, depending on if your content is raw HTML or Markdown. Each file will contain front matter that specifies the layout and other settings.

When you serve your site, Jekyll takes all these files, parses them as necessary, and renders a bunch of pages. The layouts/includes files serve as templates, while the Markdown/HTML uses these templates and injects the content.

###Serving the site

To serve the site, run
```
jekyll serve
```

Jekyll will create a new folder called `_site` and host your site at `localhost:4000`. Any file changes, with the exception of configuration files, will prompt Jekyll to regenerate the folder.

###Configuring and Editing Jekyll

Jekyll contains various filters and tags that you can use to customize your site. The ones you'll find to be most handy:

####Accessing posts

```liquid
{% for post in site.posts %}

{{ post.title }}
{{ post.date }}
{{ post.content }}

{% endfor %}
```

Notice that `title` and `date` are in the front matter for the post! This means you can include other variables in the front matter (such as image paths, categories, tags, etc.)

####Accessing Site Variables

```liquid

{{ site.title }}

{{ site.url }}

{{ site.github_username }}

{{ site.posts }}

{{ site.pages }}
```

Again, notice that some of these variables have an explicit location (`config.yml`), and you can define your own variables.

####Including partials in a layout

```liquid
{% include header.html %}

{% include footer.html %}
```

Out-of-the-box, Jekyll has some other fun features, like RSS feed support and built-in code highlighting! For more information on the various liquid tags and filters used in templates, check out the [documentation](http://jekyllrb.com/docs/templates/).

##Deploying

The benefit of having a static site is less configuration during deployment, since it's just static files (no database or other tasks).

It's even easier because Github supports Jekyll (Github was co-founded by Tom Preston-Werner, creator of Jekyll). Deploying your Jekyll site to Github will allow for instant hosting.

To host a portfolio or blog, you can name the repository `yourgithubusername.github.io` and push the site to the `master` branch.

[Using Jekyll with Github Pages](https://help.github.com/articles/using-jekyll-with-pages/)

##Other Options

* [Jekyll Themes](https://github.com/jekyll/jekyll/wiki/Themes)
* [Other Jekyll Themes](http://jekyllthemes.org/)
* [Jekyll Bootstrap](http://jekyllbootstrap.com/)

