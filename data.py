# Variable Login user
Login = {
    "user": [
        "user",
        0,
        [],
    ]  # Index 0 sebagai password , index 1 sebagai saldo , dan index 2 sebagai keranjang
}


# Variable Database sebagai penampung dictioanaexitry dengan keyword Samsung , Infinix , Xiomi , dan Oppo
Database = {
    "Samsung": [
        ["Samsung J2 Prime",2,16,"Snapdragon 888",200000,],  # Sebuah Nasted List dengan Index0 , Tipe handphon, 1 Ram,2 Storage,3 Processor ,dan  4 Harga
        ["Samsung Galaxy note", 8, 256, "Snapdragon 729", 4500000],
        ["Samsung Galaxy A24", 8, 128, "MT8781 Helio G99 (6nm)", 2985000],
        ["Samsung Galaxy A34 5G", 8, 128, "MediaTek Dimensity 1080", 4125000],
        ["Samsung Galaxy A54 5G", 8, 128, "Exynos 1380", 4970000],
    ],
    "Infinix": [
        ["Infinix Hot 11", 6, 128, "MediaTek Helio G88", 24000000],
        ["Infinix GT 10 Pro", 8, 256, "Dimensity 8050 (6 nm)", 3199000],
        ["Infinix Hot 30 Play", 4, 64, "Helio G37 (12 nm)", 1250000],
        ["Infinix Hot 30", 8, 128, "Helio G88(12nm)", 1540000],
        ["Infinix Hot 30i", 8, 128, "Helio G37", 1199000],
    ],
    "Xiomi": [
        ["Redmi Note 11", 4, 64, "MediaTek Dimensity 810 5G (6 nm)", 2500000],
        ["Redmi Note 11 Pro", 4, 128, "Snapdragon 695 5G (6 nm)", 3500000],
        ["Redmi 9A", 2, 32, "Mediatek Helio G25 (12 nm)", 1200000],
        ["Poco M4 Pro", 6, 128, "MediaTek Helio G96", 3000000],
        ["Redmi 9C", 4, 64, "Mediatek Helio G35 (12 nm)", 1650000],
    ],
    "Oppo": [
        ["OPPO A98 5G", 8, 128, "Qualcomm® Snapdragon™ 695", 5000000],
        ["OPPO Reno10 Pro+ 5G", 12, 256, "Snapdragon® 8+ Gen 1", 11000000],
        ["OPPO Reno6 5G", 8, 128, "MediaTek Dimensity 900", 5700000],
        ["OPPO A18", 4, 128, "MediaTek Helio G85", 1800000],
        ["OPPO Find N3 Flip", 12, 256, "Mediatek Dimensity 9200", 16000000],
    ],
}

# Varibale header sebagai header untuk table
header = ["ID", "Type HandPhone", "Ram (Gb)", "Storage (Gb)", "Processor", "Harga (Rp)"]

# Pengaliasan dalam mengakses databases
header_keranjang = ["ID", "Tipe HP", "Harga"]
Samsung = Database["Samsung"]
Infinix = Database["Infinix"]
Xiaomi = Database["Xiomi"]
Oppo = Database["Oppo"]

#Variable untuk warna 
color_table = 'blue'
color_table2 = 'yellow'
color_table3 = "green"