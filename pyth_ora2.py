import cx_Oracle

nom = input("Veuillez entrer le Nom du de l'operateur : ")
prenom = input("Veuillez entrer le Prenom du de l'operateur : ")
bdd = input("Veuillez indiquer la liste des BDD concernés : ")
int = input("Interne ? o/n :")

bdd_l=bdd.split(",")

nom_login = nom[:5]+"_"+prenom[0].upper()

NOM_LOGIN = nom_login.upper()

if int.lower == "o":
	EMAIL = prenom+"."+nom+"@mail.fr"
elif int.lower == "n":
	EMAIL = prenom+"."+nom+"-ext@mail.fr"
else:
	print("Veuillez taper o ou n svp")

print(nom)
print(prenom)
print(bdd_l)
print(NOM_LOGIN)
print(EMAIL)

os.system("pause")

con = cx_Oracle.connect('system', 'xxx', 'xxx')

cur = con.cursor()

cur.execute("INSERT INTO SCHEMA.TABLE VALUES ('"+nom.upper()+" "+prenom+"', NULL, "+EMAIL+", 'null', 'null', NULL, "+NOM_LOGIN+", NULL, 'OUI', '"+nom.upper()+"   "+prenom[0].upper()+"')")

for rec in bdd_l:
	cur.execute("INSERT INTO SCHEMA.TABLE2 VALUES ('"+NOM_LOGIN+"','"+rec+"',NULL)")
	
cur.close()
con.commit()
con.close()

os.system("pause")
for enr in bdd_l:
	con = cx_Oracle.connect('system', 'xxx', enr)
	cur = con.cursor()
	cur.execute("INSERT INTO SCHEMA.TABLE VALUES VALUES ('"+NOM_LOGIN+"' , null, null, 'null', 'null', null)")
	cur.execute("INSERT INTO SCHEMA.TABLE VALUES VALUES ('"+NOM_LOGIN+"_SUFFIX' , null, null, null, 'null', null)")
	cur.close()
	con.commit()
	con.close()
