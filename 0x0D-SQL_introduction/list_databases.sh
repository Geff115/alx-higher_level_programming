#!/usr/bin/env bash
# This script pipes the content of 0-list_databases.sql to MySQL.

read -sp "Enter MySQL password: " PASSWORD
echo

cat 0-list_databases.sql | mysql -hlocalhost -uroot -p"$PASSWORD"
