#!/usr/bin/env bash
# This script updates the score of Bob to 10 in a database.

if [ -z "$1" ];
then
	echo "Usage: $0 DATABASE_NAME"
	exit 1
fi

DATABASE_NAME=$1

read -sp "Enter password: " PASSWORD
echo

echo "UPDATE second_table SET score = 10 WHERE name = 'Bob'" | mysql -hlocalhost -uroot -p"$PASSWORD" "$DATABASE_NAME"
