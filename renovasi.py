def hitung_biaya_renovasi(panjang, lebar, tinggi):
    harga_cat_per_meter = 10 
    harga_lantai_per_meter = 20 

    luas_dinding = 2 * (panjang + lebar) * tinggi
    luas_lantai = panjang * lebar

    total_biaya = (luas_dinding * harga_cat_per_meter) + (luas_lantai * harga_lantai_per_meter)
    return total_biaya

def main():
    print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Program Estimasi Renovasi Rumah
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pilihan Ruangan :

[1] Kamar Tidur
[2] Ruang Tamu
[3] Kamar Mandi
[4] Dapur 
[5] Teras
    \n''')


    pilihan_ruangan = int(input("Silakan pilih ruangan yang akan direnovasi (1/2/3/4/5): "))
    panjang_ruangan = float(input("Masukkan panjang ruangan (meter): "))
    lebar_ruangan = float(input("Masukkan lebar ruangan (meter): "))
    tinggi_ruangan = float(input("Masukkan tinggi ruangan (meter): "))

    if pilihan_ruangan == 1:
        ruangan = "Kamar Tidur"
    elif pilihan_ruangan == 2:
        ruangan = "Ruang Tamu"
    elif pilihan_ruangan == 3:
        ruangan = "Kamar Mandi"
    elif pilihan_ruangan == 4:
        ruangan = "Dapur"
    elif pilihan_ruangan == 5:
        ruangan = "Teras"
    else:
        print("Pilihan ruangan tidak valid.")
        return

    biaya_renovasi = hitung_biaya_renovasi(panjang_ruangan, lebar_ruangan, tinggi_ruangan)
    print("Estimasi biaya renovasi", ruangan, "adalah: Rp", biaya_renovasi)


def run():
    if __name__ == '__main__':
        main()
