import os
from data import Login,header,Samsung,Infinix,header_keranjang
from tabulate import tabulate

#Fungsi untuk membersihkan terminal
def clear_screen():
    #Untuk os windows cls , dan linux clear
    os.system('cls' if os.name == 'nt' else 'clear')

#Fungsi login
def auth_role():
    gagal = 0
    #Jika gagal login 3x maka while akan berhenti
    while gagal < 3:
        print("Menu Login \n")
        #variable username dan password untuk menampung inputan
        username = input("Username : ")
        password = input("password : ")
        clear_screen()  
        #Jika username dan password terdetect sebagai admin maka akan masuk ke menu admin
        if username == "admin" and password == "admin":
            show_menu_admin()
        #Jika terdetect sebagai user maka masuk ke menu user
        elif username in Login.keys() and password == Login[username][0]:
            show_menu_user(username)
        else:
            #Jika username dan password tidak ada di dalam role user / admin maka variable gagal akan di tambah 1 sebagai pembatas perulangan
            gagal += 1
            print(f"noted :  Login gagal ke {gagal} , jika gagal login 3x maka akan di keluarkan ke menu awal\n")

#Fungsi registrasi user
def registrasi_user():
    while True:
        print("Silahkan buat akun baru anda \n")
        #variable username dan password untuk menampung inputan
        username = input("Username baru : ")
        if username in Login.keys():
            clear_screen()
            print("Noted : Username telah di pakai , coba yang lain\n")
        else:
            password = input("password baru : ")
            clear_screen()
            #Menambahkan username dan password ke dalam variable login atau bisa di sebut sebagai role user baru
            Login.update({username : [password,0,[]]})
            break

#Fungsi Show menu awal yaitu fungsi yang pertama di lihat oleh pengguna
def show_menu_awal():
    #Perulangan yang di mana menu akan terus di ulang jika tidak sesuai dengan inputan
    while True:
        #Menampilkan menu-menu yang terdapat pada menu awal
        print("""
================
 Toko Handphone
      Menu 
================
Login       >> 1
________________
Registrasi  >> 2
________________
Exit        >> 3
""")
        #Varible pilih sebagai penampung inputan
        pilih = input("Pilih Menu : ")
        clear_screen()
        #Percabangan jika inputan pilih bernilai str 1 maka akan ke menu auth_role
        if  pilih == "1":
            auth_role()
        #Jika inputan pilih bernilai str 2 maka akan ke menu Registrasi_useer
        elif pilih == "2":
            registrasi_user()
        #Jika inputan pilih bernilai str 3 maka memberhentikan program
        elif pilih == "3":
            print("Terima kasih telah berkunjung")
            exit()
        #Jika akan inputan pilih tidak terdapat pada menu maka akan di berikan peringatan seperti di bawah
        else:
            print("Noted : Pilih angka yang terdapat pada menu !")

#Fungsi show menu admin
def show_menu_admin():
    #Perulangan yang di mana menu akan terus di ulang jika tidak sesuai dengan inputan
    while True:
        #Menampilkan menu-menu yang terdapat pada menu admin
        print("""
=====================
              
    Dashboard Admin
              
=====================
Read Handphone   >> 1
_____________________
Update Handphone >> 2
_____________________
Edit Handphone   >> 3
_____________________
Delete Handphone >> 4
_____________________
Logout           >> 5         
""")
        #Varible pilih sebagai penampung inputan
        pilih = input("Pilih menu : ")
        clear_screen()
        #Percabangan yang dimana ketika inputan bernilai str 1 maka akan masuk ke Fungsi read_handphone
        if  pilih == "1":
            read_handphone()
        #Jika inputan pilih bernilai str 2 maka akan masuk ke Fungsi update_handphone
        elif pilih == "2":
            update_handphone()
        #Jika inputan pilih bernilai str 3 maka akan masuk ke Fungsi edit_handphone
        elif pilih == "3":
            edit_handphone()
        #Jika inputan pilih bernilai str 4 maka akan masuk ke Fungsi Delete_handphone
        elif pilih == "4":
            delete_handphone()
        #Jika inputan pilih bernilai str 5 maka akan masuk ke Fungsi show_menu_awal
        elif pilih == "5":
            show_menu_awal()
        #Jika akan inputan pilih tidak terdapat pada menu maka akan di berikan peringatan seperti di bawah
        else:
            print("Noted : Pilih angka yang terdapat pada menu !")

def back_to_menu():
    input("\nTekan enter untuk kembali...")

