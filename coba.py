import datetime as dt

# ==============
waktu_sekarang_now = dt.datetime.now()
waktu_sekarang_today = dt.datetime.today()
print(waktu_sekarang_now)
print(waktu_sekarang_today)

# ==============
tanggal_sekarang = dt.date.today()
print(tanggal_sekarang)

waktu_saat_ini = dt.datetime.now()
# datetime to string
print(waktu_saat_ini.strftime("%A, %d-%b-%Y %H:%M:%S %z"))

date_str = "09-10-2004"

# string to datetime
date = dt.datetime.strptime(date_str, "%m-%d-%Y")
print(date)

# ==============
tanggal_lahir = dt.date(2004, 9, 10)
tanggal_sekarang = dt.date.today()
umur = tanggal_sekarang.year - tanggal_lahir.year
print(f"Umur saya {umur} Tahun")

# time delta (datetime datatype)
tambah_hari = dt.timedelta(days=10000)
hasil_hari = tanggal_sekarang + tambah_hari
print(f"{hasil_hari} - {type(hasil_hari)}")
