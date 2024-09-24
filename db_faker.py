import mysql.connector
from faker import Faker
import random

# Koneksi ke database
db = mysql.connector.connect(
    host="localhost",
    user="username",  # Ganti dengan username database Anda
    password="password",  # Ganti dengan password database Anda
    database="database"  # Ganti dengan nama database Anda
)

cursor = db.cursor()
faker = Faker()

# Generate dan masukkan 10.000 data
for _ in range(10000):
    nama = faker.name()
    alamat = faker.address().replace("\n", ", ")
    tanggal_lahir = faker.date_of_birth(minimum_age=18, maximum_age=65)
    pekerjaan = random.choice(['Pegawai Negeri', 'Swasta', 'Wirausaha', 'Mahasiswa'])
    status = random.choice(['Menikah', 'Belum Menikah', 'Janda', 'Duda'])
    gaji = random.uniform(3000000, 10000000)  # Gaji acak antara 3 juta sampai 10 juta
    ibu_kandung = faker.name()
    nominal_pinjaman = random.uniform(10000000, 500000000)  # Pinjaman acak antara 10 juta sampai 500 juta
    jaminan = random.choice(['BPKB Motor', 'Sertifikat Rumah', 'Tanah', 'Aset Lainnya'])
    tenor = random.choice([6, 12, 18, 24, 36])  # Tenor dalam bulan

    sql = """
    INSERT INTO data_peminjam (Nama, Alamat, TanggalLahir, Pekerjaan, Status, Gaji, ibuKandung, NominalPinjaman, Jaminan, Tenor)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """  # Tambahkan satu %s untuk NominalPinjaman
    values = (nama, alamat, tanggal_lahir, pekerjaan, status, gaji, ibu_kandung, nominal_pinjaman, jaminan, tenor)
    cursor.execute(sql, values)

db.commit()
cursor.close()
db.close()

print("Data berhasil dimasukkan!")
