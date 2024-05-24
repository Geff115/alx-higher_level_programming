#!/usr/bin/env bash
# This script list all tables in a specified MySQL database.

if [ -z "$1" ];
then
	echo "Usage: $0 <database_name>"
	exit 1
fi

DATABASE_NAME=$1

read -sp "Enter MySQL password: " PASSWORD
echo

echo "SHOW TABLES;" | mysql -hlocalhost -uroot -p"$PASSWORD" "$DATABASE_NAME"
