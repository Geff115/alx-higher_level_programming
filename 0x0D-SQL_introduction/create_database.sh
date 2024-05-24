#!/usr/bin/env bash
# This script creates the database hbtn_0c_0 in MySQL if it does not already exist.

read -sp "Enter MySQL password: " PASSWORD
echo

cat "CREATE DATABASE IF NOT EXISTS hbtn_0c_0;" | mysql -hlocalhost -uroot -p"$PASSWORD"

cat 0-list_databases.sql | mysql -hlocalhost -uroot -p"$PASSWORD"
