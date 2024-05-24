#!/usr/bin/env bash
# This script creates a table first_table in a MySQL server.

if [ -z "$1" ];
then
	echo "Usage: $0 <database_name>"
	exit 1
fi

DATABASE_NAME = $1

read -sp "Enter MySQL password: " PASSWORD
echo

echo "CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));" | mysql -hlocalhost -uroot -p"$PASSWORD" "$DATABASE_NAME"
