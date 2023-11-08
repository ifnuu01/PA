import os
from data import Login,header,Samsung,Infinix,header_keranjang,Xiaomi,Oppo,color_table,color_table2,color_table3
from tabulate import tabulate 
from termcolor import colored
from colored import Fore, Style

#Fungsi untuk membersihkan terminal
def clear_screen():
    #Untuk os windows cls , dan linux clear
    os.system('cls' if os.name == 'nt' else 'clear')

#Fungsi back to menu atau pembatas
def back_to_menu():
    input(f"\n{Fore.yellow }Tekan enter untuk kembali...{Style.reset}")

#Fungsi login
def auth_role():
    gagal = 0
    #Jika gagal login 3x maka while akan berhenti
    while gagal < 3:
        table = tabulate([["Menu Login \n"]],tablefmt="double_grid")
        colored_table = colored(table, color_table, attrs=['bold'])
        print(colored_table)
        #variable username dan password untuk menampung inputan
        username = input(f"{Fore.blue}Username : {Style.reset}")
        password = input(f"{Fore.blue}password : {Style.reset}")
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
            print(tabulate([[f"{Fore.red}Noted :  Login gagal ke {gagal} , jika gagal login 3x maka akan di keluarkan ke menu awal{Style.reset}"]],tablefmt="double_grid"))
            #Fungsi back to menu atau sebagai pembatas
            back_to_menu()
            #Fungsi pembersih terminal
            clear_screen()

#Fungsi registrasi user
def registrasi_user():
    while True:
        table = tabulate([["Silahkan buat akun"]],tablefmt="double_grid")
        colored_table = colored(table, color_table, attrs=['bold'])
        print(colored_table)
        #variable username dan password untuk menampung inputan
        username = input(f"\n{Fore.blue}Username baru : {Style.reset}")
        if username in Login.keys():
            clear_screen()
            print(tabulate([[f"{Fore.red}Noted : Username telah di pakai , coba yang lain{Style.reset}"]],tablefmt="double_grid"))
            #Fungsi back to menu atau sebagai pembatas
            back_to_menu()
            #Fungsi pembersih terminal
            clear_screen()
        else:
            password = input(f"{Fore.blue}password baru : {Style.reset}")
            clear_screen()
            #Menambahkan username dan password ke dalam variable login atau bisa di sebut sebagai role user baru
            Login.update({username : [password,0,[]]})
            return

#Fungsi Show menu awal yaitu fungsi yang pertama di lihat oleh pengguna
def show_menu_awal():
    #Perulangan yang di mana menu akan terus di ulang jika tidak sesuai dengan inputan
    while True:
        #Menampilkan menu-menu yang terdapat pada menu awal
        tampilan = [["Login"],["Registrasi"],["Exit"]]
        table = tabulate(tampilan,headers=["No","Selamat Datang di Toko Handphone"],tablefmt="mixed_grid",showindex=range(1,len(tampilan)+1))
        colored_table = colored(table, color_table, attrs=['bold'])
        print(colored_table)
        #Varible pilih sebagai penampung inputan
        pilih = input(f"{Fore.blue}Pilih Menu : {Style.reset}")
        clear_screen()
        #Percabangan jika inputan pilih bernilai str 1 maka akan ke menu auth_role
        if  pilih == "1":
            auth_role()
        #Jika inputan pilih bernilai str 2 maka akan ke menu Registrasi_useer
        elif pilih == "2":
            registrasi_user()
        #Jika inputan pilih bernilai str 3 maka memberhentikan program
        elif pilih == "3":
            print(tabulate([[f"{Fore.green}Terima kasih telah berkunjung{Style.reset}"]],tablefmt="double_grid"))
            exit()
        #Jika akan inputan pilih tidak terdapat pada menu maka akan di berikan peringatan seperti di bawah
        else:
            print(tabulate([[f"{Fore.red}Noted : Pilih angka yang terdapat pada menu !{Style.reset}"]],tablefmt="double_grid"))
            #Fungsi back to menu atau sebagai pembatas
            back_to_menu()
            #Fungsi pembersih terminal
            clear_screen()

#Fungsi show menu admin
def show_menu_admin():
    #Perulangan yang di mana menu akan terus di ulang jika tidak sesuai dengan inputan
    while True:
        #Menampilkan menu-menu yang terdapat pada menu admin
        tampilan = [["List Handphone"],["Add Handphone"],["Edit Handphone"],["Delete Handphone "],["Logout"]]
        table = tabulate(tampilan,headers=["No","Dashboard Admin"],tablefmt="mixed_grid",showindex=range(1,len(tampilan)+1))
        colored_table = colored(table, color_table, attrs=['bold'])
        print(colored_table)
        #Varible pilih sebagai penampung inputan
        pilih = input(f"{Fore.blue}Pilih menu : {Style.reset}")
        clear_screen()
        #Percabangan yang dimana ketika inputan bernilai str 1 maka akan masuk ke Fungsi list_handphone
        if  pilih == "1":
            list_handphone()
        #Jika inputan pilih bernilai str 2 maka akan masuk ke Fungsi add_handphone
        elif pilih == "2":
            add_handphone()
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
            print(tabulate([[f"{Fore.red}Noted : Pilih angka yang terdapat pada menu !{Style.reset}"]],tablefmt="double_grid"))
            #Fungsi back to menu atau sebagai pembatas
            back_to_menu()
            #Fungsi pembersih terminal
            clear_screen()

