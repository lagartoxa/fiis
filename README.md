# fiis
Personal project to control my FIIs

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
./install.sh

Note: The install.sh script and every script from the scripts
directory must be executed from the project's directory.


## Managing Database Tables And Migrations

No need to run those commands if you ran ./install.sh .

Note: Those commands are only examples. Any Alembic parameters
can be used with the alembic.sh script


### Creating a New Migration
./scripts/alembic.sh revision --autogenerate -m "XXX - Migration's
description, where XXX is the number of the version with 3 numbers"


### Upgrading To The Last Migration
./scripts/alembic.sh upgrade head

