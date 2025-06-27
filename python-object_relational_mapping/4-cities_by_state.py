#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa with their state names"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and database name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password,
                         db=db_name)

    # Create a cursor object
    cur = db.cursor()

    # Execute a single query joining cities and states
    cur.execute("SELECT cities.id, cities.name, states.name "
                "FROM cities JOIN states ON cities.state_id = states.id "
                "ORDER BY cities.id ASC")

    # Fetch and print all result rows
    for row in cur.fetchall():
        print(row)

    # Close cursor and connection
    cur.close()
    db.close()
