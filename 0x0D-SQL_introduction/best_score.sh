#!/usr/bin/env bash
# This script list all scores in a MySQL database that are greater than or equal to 10.

if [ -z "$1" ];
then
	echo "Usage: $0 DATABASE_NAME"
	exit 1
fi

DATABASE_NAME=$1

read -sp "Enter MySQL password: " PASSWORD
echo

echo "SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC" | mysql -hlocalhost -uroot -p"$PASSWORD" "$DATABASE_NAME"
