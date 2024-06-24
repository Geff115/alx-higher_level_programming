#!/usr/bin/python3
""" Script listing cities by states"""

import MySQLdb
import sys


def list_all_cities():
    """This function lists all cities in the database
    hbtn_0e_4_usa.
    """

    db = MySQLdb.connect(
          user=sys.argv[1],
          host="localhost",
          port=3306,
          password=sys.argv[2],
          database=sys.argv[3]
    )
    mycursor = db.cursor()
    mycursor.execute("SELECT cities.id, cities.name, states.name FROM cities "
                     "JOIN states ON cities.state_id = states.id "
                     "ORDER BY cities.id ASC")
    results = mycursor.fetchall()
    for row in results:
        print(row)
    mycursor.close()
    db.close()


if __name__ == "__main__":
    list_all_cities()
