#!/usr/bin/python3
"""Script that lists all states matching a name passed as argument"""

import MySQLdb
import sys

if name == "__main__":
    # Get MySQL credentials and database name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server running on localhost at port 3306
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password,
                         db=db_name)

    # Create a cursor to execute SQL queries
    cur = db.cursor()

    # Build the SQL query with .format() (insecure, as required by task)
    query = ("SELECT * FROM states WHERE name LIKE BINARY '{}' "
             "ORDER BY id ASC".format(state_name))

    # Execute the query
    cur.execute(query)

    # Fetch and print all matching rows
    for row in cur.fetchall():
        print(row)

    # Close cursor and connection
    cur.close()
    db.close()
