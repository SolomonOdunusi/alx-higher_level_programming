#!/usr/bin/python3
""" Write a script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys

if __name__ == "__main__":

    username, password, database = sys.argv[1], sysargv[2], sysargv[3]

    db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
