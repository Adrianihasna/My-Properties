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

    global panjang
    global lebar
    global tinggi

    pilihan_ruangan = input("Silakan pilih ruangan yang akan direnovasi (1/2/3/4/5): ")
    panjang = int(input("Masukkan panjang ruangan (meter): "))
    lebar = int(input("Masukkan lebar ruangan (meter): "))
    tinggi = int(input("Masukkan tinggi ruangan (meter): "))

    global harga_cat_per_meter
    global harga_lantai_per_meter
    global harga_dinding_Keramik_per_meter
    global harga_lantaiKM_per_meter
    global harga_semen
    global harga_nat
    global harga_pasir
    global luas_lantai
    global luas_dinding
    global biaya_renovasi

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
    harga_semen = int(harga[0][1])*1//5
    harga_nat = int(harga[11][1])*3//2
    harga_pasir = int(harga[12][1])*0.045

    luas_dinding = 2 * (panjang + lebar) * tinggi
    luas_lantai = panjang * lebar

    total_biaya_kamar_tidur = (luas_dinding * harga_cat_per_meter) + (luas_lantai * harga_lantai_per_meter) + (luas_lantai * harga_semen) + (luas_lantai * harga_pasir) + (luas_lantai * harga_nat)
    total_biaya_ruang_tamu = (luas_dinding * harga_cat_per_meter) + (luas_lantai * harga_lantai_per_meter) + (luas_lantai * harga_semen) + (luas_lantai * harga_pasir) + (luas_lantai * harga_nat)
    total_biaya_kamar_mandi = (1//3)*(luas_dinding * harga_cat_per_meter) + (2//3)*(luas_dinding * harga_dinding_Keramik_per_meter) + (luas_lantai * harga_lantaiKM_per_meter) + (luas_lantai * harga_semen) + (luas_lantai * harga_pasir) + (luas_lantai * harga_nat)
    total_biaya_dapur = (luas_dinding * harga_cat_per_meter) + (luas_lantai * harga_lantai_per_meter) + (luas_lantai * harga_semen) + (luas_lantai * harga_pasir) + (luas_lantai * harga_nat)
    total_biaya_teras = (panjang * tinggi * harga_cat_per_meter) + (luas_lantai * harga_lantai_per_meter) + (luas_lantai * harga_semen) + (luas_lantai * harga_pasir) + (luas_lantai * harga_nat)
    
    if pilihan_ruangan == '1':
        ruangan = "Kamar Tidur"
        biaya_renovasi = total_biaya_kamar_tidur
        RAB_KT_RT_Dapur()
    elif pilihan_ruangan == '2':
        ruangan = "Ruang Tamu"
        biaya_renovasi = total_biaya_ruang_tamu
        RAB_KT_RT_Dapur()
    elif pilihan_ruangan == '3':
        ruangan = "Kamar Mandi"
        biaya_renovasi = total_biaya_kamar_mandi
        RAB_KM()
    elif pilihan_ruangan == '4':
        ruangan = "Dapur"
        biaya_renovasi = total_biaya_dapur
        RAB_KT_RT_Dapur()
    elif pilihan_ruangan == '5':
        ruangan = "Teras"
        biaya_renovasi = total_biaya_teras
        RAB_Teras()
    else:
        print("Pilihan ruangan tidak valid.")

    print("Estimasi biaya renovasi", ruangan, "adalah: Rp", biaya_renovasi)


from tabulate import tabulate

def hitung_biaya_cat(luas_dinding, harga_cat_per_meter):
    biaya_cat = harga_cat_per_meter * luas_dinding
    return biaya_cat

def hitung_biaya_lantai(luas_lantai, harga_lantai_per_meter):
    biaya_lantai = harga_lantai_per_meter * luas_lantai
    return biaya_lantai

def hitung_biaya_dinding_keramik(luas_dinding, harga_dinding_Keramik_per_meter):
    biaya_dinding_keramik = (2/3) * harga_dinding_Keramik_per_meter * luas_dinding
    return biaya_dinding_keramik

def hitung_biaya_lantaiKM(luas_lantai, harga_lantaiKM_per_meter):
    biaya_lantaiKM = harga_lantaiKM_per_meter * luas_lantai
    return biaya_lantaiKM

def hitung_biaya_CatKM(luas_dinding,harga_cat_per_meter) :
    # global biaya_catKM
    biaya_catKM = (1/3) * luas_dinding * harga_cat_per_meter
    return biaya_catKM

def hitung_biaya_semen(luas_lantai, harga_semen):
    biaya_semen = harga_semen * luas_lantai
    return biaya_semen

def hitung_biaya_pasir(luas_lantai, harga_pasir):
    biaya_pasir = harga_pasir * luas_lantai
    return biaya_pasir

def hitung_biaya_nat(luas_lantai, harga_nat):
    biaya_nat = harga_nat * luas_lantai
    return biaya_nat

def hitung_biaya_dinding_teras(panjang, tinggi, harga_cat_per_meter):
    biaya_dinding_teras = panjang * tinggi * harga_cat_per_meter
    return biaya_dinding_teras

def RAB_KM():
    data_Kamar_Mandi = [["Rincian", "        Biaya        "],
                        ["Cat Tembok", hitung_biaya_CatKM(luas_dinding,harga_cat_per_meter)],
                        ["Dinding Keramik", hitung_biaya_dinding_keramik(luas_dinding, harga_dinding_Keramik_per_meter)],
                        ["Semen ", hitung_biaya_semen(luas_lantai, harga_semen)],
                        ["Pasir", hitung_biaya_pasir(luas_lantai, harga_pasir)],
                        ["Nat", hitung_biaya_nat(luas_lantai, harga_nat)],
                        ["Total Biaya Renovasi", biaya_renovasi]]
    table = tabulate(data_Kamar_Mandi, headers="firstrow", tablefmt="grid")
    print("\nTabel RAB (Rencana Anggaran Biaya):")
    print(table)
    return data_Kamar_Mandi
    
def RAB_KT_RT_Dapur():
    data_KT_RT_Dapur = [["Rincian", "        Biaya        "],
                        ["Harga Cat", hitung_biaya_cat(luas_dinding, harga_cat_per_meter)],
                        ["Harga Lantai", hitung_biaya_lantai(luas_lantai, harga_lantai_per_meter)],
                        ["Semen ", hitung_biaya_semen(luas_lantai, harga_semen)],
                        ["Pasir", hitung_biaya_pasir(luas_lantai, harga_pasir)],
                        ["Nat", hitung_biaya_nat(luas_lantai, harga_nat)],
                        ["Total Biaya Renovasi", biaya_renovasi]]
    table = tabulate(data_KT_RT_Dapur, headers="firstrow", tablefmt="grid")
    print("\nTabel RAB (Rencana Anggaran Biaya):")
    print(table)

def RAB_Teras():
    data_teras = [["Rincian", "        Biaya        "],
                  ["Harga Cat", hitung_biaya_dinding_teras(panjang, tinggi, harga_cat_per_meter)],
                  ["Harga Lantai", hitung_biaya_lantai(luas_lantai, harga_lantai_per_meter)],
                  ["Semen ", hitung_biaya_semen(luas_lantai, harga_semen)],
                  ["Pasir", hitung_biaya_pasir(luas_lantai, harga_pasir)],
                  ["Nat", hitung_biaya_nat(luas_lantai, harga_nat)],
                  ["Total Biaya Renovasi", biaya_renovasi]]
    table = tabulate(data_teras, headers="firstrow", tablefmt="grid")
    print("\nTabel RAB (Rencana Anggaran Biaya):")
    print(table)

def run():
    if __name__ == '__main__':
        main()

run()