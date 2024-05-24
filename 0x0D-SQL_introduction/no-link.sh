#!/usr/bin/env bash
# This script executes an SQL query that list all records in the database.

if [ -z "$1" ];
then
	echo "Usage: $0 DATABASE_NAME"
	exit 1
fi

DATABASE_NAME=$1

read -sp "Enter your MySQL password: " PASSWORD
echo

echo "SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;" | mysql -hlocalhost -uroot -p"$PASSWORD" "$DATABASE_NAME"
