#!/usr/bin/env bash
# This script executes a MySQL query that removes scores that are less or equal to 5.

if [ -z "$1" ];
then
	echo "Usage: $0 DATABASE_NAME"
	exit 1
fi

DATABASE_NAME=$1

read -sp "Enter MySQL password: " PASSWORD
echo

echo "DELETE FROM second_table WHERE score <= 5" | mysql -hlocalhost -uroot -p"$PASSWORD" "$DATABASE_NAME"
