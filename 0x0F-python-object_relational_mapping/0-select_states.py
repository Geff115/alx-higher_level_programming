#!/usr/bin/env python3

"""List all states frm the database hbtn_0e_0_usa."""

import MySQLdb
import sys


def main():
    """This is the main function that creates a connection with
    the database hbtn_0e_0_usa and lists all states.
    """

    db = MySQLdb.connect(
          user=sys.argv[1],
          host="localhost",
          port=3306,
          password=sys.argv[2],
          db=sys.argv[3]
    )
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM states")
    results = mycursor.fetchall()
    for row in results:
        print(row)
    mycursor.close()
    db.close()


if __name__ == "__main__":
    main()
