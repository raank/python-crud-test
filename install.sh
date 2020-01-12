#!/bin/bash

cp ./database/database.db.example ./database/database.db

virtualenv .venv
./.venv/bin/pip3 install -r requirements.txt
./.venv/bin/alembic upgrade head
./.venv/bin/alembic history --verbose