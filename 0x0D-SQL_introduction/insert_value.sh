#!/usr/bin/env bash
# This script inserts into the rows of a table first_table in a MySQL database;

if [ -z "$1" ];
then
	echo "Usage: $0 <database_name>"
	exit 1
fi

DATABASE_NAME=$1

read -sp "Enter MySQL password: " PASSWORD
echo

cat 7-insert_value.sql | mysql -hlocalhost -uroot -p"$PASSWORD" "$DATABASE_NAME"

cat 6-list_values.sql | mysql -hlocalhost -uroot -p"$PASSWORD" "$DATABASE_NAME"
