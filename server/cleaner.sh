#!/bin/bash

rm -rf $(find . -path ./env -prune -false -o -name "__pycache__")
rm -rf $(find . -path ./env -prune -false -o -name "migrations")