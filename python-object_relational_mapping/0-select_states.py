#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if name == "__main__":
    # Retrieve MySQL credentials and database name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL server on localhost, port 3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create a cursor object to execute SQL queries
    cur = db.cursor()

    # Execute the SQL query to select all states ordered by id
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows from the executed query
    rows = cur.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close the cursor and the connection
    cur.close()
    db.close()
