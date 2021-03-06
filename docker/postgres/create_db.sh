#!/bin/bash
set -e

POSTGRES="psql --username ${POSTGRES_USER}"

$POSTGRES <<EOSQL
CREATE DATABASE ${SSR_DATABASE} OWNER ${POSTGRES_USER};
EOSQL