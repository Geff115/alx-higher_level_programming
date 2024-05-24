#!/usr/bin/env bash
# This script list all records of the table in a SQL server

if [ -z "$1" ];
then
	echo "Usage: $0 DATABASE_NAME"
	exit 1
fi

DATABASE_NAME=$1

read -sp "Enter password: " PASSWORD
echo

echo "SELECT score, name FROM second_table ORDER BY score DESC" | mysql -hlocalhost -uroot -p"$PASSWORD" "$DATABASE_NAME"
