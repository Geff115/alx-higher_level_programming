#!/usr/bin/env bash
# This script executes a query that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).

if [ -z "$1" ];
then
	echo "Usage: $0 DATABASE_NAME"
	exit 1
fi

DATABASE_NAME=$1

read -sp "Enter your MySQL password: " PASSWORD
echo

QUERY="SELECT city, AVG(value) AS average_temperature FROM temperatures GROUP BY city ORDER BY average_temperature DESC;"
echo "$QUERY" | mysql -hlocalhost -uroot -p"$PASSWORD" "$DATABASE_NAME"
