
def tampilkan_tipe_pembangunan():
    print("Memilih tipe pembangunan")
    print("1. Gor")
    print("2. Aula")
    print("3. Rumah Satu Lantai")
    
    kriteria = input("Masukkan kode kriteria yang ingin dipilih (1/2/3): ")
    luas_tanah = float(input("Masukkan luas tanah (dalam meter persegi): "))
    if kriteria == "1":
        harga_bahan_bangunan_per_m2 = 1500000
    elif kriteria == "2":
        harga_bahan_bangunan_per_m2 = 2000000
    elif kriteria == "3":
        harga_bahan_bangunan_per_m2 = 1200000
    else:
        print("Kriteria yang dimasukkan tidak valid.")
        exit()
        
    # Estimasi biaya konstruksi
    biaya_konstruksi = luas_tanah * harga_bahan_bangunan_per_m2
    # Estimasi biaya lainnya (biaya perizinan, biaya cadangan, dll)
    biaya_lainnya = 0.3 * biaya_konstruksi
    # Total estimasi biaya pembangunan
    total_biaya = biaya_konstruksi + biaya_lainnya
    # menampilkan estimasi harga
    print("Harga estimasi pembangunan adalah: Rp", total_biaya)
    return