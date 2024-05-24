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

echo "INSERT INTO first_table (id, name) VALUES (89, 'Best School');" | mysql -hlocalhost -uroot -p"$PASSWORD" "$DATABASE_NAME"
