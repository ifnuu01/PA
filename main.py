import os
from data import Login,header,Samsung,Infinix,header_keranjang,Xiomi,Oppo
from tabulate import tabulate

#Fungsi untuk membersihkan terminal
def clear_screen():
    #Untuk os windows cls , dan linux clear
    os.system('cls' if os.name == 'nt' else 'clear')

#Fungsi back to menu atau pembatas
def back_to_menu():
    input("\nTekan enter untuk kembali...")

#Fungsi login
def auth_role():
    gagal = 0
    #Jika gagal login 3x maka while akan berhenti
    while gagal < 3:
        print(tabulate([["Menu Login \n"]],tablefmt="double_grid"))
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
            print(tabulate([[f"noted :  Login gagal ke {gagal} , jika gagal login 3x maka akan di keluarkan ke menu awal"]],tablefmt="double_grid"))
            print()

#Fungsi registrasi user
def registrasi_user():
    while True:
        print(tabulate([["Silahkan buat akun"]],tablefmt="double_grid"))
        #variable username dan password untuk menampung inputan
        username = input("\nUsername baru : ")
        if username in Login.keys():
            clear_screen()
            print(tabulate([["Noted : Username telah di pakai , coba yang lain"]],tablefmt="double_grid"))
            print()
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
        tampilan = [["Login"],["Registrasi"],["Exit"]]
        print(tabulate(tampilan,headers=["No","Selamat Datang di Toko Handphone"],tablefmt="mixed_grid",showindex=range(1,len(tampilan)+1)))
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
            print(tabulate([["Terima kasih telah berkunjung"]],tablefmt="double_grid"))
            exit()
        #Jika akan inputan pilih tidak terdapat pada menu maka akan di berikan peringatan seperti di bawah
        else:
            print(tabulate([[]],tablefmt="double_grid"))
            print(tabulate([["Noted : Pilih angka yang terdapat pada menu !"]],tablefmt="double_grid"))

#Fungsi show menu admin
def show_menu_admin():
    #Perulangan yang di mana menu akan terus di ulang jika tidak sesuai dengan inputan
    while True:
        #Menampilkan menu-menu yang terdapat pada menu admin
        tampilan = [["Read Handphone"],["Update Handphone"],["Edit Handphone"],["Delete Handphone "],["Logout"]]
        print(tabulate(tampilan,headers=["No","Dashboard Admin"],tablefmt="mixed_grid",showindex=range(1,len(tampilan)+1)))
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
            print(tabulate([["Noted : Pilih angka yang terdapat pada menu !"]],tablefmt="double_grid"))

def menu_read():
    tampilan = [["Samsung"],["Infinix"],["Xiomi"],["Oppo"]]
    print(tabulate(tampilan,headers=["No","Daftar Brand"],tablefmt="mixed_grid",showindex=range(1,len(tampilan)+1)))
    print(tabulate([["Back >> 5"]],tablefmt="double_grid"))

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
            print(show_type(Xiomi,"Xiomi",header))
            back_to_menu()
            clear_screen()
        elif pilih == "4":
            print(show_type(Oppo,"Oppo",header))
            back_to_menu()
            clear_screen()
        elif pilih == "5":
            show_menu_admin()
        else:
            print(tabulate([["Noted : Pilih angka yang terdapat pada menu !"]],tablefmt="double_grid"))


def show_type(brand,name_brand,header):
    print(tabulate([[f"Daftar {name_brand}"]],tablefmt="double_grid"))
    table = tabulate(brand,headers=header,tablefmt="simple_grid",showindex=range(1,len(brand)+1))
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
        elif Brand =="3":
            update_type(Xiomi,"Xiomi")
        elif Brand =="4":
            update_type(Oppo,"Oppo")
        elif Brand == "5":
            show_menu_admin()
        else:
            print(tabulate([[]],tablefmt="double_grid"))
            print(tabulate([["Noted : Pilih angka yang terdapat pada menu !"]],tablefmt="double_grid"))


def update_type(brand,name_brand):
    print(tabulate([[f"Masukan data baru tentang brand {name_brand}\n"]],tablefmt="double_grid"))
    Update         = input_update()
    print(tabulate([["Noted : Data berhasil di tambahkan :) "]],tablefmt="double_grid"))
    brand.append(Update)
    update_handphone()


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
            print(tabulate([["Noted : Inputan tidak valid silahkan mengulang \n"]],tablefmt="double_grid"))

    
