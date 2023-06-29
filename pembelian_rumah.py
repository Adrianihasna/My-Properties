import os
from tabulate import tabulate
import datetime
import json


def beli():
    os.system('cls') 
    data_harga()
    global D
    global i
    global j
    global kode 
    
    try:
        with open("perbarui_data\\tipe_rumah.json", "r") as file:
            datarumah = json.load(file)
    except FileNotFoundError:
        datarumah = {}
    D = datarumah
    kode = []
    
    print('''
    Pilihan Range Harga :

    [1] < 300.000.000 
    [2] 300.000.000 - 600.000.000
    [3] 600.000.000 - 1.000.000.000
    [4] >1.000.000.000
    [5] Keluar
    ''')
    tipe = input('Masukkan Pilihan = ')
    if tipe == '1' :
        os.system('cls') 
        print('\nRumah Dengan Range 0 - 300.000.000 : ')
        for i in D :
            for j in D[i] :
                if int(D[i][j]['harga']) <= r1 :
                    kode.append(j)
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
            belitipe1()
        else :
            beli()

    elif tipe == '2' :
        os.system('cls') 
        print('\nRumah Dengan Range 300.000.000 - 600.000.000 : ')
        for i in D :
            for j in D[i] :
                if int(D[i][j]['harga']) in range(r1,r2) :
                    kode.append(j)
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
            belitipe2()
        else :
            beli()
                    
    elif tipe == '3' :
        os.system('cls') 
        print('\nRumah Dengan Range 600.000.000 - 1.000.000.000 : ')
        for i in D :
            for j in D[i] :
                if int(D[i][j]['harga']) in range(r2,r3+1) :
                    kode.append(j)
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
            belitipe3()
        else :
            beli()

    elif tipe == '4' :
        os.system('cls') 
        print('\nRumah Dengan Range lebih dari 1.000.000.000 : ')
        for i in D :
            for j in D[i] :
                if int(D[i][j]['harga']) > r3 :
                    kode.append(j)
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
            belitipe4()
        else :
            beli()

    elif tipe == '5':
        return()
    else :
        beli()


def belitipe1():  
    global pilih_kode
    global p   
    global harga

    print('''
        Pilih Tipe :
        [1] TIPE 21
        [2] TIPE 36
    ''')
    tipe1 = input('Masukkan Pilihan = ')
    if tipe1 == '1' :
        p = 'TIPE 21'
        pilih_kode = input('Masukkan Kode Rumah Yang Tersedia = ')
        if pilih_kode in kode :
            harga = D[p][pilih_kode]['harga']
            delete_ts(D)
            metode_pembayaran()
        else :
            print('**Mohon Masukkan Kode Sesuai daftar ')
            belitipe1()
    elif tipe1 == '2' :
        p = 'TIPE 36'
        pilih_kode = input('Masukkan Kode Rumah Yang Tersedia = ')
        if pilih_kode in kode :
            harga = D[p][pilih_kode]['harga']
            delete_ts(D)
            metode_pembayaran()
        else :
            print('**Mohon Masukkan Kode Sesuai daftar ')
            belitipe1()
    else :
        print('**Mohon Masukkan Kode Sesuai daftar ')
        belitipe1()


def belitipe2():  
    global pilih_kode
    global p   
    global harga

    print('''
        Pilih Tipe :
        [1] TIPE 45
        [2] TIPE 54
        [3] TIPE 60
        [4] TIPE 70
    ''')
    tipe1 = input('Masukkan Pilihan = ')
    if tipe1 == '1' :
        p = 'TIPE 45'
        pilih_kode = input('Masukkan Kode Rumah Yang Tersedia = ')
        if pilih_kode in kode :
            harga = D[p][pilih_kode]['harga']
            delete_ts(D)
            metode_pembayaran()
        else :
            print('**Mohon Masukkan Kode Sesuai daftar ')
            belitipe2()
    elif tipe1 == '2' :
        p = 'TIPE 54'
        pilih_kode = input('Masukkan Kode Rumah Yang Tersedia = ')
        if pilih_kode in kode :
            harga = D[p][pilih_kode]['harga']
            delete_ts(D)
            metode_pembayaran()
        else :
            print('**Mohon Masukkan Kode Sesuai daftar ')
            belitipe2()
    elif tipe1 == '3' :
        p = 'TIPE 60'
        pilih_kode = input('Masukkan Kode Rumah Yang Tersedia = ')
        if pilih_kode in kode :
            harga = D[p][pilih_kode]['harga']
            delete_ts(D)
            metode_pembayaran()
        else :
            print('**Mohon Masukkan Kode Sesuai daftar ')
            belitipe2()
    elif tipe1 == '4' :
        p = 'TIPE 70'
        pilih_kode = input('Masukkan Kode Rumah Yang Tersedia = ')
        if pilih_kode in kode :
            harga = D[p][pilih_kode]['harga']
            delete_ts(D)
            metode_pembayaran()
        else :
            print('**Mohon Masukkan Kode Sesuai daftar ')
            belitipe2()
    else :
        print('**Mohon Masukkan Kode Sesuai daftar ')
        belitipe2()


