# Prehistoric Creatures Lab
---
## Prereqs:
* Layouts and Controllers
* CRUD/RESTful Routing in Express Lesson
* GET & POST lesson/code-along
--- 
For this lab, you're going to add a prehistoric creatures section to the `RESTful-creatures` app.
---

## 1. Add a `prehistoric_creatures.json` file to your `RESTful-creatures` directory. Give it the following data:
```javascript
[
  {
    "type":"giant beaver",
    "img_url":"http://www.beringia.com/sites/default/files/Giant-Beaver-banner.jpg"
  },
  {
    "type":"mastodon",
    "img_url":"https://cdn-images-1.medium.com/max/1200/1*a2VvYsKGApR-E1SnT5O7yQ.jpeg"
  },
  {
    "type":"saber-toothed salmon",
    "img_url":"https://cottagelife.com/wp-content/uploads/2014/11/Oncorhynchus_rastrosus.jpg"
  },
  {
    "type":"megalonyx",
    "img_url":"https://animalgeography.files.wordpress.com/2018/08/sloth-banner-e1535192925361.jpg?w=584&h=325"
  }
]
```


## 2. Create the following routes:

| VERB | URL | Action (CRUD) | Description |
|------|-----|---------------|-------------|
| GET | /prehistoric_creatures | Index (Read) | displays all prehistoric creatures |
| GET | /prehistoric_creatures/1 | Show (Read) | displays the type and photo of a particular prehistoric creature (id = 1) |
| GET | /prehistoric_creatures/new | New (Read) | shows a form for adding a new prehistoric creature |
| POST | /prehistoric_creatures | Create | creates an prehistoric creature with the POST payload data |

**Hint:** You will need to have two folders inside your `views` directory, one for `dinosaurs` and one for `prehistoric_creatures`. Make sure to change your `res.render()` statements accordingly! (Refer to the `love-it-or-leave-it` app from the Layouts and Controllers lesson.)

## 3. Reorganize your routes into controllers
(one controller for dinosaurs and one controller for prehistoric creatures)
