import csv
from tabulate import tabulate
import os

def main():
    os.system('cls')
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

    def bangun():
        global pilihan_ruangan
        try : 
            pilihan_ruangan = int(input("Silakan pilih ruangan yang akan direnovasi (1/2/3/4/5): "))
        except ValueError : 
            print('\n**Mohon Masukkan Angka Sesuai Pilihan**')
            bangun()
        else : 
            if pilihan_ruangan in range(1,6) :
                def kriteria():
                    global panjang
                    global lebar
                    global tinggi
                    try : 
                        panjang = float(input("Masukkan panjang ruangan (meter): "))
                        lebar = float(input("Masukkan lebar ruangan (meter): "))
                        tinggi = float(input("Masukkan tinggi ruangan (meter): "))
                    except ValueError:
                        print('\n**Mohon Masukkan Input Berupa Angka**')
                        kriteria() 
                    else :
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
                        with open('perbarui_data\data_material.csv') as data :
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
                        

                        if pilihan_ruangan == 1:
                            ruangan = "Kamar Tidur"
                            biaya_renovasi = total_biaya_kamar_tidur
                            os.system('cls')
                            RAB_KT_RT_Dapur()
                            print("Estimasi biaya renovasi", ruangan, "adalah: Rp", biaya_renovasi)
                        elif pilihan_ruangan == 2:
                            ruangan = "Ruang Tamu"
                            biaya_renovasi = total_biaya_ruang_tamu
                            os.system('cls')
                            RAB_KT_RT_Dapur()
                            print("Estimasi biaya renovasi", ruangan, "adalah: Rp", biaya_renovasi)
                        elif pilihan_ruangan == 3:
                            ruangan = "Kamar Mandi"
                            biaya_renovasi = total_biaya_kamar_mandi
                            os.system('cls')
                            RAB_KM()
                            print("Estimasi biaya renovasi", ruangan, "adalah: Rp", biaya_renovasi)
                        elif pilihan_ruangan == 4:
                            ruangan = "Dapur"
                            biaya_renovasi = total_biaya_dapur
                            os.system('cls')
                            RAB_KT_RT_Dapur()
                            print("Estimasi biaya renovasi", ruangan, "adalah: Rp", biaya_renovasi)
                        elif pilihan_ruangan == 5:
                            ruangan = "Teras"
                            biaya_renovasi = total_biaya_teras
                            os.system('cls')
                            RAB_Teras()
                            print("Estimasi biaya renovasi", ruangan, "adalah: Rp", biaya_renovasi)
                kriteria()
            else :
                print('\n**Mohon Masukkan Angka Sesuai Pilihan**')
                bangun()
    bangun()
    def beranda() :
        print('''

    [1] Beranda
    [2] Pilih Ruangan Lain

        ''')
        try :
            awal = int(input('Masukkan Pilihan = '))
        except ValueError :
            print('\n**Mohon Masukkan Angka Sesuai Pilihan**')
        else :
            if awal == 1 :
                print('\n~~ Terima Kasih Sudah Menggunakan Program Kami ~~')
            elif awal == 2 :
                main()
            else : 
                beranda()
    beranda()



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
                        ["Lantai", hitung_biaya_lantaiKM(luas_lantai, harga_lantaiKM_per_meter)],
                        ["Semen ", hitung_biaya_semen(luas_lantai, harga_semen)],
                        ["Pasir", hitung_biaya_pasir(luas_lantai, harga_pasir)],
                        ["Nat", hitung_biaya_nat(luas_lantai, harga_nat)],
                        ["Total Biaya Renovasi", biaya_renovasi]]
    table = tabulate(data_Kamar_Mandi, headers="firstrow", tablefmt="grid",floatfmt=".2f")
    print("\nTabel RAB (Rencana Anggaran Biaya):")
    print(table)
    return data_Kamar_Mandi
    
def RAB_KT_RT_Dapur():
    data_KT_RT_Dapur = [["Rincian", "         Biaya         "],
                        ["Cat", hitung_biaya_cat(luas_dinding, harga_cat_per_meter)],
                        ["Lantai", hitung_biaya_lantai(luas_lantai, harga_lantai_per_meter)],
                        ["Semen ", hitung_biaya_semen(luas_lantai, harga_semen)],
                        ["Pasir", hitung_biaya_pasir(luas_lantai, harga_pasir)],
                        ["Nat", hitung_biaya_nat(luas_lantai, harga_nat)],
                        ["Total Biaya Renovasi", biaya_renovasi]]
    table = tabulate(data_KT_RT_Dapur, headers="firstrow", tablefmt="grid",floatfmt=".2f")
    print("\nTabel RAB (Rencana Anggaran Biaya):")
    print(table)

def RAB_Teras():
    data_teras = [["Rincian", "        Biaya        "],
                  ["Cat", hitung_biaya_dinding_teras(panjang, tinggi, harga_cat_per_meter)],
                  ["Lantai", hitung_biaya_lantai(luas_lantai, harga_lantai_per_meter)],
                  ["Semen ", hitung_biaya_semen(luas_lantai, harga_semen)],
                  ["Pasir", hitung_biaya_pasir(luas_lantai, harga_pasir)],
                  ["Nat", hitung_biaya_nat(luas_lantai, harga_nat)],
                  ["Total Biaya Renovasi", biaya_renovasi]]
    table = tabulate(data_teras, headers="firstrow", tablefmt="grid",floatfmt=".2f")
    print("\nTabel RAB (Rencana Anggaran Biaya):")
    print(table)

def run():
    if __name__ == '__main__':
        main()