def edit_handphone():
    while True:
        menu_read()
        Brand = input("Pilih brand dari type handphone yang mau di edit : ")
        clear_screen()
        if Brand == "1":
            edit_type(Samsung,"Samsung")
        elif Brand =="2":
            edit_type(Infinix,"Infinix")
        elif Brand =="3":
            edit_type(Xiomi,"Xiomi")
        elif Brand =="4":
            edit_type(Oppo,"Oppo")
        elif Brand == "5":
            show_menu_admin()
        else:
            print(tabulate([["Noted : Pilih angka yang terdapat pada menu !"]],tablefmt="double_grid"))

def edit_type(brand,name_brand):
    while True:
        try:
            print(show_type(brand,name_brand,header))
            pilih = int(input("Pilih ID yang mau di edit : "))
            clear_screen()
            if len(brand) <= 0 :
                print(tabulate([["Tidak ada handphone yang tersedia"]],tablefmt="double_grid"))
                back_to_menu()
                clear_screen()
                show_menu_admin()
            else:
                if pilih in [i+1 for i in range(len(brand))]:
                    print(tabulate([["Masukan data baru \n "]],tablefmt="double_grid"))
                    edit = input_update()
                    clear_screen()
                    print(tabulate([["Noted : data berhasil di edit"]],tablefmt="double_grid"))
                    brand[pilih-1] = edit
                    return
                else:
                    print(tabulate([["Noted : ID yang anda inputkan tidak ada\n"]],tablefmt="double_grid"))
        except ValueError:
            clear_screen()
            print(tabulate([["Noted : ID yang anda inputkan tidak ada\n"]],tablefmt="double_grid"))

def delete_handphone():
    while True:
        menu_read()
        Brand = input("Pilih brand dari type handphone yang mau di hapus : ")
        clear_screen()
        if Brand == "1":
            delete_type(Samsung,"Samsung")
        elif Brand =="2":
            delete_type(Infinix,"Infinix")
        elif Brand =="3":
            delete_type(Xiomi,"Xiomi")
        elif Brand =="4":
            delete_type(Oppo,"Oppo")
        elif Brand == "5":
            show_menu_admin()
        else:
            print(tabulate([["Noted : Pilih angka yang terdapat pada menu !"]],tablefmt="double_grid"))
        
def delete_type(brand,name_brand):
    while True:
        try:
            print(show_type(brand,name_brand,header))
            pilih = int(input("Pilih ID yang mau di hapus : "))
            clear_screen()
            if len(brand) <= 0 :
                print(tabulate([["Tidak ada handphone yang tersedia"]],tablefmt="double_grid"))
                back_to_menu()
                clear_screen()
                show_menu_admin()
            else:
                if pilih in [i+1 for i in range(len(brand))]:
                    del brand[pilih-1]
                    print(tabulate([["Noted : data berhasil di hapus"]],tablefmt="double_grid"))
                    return
                else:   
                    print(tabulate([["Noted : ID yang anda inputkan tidak ada\n"]],tablefmt="double_grid"))
        except ValueError:
            clear_screen()
            print(tabulate([["Noted : ID yang anda inputkan tidak ada\n"]],tablefmt="double_grid"))

def show_menu_user(nama_akun):
    while True:
        table = [["Isi saldo"],["list Produk"],["Keranjang"],["Log Out"],["Exit"]]
        header_table = ["No","Selamat Datang di TokoHanphone"]
        print(tabulate(table,headers=header_table,showindex=range(1,6),tablefmt="double_grid"))
        print(tabulate([[f"Saldo anda saat ini >> Rp.{Login[nama_akun][1]}"]],tablefmt="double_grid"))
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
            print(tabulate([["Terima kasih telah berkunjung"]],tablefmt="double_grid"))
            exit()
        else:
            print(tabulate([["Noted : Pilih angka yang terdapat pada menu !"]],tablefmt="double_grid"))

def top_up(nama_akun):
    while True:
        try:
            print(tabulate([[f"Saldo anda saat ini berjumlah {Login[nama_akun][1]}\n"]],tablefmt="double_grid"))
            top_up = int(input("Masukan nominal top up : Rp")) 
            clear_screen()
            Login[nama_akun][1] += top_up
            print(tabulate([["Noted : Anda berhasil top up"]],tablefmt="double_grid"))
            back_to_menu()
            clear_screen()
            show_menu_user(nama_akun)
        except ValueError:clear_screen();print(tabulate([["Inputan anda tikak valid"]],tablefmt="double_grid"))

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
            show_type_user(Xiomi,"Xiomi",nama_akun)
        elif pilih == "4":
            show_type_user(Oppo,"Oppo",nama_akun)
        elif pilih == "5":
            show_menu_user(nama_akun)
        else:
            print(tabulate([["Noted : Pilih angka yang terdapat pada menu !"]],tablefmt="double_grid"))

