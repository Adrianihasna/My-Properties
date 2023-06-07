def beli():
    Tipe_A = 300000000 # 300 juta
    Tipe_B = 600000000  # 600 juta
    Tipe_C = 1000000000  # 1 milyar

    harga_yang_dicari = int(input("Masukkan harga rumah yang Anda cari (Rupiah): "))

    if harga_yang_dicari <= Tipe_A :
        print("Tipe Rumah : A")
    elif harga_yang_dicari >= Tipe_A and harga_yang_dicari <= Tipe_B :
        print("Tipe Rumah : B")
    elif harga_yang_dicari >= Tipe_B and harga_yang_dicari <= Tipe_C:
        print("Tipe Rumah : C")
    else:
        print("Tipe rumah dengan harga yang anda cari belum tersedia")

    pembelian = input("Apakah Anda ingin melakukan pembelian? (Ya/Tidak): ")
    pembelian.lower()

