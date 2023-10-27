import os
# from tabulate import tabulate

Login = {
    "admin" : {"admin" : "admin"},
    "user"  : {"user"  : "user"}
}

# Database = {
#     "Merk"  : {"Samasung"   : [["Samsung J2 Prime",2,12,200000]],
#                "Infinix"    : [["Infinix Hot 11",6,128,24000000]] }
# }
# database = [{"Samsung" : [{"nama"   : "Samsung Galaxy",
#                         "Harga"     : 2000000},
#                         {"nama"     : "Samsung J2 Prime",
#                         "Harga"     : 2000000}]},
#             {"Infinix": [{"nama"    : "Infinix Galaxy",
#                         "Harga"     : 2000000}]} 
#             ]
# for data in database:
#     print('\n')
#     for i,j in data.items():
#         print(i)
#         for hp in j:
#             for key,data_hp in hp.items():
#                 print(data_hp)

def Auth_login():
    gagal = 0
    while gagal < 3:
        print("Menu Login \n")
        username = input("Username : ")
        password = input("password : ")
        os.system('clear')
        if username in Login["admin"] and password == Login["admin"][username]:
            print("yes admin")
        elif username in Login["user"] and password == Login["user"][username]:
            print("yes user")
        else:
            gagal += 1
            print(f"noted :  Login gagal ke {gagal} , jika gagal login 3x maka akan di keluarkan ke menu awal\n")

def Registrasi_user():
    print("Silahkan buat akun baru anda \n")
    username = input("Username : ")
    password = input("password : ")
    Login["user"].update({username : password})

def Show_menu_awal():
    while True:
        os.system('clear')
        print("""

 Toko Handphone                   
     Menu : 
================
              
Login       >> 1
Registrasi  >> 2
Exit        >> 3

""")
        pilih = input("Pilih Menu : ")
        os.system('clear')
        if  pilih == "1":
            Auth_login()
        elif pilih == "2":
            Registrasi_user()
        elif pilih == "3":
            exit()
        else:
            print("Noted : Pilih angka yang terdapat pada menu !")


if __name__ == "__main__":
    Show_menu_awal()