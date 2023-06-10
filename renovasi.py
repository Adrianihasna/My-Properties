import csv

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

    pilihan_ruangan = input("Silakan pilih ruangan yang akan direnovasi (1/2/3/4/5): ")
    panjang = float(input("Masukkan panjang ruangan (meter): "))
    lebar = float(input("Masukkan lebar ruangan (meter): "))
    tinggi = float(input("Masukkan tinggi ruangan (meter): "))

    harga = []
    with open('My-Property\perbarui_data\DATA_MATERIAL.csv') as data :
        data = csv.reader(data,delimiter=',')
        for i in data :
            harga.append(i)
    header = harga.pop(0)
    
    harga_cat_per_meter = int(harga[7][1])/5
    harga_lantai_per_meter = int(harga[6][1])
    harga_dinding_Keramik_per_meter = int(harga[8][1])
    harga_lantaiKM_per_meter = int(harga[10][1])
    harga_semen = int(harga[11][1])*1/5
    harga_nat = int(harga[1][1])*3/2
    harga_pasir = int(harga[12][1])*0.045

    luas_dinding = 2 * (panjang + lebar) * tinggi
    luas_lantai = panjang * lebar

    total_biaya_kamar_tidur = (luas_dinding * harga_cat_per_meter) + (luas_lantai * harga_lantai_per_meter) + (luas_lantai * harga_semen) + (luas_lantai * harga_pasir) + (luas_lantai * harga_nat)
    total_biaya_ruang_tamu = (luas_dinding * harga_cat_per_meter) + (luas_lantai * harga_lantai_per_meter) + (luas_lantai * harga_semen) + (luas_lantai * harga_pasir) + (luas_lantai * harga_nat)
    total_biaya_kamar_mandi = (1/3)*(luas_dinding * harga_cat_per_meter) + (2/3)*(luas_dinding * harga_dinding_Keramik_per_meter) + (luas_lantai * harga_lantaiKM_per_meter) + (luas_lantai * harga_semen) + (luas_lantai * harga_pasir) + (luas_lantai * harga_nat)
    total_biaya_dapur = (luas_dinding * harga_cat_per_meter) + (luas_lantai * harga_lantai_per_meter) + (luas_lantai * harga_semen) + (luas_lantai * harga_pasir) + (luas_lantai * harga_nat)
    total_biaya_teras = (panjang * tinggi * harga_cat_per_meter) + (luas_lantai * harga_lantai_per_meter) + (luas_lantai * harga_semen) + (luas_lantai * harga_pasir) + (luas_lantai * harga_nat)
    
    if pilihan_ruangan == '1':
        ruangan = "Kamar Tidur"
        biaya_renovasi = total_biaya_kamar_tidur
    elif pilihan_ruangan == '2':
        ruangan = "Ruang Tamu"
        biaya_renovasi = total_biaya_ruang_tamu
    elif pilihan_ruangan == '3':
        ruangan = "Kamar Mandi"
        biaya_renovasi = total_biaya_kamar_mandi
    elif pilihan_ruangan == '4':
        ruangan = "Dapur"
        biaya_renovasi = total_biaya_dapur
    elif pilihan_ruangan == '5':
        ruangan = "Teras"
        biaya_renovasi = total_biaya_teras
    else:
        print("Pilihan ruangan tidak valid.")

    
    print("Estimasi biaya renovasi", ruangan, "adalah: Rp", biaya_renovasi)

    total_biaya_renov()

from tabulate import tabulate

def total_biaya_renov():
    # Daftar pekerjaan dan perkiraan biaya
    pekerjaan = {
        'Struktural': 5000000,
        'Listrik': 2000000,
        'Plumbing': 1500000,
        'Lantai': 3000000,
        'Cat dinding': 2500000
    }
    
    total_biaya = 0
    
    # Menghitung total biaya
    for biaya in pekerjaan.values():
        total_biaya += biaya
    
    # Menambahkan biaya cadangan (contingency) sebesar 10% dari total biaya
    biaya_cadangan = total_biaya * 0.1
    total_biaya += biaya_cadangan
    
    # Menyiapkan data untuk tabel
    data = []
    for pekerjaan, biaya in pekerjaan.items():
        data.append([pekerjaan, f"{biaya:,}"])
    
    data.append(['Total Biaya', f"{total_biaya:,.2f}"])
    data.append(['Biaya Cadangan (10%)', f"{biaya_cadangan:,.2f}"])
    
    # Menampilkan tabel
    print("RAB (Rencana Anggaran Biaya) Renovasi Ruang:")
    print("------------------------------------------")
    print(tabulate(data, headers=['Pekerjaan', 'Biaya'], tablefmt='grid'))
    
# Memanggil fungsi hitung_biaya_renovasi


def run():
    if __name__ == '__main__':
        main()