#Fungsi menu read
def menu_read():
    #Menampung data yang ingin di tampilkan ke dalam variable tampilan
    tampilan = [["Samsung"],["Infinix"],["Xiaomi"],["Oppo"]]
    #Melakukan print dengan tabulate yang dimana headernya No,Daftar Brand, style table mixed_grid dengan memunculkan id berdasarkan range
    table = tabulate(tampilan,headers=["No","Daftar Brand"],tablefmt="mixed_grid",showindex=range(1,len(tampilan)+1))
    colored_table = colored(table, color_table, attrs=['bold'])
    print(colored_table)
    #Melakukan penambahan menu back 
    table2 = tabulate([["Back >> 5"]],tablefmt="double_grid")
    colored_table2 = colored(table2, color_table2, attrs=['bold'])
    print(colored_table2)

#Fungsi read handphone
def list_handphone():
    #Melakukan perulangan 
    while True:
        #Menampilkan fungsi yang ada pada menu read
        menu_read()
        #Variable pilih sebagai penampung inputan dari user
        pilih = input(f"{Fore.blue}Pilih no brand : {Style.reset}")
        #Fungsi membersihkan terminal
        clear_screen()
        #Percabangan di mana ketika inputan variable pilih bernilai 1 proses di bawah akan di jalankan
        if pilih == "1":
            #Memananggil dan mengambil nilai dari fungsi showtype
            print(show_type(Samsung,"Samsung",header))
            #Fungsi back to menu / pembatas
            back_to_menu()
            #Fungsi membersihkan terminal
            clear_screen()
        #Percabangan di mana ketika inputan variable pilih bernilai 2 proses di bawah akan di jalankan
        elif pilih == "2":
            #Memananggil dan mengambil nilai dari fungsi showtype
            print(show_type(Infinix,"Infinix",header))
            #Fungsi back to menu / pembatas
            back_to_menu()
            #Fungsi membersihkan terminal
            clear_screen()
        #Percabangan di mana ketika inputan variable pilih bernilai 3 proses di bawah akan di jalankan
        elif pilih == "3":
            #Memananggil dan mengambil nilai dari fungsi showtype
            print(show_type(Xiaomi,"Xiaomi",header))
            #Fungsi back to menu / pembatas
            back_to_menu()
            #Fungsi membersihkan terminal
            clear_screen()
        #Percabangan di mana ketika inputan variable pilih bernilai 4 proses di bawah akan di jalankan
        elif pilih == "4":
            #Memananggil dan mengambil nilai dari fungsi showtype
            print(show_type(Oppo,"Oppo",header))
            #Fungsi back to menu / pembatas
            back_to_menu()
            #Fungsi membersihkan terminal
            clear_screen()
        #Percabangan di mana ketika inputan variable pilih bernilai 5 proses di bawah akan di jalankan
        elif pilih == "5":
            #Fungsi show menu admin dimana ketika memilih inputan dengan nilai 5 maka akan jalan ke show menu admin
            show_menu_admin()
        #Percabangan ketika kondisi di atas tidak terpenuhi maka program di bawah akan di jalankan 
        else:
            #Ketika inputan tidak ada maka program di bawah akan di jalankan sebagai Noted/ peringatan
            print(tabulate([[f"{Fore.red}Noted : Pilih angka yang terdapat pada menu !{Style.reset}"]],tablefmt="double_grid"))
            #Fungsi back to menu atau sebagai pembatas
            back_to_menu()
            #Fungsi pembersih terminal
            clear_screen()


#Fungsi show type
def show_type(brand,name_brand,header):
    #Menampilkan table tipe hp dengan tabulate
    table2 = tabulate([[f"Daftar {name_brand}"]],tablefmt="double_grid")
    colored_table2 = colored(table2, color_table, attrs=['bold'])
    print(colored_table2)
    table = tabulate(brand,headers=header,tablefmt="simple_grid",showindex=range(1,len(brand)+1))
    colored_table = colored(table, color_table, attrs=['bold'])
    #Mengembalikan nilai dari variable table
    return colored_table

#FUngsi Update handphone
def add_handphone():
    #Melakukan perulangan tanpa batas
    while True:
        #Menampilkan fungsi dari menu read
        menu_read()
        #variable brand sebagai penampung dari inputan user
        Brand = input("Pilih brand yang mau di tambah : ")
        #Fungsi pembersi terminal
        clear_screen()
        #Percabangan dimana ketika inputan bernilai str 1 maka akan menjalankan program di bawah
        if Brand == "1":
            #Menjalankan fungsi dari update type dengan parameter / argument Variable Samsung dan str Samsung
            add_type(Samsung,"Samsung")
        #Percabangan dimana ketika inputan bernilai str 2 maka akan menjalankan program di bawah
        elif Brand =="2":
            #Menjalankan fungsi dari update type dengan parameter / argument Variable Infinix dan str Infinix
            add_type(Infinix,"Infinix")
        #Percabangan dimana ketika inputan bernilai str 3 maka akan menjalankan program di bawah
        elif Brand =="3":
            #Menjalankan fungsi dari update type dengan parameter / argument Variable Xiaomi dan str Xiaomi
            add_type(Xiaomi,"Xiaomi")
        #Percabangan dimana ketika inputan bernilai str 4 maka akan menjalankan program di bawah
        elif Brand =="4":
            #Menjalankan fungsi dari update type dengan parameter / argument Variable Oppo dan str Oppo
            add_type(Oppo,"Oppo")
        #Percabangan dimana ketika inputan bernilai str 5 maka akan menjalankan program di bawah
        elif Brand == "5":
            #Menjalankan fungsi show menu admin
            show_menu_admin()
        #Percabangan jika kondisi di atas tidak terpenuhi maka program di bawah ini akan di jalankan
        else:
            #Menampilkan Noted / peringatan 
            print(tabulate([[f"{Fore.red}Noted : Pilih angka yang terdapat pada menu !{Style.reset}"]],tablefmt="double_grid"))
            #Fungsi back to menu atau sebagai pembatas
            back_to_menu()
            #Fungsi pembersih terminal
            clear_screen()

