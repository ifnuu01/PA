#Variable Login user
Login = {
    "user"  : ["user",0,[]] #Index 0 sebagai pass , index 1 sebagai saldo , dan 2 sebagai keranjang
}


Database = {"Samsung"    : [["Samsung J2 Prime",2,16,"Snapdragon 888",200000],
                             ["Samsung Galaxy note",8,256,"Snapdragon 729",4500000],
                             ["Samsung Galaxy A24",8,128,"MT8781 Helio G99 (6nm)",2985000],
                             ["Samsung Galaxy A34 5G",8,128,"MediaTek Dimensity 1080",4125000],
                             ["Samsung Galaxy A54 5G",8,128,"Exynos 1380",4970000]],
            "Infinix"     : [["Infinix Hot 11",6,128,"MediaTek Helio G88",24000000],
                             ["Infinix GT 10 Pro",8,256,"Dimensity 8050 (6 nm)",3199000],
                             ["Infinix Hot 30 Play",4,64,"Helio G37 (12 nm)",1250000],
                             ["Infinix Hot 30",8,128,"Helio G88(12nm)",1540000],
                             ["Infinix Hot 30i",8,128,"Helio G37",1199000]],
            "Xiomi"       : [[]],
            "Oppo"        : [[]]
}

header = ["ID","Type HandPhone","Ram (Gb)","Storage (Gb)","Processor","Harga (Rp)"]

header_keranjang = ["ID", "Tipe HP", "Harga"]
Samsung = Database["Samsung"]
Infinix = Database["Infinix"]
