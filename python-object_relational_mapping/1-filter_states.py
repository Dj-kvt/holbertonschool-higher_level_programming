#!/usr/bin/python3
"""Script that lists all states starting with 'N' from the database"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and database name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the MySQL server on localhost at port 3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create a cursor object to execute queries
    cur = db.cursor()

    # Execute SQL query to select states starting with 'N'
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")

    # Fetch all results
    rows = cur.fetchall()

    # Print each result row
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
