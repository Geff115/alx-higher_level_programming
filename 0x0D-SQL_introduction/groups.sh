#!/usr/bin/env bash
# This script executes a query on a database that list the number of records with the same score

if [ -z "$1" ];
then
	echo "Usage: $0 DATABASE_NAME"
	exit 1
fi

DATABASE_NAME=$1

read -sp "Enter your MySQL password: " PASSWORD
echo

echo "SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC" | mysql -hlocalhost -uroot -p"$PASSWORD" "$DATABASE_NAME" | column -t
