import os
"""
Project akhir
"""

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

def authAdmin():
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

def authUser():
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

def MenuAdmin():
    while True:
        print("""
DASHBOARD ADMIN
              
List Perpus >> 1
Tambah buku >> 2
Edit buku   >> 3
Hapus buku  >> 4
Log out     >> 5

""")
        pilih = input("Pilih Menu : ")    
        os.system('cls')
        if  pilih == "1":
            print("1")
        elif pilih == "2":
            print("1")
        elif pilih == "3":
            print("1")
        elif pilih == "4":
            print("1")
        elif pilih == "5":
            main()
        else:
            print("Noted : Pilih angka yang terdapat pada menu !")

if __name__ == "__main__":
    os.system('cls')
    main()