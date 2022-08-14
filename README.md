# FIIs
Personal project to control my FIIs.

For now this project has 10 APIs:
 - Create FII types (CRI, shopping, etc)
 - Delete FII types
 - List FII types
 - Create FIIs
 - Delete FIIs
 - List FIIs
 - Create FII dividends
 - Delete FII dividends
 - List all dividends
 - List dividends by FII


## To be developed
 - APIs to register the FIIs I bought
 - Web scrapping feature to get the monthly dividend value automatically
 - Automated tests


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

