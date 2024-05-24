#!/usr/bin/env bash
# This script creates a table second_table and inserts rows into it in the hbtn_0c_0 database.

if [ -z "$1" ];
then
	echo "Usage: $0 DATABASE_NAME"
	exit 1
fi

DATABASE_NAME="$1"

read -sp "Enter MySQL password: " PASSWORD
echo

mysql -hlocalhost -uroot -p"$PASSWORD" "$DATABASE_NAME" <<EOF
-- Creating a table second_table if it does not exist
CREATE TABLE IF NOT EXISTS second_table (
	id INT,
	name VARCHAR(256),
	score INT
);

-- Inserting rows into the second_table
INSERT INTO second_tabel(id, name, score) VALUES(1, 'John', 10);
INSERT INTO second_table(id, name, score) VALUES(2, 'Alex', 3);
INSERT INTO second_table(id, name, score) VALUES(3, 'Bob', 14);
INSERT INTO second_table(id, name, score) VALUES(4, 'George', 8);
EOF

if [ $? -eq 0 ];
then
	echo "Script executed successfully"
else
	echo "Error: Script execution failed"
fi
