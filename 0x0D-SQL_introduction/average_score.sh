#!/usr/bin/env bash
# This script executes a query that computes the average score from a score column in the second_table column.

if [ -z "$1" ];
then
	echo "Usage: $0 DATABASE_NAME"
	exit 1
fi

DATABASE_NAME=$1

read -sp "Enter your MySQL password: " PASSWORD
echo

echo "SELECT AVG(score) as average FROM second_table" | mysql -hlocalhost -uroot -p"$PASSWORD" "$DATABASE"