def belitipe3():  
    global pilih_kode
    global p   
    global harga

    print('''
        Pilih Tipe :
        [1] TIPE 60
        [2] TIPE 70
        [3] TIPE 120
    ''')
    tipe1 = input('Masukkan Pilihan = ')
    if tipe1 == '1' :
        p = 'TIPE 60'
        pilih_kode = input('Masukkan Kode Rumah Yang Tersedia = ')
        if pilih_kode in kode :
            harga = D[p][pilih_kode]['harga']
            delete_ts(D)
            metode_pembayaran()
        else :
            print('**Mohon Masukkan Kode Sesuai daftar ')
            belitipe3()
    elif tipe1 == '2' :
        p = 'TIPE 70'
        pilih_kode = input('Masukkan Kode Rumah Yang Tersedia = ')
        if pilih_kode in kode :
            harga = D[p][pilih_kode]['harga']
            delete_ts(D)
            metode_pembayaran()
        else :
            print('**Mohon Masukkan Kode Sesuai daftar ')
            belitipe3()
    elif tipe1 == '3' :
        p = 'TIPE 120'
        pilih_kode = input('Masukkan Kode Rumah Yang Tersedia = ')
        if pilih_kode in kode :
            harga = D[p][pilih_kode]['harga']
            delete_ts(D)
            metode_pembayaran()
        else :
            print('**Mohon Masukkan Kode Sesuai daftar ')
            belitipe3()
    else :
        print('**Mohon Masukkan Kode Sesuai daftar ')
        belitipe3()


def belitipe4():  
    global pilih_kode
    global p   
    global harga

    print('''
        Pilih Tipe :
        [1] TIPE 120
    ''')
    tipe1 = input('Masukkan Pilihan = ')
    if tipe1 == '1' :
        p = 'TIPE 120'
        pilih_kode = input('Masukkan Kode Rumah Yang Tersedia = ')
        if pilih_kode in kode :
            harga = D[p][pilih_kode]['harga']
            delete_ts(D)
            metode_pembayaran()
        else :
            print('**Mohon Masukkan Kode Sesuai daftar ')
            belitipe4()
    else :
        print('**Mohon Masukkan Kode Sesuai daftar ')
        belitipe4()


def delete_ts(obj):
    if isinstance(obj, list):
        for i in obj:
            delete_ts(i)
    elif isinstance(obj, dict):
        if pilih_kode in obj:
            del obj[pilih_kode]
        for key in obj:
            delete_ts(obj[key])
    with open("perbarui_data\\tipe_rumah.json", "w") as file:
        json.dump(obj, file, indent=4, )


def pajak():
    global biaya_pajak
    biaya_pajak = int(harga) * 1.11 // 1


def metode_pembayaran():
    global total_bayar
    global pembayaran
    data_harga()
    pajak()
    print('''
~~~~~~~~~~ METODE PEMBAYARAN ~~~~~~~~~~
[1] CASH
[2] KREDIT

    ''')
    metode = input('\nMasukkan Pilihan Metode Pembayaran = ')
    if metode == '1' :
        pembayaran = 'Tunai'
        total_bayar = biaya_pajak + (notaris * int(harga)) + PNBP + provisi
        print()
        print(f'Total Biaya yang Harus Anda Bayar = {total_bayar}')
        print('Rincian : ')
        print(f'Harga Rumah dan Pajak \t= {biaya_pajak}')
        print(f'Biaya Notaris         \t= {notaris*int(harga)}')
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
            global dp

            dp = .15*int(harga)//1
            try:
                waktu = float(input('Masukkan jangka waktu dalam tahun = '))
            except ValueError :
                print('**Mohon Masukkan Dalam Bentuk Angka**')
                bayar_kredit()
            else :
                if waktu == 0 :
                    pembayaran = 'Tunai'
                    total_bayar = (biaya_pajak + (notaris * int(harga)) + PNBP + provisi) - dp //1
                    kuitansi_tunai()
                elif waktu > 0 and waktu <=15 : 
                    pembayaran = 'Kredit'
                    hutang = (biaya_pajak + (notaris * int(harga)) + PNBP + provisi) - dp //1
                    cicilan_bunga = ((bunga*hutang)*waktu)//(waktu*12) //1
                    total_bayar = hutang//(12*waktu) + cicilan_bunga //1
                    kuitansi_kredit()
                else :
                    print('**Waktu kredit maksimal adalah 15 tahun**')
                    bayar_kredit()


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
    TIPE RUMAH          : {p}
    TOTAL BAYAR         : {total_bayar}
    METODE PEMBAYARAN   : {pembayaran}
                   
                   ''')

    print(f'''
                    KUITANSI
                                        {formattanggal}

    NAMA                : {nama}
    ALAMAT              : {alamat}
    NO. HP              : {nomor_hp}
    TIPE RUMAH          : {p}
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
    TIPE RUMAH          : {p}
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
    TIPE RUMAH          : {p}
    UANG MUKA           : {dp}
    METODE PEMBAYARAN   : {pembayaran}
    CICILAN TIAP BULAN  : {total_bayar}
    TOTAL CICILAN       : {hutang}
    JANGKA WAKTU        : {waktu} Tahun

                   ''')

