import os
from tabulate import tabulate

Login = {
    "user"  : "user",
}

Database = {"Samasung"    : [["Samsung J2 Prime",2,16,"Snapdragon 888",200000],["Samsung Galaxy note",8,256,"Snapdragon 729",4500000]],
            "Infinix"     : [["Infinix Hot 11",6,128,"MediaTek Helio G88",24000000]]
}



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
            print("yes admin")
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

 Toko Handphone                   
     Menu : 
================
              
Login       >> 1
Registrasi  >> 2
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


if __name__ == "__main__":
    os.system('pip install tabulate')
    Clear_screen()
    Show_menu_awal()