#Fungsi update type
def add_type(brand,name_brand):
    #Memberikan Noted awal atau arahan dengan tabulate
    table = tabulate([[f"Masukan data baru tentang brand {name_brand}\n"]],tablefmt="double_grid")
    colored_table = colored(table, color_table, attrs=['bold'])
    print(colored_table)
    #Varibale update sebagai penampung dari nilai fungsi input update
    Update         = input_update()
    #Menambahkan data ke dalam database
    brand.append(Update)
    #Menampilkan Noted / peringatan dengan tabulate
    print(tabulate([[f"{Fore.green}Noted : Data berhasil di tambahkan :) {Style.reset}"]],tablefmt="double_grid"))
    #Fungsi back to menu atau sebagai pembatas
    back_to_menu()
    #Fungsi pembersih terminal
    clear_screen()
    #Fungsi update handphone
    add_handphone()

#Fungsi input update 
def input_update():
    #Melakukan perulangan
    while True:
        #try yaitu seperti namanya mengulang ketika expect terpenuhi
        try:
            table = tabulate([["Masukan Data : "]],tablefmt="double_grid")
            colored_table = colored(table, color_table, attrs=['bold'])
            print(colored_table)
            #Varibale type handphone , ram , storage , processor , dan harga sebagai penampung dari inputan user
            Type_handphone = input(f"{Fore.blue}Masukan type handphone : {Style.reset}")
            Ram            = int(input(f"{Fore.blue}Ram (Gb): {Style.reset}"))
            Storage        = int(input(f"{Fore.blue}Storage / Penyimpanan (Gb): {Style.reset}"))
            Processor      = input(f"{Fore.blue}Processor : {Style.reset}")
            Harga          = int(input(f"{Fore.blue}Harga : Rp{Style.reset}"))
            #Fungsi pembersi terminal
            clear_screen()
            if Harga < 0 or Ram < 0 or Storage < 0:
                print(tabulate([[f"{Fore.red}Noted : Inputan tidak valid silahkan mengulang {Style.reset}\n"]],tablefmt="double_grid"))
                #Fungsi back to menu atau sebagai pembatas
                back_to_menu()
                #Fungsi pembersih terminal
                clear_screen()
            else:
                #Mengembalikan nilai inputan di atas ke dalam list
                return [Type_handphone,Ram,Storage,Processor,Harga]
        #Expect berjalan atau berfungsi sebagai penanda jika terjadi ValueError di dalam inputan maka program di bawah akan dijalankan
        except ValueError:
            #Fungsi pembersih terminal
            clear_screen()
            #Menampilkan Noted / peringatan dengan tabulate
            print(tabulate([[f"{Fore.red}Noted : Inputan tidak valid silahkan mengulang {Style.reset}\n"]],tablefmt="double_grid"))
            #Fungsi back to menu atau sebagai pembatas
            back_to_menu()
            #Fungsi pembersih terminal
            clear_screen()

#Fungsi edit handphone 
def edit_handphone():
    #Melakukan perulangan 
    while True:
        #Menampilkan fungsi menu read
        menu_read()
        #Varibale brand sebagai penampung nilai dari inputan user
        Brand = input(f"{Fore.blue}Pilih brand dari type handphone yang mau di edit : {Style.reset}")
        #Fungsi pembersi terminal
        clear_screen()
        #Percabangan ketika nilai variable brand bernilai str 1 maka progran di bawah akan di jalankan
        if Brand == "1":
            #Menjalankan fungsi edit type dengan parameter/argumen Variable Samsung dan str Samsung
            edit_type(Samsung,"Samsung")
        #Percabangan ketika nilai variable brand bernilai str 2 maka progran di bawah akan di jalankan
        elif Brand =="2":
            #Menjalankan fungsi edit type dengan parameter/argumen Variable Infinix dan str Infinix
            edit_type(Infinix,"Infinix")
        #Percabangan ketika nilai variable brand bernilai str 3 maka progran di bawah akan di jalankan
        elif Brand =="3":
            #Menjalankan fungsi edit type dengan parameter/argumen Variable Xiaomi dan str Xiaomi
            edit_type(Xiaomi,"Xiaomi")
        #Percabangan ketika nilai variable brand bernilai str 4 maka progran di bawah akan di jalankan
        elif Brand =="4":
            #Menjalankan fungsi edit type dengan parameter/argumen Variable Oppo dan str Oppo
            edit_type(Oppo,"Oppo")
        #Percabangan ketika nilai variable brand bernilai str 5 maka progran di bawah akan di jalankan
        elif Brand == "5":
            #Menjalankan funsgi show menu admin atau kembali ke dashboard admin
            show_menu_admin()
        #Percabangan ketika kondisi di atas tidak terpenuhi 
        else:
            #Menampilkan Noted / peringatan dengan tabulate
            print(tabulate([[f"{Fore.red}Noted : Pilih angka yang terdapat pada menu !{Style.reset}"]],tablefmt="double_grid"))
            #Fungsi back to menu atau sebagai pembatas
            back_to_menu()
            #Fungsi pembersih terminal
            clear_screen()

