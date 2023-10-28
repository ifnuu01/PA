import os
from tabulate import tabulate


Login = {
    "user"  : "user",
}


Database = {"Samasung"    : [["Samsung J2 Prime",2,16,"Snapdragon 888",200000],["Samsung Galaxy note",8,256,"Snapdragon 729",4500000]],
            "Infinix"     : [["Infinix Hot 11",6,128,"MediaTek Helio G88",24000000]]
}

header = ["ID","Type HandPhone","Ram (Gb)","Storage (Gb)","Processor","Harga (Rp)"]


def Clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def Auth_role():
    gagal = 0
    while gagal < 3:
        print("Menu Login \n")
        username = input("Username : ")
        password = input("password : ")
        Clear_screen()
        if username == "admin" and password == "admin":
            Show_menu_admin()
        elif username in Login and password == Login[username]:
            print("yes  user")
        else:
            gagal += 1
            print(f"noted :  Login gagal ke {gagal} , jika gagal login 3x maka akan di keluarkan ke menu awal\n")


def Registrasi_user():
    print("Silahkan buat akun baru anda \n")
    username = input("Username : ")
    password = input("password : ")
    Login.update({username : password})


def Show_menu_awal():
    while True:
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
        pilih = input("Pilih Menu : ")
        Clear_screen()
        if  pilih == "1":
            Auth_role()
        elif pilih == "2":
            Registrasi_user()
        elif pilih == "3":
            print("Terima kasih telah berkunjung")
            exit()
        else:
            print("Noted : Pilih angka yang terdapat pada menu !")

def Show_menu_admin():
    while True:
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
        pilih = input("Pilih menu : ")
        Clear_screen()
        if  pilih == "1":
            Read_handphone()
        elif pilih == "2":
            Registrasi_user()
        elif pilih == "3":
            print("Terima kasih telah berkunjung")
            exit()
        elif pilih == "4":
            print("d")
        elif pilih == "5":
            Show_menu_awal()
        else:
            print("Noted : Pilih angka yang terdapat pada menu !")

def Back_to_menu():
    input("\nTekan enter untuk kembali...")

def Read_handphone():
    while True:
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


def Show_type_samsung():
    Samsung = Database["Samasung"]
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


Read_handphone()

# if __name__ == "__main__":
#     os.system('pip install tabulate')
#     Clear_screen()
#     Show_menu_awal()