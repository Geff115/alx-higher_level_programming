#!/usr/bin/env bash
# This script deletes the database hbtn_0c_0 if it exists.

read -sp "Enter MySQL password: " PASSWORD
echo

cat 2-delete_database_if_exists.sql | mysql -hlocalhost -uroot -p"$PASSWORD"
