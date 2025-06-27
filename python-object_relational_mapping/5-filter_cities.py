#!/usr/bin/python3
"""Lists all cities of a state, safe from SQL injection"""

import MySQLdb
import sys

if name == "__main__":
    # Get MySQL credentials and state name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password,
                         db=db_name)

    # Create a cursor
    cur = db.cursor()

    # Execute secure parameterized query (SQL injection safe)
    cur.execute("SELECT cities.name FROM cities "
                "JOIN states ON cities.state_id = states.id "
                "WHERE states.name = %s ORDER BY cities.id ASC", (state_name,))

    # Fetch all city names and join them with commas
    cities = cur.fetchall()
    print(", ".join(city[0] for city in cities))

    # Close cursor and connection
    cur.close()
    db.close()