#Fungsi edit type
def edit_type(brand,name_brand):
    #Melakukan perulangan
    while True:
        #Pernyataan try sebagai menajalankan python kode yang di sebabkan karena pengecualian 
        try:
            #Menampilkan table tipe hp dengan fungsi show type dan argument brand, name_brand, dan header
            print(show_type(brand,name_brand,header))
            #Variable pilih sebagai penampung inputan dari user 
            pilih = int(input(f"{Fore.blue}Pilih ID yang mau di edit : {Style.reset}"))
            #Fungsi pembersih terminal 
            clear_screen()
            #Percabangan jika panjang dari brand atau list dari tipe handphone kurang atau sama dengan 0 maka blok kode di bawah akan di jalankan 
            if len(brand) <= 0 :
                #Menampilkan Noted / peringatan dengan tabulate 
                print(tabulate([[f"{Fore.red}Tidak ada handphone yang tersedia{Style.reset}"]],tablefmt="double_grid"))
                #Fungsi back to menu atau pembatas
                back_to_menu()
                #Fungsi pembersih terminal
                clear_screen()
                #Fungsi show menu admin 
                show_menu_admin()
            #Ketika kondisi di atas tidak terpenuhi maka blok kode di bawah akan di jalankan 
            else:
                #Percabangan jika nilai dari variable pilih berada atau  ada di dalam list yang menampung ID dari tipe handphone 
                if pilih in [i+1 for i in range(len(brand))]:
                    #Menampilkan Noted / peringatan dengan tabulate
                    table = tabulate([["Masukan data baru \n "]],tablefmt="double_grid")
                    colored_table = colored(table, color_table, attrs=['bold'])
                    print(colored_table)
                    #Varibale edit sebagai penampung dari nilai fungsi input update
                    edit = input_update()
                    #Fungsi pembersih terminal
                    clear_screen()
                    #Melukan changes nilai di dalam database yang di inginkan
                    brand[pilih-1] = edit
                    #Menampilkan Noted / peringatan dengan tabulate
                    print(tabulate([[f"{Fore.green}Noted : data berhasil di edit{Style.reset}"]],tablefmt="double_grid"))
                    #Fungsi back to menu atau sebagai pembatas
                    back_to_menu()
                    #Fungsi pembersih terminal
                    clear_screen()
                    #Mengembalikan nilai kosong atau return tanpa nilai untuk keluar dari fungsi dan mengembalikan kembali ke pemanggil fungsi 
                    return
                #Percabangan ketika kondisi di atas tidak terpenuhi maka blok kode di bawah ini akan di jalankan 
                else:
                    #Menampilkan Noted / peringatan
                    print(tabulate([[f"{Fore.red}Noted : ID yang anda inputkan tidak ada{Style.reset}\n"]],tablefmt="double_grid"))
        #Excpect Sebagai menangani pengecualian agar tidak terjadi ValueError di dalam inputan 
        except ValueError:
            #Fungsi pembersih terminal
            clear_screen()
            #Menampilkan Noted / peringatan
            print(tabulate([[f"{Fore.red}Noted : ID yang anda inputkan tidak ada{Style.reset}\n"]],tablefmt="double_grid"))
            #Fungsi back to menu atau sebagai pembatas
            back_to_menu()
            #Fungsi pembersih terminal
            clear_screen()

#Fungsi delete handphone 
def delete_handphone():
    #Melakukan perulangan 
    while True:
        #Menampilkan fungsi menu read 
        menu_read()
        #Varibale brand sebagai penampung inputan user
        Brand = input(f"{Fore.blue}Pilih brand dari type handphone yang mau di hapus : {Style.reset}")
        #Fungsi pembersih terminal
        clear_screen()
        #Percabangan jika nilai dari varible brand bernilai str 1 maka blok kode di bawah di jalankan
        if Brand == "1":
            #Menjalakan fungsi delete type dengan parameter / argument Varible Samsung, dan str Samsung
            delete_type(Samsung,"Samsung")
        #Percabangan jika nilai dari varible brand bernilai str 2 maka blok kode di bawah di jalankan
        elif Brand =="2":
            #Menjalakan fungsi delete type dengan parameter / argument Varible Infinix, dan str Infinix
            delete_type(Infinix,"Infinix")
        #Percabangan jika nilai dari varible brand bernilai str 3 maka blok kode di bawah di jalankan
        elif Brand =="3":
            #Menjalakan fungsi delete type dengan parameter / argument Varible Xiaomi, dan str Xiaomi
            delete_type(Xiaomi,"Xiaomi")
        #Percabangan jika nilai dari varible brand bernilai str 4 maka blok kode di bawah di jalankan
        elif Brand =="4":
            #Menjalakan fungsi delete type dengan parameter / argument Varible Oppo, dan str Oppo
            delete_type(Oppo,"Oppo")
        #Percabangan jika nilai dari varible brand bernilai str 5 maka blok kode di bawah di jalankan
        elif Brand == "5":
            #Menjalankan fungsi show menu admin
            show_menu_admin()
        #Percabangan ketika kondisi di atas tidak terpenuhi maka blok kode di bawah akan di jalankan
        else:
            #Menampilkan Noted / peringatan dengan tabulate
            print(tabulate([[f"{Fore.red}Noted : Pilih angka yang terdapat pada menu !{Style.reset}"]],tablefmt="double_grid"))
            #Fungsi back to menu atau sebagai pembatas
            back_to_menu()
            #Fungsi pembersih terminal
            clear_screen()
        
