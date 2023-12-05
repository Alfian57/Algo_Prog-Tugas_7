import datetime as dt

list_makanan = [
    {"nama": "Nasi Goreng", "harga": 15000},
    {"nama": "Mie Goreng", "harga": 9000},
    {"nama": "Mie Goreng Telur", "harga": 12000},
    {"nama": "Megelangan", "harga": 20000},
    {"nama": "Nasi Orak orik", "harga": 13000},
]

list_pesanan = []


def print_menu():
    counter = 1
    print("\n")
    for makanan in list_makanan:
        print(f"{counter}. {makanan['nama']} (Rp.{makanan['harga']})")
        counter += 1


def tambah_pesanan(makanan, jumlah):
    data = {"nama": makanan["nama"], "harga": makanan["harga"], "jumlah": jumlah}
    list_pesanan.append(data)


def hitung_tagihan():
    tagihan = 0

    for pesanan in list_pesanan:
        harga = pesanan["harga"] * pesanan["jumlah"]
        tagihan += harga

    return tagihan


def print_struk(pelanggan, uang_pembayaran):
    tagihan = hitung_tagihan()
    kembalian = uang_pembayaran - tagihan

    print("\n=======================")
    print("=========Struk=========")
    print("Nama                 : ", pelanggan)
    print("Beli                 : ")
    for pesanan in list_pesanan:
        print(f"\t- {pesanan['nama']} (Rp.{pesanan['harga']}) x {pesanan['jumlah']}")
    print("Tagihan            : Rp.", tagihan)
    print("Uang Pembayaran    : Rp.", uang_pembayaran)
    print("Kembalian          : Rp.", kembalian)
    print("Waktu Pemesanan    : Rp.", dt.datetime.now())


while True:
    pelanggan = input("Masukan nama pelanggan : ")
    while True:
        print_menu()
        menu_makanan = input("Pilih makanan yang dipesan atau ketik 'selesai' : ")
        if menu_makanan == "selesai":
            break

        jumlah_makanan = int(input("Masukan jumlah pembelian : "))
        menu_makanan_int = int(menu_makanan)

        if menu_makanan_int > 0 and menu_makanan_int <= len(list_makanan):
            tambah_pesanan(list_makanan[menu_makanan_int - 1], jumlah_makanan)
        else:
            print("\n\n================")
            print("Menu tidak valid")
            print("================")

    uang_pembayaran = int(input("Masukan uang yang dibayarakan :  "))
    print_struk(pelanggan, uang_pembayaran)
    list_pesanan = []

    ulang = input("Apakah ingin memesan lagi ? [y/n] : ")
    if ulang == "N" or ulang == "n":
        break
