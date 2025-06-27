#!/usr/bin/python3
"""Safe script that lists states matching a name"""

import MySQLdb
import sys

if name == "__main__":
    # Get credentials and state name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the local MySQL database
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password,
                         db=db_name)

    # Create a cursor to execute SQL queries
    cur = db.cursor()

    # Use parameterized query to prevent SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (state_name,))

    # Print all matching rows
    for row in cur.fetchall():
        print(row)

    # Close the cursor and connection
    cur.close()
    db.close()
