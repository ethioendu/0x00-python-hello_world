#!/usr/bin/python3
'''
a python a script that lists all states
from the database hbtn_0e_0_usa.
'''

import MySQLdb


def list_states(username, password, database):
    """Connect to MySQL server."""
    db = MySQLdb.connect(user=username, passwd=password,
                         db=database, host='localhost', port=3306)
    ''' Create a cursor object to execute SQL queries.'''
    cursor = db.cursor()

    ''' Execute the query to fetch states.'''
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    ''' Fetch all the rows returned by the query.'''
    rows = cursor.fetchall()

    ''' Display the results.'''
    for row in rows:
        print(row)

    ''' Close the cursor and database connection.'''
    cursor.close()
    db.close()


''' Entry point of the script.'''
if __name__ == '__main__':
    import sys

    ''' Get the command-line arguments.'''
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    ''' Call the function to list states.'''
    list_states(username, password, database)
