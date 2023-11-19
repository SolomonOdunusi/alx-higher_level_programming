#!/usr/bin/python3
"""A scirpt that lists states"""
import MySQLdb
import sys

if __name__ == "__main__":
    """ It filters the states"""
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
    )
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM statesWHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    cursor.close()
    db.close()
