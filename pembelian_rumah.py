import os
import pandas as pd 
from tabulate import tabulate

def beli() :
    os.system('cls')    
    global Tipe_21
    global Tipe_36
    global Tipe_45
    global Tipe_54
    global Tipe_60
    global Tipe_70
    global Tipe_120
    global tipe_rumah

    print('''
    Pilihan Range Harga :

    [1] < 300.000.000 (300 juta)
    [2] 300.000.000 - 600.000.000
    [3] 600.000.000 - 1.000.000.000
    [4] >1.000.000.000
    [5] Keluar
    ''')
    tipe = input('Masukkan Pilihan Range = ')
    if tipe == '1' :
        os.system('cls') 
        print('\nRumah Dengan Range 0 - 300.000.000 : ')
        tipe21()
    elif tipe == '2' :
        os.system('cls') 
        print('\nRumah Dengan Range 300.000.000 - 600.000.000 : ')
        tipe36()
    elif tipe == '3' :
        os.system('cls') 
        print('\nRumah Dengan Range 600.000.000 - 1.000.000.000 : ')
        tipe45()
        tipe54()
    elif tipe == '4' :
        os.system('cls') 
        print('\nRumah Dengan Range lebih dari 1.000.000.000 : ')
        tipe60()
        tipe70()
        tipe120()
    elif tipe == '5':
        print()
    else :
        beli()

    pembelian = input('Lakukan Pembelian (ya/tidak) = ')
    pembelian.lower()
    if pembelian == "ya":
        print('''
        TIPE RUMAH :

        [1] TIPE 21
        [2] TIPE 36
        [3] TIPE 45
        [4] TIPE 54
        [5] TIPE 60
        [6] TIPE 70
        [7] TIPE 120

        ''')
        hitung_biaya_pajak()
        pilih_tipe = input('Masukkan Tipe Rumah yang ingin Dibeli = ')
        if pilih_tipe == '1' :
            Tipe_21 = 250_000_000
            tipe_rumah = 'Tipe_21'
            metode_pembayaran()
        elif pilih_tipe == '2' :
            Tipe_36 = 500_000_000
            tipe_rumah = 'Tipe_36'
            metode_pembayaran()
        elif pilih_tipe == '3' :
            Tipe_45 = 700_000_000
            tipe_rumah = 'Tipe_45'
            metode_pembayaran()
        elif pilih_tipe == '4' :
            Tipe_54 = 900_000_000
            tipe_rumah = 'Tipe_54'
            metode_pembayaran()
        elif pilih_tipe == '5' :
            Tipe_60 = 1_000_000_000
            tipe_rumah = 'Tipe_60'
            metode_pembayaran()
        elif pilih_tipe == '6' :
            Tipe_70 = 1_300_000_000
            tipe_rumah = 'Tipe_70'
            metode_pembayaran()
        elif pilih_tipe == '7' :
            Tipe_120 = 1_500_000_000
            tipe_rumah = 'Tipe_120'
            metode_pembayaran()
    else:
       beli()


def tipe21():
    print(f'''
~~~~~~~~~~~~~~~ TIPE 21 ~~~~~~~~~~~~~~~
Harga           = {Tipe_21}
Luas Bangunan   = 21 m^2
Luas Tanah      = 50 m^2
Fasilitas       = "1 kamar tidur, 1 kamar mandi, ruang tamu, dapur"

    ''')

def tipe36():
    print(f'''
~~~~~~~~~~~~~~~ TIPE 36 ~~~~~~~~~~~~~~~
Harga           = {Tipe_36}
Luas Bangunan   = 31 m^2
Luas Tanah      = 70 m^2
Fasilitas       = "2 kamar tidur, 1 kamar mandi, ruang tamu, ruang makan, dapur, carport"     

    ''')

def tipe45():
    print(f'''
~~~~~~~~~~~~~~~ TIPE 45 ~~~~~~~~~~~~~~~
Harga           = {Tipe_45}
Luas Bangunan   = 45 m^2
Luas Tanah      = 90 m^2
Fasilitas       = "2 kamar tidur, 1 kamar mandi, ruang tamu, ruang makan, dapur, carport"
          
    ''')

def tipe54():
    print(f'''
~~~~~~~~~~~~~~~ TIPE 54 ~~~~~~~~~~~~~~~
Harga           = {Tipe_54}
Luas Bangunan   = 54 m^2
Luas Tanah      = 120 m^2
Fasilitas       = "3 kamar tidur, 2 kamar mandi, ruang tamu, ruang makan, dapur, carport"

    ''')

def tipe60():
    print(f'''
~~~~~~~~~~~~~~~ TIPE 60 ~~~~~~~~~~~~~~~
Harga           = {Tipe_60}
Luas Bangunan   = 60 m^2
Luas Tanah      = 130 m^2
Fasilitas       = "3 kamar tidur, 2 kamar mandi, ruang tamu, ruang makan, dan dapur, carport"          
          
    ''')

def tipe70():
    print(f'''
~~~~~~~~~~~~~~~ TIPE 70 ~~~~~~~~~~~~~~~
Harga           = {Tipe_70}
Luas Bangunan   = 70 m^2
Luas Tanah      = 140 m^2
Fasilitas       = "3 kamar tidur, 3 kamar mandi, ruang tamu, ruang makan, dapur, taman, carport"          
          
    ''')

def tipe120():
    print(f'''
~~~~~~~~~~~~~~~ TIPE 120 ~~~~~~~~~~~~~~~
Harga           = {Tipe_120}
Luas Bangunan   = 120 m^2
Luas Tanah      = 160 m^2
Fasilitas       = "4 kamar tidur, 4 kamar mandi, ruang tamu, ruang makan, dapur, taman, carport"          
          
    ''')

beli()

def hitung_biaya_pajak(): 
    global biaya_pajak
    biaya_pajak = tipe_rumah * 1.11

def metode_pembayaran():
    global total_bayar
    global pembayaran
    print('''
~~~~~~~~~~ METODE PEMBAYARAN ~~~~~~~~~~
[1] CASH
[2] KREDIT

    ''')
    metode = input('Masukkan Pilihan Metode Pembayaran = ')
    if metode == '1' :
        pembayaran = 'Tunai'
        total_bayar = biaya_pajak + notaris + PNBP + provisi
        print(f'Total Biaya yang Harus Anda Bayar = {total_bayar}')
        print('Rincian : ')
        print(f'Harga Rumah dan Pajak \t= {biaya_pajak}')
        print(f'Biaya Notaris         \t= {notaris}')
        print(f'Biaya PNBP            \t= {PNBP}')
        print(f'Biaya Provisi         \t= {provisi}')
    elif metode == '2' :

        print('kredit')

def kuitansi():
    nama = input("Masukkan nama: ")
    alamat = input("Masukkan alamat: ")
    nomor_hp = input("Masukkan nomor HP: ")
    print("\n--- Kwitansi ---")
    print("Nama: ", nama)
    print("Alamat: ", alamat)
    print("Nomor HP: ", nomor_hp)
    print("Tipe Rumah: ", tipe_rumah)
    print("Metode Pembayaran: ", pembayaran)

def data_harga() :
    global bunga
    global notaris
    global PNBP
    global provisi 
    dp = float(input('Masukkan uang muka yang ingin dibayarkan = '))
    waktu = float(input('Masukkan Jangka waktu dalam tahun = '))
    bunga = 0.05 
    notaris = 0.01
    PNBP = 650_000_000
    provisi = 1_500_000
