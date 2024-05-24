#!/usr/bin/env bash
# This script prints the full description of the table first_table in a MySQL server.

if [ -z "$1" ];
then
	echo "Usage: $0 <database_name>"
	exit 1
fi

DATABASE_NAME=$1

read -sp "Enter MySQL password: " PASSWORD
echo

echo "SHOW CREATE TABLE first_table;" | mysql -hlocalhost -uroot -p"$PASSWORD" "$DATABASE_NAME"
