#Variable Login user
Login = {
    "user"  : ["user",0,[]] #Index 0 sebagai pass , index 1 sebagai saldo , dan 2 sebagai keranjang
}

Database = {"Samsung"    : [["Samsung J2 Prime",2,16,"Snapdragon 888",200000],
                             ["Samsung Galaxy note",8,256,"Snapdragon 729",4500000]],
            "Infinix"     : [["Infinix Hot 11",6,128,"MediaTek Helio G88",24000000],]
}

header = ["ID","Type HandPhone","Ram (Gb)","Storage (Gb)","Processor","Harga (Rp)"]

header_keranjang = ["ID", "Tipe HP", "Harga"]

Samsung = Database["Samsung"]
Infinix = Database["Infinix"]
