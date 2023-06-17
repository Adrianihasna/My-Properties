import os
from tabulate import tabulate
import datetime

def beli() :
    data_harga()
    os.system('cls')    
    print('''
    Pilihan Range Harga :

    [1] < 300.000.000 
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
        return()
    else :
        beli()

    pembelian = input('Lakukan Pembelian (y/n) = ')
    pembelian = pembelian.lower()
    if pembelian == "y":
        def beli_tipe_rumah():
            global tipe_rumah
            global harga_tipe_rumah
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
            pilih_tipe = input('Masukkan Tipe Rumah yang ingin Dibeli = ')
            if pilih_tipe == '1' :
                harga_tipe_rumah = Tipe_21
                tipe_rumah = 'Tipe 21'
                metode_pembayaran()
            elif pilih_tipe == '2' :
                harga_tipe_rumah = Tipe_36
                tipe_rumah = 'Tipe 36'
                metode_pembayaran()
            elif pilih_tipe == '3' :
                harga_tipe_rumah = Tipe_45
                tipe_rumah = 'Tipe 45'
                metode_pembayaran()
            elif pilih_tipe == '4' : 
                harga_tipe_rumah = Tipe_54
                tipe_rumah = 'Tipe 54'
                metode_pembayaran()
            elif pilih_tipe == '5' : 
                harga_tipe_rumah = Tipe_60
                tipe_rumah = 'Tipe 60'
                metode_pembayaran()
            elif pilih_tipe == '6' : 
                harga_tipe_rumah = Tipe_70
                tipe_rumah = 'Tipe 70'
                metode_pembayaran()
            elif pilih_tipe == '7' :
                harga_tipe_rumah = Tipe_120
                tipe_rumah = 'Tipe 120'
                metode_pembayaran()
            else :
                print('**Tipe Rumah Tidak Tersedia**')
                beli_tipe_rumah()
        beli_tipe_rumah()
    else:
       beli()


def tipe21():
    data_harga()
    print(f'''
~~~~~~~~~~~~~~~ TIPE 21 ~~~~~~~~~~~~~~~
Harga           = {Tipe_21}
Luas Bangunan   = 21 m^2
Luas Tanah      = 50 m^2
Fasilitas       = "1 kamar tidur, 1 kamar mandi, ruang tamu, dapur"

    ''')

def tipe36():
    data_harga()
    print(f'''
~~~~~~~~~~~~~~~ TIPE 36 ~~~~~~~~~~~~~~~
Harga           = {Tipe_36}
Luas Bangunan   = 31 m^2
Luas Tanah      = 70 m^2
Fasilitas       = "2 kamar tidur, 1 kamar mandi, ruang tamu, ruang makan, dapur, carport"     

    ''')

def tipe45():
    data_harga()
    print(f'''
~~~~~~~~~~~~~~~ TIPE 45 ~~~~~~~~~~~~~~~
Harga           = {Tipe_45}
Luas Bangunan   = 45 m^2
Luas Tanah      = 90 m^2
Fasilitas       = "2 kamar tidur, 1 kamar mandi, ruang tamu, ruang makan, dapur, carport"
          
    ''')

def tipe54():
    data_harga()
    print(f'''
~~~~~~~~~~~~~~~ TIPE 54 ~~~~~~~~~~~~~~~
Harga           = {Tipe_54}
Luas Bangunan   = 54 m^2
Luas Tanah      = 120 m^2
Fasilitas       = "3 kamar tidur, 2 kamar mandi, ruang tamu, ruang makan, dapur, carport"

    ''')

def tipe60():
    data_harga()
    print(f'''
~~~~~~~~~~~~~~~ TIPE 60 ~~~~~~~~~~~~~~~
Harga           = {Tipe_60}
Luas Bangunan   = 60 m^2
Luas Tanah      = 130 m^2
Fasilitas       = "3 kamar tidur, 2 kamar mandi, ruang tamu, ruang makan, dan dapur, carport"          
          
    ''')

def tipe70():
    data_harga()
    print(f'''
~~~~~~~~~~~~~~~ TIPE 70 ~~~~~~~~~~~~~~~
Harga           = {Tipe_70}
Luas Bangunan   = 70 m^2
Luas Tanah      = 140 m^2
Fasilitas       = "3 kamar tidur, 3 kamar mandi, ruang tamu, ruang makan, dapur, taman, carport"          
          
    ''')

def tipe120():
    data_harga()
    print(f'''
~~~~~~~~~~~~~~~ TIPE 120 ~~~~~~~~~~~~~~~
Harga           = {Tipe_120}
Luas Bangunan   = 120 m^2
Luas Tanah      = 160 m^2
Fasilitas       = "4 kamar tidur, 4 kamar mandi, ruang tamu, ruang makan, dapur, taman, carport"          
          
    ''')


def hitung_biaya_pajak(): 
    data_harga()
    global biaya_pajak
    biaya_pajak = harga_tipe_rumah * 1.11

def metode_pembayaran():
    global total_bayar
    global pembayaran
    hitung_biaya_pajak()
    data_harga()

    print('''
~~~~~~~~~~ METODE PEMBAYARAN ~~~~~~~~~~
[1] CASH
[2] KREDIT

    ''')
    metode = input('\nMasukkan Pilihan Metode Pembayaran = ')
    if metode == '1' :
        pembayaran = 'Tunai'
        total_bayar = biaya_pajak + (notaris * harga_tipe_rumah) + PNBP + provisi
        print()
        print(f'Total Biaya yang Harus Anda Bayar = {total_bayar}')
        print('Rincian : ')
        print(f'Harga Rumah dan Pajak \t= {biaya_pajak}')
        print(f'Biaya Notaris         \t= {notaris*harga_tipe_rumah}')
        print(f'Biaya PNBP            \t= {PNBP}')
        print(f'Biaya Provisi         \t= {provisi}')
        print()
        kuitansi_tunai()
    elif metode == '2' :
        def bayar_kredit():
            global hutang
            global dp
            global pembayaran
            global total_bayar
            global cicilan_bunga
            global waktu
            try:
                dp = int(input('Masukkan uang muka yang ingin dibayarkan = '))
                waktu = float(input('Masukkan Jangka waktu dalam tahun = '))
            except ValueError :
                print('**Mohon Masukkan Dalam Bentuk Angka**')
                bayar_kredit()
            else :
                if waktu == 0 :
                    pembayaran = 'Tunai'
                    total_bayar = (biaya_pajak + (notaris * harga_tipe_rumah) + PNBP + provisi) - dp
                    kuitansi_tunai()
                else :
                    pembayaran = 'Kredit'
                    hutang = (biaya_pajak + (notaris * harga_tipe_rumah) + PNBP + provisi) - dp
                    cicilan_bunga = ((bunga*hutang)*waktu)//(waktu*12)
                    total_bayar = hutang//(12*waktu) + cicilan_bunga
                    kuitansi_kredit()
        bayar_kredit()
    else :
        metode_pembayaran()     
    return

def data_harga() :
    global bunga
    global notaris
    global PNBP
    global provisi 
    global Tipe_21
    global Tipe_36
    global Tipe_45
    global Tipe_54
    global Tipe_60
    global Tipe_70
    global Tipe_120

    bunga = 0.05
    notaris = 0.01 
    PNBP = 650_000
    provisi = 1_500_000
    Tipe_21 = 250_000_000
    Tipe_36 = 500_000_000
    Tipe_45 = 700_000_000
    Tipe_54 = 900_000_000
    Tipe_60 = 1_000_000_000
    Tipe_70 = 1_300_000_000
    Tipe_120 = 1_500_000_000

def kuitansi_tunai():
    nama = input("Masukkan nama: ")
    alamat = input("Masukkan alamat: ")
    nomor_hp = input("Masukkan nomor HP: ")
    tanggal = datetime.date.today()
    formattanggal = tanggal.strftime('%d/%m/%y')
    with open('kuitansi.txt','a')as file :
        file.write(f'''
                        KUITANSI
                                        {formattanggal}

    NAMA                : {nama}
    ALAMAT              : {alamat}
    NO. HP              : {nomor_hp}
    TIPE RUMAH          : {tipe_rumah}
    TOTAL BAYAR         : {total_bayar}
    METODE PEMBAYARAN   : {pembayaran}
                   
                   ''')

    print(f'''
                    KUITANSI
                                        {formattanggal}

    NAMA                : {nama}
    ALAMAT              : {alamat}
    NO. HP              : {nomor_hp}
    TIPE RUMAH          : {tipe_rumah}
    TOTAL BAYAR         : {total_bayar}
    METODE PEMBAYARAN   : {pembayaran}
                   ''')
 
def kuitansi_kredit():
    nama = input("Masukkan nama: ")
    alamat = input("Masukkan alamat: ")
    nomor_hp = input("Masukkan nomor HP: ")
    tanggal = datetime.date.today()
    formattanggal = tanggal.strftime('%d/%m/%y')
    with open('kuitansi.txt','a')as file :
        file.write(f'''
                        KUITANSI
                                        {formattanggal}

    NAMA                : {nama}
    ALAMAT              : {alamat}
    NO. HP              : {nomor_hp}
    TIPE RUMAH          : {tipe_rumah}
    UANG MUKA           : {dp}
    METODE PEMBAYARAN   : {pembayaran}
    CICILAN TIAP BULAN  : {total_bayar}
    TOTAL CICILAN       : {hutang}
    JANGKA WAKTU        : {waktu} Tahun
                   
                   ''')

    print(f'''
                    KUITANSI
                                        {formattanggal}

    NAMA                : {nama}
    ALAMAT              : {alamat}
    NO. HP              : {nomor_hp}
    TIPE RUMAH          : {tipe_rumah}
    UANG MUKA           : {dp}
    METODE PEMBAYARAN   : {pembayaran}
    CICILAN TIAP BULAN  : {total_bayar}
    TOTAL CICILAN       : {hutang}
    JANGKA WAKTU        : {waktu} Tahun

                   ''')