def show_type_user(brand,name_brand,nama_akun):
    while True:
        print(show_type(brand,name_brand,header))
        pilihan = input("ingin memasukan produk ke keranjang [y/n] :")
        clear_screen()
        if pilihan == "y":
            if len(brand) <= 0 :
                print(tabulate([["Tidak ada handphone yang tersedia"]],tablefmt="double_grid"))
                back_to_menu()
                clear_screen()
                show_menu_user(nama_akun)
            else:
                masuk_keranjang(brand,name_brand,nama_akun)
             #menambahkan ke keranjang
        elif pilihan =="n":
            read_handphone_user(nama_akun)
        else:
            print(tabulate([["Noted : Pilih y / n !! , Silahkan ulangi\n"]],tablefmt="double_grid"))

def masuk_keranjang(brand,name_brand,nama_akun):
    while True:
        try:
            print(show_type(brand,name_brand,header))
            pilih = int(input("Masukan ID handphone yang mau di masukan ke keranjang : "))
            clear_screen()
            if pilih in [i+1 for i in range(len(brand))]:
                produk = brand[pilih - 1][0]
                harga = brand[pilih -1 ][4]
                keranjang = [produk,harga]
                Login[nama_akun][2].append(keranjang)
                print(tabulate([["Data berhasil di masukan ke keranjang\n"]],tablefmt="double_grid"))
                back_to_menu()
                clear_screen()
                show_menu_user(nama_akun)
            else:
                print(tabulate([["Noted : ID yang anda inputkan tidak ada\n"]],tablefmt="double_grid"))
        except ValueError:clear_screen();print(tabulate([["Noted : ID yang anda inputkan tidak ada\n"]],tablefmt="double_grid"))

def keranjang(nama_akun):
    while True:
        keranjang_akun = Login[nama_akun][2]
        print(show_type(keranjang_akun,"Keranjang",header_keranjang))
        Pilihan_checkout= input("Apakah ada barang yang ingin di check out[y/n]: ")
        clear_screen()
        if  Pilihan_checkout == "y":
            if len(Login[nama_akun][2]) <= 0 :
                print(tabulate([["Keranjang Anda Kosong"]],tablefmt="double_grid"))
                back_to_menu()
                clear_screen()
                show_menu_user(nama_akun)
            else:
                check_out(nama_akun, keranjang_akun)
        elif Pilihan_checkout == "n":
            show_menu_user(nama_akun)
        else:
            print(tabulate([["Noted : Pilih y / n !!, Silahkan ulangi lagi\n"]],tablefmt="double_grid"))

#Fungsi Checkout
def check_out(nama_akun, keranjang_akun):
    while True: 
        print(show_type(keranjang_akun,"Keranjang",header_keranjang))
        ID_checkout = int(input("Masukkan ID hanphone yang mau di check out: "))
        clear_screen()
        if ID_checkout in [i+1 for i in range(len(Login[nama_akun][2]))]:        
            barang_checkout= Login[nama_akun][2][ID_checkout-1]
            print(tabulate([[f"Saldo anda saat ini adalah Rp. {Login[nama_akun][1]}\n"]],tablefmt="double_grid"))
            Transaksi = input("Apakah anda ingin melanjutkan transaksi(y/n): ")
            clear_screen()
            if Transaksi == "y":
                if Login[nama_akun][1] < barang_checkout[1]:
                    print(tabulate([["Noted : Saldo Tidak Cukup\n"]],tablefmt="double_grid"))
                    back_to_menu()
                    clear_screen()
                    show_menu_user(nama_akun)
                else:
                    sisa_saldo = Login[nama_akun][1]-barang_checkout[1]
                    Login[nama_akun][1] = sisa_saldo
                    display_struk(nama_akun,ID_checkout)
                    del Login[nama_akun][2][ID_checkout-1]
                    back_to_menu()
                    clear_screen()
                    show_menu_user(nama_akun)
            elif Transaksi =="n":
                print(tabulate([["Transaksi gagal"]],tablefmt="double_grid"))
                back_to_menu()
                show_menu_user(nama_akun)
            else:
                print(tabulate([["Noted : Pilih y / n !! Silahkan ulangi \n"]],tablefmt="double_grid"))
        else:
            print(tabulate([["Noted : Masukan ID yang tertera pada keranjang , Silahkan ulangi dari awal\n"]],tablefmt="double_grid"))


def display_struk(nama_akun,ID_checkout):
    header_table = ["Selamat Pembayaran Anda Berhasil"]
    table = [[f"Nama Produk   : {Login[nama_akun][2][ID_checkout-1][0]}"],[f"Total Harga   : Rp {Login[nama_akun][2][ID_checkout-1][1]}"]]
    print(tabulate(table,headers=header_table,tablefmt="double_grid"))

if __name__ == "__main__":
    os.system('pip install tabulate')
    clear_screen()
    show_menu_awal()