def read_handphone():
    while True:
        menu_read()
        pilih = input("Pilih no brand : ")
        clear_screen()
        if pilih == "1":
            print(show_type(Samsung,"Samsung",header))
            back_to_menu()
            clear_screen()
        elif pilih == "2":
            print(show_type(Infinix,"Infinix",header))
            back_to_menu()
            clear_screen()
        elif pilih == "3":
            show_menu_admin()
        else:
            print("Noted : Pilih angka yang terdapat pada menu !")

def menu_read():
    print("""
==============
 Daftar Brand 
==============
Samsung >> 1
______________
Infinix >> 2
______________
Back    >> 3
""")

def show_type(brand,name_brand,header):
    print(f"Daftar {name_brand}")
    for i in range(len(brand)):brand[i].insert(0,i+1)
    table = tabulate(brand,headers=header,tablefmt="simple_grid")
    for i in range(len(brand)):del brand[i][0]
    return table


def update_handphone():
    while True:
        menu_read()
        Brand = input("Pilih brand yang mau di tambah : ")
        clear_screen()
        if Brand == "1":
            update_type(Samsung,"Samsung")
        elif Brand =="2":
            update_type(Infinix,"Infinix")
        elif Brand == "3":
            show_menu_admin()
        else:
            print("Noted : Pilih angka yang terdapat pada menu !")

def input_update():
    while True:
        try:
            Type_handphone = input("Masukan type handphone : ")
            Ram            = int(input("Ram (Gb): "))
            Storage        = int(input("Storage / Penyimpanan (Gb): "))
            Processor      = input("Processor : ")
            Harga          = int(input("Harga : Rp"))
            clear_screen()
            return [Type_handphone,Ram,Storage,Processor,Harga]
        except ValueError:
            clear_screen()
            print("Noted : Inputan tidak valid silahkan mengulang \n")


def update_type(brand,name_brand):
    print(f"Masukan data baru tentang brand {name_brand}\n")
    print("===============================================")
    Update         = input_update()
    print("Noted : Data berhasil di tambahkan :) ")
    brand.append(Update)
    update_handphone()
    
def edit_handphone():
    while True:
        menu_read()
        Brand = input("Pilih brand dari type handphone yang mau di edit : ")
        clear_screen()
        if Brand == "1":
            edit_type(Samsung,"Samsung")
        elif Brand =="2":
            edit_type(Infinix,"Infinix")
        elif Brand == "3":
            show_menu_admin()
        else:
            print("Noted : Pilih angka yang terdapat pada menu !")

def edit_type(brand,name_brand):
    while True:
        try:
            print(show_type(brand,name_brand,header))
            pilih = int(input("Pilih ID yang mau di edit : "))
            clear_screen()
            if pilih-1 < len(brand):
                print("Masukan data baru \n ")
                print("=====================")
                edit = input_update()
                clear_screen()
                print("Noted : data berhasil di edit")
                brand[pilih-1] = edit
                return
            else:
                print("Noted : ID yang anda inputkan tidak ada\n")
        except ValueError:
            clear_screen()
            print("Noted : ID yang anda inputkan tidak ada\n")

def delete_handphone():
    while True:
        menu_read()
        Brand = input("Pilih brand dari type handphone yang mau di hapus : ")
        clear_screen()
        if Brand == "1":
            delete_type(Samsung,"Samsung")
        elif Brand =="2":
            delete_type(Infinix,"Infinix")
        elif Brand == "3":
            show_menu_admin()
        else:
            print("Noted : Pilih angka yang terdapat pada menu !")
        
def delete_type(brand,name_brand):
    while True:
        try:
            print(show_type(brand,name_brand,header))
            pilih = int(input("Pilih ID yang mau di hapus : "))
            clear_screen()
            if pilih-1 < len(brand):
                del brand[pilih-1]
                print("Noted : data berhasil di hapus")
                return
            else:
                print("Noted : ID yang anda inputkan tidak ada\n")
        except ValueError:
            clear_screen()
            print("Noted : ID yang anda inputkan tidak ada\n")

def show_menu_user(nama_akun):
    while True:
        print(f"""
=====================
              
    Dashboard User
      
=====================
Isi saldo        >> 1
_____________________
list Produk      >> 2
_____________________
Keranjang        >> 3
_____________________
Log Out          >> 4
_____________________
Exit             >> 5
_____________________
Saldo anda saat ini >> Rp.{Login[nama_akun][1]}
""")
        pilihan_user = input("Pilih menu: ")
        clear_screen()
        if pilihan_user == "1":
            top_up(nama_akun)
        elif pilihan_user == "2":
            read_handphone_user(nama_akun)
        elif pilihan_user == "3":
            keranjang(nama_akun)
        elif pilihan_user == "4":
            show_menu_awal()
        elif pilihan_user == "5":
            print("Terima kasih telah berkunjung")
            exit()
        else:
            print("Noted : Pilih angka yang terdapat pada menu !")

