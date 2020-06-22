import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="perhotelan"
    )
cursor=db.cursor()

#1.Select
Squery3=("select * from transaksi")
cursor.execute(Squery3)

result = cursor.fetchall()
for (data) in result:
    print(data)

#1.Insert
Iquery3 = "insert into transaksi(id_tamuFK,nama_kamarFK,tanggal) values (%s,%s, %s)"
data1 = ('B010', 'V VIP', '2010-11-21')
cursor.execute(Iquery3, data1)
db.commit()
print("{} record ditambahkan".format(cursor.rowcount))

#1.Update
Uquery3 = "update transaksi id_tamuFK=%s, nama_kamarFK=%s where tanggal=%s"
update1 = ('B002','VIP','2019-12-01')
cursor.execute(Uquery3, update1)
db.commit()
print("{} Record diubah".format(cursor.rowcount))

#1.Delete
Dquery3 = "delete from transaksi where tanggal=%s"
del1 = ('2019-10-02',)
cursor.execute(Dquery3,del1)
db.commit()
print("{} Record dihapus".format(cursor.rowcount))

cursor.close()
db.close()
