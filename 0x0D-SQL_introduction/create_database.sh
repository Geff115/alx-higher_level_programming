#!/usr/bin/env bash
# This script creates the database hbtn_0c_0 in MySQL if it does not already exist.

read -sp "Enter MySQL password: " PASSWORD
echo

echo "CREATE DATABASE IF NOT EXISTS hbtn_0c_0;" | mysql -hlocalhost -uroot -p"$PASSWORD"
