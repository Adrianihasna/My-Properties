import os 
from perbarui_data import perbarui_data
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
    global menu
    try :
        menu = int(input('\nMasukkan pilihan Menu = '))
    except ValueError :
        print('\nKesalahan Input')
        utama()
    else :
        if menu in range(1,6):
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
                login = perbarui_data.login_akun()
                beranda()
                utama()
            elif menu == 5:
                #Program Selesai
                print('\nTERIMA KASIH SUDAH MENGGUNAKAN PROGRAM INI')
                exit()
        else : 
            print('\nKesalahan Input')
            utama()

beranda()
utama()
