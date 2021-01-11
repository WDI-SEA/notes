# CRUD & REST

## Objectives

* Name the HTTP Verb associated with each CRUD function

## Review CRUD

[Formal definition on wiki](http://en.wikipedia.org/wiki/Create,_read,_update_and_delete)

Recall CRUD from the SQL database lessons. Most sites you interact with on the internet are CRUD sites. Almost everything you do on the web is a CRUD action. For example:

* _**Create**_ a youtube user, a video, a comment, etc.
* _**Read**_ comments, view videos, etc.
* _**Update**_ your profile, edit a video title, etc.
* _**Delete**_ a video, comment, or an entire channel!

Come up with at four user interactions for each of the following apps that correspond to the CRUD actions:

* gmail
* tinder
* iOS clock (the built-in app that comes with the iPhone, skip if you're unfamiliar with it)
* craigslist


## RESTful Routing

On the web, the best practice for CRUD actions uses something called RESTful routing. The basic idea is your route \(URL pattern\) should relate to (a) the type of item you are interacting with, as well as (b) the action you'll be performing to change/view the state of the item\(s\). Instead of relying exclusively on the URL to indicate what webpage you want to go to \(and using just one method\), RESTful routing is a combination of HTTP Verbs and URLs. 

RESTful stands for **RE**presentational **S**tate **T**ransfer. It is a set of principles that provide a way of mapping HTTP Verbs _\(GET, POST, PUT, DELETE\)_ and CRUD actions together. When you click through a website by clicking on links, you're making a state transition which brings you to the next page \(the next _state_ of the application\). A RESTful route incorporates:

* the _item or data_ you're interacting with
* the _CRUD action_ you're performing on that item or data

### Example: Dinosaurs

So if you were CRUDing a database of dinosaurs, the following routes would form a full set of CRUD RESTful routes. There are seven main RESTful routes:

| VERB | URL pattern | Action \(CRUD\) | Description |
| :--- | :--- | :--- | :--- |
| GET | /dinosaurs | Index \(Read\) | lists all dinosaurs |
| GET | /dinosaurs/new | New \(Read\) | shows a form to make a new dinosaur |
| POST | /dinosaurs | Create \(Create\) | creates an dinosaur with the POST payload(form) data |
| GET | /dinosaurs/:id | Show \(Read\) | list information about a specific dinosaur \(i.e. /dinosaurs/1\) |
| GET | /dinosaurs/edit/:id | Edit \(Read\) | shows a form for editting a specific dinosaurs \(i.e. /dinosaurs/edit/1\) |
| PUT | /dinosaurs/:id | Update \(Update\) | updates the data for a specific dinosaur \(i.e. /dinosaurs/1\) |
| DELETE | /dinosaurs/:id | Destroy \(Delete\) | deletes the dinosaur with the specified id \(i.e. /dinosaurs/1\) |

_NOTE: With all of your POST, PUT, and DELETE routes, you'll want to add a redirect to a GET page_
_ALSO NOTE: POST and PUT actions require an initial GET action to get the forms that will receive the new data. Students sometimes forget that showing and new/edit form, for example, is a GET action because you are simply returning the html that presents a form for the user to enter data into. The POST/PUT part happens once the form has been submitted and doesn't have a correspondign HTML representation. This part is truly just backend code._

[Read more on wiki](http://en.wikipedia.org/wiki/Representational_state_transfer)