#Fungsi delete type dengan parameter / argument brand , name_akun
def delete_type(brand,name_brand):
    #Melakukan perulangan 
    while True:
        #Pernyataan "try" digunakan untuk mencoba menjalankan potongan kode yang mungkin menyebabkan pengecualian
        try:
            #Menampilkan fungsi showtype dengan parameter / argument variable brand , nama _brand , dan header
            print(show_type(brand,name_brand,header))
            #Variable pilih sebagai penampung dari inputan user
            pilih = int(input(f"{Fore.blue}Pilih ID yang mau di hapus : {Style.reset}"))
            #Fungsi pembersih terminal
            clear_screen()
            #Percabangan dimana ketika panjang dari brand / tipe handphone lebih kecil atua samadengan 0 maka blok kode di bawah akan di jalakan
            if len(brand) <= 0 :
                #Menampilkan Noted / peringatan dengan tabulate
                print(tabulate([[f"{Fore.red}Tidak ada handphone yang tersedia{Style.reset}"]],tablefmt="double_grid"))
                #Fungsi back to menu / pembatas
                back_to_menu()
                #Fungsi pembersih terminal
                clear_screen()
                #Memanggil fungsi show menu admin / kembali ke menu dashboard admin
                show_menu_admin()
            #Percabangan , ketika kondisi di atas tidak terpenuhi maka blok kode di bawah akan di jalankan
            else:
                #Percabangan ketika nilai dari variable pilih ada dalam list yang menampung panjang / ID dari tipe hp maka blok kode di bawah akan di jalankan
                if pilih in [i+1 for i in range(len(brand))]:
                    #Menghapus tipe hp berhadasarkan ID yang di pilih
                    del brand[pilih-1]
                    #Menampilkan Noted / peringatan dengan tabulate 
                    print(tabulate([[f"{Fore.green}Noted : data berhasil di hapus{Style.reset}"]],tablefmt="double_grid"))
                    #Fungsi back to menu atau sebagai pembatas
                    back_to_menu()
                    #Fungsi pembersih terminal
                    clear_screen()
                    #Mengembalikan nilai kosong atau return tanpa nilai untuk keluar dari fungsi dan mengembalikan kembali ke pemanggil fungsi 
                    return
                #Percabangan ketika kondisi di atas tidak terpenuhi
                else:   
                    #Menampikan Noted / peringatan dengan tabulate 
                    print(tabulate([[f"{Fore.red}Noted : ID yang anda inputkan tidak ada{Style.reset}\n"]],tablefmt="double_grid"))
                    #Fungsi back to menu atau sebagai pembatas
                    back_to_menu()
                    #Fungsi pembersih terminal
                    clear_screen()
        #Excpect Sebagai menangani pengecualian agar tidak terjadi ValueError di dalam inputan 
        except ValueError:
            #Fungsi pembersih terminal
            clear_screen()
            #Menampilkan Noted / peringatan
            print(tabulate([[f"{Fore.red}Noted : ID yang anda inputkan tidak ada{Style.reset}\n"]],tablefmt="double_grid"))
            #Fungsi back to menu atau sebagai pembatas
            back_to_menu()
            #Fungsi pembersih terminal
            clear_screen()

#Fungsi show menu user dengan parameter atau argument nama_akun
def show_menu_user(nama_akun):
    #Melakukan perulangan 
    while True:
        #Variable table sebagai penampung dari nasted list 
        table = [["Isi saldo"],["list Produk"],["Keranjang"],["Log Out"],["Exit"]]
        #Variable header_table yang nnt berfungsi sebagai header dari table
        header_table = ["No","Selamat Datang di TokoHanphone"]
        #Menampilkan table dengan tabulate yang dmn isinya ialah variable table dan headernya : variable header_table , dengan showindex berdasarkan range yang berguna sebagai ID, dengan styke double_grid
        table = tabulate(table,headers=header_table,showindex=range(1,6),tablefmt="double_grid")
        colored_table = colored(table, color_table, attrs=['bold'])
        print(colored_table)
        #Menampilkan saldo user
        table2 = tabulate([[f"Saldo anda saat ini >> Rp.{Login[nama_akun][1]}"]],tablefmt="double_grid")
        colored_table = colored(table2, color_table3, attrs=['bold'])
        print(colored_table)
        #Variable pilihan_user sebagai penampung inputan user 
        pilihan_user = input(f"{Fore.blue}Pilih menu: {Style.reset}")
        #Fungsi pembersih terminal 
        clear_screen()
        #Percabangan ketika kondisi dari nilai variable pilihan_user bernilai str 1 makak blok kode di bawah di jalankan 
        if pilihan_user == "1":
            #Memanggil fungsi top_up dengan argument / parameter nama_akun
            top_up(nama_akun)
        #Percabangan ketika kondisi dari nilai variable pilihan_user bernilai str 2 makak blok kode di bawah di jalankan 
        elif pilihan_user == "2":
            #Memanggil fungsin read handphone user dengan parameter / argument nama_akun
            list_handphone_user(nama_akun)
        #Percabangan ketika kondisi dari nilai variable pilihan_user bernilai str 3 makak blok kode di bawah di jalankan 
        elif pilihan_user == "3":
            #Memanggil fungsi keranjang dengan parameter / argument nama_akun
            keranjang(nama_akun)
        #Percabangan ketika kondisi dari nilai variable pilihan_user bernilai str 4 makak blok kode di bawah di jalankan 
        elif pilihan_user == "4":
            #Memanggil fungsi show menu awal / kembali ke menu awal 
            show_menu_awal()
        #Percabangan ketika kondisi dari nilai variable pilihan_user bernilai str 5 makak blok kode di bawah di jalankan 
        elif pilihan_user == "5":
            #Menampilkan Noted 
            print(tabulate([[f"{Fore.green}Terima kasih telah berkunjung{Style.reset}"]],tablefmt="double_grid"))
            #Keluar dari program 
            exit()
        #Percabangan ketika kondisi di atas tidak terpenuh maka blok kode di bawah akan di jalankan 
        else:
            #Menampilkan Noted / peringatan dengan tabulate
            print(tabulate([[f"{Fore.red}Noted : Pilih angka yang terdapat pada menu !{Style.reset}"]],tablefmt="double_grid"))
            #Fungsi back to menu atau sebagai pembatas
            back_to_menu()
            #Fungsi pembersih terminal
            clear_screen()