def top_up(nama_akun):
    while True:
        try:
            print(f"Saldo anda saat ini berjumlah {Login[nama_akun][1]}\n")
            top_up = int(input("Masukan nominal top up : Rp")) 
            clear_screen()
            Login[nama_akun][1] += top_up
            print("Noted : Anda berhasil top up")
            back_to_menu()
            clear_screen()
            show_menu_user(nama_akun)
        except ValueError:clear_screen();print("Inputan anda tikak valid")

def read_handphone_user(nama_akun):
    while True:
        menu_read()
        pilih = input("Pilih no brand : ")
        clear_screen()
        if pilih == "1":
            show_type_user(Samsung,"Samsung",nama_akun)
        elif pilih == "2":
            show_type_user(Infinix,"Infinix",nama_akun)
        elif pilih == "3":
            show_menu_user(nama_akun)
        else:
            print("Noted : Pilih angka yang terdapat pada menu !")

def show_type_user(brand,name_brand,nama_akun):
    while True:
        print(show_type(brand,name_brand,header))
        pilihan = input("ingin memasukan produk ke keranjang [y/n] :")
        clear_screen()
        if pilihan == "y":
            masuk_keranjang(brand,name_brand,nama_akun)
             #menambahkan ke keranjang
        elif pilihan =="n":
            read_handphone_user(nama_akun)
        else:
            print("Noted : Pilih y / n !! , Silahkan ulangi\n")

def masuk_keranjang(brand,name_brand,nama_akun):
    while True:
        try:
            print(show_type(brand,name_brand,header))
            pilih = int(input("Masukan ID handphone yang mau di masukan ke keranjang : "))
            clear_screen()
            if pilih -1 < len(brand):
                produk = brand[pilih - 1][0]
                harga = brand[pilih -1 ][4]
                keranjang = [produk,harga]
                Login[nama_akun][2].append(keranjang)
                print("Data berhasil di masukan ke keranjang\n")
                back_to_menu()
                show_menu_user(nama_akun)
            else:
                print("Noted : ID yang anda inputkan tidak ada\n")
        except ValueError:clear_screen();print("Noted : ID yang anda inputkan tidak ada\n")

def keranjang(nama_akun):
    while True:
        keranjang_akun = Login[nama_akun][2]
        print(show_type(keranjang_akun,"Keranjang",header_keranjang))
        Pilihan_checkout= input("Apakah ada barang yang ingin di check out[y/n]: ")
        clear_screen()
        if  Pilihan_checkout == "y":
            Check_out(nama_akun, keranjang_akun)
        elif Pilihan_checkout == "n":
            show_menu_user(nama_akun)
        else:
            print("Noted : Pilih y / n !!, Silahkan ulangi lagi\n")

#Fungsi Checkout
def Check_out(nama_akun, keranjang_akun):
    while True: 
        print(show_type(keranjang_akun,"Keranjang",header_keranjang))
        ID_checkout = int(input("Masukkan ID hanphone yang mau di check out: "))
        clear_screen()
        if ID_checkout-1 < len(Login[nama_akun][2]):        
            barang_checkout= Login[nama_akun][2][ID_checkout-1]
            print(f"Saldo anda saat ini adalah Rp. {Login[nama_akun][1]}\n")
            Transaksi = input("Apakah anda ingin melanjutkan transaksi(y/n): ")
            clear_screen()
            if Transaksi == "y":
                if Login[nama_akun][1] < barang_checkout[1]:
                    print("Noted : Saldo Tidak Cukup\n")
                    back_to_menu()
                    show_menu_user(nama_akun)
                else:
                    sisa_saldo = Login[nama_akun][1]-barang_checkout[1]
                    Login[nama_akun][1] = sisa_saldo
                    print (f"""
Selamat Pembayaran Anda Berhasil
================================
Nama Produk   : 
{Login[nama_akun][2][ID_checkout-1][0]}
________________________________
Total Harga   :
Rp {Login[nama_akun][2][ID_checkout-1][1]}
________________________________
""")
                    del Login[nama_akun][2][ID_checkout-1]
                    back_to_menu()
                    show_menu_user(nama_akun)
            elif Transaksi =="n":
                print("Transaksi gagal")
                back_to_menu()
                show_menu_user(nama_akun)
            else:
                print("Noted : Pilih y / n !! Silahkan ulangi \n")
        else:
            print("Noted : Masukan ID yang tertera pada keranjang , Silahkan ulangi dari awal\n")


if __name__ == "__main__":
    os.system('pip install tabulate')
    clear_screen()
    show_menu_awal()