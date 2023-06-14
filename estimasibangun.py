import csv
from tabulate import tabulate
import os

def main():
    os.system('cls')
    print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Program Estimasi Pembangunan
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pilihan Bangunan :

[1] Aula
[2] Gor
[3] Rumah Satu Lantai
    \n''')

    def bangun():
        global Jenis_Pembangunan
        try :
            Jenis_Pembangunan = int(input("Silakan pilih Pembangunan (1/2/3): "))
        except ValueError :
            print('\n**Mohon Masukkan Angka Sesuai Pilihan**')
            bangun()
        else : 
            if Jenis_Pembangunan in range(1,4) :
                def kriteria():
                    global panjang
                    global lebar
                    global tinggi
                    try :
                        panjang = int(input("Masukkan panjang (meter): "))
                        lebar = int(input("Masukkan lebar ruangan (meter): "))
                        tinggi = int(input("Masukkan tinggi ruangan (meter): "))
                    except ValueError :
                        print('\n**Mohon Masukkan Input Berupa Angka**\n')
                        kriteria()
                    else: 
                        global harga_semen
                        global harga_cat
                        global harga_pasir
                        global harga_batusplit
                        global harga_lantai
                        global harga_besi
                        global harga_genteng
                        global harga_bata
                        global luas_dinding
                        global luas_lantai
                        global Biaya_Pembangunan

                        biaya = []
                        with open('perbarui_data\DATA_MATERIAL.csv') as data :
                            data = csv.reader(data,delimiter=',')
                            for i in data :
                                biaya.append(i)
                        header = biaya.pop(0)

                        harga_semen = int(biaya[0][1])*1//5
                        harga_cat = int(biaya[7][1])/5
                        harga_pasir = int(biaya[12][1])*0.045
                        harga_batusplit = int(biaya[4][1])
                        harga_lantai = int(biaya[6][1])
                        harga_besi = int(biaya[3][1])
                        harga_genteng = int(biaya[2][1])
                        harga_bata = int(biaya[13][1])

                        luas_dinding = 2 * (panjang + lebar) * tinggi
                        luas_lantai = panjang * lebar

                        biaya_total_aula = ((harga_bata + harga_besi + harga_cat + harga_semen) * luas_dinding) + ((harga_semen + harga_lantai + harga_genteng + harga_besi + harga_batusplit + harga_pasir) * luas_lantai)
                        biaya_total_gor = ((harga_bata + harga_besi + harga_cat + harga_semen) * luas_dinding) + ((harga_semen + harga_genteng + harga_besi + harga_batusplit + harga_pasir) * luas_lantai)
                        biaya_total_rumah = ((harga_bata + harga_besi + harga_cat + harga_semen) * luas_dinding) + ((harga_semen + harga_lantai + harga_genteng + harga_besi + harga_batusplit + harga_pasir) * luas_lantai)

                        if Jenis_Pembangunan == 1 :
                            tipe_pembangunan = "Aula"
                            Biaya_Pembangunan = biaya_total_aula
                            os.system('cls')
                            RAB_Aula()
                            print("\nEstimasi biaya pembangunan", tipe_pembangunan, "adalah: Rp", Biaya_Pembangunan)
                        elif Jenis_Pembangunan == 2 :
                            tipe_pembangunan = "Gor"
                            Biaya_Pembangunan = biaya_total_gor
                            os.system('cls')
                            RAB_Gor()
                            print("\nEstimasi biaya pembangunan", tipe_pembangunan, "adalah: Rp", Biaya_Pembangunan)
                        elif Jenis_Pembangunan == 3 :
                            tipe_pembangunan = "Rumah Satu Lantai"
                            Biaya_Pembangunan = biaya_total_rumah
                            os.system('cls')
                            RAB_Rumah()
                            print("\nEstimasi biaya pembangunan", tipe_pembangunan, "adalah: Rp", Biaya_Pembangunan)
                kriteria()   
            else :   
                print('\n**Mohon Masukkan Angka Sesuai Pilihan**')
                bangun()
    bangun()
    def beranda() :
        print('''

    [1] Beranda
    [2] Pilih Bangunan Lain

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