#Fungsi top up dengan parameter nama_akun
def top_up(nama_akun):
    #Melakukan perulangan
    while True:
        #Pernyataan "try" digunakan untuk mencoba menjalankan potongan kode yang mungkin menyebabkan pengecualian
        try:
            #Menampilkan saldo 
            table = tabulate([[f"Saldo anda saat ini berjumlah {Login[nama_akun][1]}\n"]],tablefmt="double_grid")
            colored_table = colored(table, color_table3, attrs=['bold'])
            print(colored_table)
            #Variable top_up sebagai penampung inputan user
            top_up = int(input(f"{Fore.blue}Masukan nominal top up : Rp{Style.reset}")) 
            #Fungsi pembersih terminal 
            clear_screen()
            if top_up > 0: 
                #Menambahkan saldo 
                Login[nama_akun][1] += top_up
                #Menampilkan Noted / peringatan dengan tabulate
                print(tabulate([[f"{Fore.green}Noted : Anda berhasil top up{Style.reset}"]],tablefmt="double_grid"))
                back_to_menu()
                #Fungsi pembersih terminal 
                clear_screen()
                show_menu_user(nama_akun)
            else:
                print(tabulate([[f"{Fore.red}Noted : Nominal harus lebih besar dari nol (0) {Style.reset}"]],tablefmt="double_grid"))
                #Fungsi back to menu atau sebagai pembatas
                back_to_menu()
                #Fungsi pembersih terminal
                clear_screen()
        #Excpect Sebagai menangani pengecualian agar tidak terjadi ValueError di dalam inputan 
        except ValueError:
            clear_screen()
            #Menampilkan Noted / peringatan dengan tabulate
            print(tabulate([[f"{Fore.red}Inputan anda tikak valid{Style.reset}"]],tablefmt="double_grid"))
            #Fungsi back to menu atau sebagai pembatas
            back_to_menu()
            #Fungsi pembersih terminal
            clear_screen()

def list_handphone_user(nama_akun):
    #Melakukan perulangan 
    while True:
        #Menampilkan fungsi menu_read
        menu_read()
        #Variable pilih sebagai penampung inputan dari user
        pilih = input(f"{Fore.blue}Pilih no brand : {Style.reset}")
        #Fungsi pembersih terminal 
        clear_screen()
        #Percabangan ketika kondisi dari nilai variable pilihan_user bernilai str 1 makak blok kode di bawah di jalankan 
        if pilih == "1":
            #Memanggil fungsi show type user dengan parameter / argument Samsung, Str Samsung , dan nama_akun
            show_type_user(Samsung,"Samsung",nama_akun)
        #Percabangan ketika kondisi dari nilai variable pilihan_user bernilai str 2 makak blok kode di bawah di jalankan 
        elif pilih == "2":
            #Memanggil fungsi show type user dengan parameter / argument Infinix, Str Infinix , dan nama_akun
            show_type_user(Infinix,"Infinix",nama_akun)
        #Percabangan ketika kondisi dari nilai variable pilihan_user bernilai str 3 makak blok kode di bawah di jalankan 
        elif pilih == "3":
            #Memanggil fungsi show type user dengan parameter / argument Xiaomi, Str Xiaomi , dan nama_akun
            show_type_user(Xiaomi,"Xiaomi",nama_akun)
        #Percabangan ketika kondisi dari nilai variable pilihan_user bernilai str 4 makak blok kode di bawah di jalankan 
        elif pilih == "4":
            #Memanggil fungsi show type user dengan parameter / argument Oppo, Str Oppo , dan nama_akun
            show_type_user(Oppo,"Oppo",nama_akun)
        #Percabangan ketika kondisi dari nilai variable pilihan_user bernilai str 5 makak blok kode di bawah di jalankan 
        elif pilih == "5":
            #Memanggil fungsi show menu user dengan parameter / argument nama_akun / kembali ke menu user
            show_menu_user(nama_akun)
        #Percabangan ketika kondisi di atas tidak terpenuh maka blok kode di bawah akan di jalankan 
        else:
            #Menampilkan Noted / peringatan dengan tabulate
            print(tabulate([[f"{Fore.red}Noted : Pilih angka yang terdapat pada menu !{Style.reset}"]],tablefmt="double_grid"))
            #Fungsi back to menu atau sebagai pembatas
            back_to_menu()
            #Fungsi pembersih terminal
            clear_screen()

#Fungsi show type user 
def show_type_user(brand,name_brand,nama_akun):
    #Melakukan perulangan
    while True:
        #Menampilkan fungsi show type dengan parameter / argument brand , nama_brand , dan header
        print(show_type(brand,name_brand,header))
        #Variable pilihan sebagai penampung dari inputan user
        pilihan = input(f"{Fore.blue}ingin memasukan produk ke keranjang ({Fore.green}y/{Fore.red}n{Fore.blue}) :{Style.reset}")
        #Fungsi pembersih terminal 
        clear_screen()
        #Percabangan jika nilai dari variable pilihan sama dengan str y maka blok kode di bawah akan di jalankan
        if pilihan == "y":
            #Percabangan jika panjang dari brand lebih kecil atau sama dengan 0 maka blok kode di bawah akan di jalankan
            if len(brand) <= 0 :
                #Menampilakn Noted / peringatan dengan tabulate 
                print(tabulate([[f"{Fore.red}Tidak ada handphone yang tersedia{Style.reset}"]],tablefmt="double_grid"))
                #Fungsi back to menu / pembatas
                back_to_menu()
                #Fungsi pembersih terminal 
                clear_screen()
                #Memanggil fungsi show menu user / kembali ke menu user
                show_menu_user(nama_akun)
            #Percabangan ketika kondisi di atas tidak terpenuh maka blok kode di bawah akan di jalankan 
            else:
                #Memanggil fungsi masuk keranjang dengan parameter / argument brand,name_brand, nama_akun
                masuk_keranjang(brand,name_brand,nama_akun)
             #menambahkan ke keranjang
        #Percabangan jika nilai dari variable pilihan sama dengan str n maka blok kode di bawah akan di jalankan
        elif pilihan =="n":
            #Memanggil fungsi read handphone user dengan parameter nama_akun
            list_handphone_user(nama_akun)
        #Percabangan ketika kondisi di atas tidak terpenuh maka blok kode di bawah akan di jalankan 
        else:
            #Menampilkan Noted / peringatan dengan tabulate
            print(tabulate([[f"{Fore.red}Noted : Pilih {Fore.green}y / {Fore.red}n !! , Silahkan ulangi{Style.reset}\n"]],tablefmt="double_grid"))
            #Fungsi back to menu atau sebagai pembatas
            back_to_menu()
            #Fungsi pembersih terminal
            clear_screen()

