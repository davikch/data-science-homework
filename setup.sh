#!/bin/bash

docker compose -f compose.yaml -f compose.redash.yaml build
docker compose -f compose.redash.yaml run --rm server create_db
