#!/usr/bin/env bash
# This script connects displays the number of records of id=89 in a table first_table of MySQL database.

if [ -z "$1" ];
then
	echo "Usage: $0 DATABASE_NAME"
	exit 1
fi

DATABASE_NAME=$1

read -sp "Enter password: " PASSWORD
echo

echo "SELECT COUNT(*) FROM first_table WHERE id = 89;" | mysql -hlocalhost -uroot -p "$PASSWORD" "$DATABASE_NAME"
