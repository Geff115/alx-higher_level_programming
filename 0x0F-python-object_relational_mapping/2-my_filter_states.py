#!/usr/bin/python3
""" list states by user input"""

import MySQLdb
import sys


def display_states_by_argument():
    """This function takes in an argument and displays all values
    in the states table of hbtn_0e_0_usa, where name matches the
    argument.
    """

    db = MySQLdb.connect(
          user=sys.argv[1],
          host="localhost",
          port=3306,
          password=sys.argv[2],
          db=sys.argv[3]
    )
    mycursor = db.cursor()
    myquery = """
SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id ASC"""
    myquery = myquery.format(sys.argv[4])
    mycursor.execute(myquery)
    results = mycursor.fetchall()
    for row in results:
        print(row)
    mycursor.close()
    db.close()


if __name__ == "__main__":
    display_states_by_argument()
