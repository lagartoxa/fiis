# FIIs
Personal project to control my FIIs.

This project has APIs to create, list and delete (sorry, no update APIs yet):
 - FIIs
 - FII types
 - FII daily quotations
 - FII monthly dividends
 - Register FII purchases

You can see them at http://localhost:8000/docs


## To be Developed
 - Web scrapping feature to get the monthly dividend value automatically
 - Cycles to automatically get daily quotations
 - APIs to update the data in the database
 - Automated tests


# How to Run
Follow the instructions in the Installation section, then start the backend
by running:

```
$ run_backend.sh
```

You can see the available APIs by openning http://localhost:8000/docs
on your browser

# Installation

## Database
First create a user project with password project and grant
all privileges to him, for the fiis database:

```
$ psql -h localhost -U YOUR_ADMIN_DB_USER -d postgres
postgres=# CREATE DATABASE fiis;
postgres=# GRANT ALL PRIVILEGES ON DATABASE fiis TO project;
```


## Install And Configure The Backend
```
$ ./install.sh
```

Note: The install.sh script and every script from the scripts
directory must be executed from the project's directory.


## Managing Database Tables And Migrations
No need to run those commands if you ran ./install.sh .

Note: Those commands are only examples. Any Alembic parameters
can be used with the alembic.sh script


### Creating a New Migration
```
$ ./scripts/alembic.sh revision --autogenerate -m "XXX - Migration's
description, where XXX is the number of the version with 3 numbers"
```


### Upgrading To The Last Migration
```
$ ./scripts/alembic.sh upgrade head
```


# Developing

## Front End
I plan to code some front end for this project, but this won't happen any time soon


## Database
At backend/db/repositories you can find the Repositories for all the database tables
and also the base repository, class from which every repository inherits. Please
don't create queries outside the repositories directory.


## Code Location
 - Routers: backend/app/routers
 - Schemas: backend/app/db/schemas
 - Database Tables: backend/app/db/models
 - Database Repositories: backend/app/db/repositories
 - Scripts: scripts (installation and alembic scripts)

