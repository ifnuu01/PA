import os
from data import Login,Database,header,Samsung,Infinix
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
            print("yes  user")
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
            print("d")
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
            print(show_type(Samsung,"Samsung"))
            back_to_menu()
            clear_screen()
        elif pilih == "2":
            print(show_type(Infinix,"Infinix"))
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

def show_type(brand,name_brand):
    print(f"Brand {name_brand}")
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
        Brand = input("Pilih brand yang mau diedit : ")
        clear_screen()
        if Brand == "1":
            edit_type(Samsung,"Samsung")
        elif Brand =="2":
            edit_type(Infinix,"Infinix")
        elif Brand == "3":
            show_menu_admin()
        else:
            print("Noted : Pilih angka yang terdapat pada menu !")

def input_edit(brand,type_brand):
    while True:
        try:
            print(type_brand)
            pilih = int(input("Pilih ID yang mau di edit : "))
            clear_screen()
            if pilih in [i+1 for i in range(len(brand))]:
                print("Masukan data baru \n ")
                print("=====================")
                edit = input_update()
                clear_screen()
                print("Noted : data berhasil di edit")
                return edit , pilih
            else:
                print("Noted : ID yang anda inputkan tidak ada\n")
        except ValueError:
            clear_screen()
            print("Noted : ID yang anda inputkan tidak ada\n")

def edit_type(brand,name_brand):
    Edit , Pilih = input_edit(brand,show_type(brand,name_brand))
    brand[Pilih-1] = Edit


if __name__ == "__main__":
    os.system('pip install tabulate')
    clear_screen()
    show_menu_awal()