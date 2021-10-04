# User Stories and Wireframing

## Agile Development, Wireframes, and User Stories

#### Objectives

* Explain the basics of Agile methods and why it's used
* Describe user stories and how they are different than to-dos
* Practice creating user stories for an example app

## Agile Development, Wireframes, and User Stories

### Agile and Waterfall

**Waterfall**

_The waterfall model is a sequential design process, used in software development processes, in which progress is seen as flowing steadily downwards \(like a waterfall\) through the phases of Conception, Initiation, Analysis, Design, Construction, Testing, Production/Implementation and Maintenance._- [Wikipedia](http://en.wikipedia.org/wiki/Waterfall_model)

![Waterfall model](https://i.imgur.com/yJMVO91.png)

Waterfall is a good example of a linear methodology. It has it's own benefits:

* simple, easy to understand and use.
* easy to manage due to the rigidity of the model -- each phase has specific deliverables and a review process
* phases are processed, completed one at a time, and do not overlap
* works well for smaller projects where requirements are very well understood

However, other methodologies have evolved as the need for greater flexibility has arisen.

**Agile**

_Agile software development is a group of software development methods in which requirements and solutions evolve through collaboration between self-organizing, cross-functional teams. It promotes adaptive planning, evolutionary development, early delivery, continuous improvement, and encourages rapid and flexible response to change_- [Wikipedia](http://en.wikipedia.org/wiki/Agile_software_development)

**The Agile Manifesto**

This was a formal "proclamation" of key values and principles for approaching software development that was put together in 2001. The four key concepts value:

* **Individuals and interactions over processes and tools:** self-organization and motivation are important, as are interactions like co-location and pair programming
* **Working software over comprehensive documentation:** working software is more useful and welcome than just presenting documents to clients in meetings
* **Customer collaboration over contract negotiation:** requirements cannot be fully collected at the beginning of the software development cycle, therefore continuous customer or stakeholder involvement is very important
* **Responding to change over following a plan:** agile methods are focused on quick responses to change and continuous development

However, keep in mind that _not all of these values are beneficial for all projects_. For example, freelancers will usually want a set plan and contract in place in order to prevent **scope creep**.

The core principles of agile development remain the same:

* Iterative, incremental and evolutionary
* Efficient and face-to-face communication
* Very short feedback loop and adaptation cycle
* Quality focus
* Adaptive over predictive
* Iterative over waterfall
* Code over documentation

**Agile practices**

_Agile development is supported by a bundle of concrete practices suggested by the agile methods, covering areas like requirements, design, modeling, coding, testing, project management, process, quality, etc. Some notable agile practices include_ - Wiki

### Agile practices

* **Test-driven development** \(TDD\) is a software development process that relies on the repetition of a very short development cycle: first the developer writes an \(initially failing\) automated test case that defines a desired improvement or new function, then produces the minimum amount of code to pass that test, and finally refactors the new code to acceptable standards.
* **Continuous integration** \(CI\) is the practice of merging all developer working copies with a shared mainline several times a day. It was adopted as part of extreme programming \(XP\), which did advocate integrating more than once per day, perhaps as many as tens of times per day. The main aim of CI is to prevent integration problems, referred to as "integration hell" in early descriptions of XP. CI isn't universally accepted as an improvement over frequent integration, so it is important to distinguish between the two as there is disagreement about the virtues of each. During WDI we will look at [Travis CI](https://travis-ci.com/) as an example of Continuous Integration.
* **Information radiators** is a generic term for any handwritten, drawn, printed or electronic displays that a team places in a highly visible location to track progress or metrics. Examples include scrum board, task board, or a burndown chart.
* **Pair programming** \(sometimes referred to as peer programming\) is an agile software development technique in which two programmers work as a pair together on one workstation. One, the driver, writes code while the other, the observer, pointer or navigator, reviews each line of code as it is typed in. The two programmers switch roles frequently.
* **Refactoring** is the process of restructuring existing computer code -- changing the factoring -- without changing its external behavior. Refactoring improves nonfunctional attributes of the software.
* **Scrum meetings** are short meetings used to plan, review, and increase accountability and clarity across a team. Examples include sprint planning, daily scrum, sprint review and retrospective, and **STAND UPS**.
* **User personas** are used in user-centered design and marketing. They can be described as fictional characters created to represent the different user types that might use a site, brand, or product in a similar way. Marketers may use personas together with market segmentation, where the qualitative personas are constructed to be representative of specific segments.
* **User story** is a description consisting of one or more sentences in the everyday or business language of the end user or user of a system that captures what a user does or needs to do as part of his or her job function. User stories are used with agile software development methodologies as the basis for defining the functions a business system must provide, and to facilitate requirements management. It captures the 'who', 'what' and 'why' of a requirement in a simple, concise way, often limited in detail by what can be hand-written on a small paper notecard.
* **Wireframes** A website wireframe, also known as a **page schematic** or **screen blueprint**, is a visual guide that represents the **skeletal framework** of a **website**.

### Wireframes

_A website wireframe, also known as a **page schematic** or **screen blueprint**, is a visual guide that represents the **skeletal framework** of a **website**._ - Wikipedia

\[...continued...\] **Wireframes** are created for the purpose of arranging elements to best accomplish a particular purpose. The purpose is usually being informed by a business objective and a creative idea. The wireframe depicts the **page layout** or **arrangement** of the website's **content**, including **interface elements** and **navigational systems**, and how they work together. The wireframe usually lacks typographic style, color, or graphics, since the main focus lies in **functionality**, behavior, and priority of content.

The key points to get across when creating a wireframe are:

* Information design
* Navigation design
* Interface design

**An example of a wireframe**

Let's look at the difference between YouTube's page for a particular video and how a wireframe compares:

![Youtube Balsamiq](http://3.bp.blogspot.com/-8e_J8hkX_kM/TbSz0jywljI/AAAAAAAAAY4/Nei-hnfPGaI/s1600/Balsamiq+myTube+example.jpg)

![Youtube actual](https://make.wordpress.org/support/wp-content/blogs.dir/21/files/2012/10/embed-youtube-page.jpg)

Wireframes focus on:

* The range of functions available
* The relative priorities of the information and functions
* The rules for displaying certain kinds of information
* The effect of different scenarios on the display

**Useful wireframing tools**

* [draw.io](http://www.draw.io)
* [balsamiq.com](http://www.balsamiq.com)
* [InvisionApp](http://www.invisionapp.com/)
* [MarvelApp](https://marvelapp.com/)
* Writing utensils \(markers, pens, pencils\)

### User Stories

Once you have constructed User Personas, to better understand your Users, you must construct User stories to identify each pathway they may want to take through your app or website.

User stories exist in different formats, but this is one that works quite well:

_As a **\[role\]**, I want to **\[goal\]** so I can **\[benefit/purpose\]**_

For example:

* _As a user, I want to read reviews of a selected book to help me decide whether to buy \*\*_
* _As an admin, I want to update the inventory of a selected book so my users know what is available.\*\*_

### Conclusion

* Describe agile development.
* Compare agile development to waterfall development.
* What are users stories and why are they used?
* What are wireframes and why are they used?

