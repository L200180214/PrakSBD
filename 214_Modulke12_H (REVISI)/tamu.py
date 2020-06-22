import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="perhotelan"
    )
cursor=db.cursor()

#1.Select
Squery1=("select * from tamu")
cursor.execute(Squery1)

result = cursor.fetchall()
for (data) in result:
    print(data)

#1.Insert
Iquery1 = "insert into tamu(id_tamu, nama, alamat) values (%s,%s, %s)"
data1 = ('B019', 'Nadia', 'Bali')
cursor.execute(Iquery1, data1)
db.commit()
print("{} record ditambahkan".format(cursor.rowcount))

#1.Update
Uquery1 = "update tamu set nama=%s, alamat=%s where id_tamu=%s"
update1 = ('Aris','Bandung','B003')
cursor.execute(Uquery1, update1)
db.commit()
print("{} Record diubah".format(cursor.rowcount))

#1.Delete
Dquery1 = "delete from tamu where id_tamu=%s"
del1 = ('B001',)
cursor.execute(Dquery1,del1)
db.commit()
print("{} Record dihapus".format(cursor.rowcount))

cursor.close()
db.close()
