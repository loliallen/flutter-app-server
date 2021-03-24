#!/bin/bash

rm -rf $(find . -path ./env -prune -false -o -name "*pycache*")
rm -rf $(find . -path ./env -prune -false -o -name "migrations")