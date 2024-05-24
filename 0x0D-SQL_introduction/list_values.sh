#!/usr/bin/env bash
# This script list all rows in the table first_table in a MySQL database

if [ -z "$1" ];
then
	echo "Usage: $0 <database_name>"
	exit 1
fi

DTABASE_NAME=$1

read -sp "Enter MySQL password: " PASSWORD
echo

echo "SELECT * FROM first_table;" | mysql -hlocalhost -uroot -p"$PASSWORD" "$DATABASE_NAME"
