#!/usr/bin/python3
""" list states in ascending order by id"""

import MySQLdb
import sys


def main():
    """This function selects all states order by
    states id.
    """

    db = MySQLdb.connect(
          user=sys.argv[1],
          host="localhost",
          port=3306,
          password=sys.argv[2],
          db=sys.argv[3]
          )
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    results = mycursor.fetchall()
    for row in results:
        if row[1].startswith("N"):
            print(row)
    mycursor.close()
    db.close()


if __name__ == "__main__":
    main()
