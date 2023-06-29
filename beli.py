import os
from tabulate import tabulate
import datetime
import json

def beli():
    os.system('cls') 
    try:
        with open("perbarui_data\\tipe_rumah.json", "r") as file:
            datarumah = json.load(file)
    except FileNotFoundError:
        datarumah = {}
    
    D = datarumah
    
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
        for i in D :
            for j in D[i] :
                if int(D[i][j]['harga']) <= r1 :
                    print(f'''
~~~~~~~~~~~~~~~ {i} ~~~~~~~~~~~~~~~
Kode Rumah  : {j}
Harga           : {D[i][j]['harga']}
Luas Bangunan   : {D[i][j]['luasbangunan']}
Luas Tanah      : {D[i][j]['luastanah']}
Fasilitas       : {D[i][j]['fasilitas']}
Lokasi          : {D[i][j]['lokasi']}
            
            ''')
        pembelian = input('Lakukan Pembelian (y/n) = ')
        pembelian = pembelian.lower()
        if pembelian == "y":            
            pilih_kode = input('Masukkan Kode Rumah Yang Tersedia = ')
            if pilih_kode in j : 
                metode_pembayaran()
            else :
                print('**Mohon Masukkan Kode Sesuai daftar ')
    elif tipe == '2' :
        os.system('cls') 
        print('\nRumah Dengan Range 300.000.000 - 600.000.000 : ')
        for i in D :
            for j in D[i] :
                if int(D[i][j]['harga']) in range(r1,r2) :
                    print(f'''
~~~~~~~~~~~~~~~ {i} ~~~~~~~~~~~~~~~
Kode Rumah  : {j}
Harga           : {D[i][j]['harga']}
Luas Bangunan   : {D[i][j]['luasbangunan']}
Luas Tanah      : {D[i][j]['luastanah']}
Fasilitas       : {D[i][j]['fasilitas']}
Lokasi          : {D[i][j]['lokasi']}
            
            ''')
                    
    elif tipe == '3' :
        os.system('cls') 
        print('\nRumah Dengan Range 600.000.000 - 1.000.000.000 : ')
        for i in D :
            for j in D[i] :
                if int(D[i][j]['harga']) in range(r2,r3+1) :
                    print(f'''
~~~~~~~~~~~~~~~ {i} ~~~~~~~~~~~~~~~
Kode Rumah  : {j}
Harga           : {D[i][j]['harga']}
Luas Bangunan   : {D[i][j]['luasbangunan']}
Luas Tanah      : {D[i][j]['luastanah']}
Fasilitas       : {D[i][j]['fasilitas']}
Lokasi          : {D[i][j]['lokasi']}
            
            ''')
    elif tipe == '4' :
        os.system('cls') 
        print('\nRumah Dengan Range lebih dari 1.000.000.000 : ')
        for i in D :
            for j in D[i] :
                if int(D[i][j]['harga']) > r3 :
                    print(f'''
~~~~~~~~~~~~~~~ {i} ~~~~~~~~~~~~~~~
Kode Rumah  : {j}
Harga           : {D[i][j]['harga']}
Luas Bangunan   : {D[i][j]['luasbangunan']}
Luas Tanah      : {D[i][j]['luastanah']}
Fasilitas       : {D[i][j]['fasilitas']}
Lokasi          : {D[i][j]['lokasi']}
            
            ''')
    elif tipe == '5':
        return()
    else :
        beli()

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
        bayar_kredit()
    else :
        metode_pembayaran()   

def data_harga():
    global r1
    global r2
    global r3
    global bunga
    global notaris
    global PNBP
    global provisi 

    r1 = 300_000_000
    r2 = 600_000_000
    r3 = 1_000_000_000
    bunga = 0.05
    notaris = 0.01 
    PNBP = 650_000
    provisi = 1_500_000

def bayar_kredit():
            global hutang
            global pembayaran
            global total_bayar
            global cicilan_bunga
            global waktu
            try:
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
    TIPE RUMAH          : 
    TOTAL BAYAR         : {total_bayar}
    METODE PEMBAYARAN   : {pembayaran}
                   
                   ''')

    print(f'''
                    KUITANSI
                                        {formattanggal}

    NAMA                : {nama}
    ALAMAT              : {alamat}
    NO. HP              : {nomor_hp}
    TIPE RUMAH          : 
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
    TIPE RUMAH          : 
    UANG MUKA           : 
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
    TIPE RUMAH          : 
    UANG MUKA           : 
    METODE PEMBAYARAN   : {pembayaran}
    CICILAN TIAP BULAN  : {total_bayar}
    TOTAL CICILAN       : {hutang}
    JANGKA WAKTU        : {waktu} Tahun

                   ''')

beli()