#Fungsi masuk keranjang 
def masuk_keranjang(brand,name_brand,nama_akun):
    #Melakukan perulangan
    while True:
        #Pernyataan "try" digunakan untuk mencoba menjalankan potongan kode yang mungkin menyebabkan pengecualian
        try:
            print(show_type(brand,name_brand,header))
            pilih = int(input(f"{Fore.blue}Masukan ID handphone yang mau di masukan ke keranjang : {Style.reset}"))
            #Fungsi pembersih terminal 
            clear_screen()
            #Percabangan , ketika nilai dari variable pilih ada di dalam list yang menampung angka ID maka blok kode di bawah akan di jalankan
            if pilih in [i+1 for i in range(len(brand))]:
                #Variable produk menampunh brand dengan index pilih -1 dan mengakses index 0 yaitu nama produk
                produk = brand[pilih - 1][0]
                #Variable harga menampunh brand dengan index pilih -1 dan mengakses index 4 yaitu Harga produk
                harga = brand[pilih -1 ][4]
                #Variable keranjang menampunh list dengan isinya variable produk dan harga
                keranjang = [produk,harga]
                #Menambahkan keranjang ke database
                Login[nama_akun][2].append(keranjang)
                #Menampilkan Noted / peringatan dengan tabulate
                print(tabulate([[f"{Fore.green}Data berhasil di masukan ke keranjang{Style.reset}\n"]],tablefmt="double_grid"))
                #Fungsi back to menu / pembatas
                back_to_menu()
                #Fungsi pembersih terminal
                clear_screen()
                #Memanggil fungsi show menu user / kembali ke menu user
                show_menu_user(nama_akun)
            #Percabangan ketika kondisi di atas tidak terpenuh maka blok kode di bawah akan di jalankan 
            else:
                #Menampilkan Noted / peringatan dengan tabulate
                print(tabulate([[f"{Fore.red}Noted : ID yang anda inputkan tidak ada{Style.reset}\n"]],tablefmt="double_grid"))
                #Fungsi back to menu atau sebagai pembatas
                back_to_menu()
                #Fungsi pembersih terminal
                clear_screen()
        #Excpect Sebagai menangani pengecualian agar tidak terjadi ValueError di dalam inputan 
        except ValueError:
            #Fungsi pembersih terminal 
            clear_screen()
            #Menampilkan Noted / peringatan dengan tabulate
            print(tabulate([[f"{Fore.red}Noted : ID yang anda inputkan tidak ada{Style.reset}\n"]],tablefmt="double_grid"))
            #Fungsi back to menu atau sebagai pembatas
            back_to_menu()
            #Fungsi pembersih terminal
            clear_screen()

#Fungsi keranjang dengan parameter atau brand 
def keranjang(nama_akun):
    #Melakukan perulangan
    while True:
        #Variable keranjang_akun sebagai alias dari Login[nama_akun][2]
        keranjang_akun = Login[nama_akun][2]
        #Menampilkan fungsi show type dengan parameter / argument keranjang_akun , str Keranjang , dan header_keranjang
        print(show_type(keranjang_akun,"Keranjang",header_keranjang))
        #Variable pilihan chekcout sebagai penampung dari inputan user
        Pilihan_checkout= input(f"{Fore.blue}Apakah ada barang yang ingin di check out({Fore.green}y/{Fore.red}n{Fore.blue}): {Style.reset}")
        #Fungsi pembersih terminal 
        clear_screen()
        #Percabangan dimana ketika nilai dari variable Pilihan_checkout sama dengan str y maka blok kode di bawah akan di jalankan
        if  Pilihan_checkout == "y":
            #Percabangan jika len keranjang akun lebih kecil atau sama dengan 0 maka blok kode di bawah akan di jalankan
            if len(keranjang_akun) <= 0 :
                #Menampilkan Noted / peringatan dengan tabulate
                print(tabulate([[f"{Fore.red}Noted : Keranjang Anda Kosong{Style.reset}"]],tablefmt="double_grid"))
                #Fungsi back to menu / pembatas
                back_to_menu()
                #Fungsi pembersih terminal
                clear_screen()
                #Memanggil fungsi show menu user / kembali ke menu user
                show_menu_user(nama_akun)
            #Percabangan ketika kondisi di atas tidak terpenuh maka blok kode di bawah akan di jalankan 
            else:
                #Memanggil fungsi Check out
                check_out(nama_akun, keranjang_akun)
        #Percabangan dimana ketika nilai dari variable Pilihan_checkout sama dengan str n maka blok kode di bawah akan di jalankan
        elif Pilihan_checkout == "n":
            #Memanggil fungsi show menu user
            show_menu_user(nama_akun)
        #Percabangan ketika kondisi di atas tidak terpenuh maka blok kode di bawah akan di jalankan 
        else:
            #Menampilkan Noted / peringatan dengan tabulate
            print(tabulate([[f"{Fore.red}Noted : Pilih {Fore.green}y / {Fore.red}n !!, Silahkan ulangi lagi{Style.reset}\n"]],tablefmt="double_grid"))
            #Fungsi back to menu atau sebagai pembatas
            back_to_menu()
            #Fungsi pembersih terminal
            clear_screen()

