# Welcome to Home Sweet Home

## After forking to your github:
* Clone down to your machine
* git remote -v to check remote connections
* git remote add link  'link' should be the primary repo that you forked(in this case my repo).
* git remote -v again to verify upstream connection
* now you may git pull upstream master, to get the latest version of the master project
* Create a postgresql database called hsh
* Perform migrations:
  * python3 manage.py makemigrations
  * python3 manage.py migrate
* Start the server:
  * python3 manage.py runserver

## Create code for the project
* Remember to work on a different branch then your main
* When you are ready to push, push to the branch you are working on
* Then go to github and do a pull request from your branch to your master branch
* If that goes well see below

## When you are ready to create pull request:
* Push to your github
* Login to your github and create a pull request from your develpment branch to your master branch
* After that create a pull request from your master branch to my test branch
* Send me a text and I will accept your pull request and if the app still works, I will create a pull request from test to master and accept it
* Then I will send a message out, so everyone can pull from the master(git pull upstream master)
* When you are ready to pull down from the master, make sure you are on your master branch first then git pull upstream master.
* Now your local master will be current, but not your development branch or your github master
* Still in your master branch, git add, git commit, git commit.  This will get your github master current with the project master.
* At this point I would push your development branch to github and then go to github and create a pull request to your github master.  Resolve any conflicts and now you can continue developing.


# Home-Sweet-Home

## Introduction

We don't want you to spend hours looking at every 3 bedroom 2 bath house in your area. We want to give you the options you want to narrow your search down to the home you want.Find properties, agents, and more at Home-Sweet-Home!

<!-- ![Example View]() -->

### Deployed Link:
[Home-Sweet-Home--Deployed-Link]()

## Technologies

- HTML
- CSS
- Materialize
- Python
- Django
- Postgres
- Github
- Trello
- Lucid Charts

## Planning
[Pitch-Powerpoint] (https://docs.google.com/presentation/d/180JjYcUhAP_-SmbumdZI_I5g_1irsdCdole1WPfydo0/edit#slide=id.g7bb1c307cf_0_463)

[Model ERD](https://www.lucidchart.com/documents/edit/1a9b60ca-7426-4a62-8ae2-8f7cfb963f92/0_0?shared=true)

[Trello Board](https://trello.com/b/8IvZxO65/project-3-app)


##Ice Box
- ???