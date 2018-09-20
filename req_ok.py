import cx_Oracle

con = cx_Oracle.connect('USER', 'PWD', 'BDD')

# querry #1
cur = con.cursor()
cur.execute("select * from v$version")
for row in cur:
	print(row[0])

cur.close()
#con.commit()
con.close()
