import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="perhotelan"
    )
cursor=db.cursor()

#1.Select
Squery2=("select * from kamar")
cursor.execute(Squery2)

result = cursor.fetchall()
for (data) in result:
    print(data)

#1.Insert
Iquery2 = "insert into kamar(nama_kamar, kelas_kamar, tarif) values (%s,%s, %s)"
data1 = ('Boulevard', 'Eco', 1500000)
cursor.execute(Iquery2, data1)
db.commit()
print("{} record ditambahkan".format(cursor.rowcount))

#1.Update
Uquery2 = "update kamar set kelas_kamar=%s, tarif=%s where nama_kamar=%s"
update1 = ('VIP','2500000','CL21')
cursor.execute(Uquery2, update1)
db.commit()
print("{} Record diubah".format(cursor.rowcount))

#1.Delete
Dquery2 = "delete from kamar where nama_kamar=%s"
del1 = ('CL04',)
cursor.execute(Dquery2,del1)
db.commit()
print("{} Record dihapus".format(cursor.rowcount))

cursor.close()
db.close()