#Fungsi Checkout
def check_out(nama_akun, keranjang_akun):
    #Melakukan perulangan
    while True: 
        try:
            #Menampilkan keranjang dari user
            print(show_type(keranjang_akun,"Keranjang",header_keranjang))
            #Memasukkan pilihan barang yang ingin di checkout
            ID_checkout = int(input(f"{Fore.blue}Masukkan ID hanphone yang mau di check out: {Style.reset}"))
            #Fungsi pembersih terminal 
            clear_screen()
            #Percabangan ketika barang yang ingin di checkout terdapat pada keranjang
            if ID_checkout in [i+1 for i in range(len(Login[nama_akun][2]))]:        
                barang_checkout= Login[nama_akun][2][ID_checkout-1]
                #Menampilkan saldo user
                table = tabulate([[f"Saldo anda saat ini adalah Rp. {Login[nama_akun][1]}\n"]],tablefmt="double_grid")
                colored_table = colored(table, color_table3, attrs=['bold'])
                print(colored_table)
                #Mengkonfirmasi transaksi user
                Transaksi = input(f"{Fore.blue}Apakah anda ingin melanjutkan transaksi({Fore.green}y/{Fore.red}n{Fore.blue}): {Style.reset}")
                #Fungsi pembersih terminal 
                clear_screen()
                #Percabangan ketika user ingin melanjutkan transaksi
                if Transaksi == "y":
                    #Percabangan jika saldo user tidak cukup
                    if Login[nama_akun][1] < barang_checkout[1]:
                        #Menampilkan Noted / peringatan dengan tabulate
                        print(tabulate([[f"{Fore.red}Noted : Saldo Tidak Cukup{Style.reset}\n"]],tablefmt="double_grid"))
                        back_to_menu()
                        #Fungsi pembersih terminal 
                        clear_screen()
                        show_menu_user(nama_akun)
                    #Percabangan ketika saldo user cukup 
                    else:
                        #Menghitung sisa saldo
                        sisa_saldo = Login[nama_akun][1]-barang_checkout[1]
                        #Menyimpan sisa saldo user ke database
                        Login[nama_akun][1] = sisa_saldo
                        #Memanggil fungsi display struk
                        display_struk(nama_akun,ID_checkout)
                        #Menghapus barang yang dibeli dari keranjang
                        del Login[nama_akun][2][ID_checkout-1]
                        back_to_menu()
                        #Fungsi pembersih terminal 
                        clear_screen()
                        #Fungsi menampilkan menu user
                        show_menu_user(nama_akun)
                #Percabangan ketika user tidak ingin melanjutkan transaksi
                elif Transaksi =="n":
                    #Menampilkan Noted / peringatan dengan tabulate
                    print(tabulate([[f"{Fore.red}Transaksi gagal{Style.reset}"]],tablefmt="double_grid"))
                    #Fungsi back to menu / pembatas
                    back_to_menu()
                    #Fungsi pembersih terminal 
                    clear_screen()
                    #Fungsi menampilkan menu user
                    show_menu_user(nama_akun)
                #Percabangan ketika kondisi di atas tidak terpenuh maka blok kode di bawah akan di jalankan 
                else:
                    #Menampilkan Noted / peringatan dengan tabulate
                    print(tabulate([[f"{Fore.red}Noted : Pilih {Fore.green}y / {Fore.red}n !! Silahkan ulangi {Style.reset}\n"]],tablefmt="double_grid"))
                    #Fungsi back to menu atau sebagai pembatas
                    back_to_menu()
                    #Fungsi pembersih terminal
                    clear_screen()
            #Percabangan ketika kondisi di atas tidak terpenuh maka blok kode di bawah akan di jalankan 
            else:
                #Menampilkan Noted / peringatan dengan tabulate
                print(tabulate([[f"{Fore.red}Noted : Masukan ID yang tertera pada keranjang , Silahkan ulangi dari awal{Style.reset}\n"]],tablefmt="double_grid"))
                #Fungsi back to menu atau sebagai pembatas
                back_to_menu()
                #Fungsi pembersih terminal
                clear_screen()
        except ValueError:
            #Fungsi pembersih terminal
            clear_screen()
            #Menampilkan Noted / peringatan dengan tabulate
            print(tabulate([[f"{Fore.red}Noted : Masukan ID yang tertera pada keranjang , Silahkan ulangi dari awal{Style.reset}\n"]],tablefmt="double_grid"))
            #Fungsi back to menu atau sebagai pembatas
            back_to_menu()
            #Fungsi pembersih terminal
            clear_screen()

#Fungsi untuk display struk
def display_struk(nama_akun,ID_checkout):
    #Membuat header untuk struk
    header_table = [f"{Fore.green}Selamat Pembayaran Anda Berhasil{Style.reset  }"]
    #Menyimpan data produk yang ingin di checkout dalam sebuah lisy
    table = [[f"Nama Produk   : {Login[nama_akun][2][ID_checkout-1][0]}"],[f"Total Harga   : Rp {Login[nama_akun][2][ID_checkout-1][1]}"]]
    #Menampilkan list dengan menggunakan tabel
    table = tabulate(table,headers=header_table,tablefmt="double_grid")
    colored_table = colored(table, color_table, attrs=['bold'])
    print(colored_table)

#Menjalakan fungsi
if __name__ == "__main__":
    os.system('pip install tabulate')
    #Fungsi pembersih terminal 
    clear_screen()
    #Memanggil fungsi awal
    show_menu_awal()