def biaya_semen(luas_lantai, luas_dinding, harga_semen):
    biaya_semen = (luas_lantai + luas_dinding) * harga_semen
    return biaya_semen

def biaya_cat(luas_dinding, harga_cat):
    biaya_cat = luas_dinding * harga_cat
    return biaya_cat

def biaya_pasir(luas_lantai, harga_pasir):
    biaya_pasir = luas_lantai  * harga_pasir
    return biaya_pasir

def biaya_batusplit(luas_lantai, harga_batusplit):
    biaya_batusplit = luas_lantai * harga_batusplit
    return biaya_batusplit

def biaya_lantai(luas_lantai, harga_lantai):
    biaya_lantai = luas_lantai * harga_lantai
    return biaya_lantai

def biaya_besi(luas_lantai, luas_dinding, harga_besi):
    biaya_besi = (luas_lantai + luas_dinding) * harga_besi
    return biaya_besi

def biaya_genteng(luas_lantai, harga_genteng):
    biaya_genteng = luas_lantai * harga_genteng
    return biaya_genteng

def biaya_bata(luas_dinding, harga_bata):
    biaya_bata = luas_dinding * harga_bata
    return biaya_bata

def RAB_Aula():
    data_aula = [[" Nama Material ", "           Biaya           " ],
                 [" semen ",biaya_semen(luas_lantai, luas_dinding, harga_semen)],
                 [" cat ", biaya_cat(luas_dinding, harga_cat)],
                 [" pasir ", biaya_pasir(luas_lantai, harga_pasir)],
                 [" batusplit ", biaya_batusplit(luas_lantai, harga_batusplit)],
                 [" lantai ", biaya_lantai(luas_lantai, harga_lantai)],
                 [" besi ", biaya_besi(luas_lantai, luas_dinding, harga_besi)],
                 [" genteng ", biaya_genteng(luas_lantai, harga_genteng)],
                 [" bata ", biaya_bata(luas_dinding, harga_bata)],
                 [" total biaya pembangunan", Biaya_Pembangunan]]
    table = tabulate(data_aula, headers="firstrow", tablefmt="grid",floatfmt=".2f")
    print("\nTabel RAB (Rencana Anggaran Biaya):")
    print(table)
    return data_aula

def RAB_Gor():
    data_gor = [[" Nama Material ", "Biaya " ],
                [" semen ", biaya_semen(luas_lantai, luas_dinding, harga_semen)],
                [" cat ", biaya_cat(luas_dinding, harga_cat)],
                [" pasir ", biaya_pasir(luas_lantai, harga_pasir)],
                [" batusplit ", biaya_batusplit(luas_lantai, harga_batusplit)],
                [" besi ", biaya_besi(luas_lantai, luas_dinding, harga_besi)],
                [" genteng ", biaya_genteng(luas_lantai, harga_genteng)],
                [" bata ", biaya_bata(luas_dinding, harga_bata)],
                [" total biaya pembangunan", Biaya_Pembangunan]]
    table = tabulate(data_gor, headers="firstrow", tablefmt="grid",floatfmt=".2f")
    print("\nTabel RAB (Rencana Anggaran Biaya):")
    print(table)

def RAB_Rumah():
    data_rumah = [[" Nama Material ", "Biaya " ],
                 [" semen ", biaya_semen(luas_lantai, luas_dinding, harga_semen)],
                 [" cat ", biaya_cat(luas_dinding, harga_cat)],
                 [" pasir ", biaya_pasir(luas_lantai, harga_pasir)],
                 [" batusplit ", biaya_batusplit(luas_lantai, harga_batusplit)],
                 [" lantai ", biaya_batusplit(luas_lantai, harga_lantai)],
                 [" besi ", biaya_besi(luas_lantai, luas_dinding, harga_besi)],
                 [" genteng ", biaya_genteng(luas_lantai, harga_genteng)],
                 [" bata ", biaya_bata(luas_dinding, harga_bata)],
                 [" total biaya pembangunan", Biaya_Pembangunan]]
    table = tabulate(data_rumah, headers="firstrow", tablefmt="grid",floatfmt=".2f")
    print("\nTabel RAB (Rencana Anggaran Biaya):")
    print(table)
def run():
    if __name__ == '__main__':
        main()
