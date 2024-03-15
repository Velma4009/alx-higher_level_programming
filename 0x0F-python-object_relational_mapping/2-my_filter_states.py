
#!/usr/bin/python3

""" This module takes in an argument and displays all
values in ths states table in the database hbtn_0e_0_usa
where name matches the argument
"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost',
                         port=3306, user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE BINARY name =  '{}'\
            ORDER BY states.id".format(sys.argv[4]))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
