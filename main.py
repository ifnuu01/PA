import os
from tabulate import tabulate

admin ={
    "admin":"admin"
}
user ={
    "user":"user"
}

table = [["MTK",15000,5],
         ["BAHASA INDONESIA",15000,2],
         ["PANCASILA",15000,4],
         ["KARTINI",15000,5]]

header = ["ID","Judul buku","Harga Rp","Jumlah tersedia"]



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
            Display()
        elif pilih == "2":
            Create()
        elif pilih == "3":
            print("1")
        elif pilih == "4":
            print("1")
        elif pilih == "5":
            main()
        else:
            print("Noted : Pilih angka yang terdapat pada menu !")

def BackToMenuAdmin():
    while True:
        pilih = input("Kembali ke menu (y/n)? : ")
        os.system('cls')
        if pilih == "y":
            MenuAdmin()
        elif pilih =="n":
            break
        else:
            print("Pilih input y atua n saja !\n")

def Display():
    while True:
        print(tabulate(table,headers=header,showindex="always",tablefmt="heavy_grid"))
        BackToMenuAdmin()

def Create():
    while True:
        JumlahJudul = int(input("Masukan jumlah judul buku yang mau di tambah : "))
        angka = 0
        for i in range(JumlahJudul):
            angka += 1
            Judul   = input(f"Masukan judul buku ke {angka} : ")
            Harga   = int(input("Masukan harga buku : Rp"))
            Jumlah  = int(input("Masukan jumlah buku : "))
            os.system('cls')
            tambah = [Judul,Harga,Jumlah]
            table.append(tambah)
        print("Data buku berhasil di tambahkan! \n")
        BackToMenuAdmin()






if __name__ == "__main__":
    main()