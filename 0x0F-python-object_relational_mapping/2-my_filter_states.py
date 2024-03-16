#!/usr/bin/python3
"""
a script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    '''Create a cursor object to execute SQL queries.'''

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                .format(sys.argv[4]))
    '''Fetch all the rows returned by the query.'''
    rows = cur.fetchall()
    ''' Display the results.'''
    for row in rows:
        print(row)

    '''Close the cursor and database connection.'''
    cur.close()
    db.close()
