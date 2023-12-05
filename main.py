list_mahasiswa = []


def menu():
    print("1. List Mahasiswa")
    print("2. Input Mahasiswa")
    print("3. Cari Mahasiswa")
    print("4. Hapus Mahasiswa")
    print("5. Edit Mahasiswa")
    print("6. Exit")


def input_mahasiswa(nama, nim):
    data = {"nim": nim, "nama": nama}
    list_mahasiswa.append(data)


def cari_mahasiswa(nim):
    for mahasiswa in list_mahasiswa:
        if mahasiswa["nim"] == nim:
            return mahasiswa

    return None


def hapus_mahasiswa(nim):
    global list_mahasiswa
    new_list_mahasiswa = []
    is_found = False

    for mahasiswa in list_mahasiswa:
        if mahasiswa["nim"] != nim:
            new_list_mahasiswa.append(mahasiswa)
        else:
            is_found = True

    list_mahasiswa = new_list_mahasiswa

    return is_found


def edit_mahasiswa(nim, new_nama):
    is_found = False
    for mahasiswa in list_mahasiswa:
        if mahasiswa["nim"] == nim:
            mahasiswa["nama"] = new_nama
            is_found = True

    return is_found


def print_mahasiswa():
    for mahasiswa in list_mahasiswa:
        # print(mahasiswa["nim"], " - ", mahasiswa["nama"])
        print(f"{mahasiswa['nim']} - {mahasiswa['nama']}")


while True:
    print("\n======Program Management Mahasiswa======")
    menu()
    input_menu = input("Masukan menu [1-6] : ")
    if input_menu == "1":
        print_mahasiswa()

    elif input_menu == "2":
        nama_mahasiswa = input("Masukan nama mahasiswa : ")
        nim_mahasiswa = input("Masukan NIM mahasiswa : ")
        input_mahasiswa(nama_mahasiswa, nim_mahasiswa)
        print("\nBerhasil Melakukan Insert Mahasiswa")

    elif input_menu == "3":
        nim_mahasiswa = input("Masukan NIM mahasiswa : ")

        mahasiswa = cari_mahasiswa(nim_mahasiswa)
        if mahasiswa == None:
            print("\nMahasiswa tidak ditemukan")
        else:
            print("\nNama Mahasiswa   : ", mahasiswa["nama"])

    elif input_menu == "4":
        nim_mahasiswa = input("Masukan NIM mahasiswa : ")
        if hapus_mahasiswa(nim_mahasiswa) == True:
            print("\nBerhasil Melakukan Hapus Mahasiswa")
        else:
            print("\nNIM Tidak Ditemukan")

    elif input_menu == "5":
        nim_mahasiswa = input("Masukan NIM mahasiswa : ")
        new_nama_mahasiswa = input("Masukan nama baru mahasiswa : ")

        if edit_mahasiswa(nim_mahasiswa, new_nama_mahasiswa) == True:
            print("\nBerhasil Melakukan Update Mahasiswa")
        else:
            print("\nNIM Tidak Ditemukan")

    elif input_menu == "6":
        break
    else:
        print("\nPilihan Menu Tidak Ada")
