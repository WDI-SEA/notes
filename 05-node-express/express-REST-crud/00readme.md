# CRUD in Express

## Objectives

* Name the HTTP Verb associated with each CRUD function

## Review CRUD

Recall CRUD from the SQL database lessons. Most sites you interact with on the internet are CRUD sites. Almost everything you do on the web is a CRUD action. For example:
* ***Create*** a youtubeuser, a video, a comment
* ***Read*** comments, view videos, etc.
* ***Update*** your profile, edit a video title, etc.
* ***Delete*** a video, comment, or an entire channel!

[Formal definition on wiki](http://en.wikipedia.org/wiki/Create,_read,_update_and_delete)

## RESTful Routing

RESTful Routing is the (best) practice of choosing routes (URL patterns + HTTP verbs) that reflect the CRUD functionality of that route.
A RESTful route incorporates:
* the _item or data_ you're interacting with
* the _CRUD action_ you're performing on that item or data

On the web the best practice for CRUD actions uses something called RESTful routing. The basic idea is your route (URL) should relate to the type of item you are interacting with, as well as the action you'll be performing to change/view the state of the item(s).

### Example: Dinosaurs
So if you were CRUDing a database of dinosaurs, the following routes would form a full set of CRUD RESTful routes

| VERB | URL | Action (CRUD) | Description |
|------|-----|---------------|-------------|
| GET | /dinosaurs | Index (Read) | lists all dinosaurs |
| GET | /dinosaurs/1 | Show (Read) | list information about a specific dinosaur (id = 1) |
| POST | /dinosaurs | Create | creates an dinosaur with the POST payload data |
| GET | /dinosaurs/edit/1 | Show(Read) | form for editting a specific dinosaurs (id = 1)|
| PUT | /dinosaurs/1 | Update | updates the data for a specific dinosaur (id = 1) |
| DELETE | /dinosaurs/1 | Delete (Destroy) | deletes the dinosaur with the specified id (1) |

[Read more on wiki](http://en.wikipedia.org/wiki/Representational_state_transfer)