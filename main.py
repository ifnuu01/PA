import os
from tabulate import tabulate

admin ={
    "admin":"admin"
}
user ={
    "user":"user"
}


def main():
    while True:
        os.system('cls')
        print("""
Selamat Datang di E-Perpustakaan

Menu : 

Login Admin >> 1
Login User  >> 2
Registrasi  >> 3
Quit        >> 4

""")
        pilih = input("Pilih Menu : ")
        os.system('cls')
        if  pilih == "1":
            authAdmin()
        elif pilih == "2":
            authUser()
        elif pilih == "3":
            Registrasi()
        elif pilih == "4":
            exit()
        else:
            print("Noted : Pilih angka yang terdapat pada menu !")

def Auth_admin():
    gagal = 0
    while gagal < 3:
        username = input("Username : ")
        password = input("Password : ")
        os.system('cls')
        if username in admin and password == admin[username]:
            MenuAdmin()
        else:
            gagal += 1
            print(f"Login gagal ke {gagal}\nNoted : Batas login 3x")

def Auth_user():
    gagal = 0
    while gagal < 3:
        username = input("Username : ")
        password = input("Password : ")
        os.system('cls')
        if username in user and password == user[username]:
            print("Hai")
        else:
            gagal += 1
            print(f"Login gagal ke {gagal}\nNoted : Batas login 3x")

def Registrasi():
    username = input("Username baru : ")
    password = input("Password : ")
    os.system('cls')
    user.update({username:password})
