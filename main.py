import os
from data import Login,Database,header
from tabulate import tabulate

#Fungsi untuk membersihkan terminal
def Clear_screen():
    #Untuk os windows cls , dan linux clear
    os.system('cls' if os.name == 'nt' else 'clear')

#Fungsi login
def Auth_role():
    gagal = 0
    #Jika gagal login 3x maka while akan berhenti
    while gagal < 3:
        print("Menu Login \n")
        #variable username dan password untuk menampung inputan
        username = input("Username : ")
        password = input("password : ")
        Clear_screen()  
        #Jika username dan password terdetect sebagai admin maka akan masuk ke menu admin
        if username == "admin" and password == "admin":
            Show_menu_admin()
        #Jika terdetect sebagai user maka masuk ke menu user
        elif username in Login and password == Login[username]:
            print("yes  user")
        else:
            #Jika username dan password tidak ada di dalam role user / admin maka variable gagal akan di tambah 1 sebagai pembatas perulangan
            gagal += 1
            print(f"noted :  Login gagal ke {gagal} , jika gagal login 3x maka akan di keluarkan ke menu awal\n")

#Fungsi registrasi user
def Registrasi_user():
    print("Silahkan buat akun baru anda \n")
    #variable username dan password untuk menampung inputan
    username = input("Username : ")
    password = input("password : ")
    #Menambahkan username dan password ke dalam variable login atau bisa di sebut sebagai role user baru
    Login.update({username : password})

#Fungsi Show menu awal yaitu fungsi yang pertama di lihat oleh pengguna
def Show_menu_awal():
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
        Clear_screen()
        #Percabangan jika inputan pilih bernilai str 1 maka akan ke menu Auth_role
        if  pilih == "1":
            Auth_role()
        #Jika inputan pilih bernilai str 2 maka akan ke menu Registrasi_useer
        elif pilih == "2":
            Registrasi_user()
        #Jika inputan pilih bernilai str 3 maka memberhentikan program
        elif pilih == "3":
            print("Terima kasih telah berkunjung")
            exit()
        #Jika akan inputan pilih tidak terdapat pada menu maka akan di berikan peringatan seperti di bawah
        else:
            print("Noted : Pilih angka yang terdapat pada menu !")

#Fungsi show menu admin
def Show_menu_admin():
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
        Clear_screen()
        #Percabangan yang dimana ketika inputan bernilai str 1 maka akan masuk ke Fungsi Read_handphone
        if  pilih == "1":
            Read_handphone()
        #Jika inputan pilih bernilai str 2 maka akan masuk ke Fungsi Update_handphone
        elif pilih == "2":
            Update_handphone()
        #Jika inputan pilih bernilai str 3 maka akan masuk ke Fungsi Edit_handphone
        elif pilih == "3":
            print("Terima kasih telah berkunjung")
            exit()
        #Jika inputan pilih bernilai str 4 maka akan masuk ke Fungsi Delete_handphone
        elif pilih == "4":
            print("d")
        #Jika inputan pilih bernilai str 5 maka akan masuk ke Fungsi Show_menu_awal
        elif pilih == "5":
            Show_menu_awal()
        #Jika akan inputan pilih tidak terdapat pada menu maka akan di berikan peringatan seperti di bawah
        else:
            print("Noted : Pilih angka yang terdapat pada menu !")

def Back_to_menu():
    input("\nTekan enter untuk kembali...")

def Read_handphone():
    while True:
        Menu_read()
        pilih = input("Pilih no brand : ")
        Clear_screen()
        if pilih == "1":
            Show_type_samsung()
        elif pilih == "2":
            Show_type_infinix()
        elif pilih == "3":
            Show_menu_admin()
        else:
            print("Noted : Pilih angka yang terdapat pada menu !")

def Menu_read():
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

def Show_type_samsung():
    Samsung = Database["Samsung"]
    print("Brand Samsung")
    for i in range(len(Samsung)):Samsung[i].insert(0,i+1)
    print(tabulate(Samsung,headers=header,tablefmt="simple_grid"))
    for i in range(len(Samsung)):del Samsung[i][0]
    Back_to_menu()
    Clear_screen()

def Show_type_infinix():
    Infinix = Database["Infinix"]
    print("Brand Infinix")
    for i in range(len(Infinix)):Infinix[i].insert(0,i+1)
    print(tabulate(Infinix,headers=header,tablefmt="simple_grid"))
    for i in range(len(Infinix)):del Infinix[i][0]
    Back_to_menu()
    Clear_screen()


def Update_handphone():
    while True:
        Menu_read()
        Brand = input("Pilih brand yang mau di tambah : ")
        Clear_screen()
        if Brand == "1":
            Update_samsung()
        elif Brand =="2":
            Update_infinix()
        elif Brand == "3":
            Show_menu_admin()
        else:
            print("Noted : Pilih angka yang terdapat pada menu !")

def Input_update():
    while True:
        try:
            Type_handphone = input("Masukan type handphone : ")
            Ram            = int(input("Ram (Gb): "))
            Storage        = int(input("Storage / Penyimpanan (Gb): "))
            Processor      = input("Processor : ")
            Harga          = int(input("Harga : Rp"))
            return [Type_handphone,Ram,Storage,Processor,Harga]
        except ValueError:
            Clear_screen()
            print("Noted : Inputan tidak valid silahkan mengulang \n")


def Update_samsung():
    Samsung        = Database["Samsung"]
    Update         = Input_update()
    Samsung.append(Update)
    print("Noted : Data berhasil di tambahkan :) ")
    Update_handphone()

def Update_infinix():
    Infinix        = Database["Infinix"]
    Update         = Input_update()
    Infinix.append(Update)
    print("Noted : Data berhasil di tambahkan :) ")
    Update_handphone()
    

if __name__ == "__main__":
    os.system('pip install tabulate')
    Clear_screen()
    Show_menu_awal()