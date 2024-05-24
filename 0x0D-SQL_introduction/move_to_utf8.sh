#!/usr/bin/env bash
# This script executes a MySQL query  that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.

if [ -z "$1" ];
then
	echo "Usage: $0 DATABASE_NAME"
	exit 1
fi

DATABASE_NAME=$1

read -sp "Enter your MySQL password: " PASSWORD
echo

mysql -hlocalhost -uroot -p"$PASSWORD" "$DATABASE_NAME" <<EOF
ALTER DATABASE $DATABASE_NAME CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
ALTER TABLE hbtn_0c_0.first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE hbtn_0c_0.first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
EOF
