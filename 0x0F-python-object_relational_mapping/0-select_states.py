#!/usr/bin/python3
"""
Lists all states from the datahase hbtn_0e_0_usa.
Usage: ./0-select_states.py <mysql username> \
                             <mysql password> \
                             <database name>
"""
import sys
import MySQLdb

if __name__ == '__main__':
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=db_name
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    for state in cur.fetchall():
        print(state)

    cur.close()
    db.close()

