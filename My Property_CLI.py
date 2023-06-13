import os 
from perbarui_data import Perbarui_data
import renovasi as renov
import estimasibangun as estimasi
import pembelian_rumah as beli 

os.system('cls')

def beranda() :
    print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Selamat Datang Di My Property
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pilihan menu :

[1] Estimasi Pembangunan 
[2] Estimasi Renovasi Rumah 
[3] Pembelian Rumah 
[4] Perbarui Harga 
[5] Keluar 
\n''')


def utama():
    try :
        menu = int(input('Masukkan pilihan Menu = '))
    except ValueError :
        print('Kesalahan Input')
        utama()
    else :
        while menu not in range(1,6) :
            menu = int(input('Masukkan pilihan Menu = '))
        if menu == 1 :
            #Program Estimasi Pembangunan Rumah
            estimasi_pembangunan = estimasi.main()
            beranda()
            utama()
        elif menu == 2 :
            # Program Estimasi Renovasi Rumah
            renovasi = renov.main()
            beranda()
            utama()
        elif menu == 3 :
            #Program Pembelian Rumah
            print('Pembelian rumah')
            pembelian = beli.beli()
            beranda()
            utama()
        elif menu == 4 :
            #Program Perbarui Data 
            login = Perbarui_data.login_akun()
            beranda()
            utama()
        elif menu == 5:
            #Program Selesai
            print('\nTERIMA KASIH SUDAH MENGGUNAKAN PROGRAM INI')
        else : 
            print('Mohon Masukkan Pilihan Sesuai Menu')

beranda()
utama()