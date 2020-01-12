#!/bin/bash

cp ./database/database.db.example ./database/database.db
cp .env.dist .env

virtualenv .venv
./.venv/bin/pip3 install -r requirements.txt
./.venv/bin/alembic upgrade head
./.venv/bin/alembic history --verbose

cp ./database/database.db ./database/tests.db

source ./.venv/bin/activate