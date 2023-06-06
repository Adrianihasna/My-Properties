import os 
os.system('cls')

print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Selamat Datang Di My Property
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pilihan menu :

[1] Estimasi Pembangunan Rumah 
[2] Estimasi Renovasi Rumah 
[3] Pembelian Rumah 
[4] Perbarui Harga 
[5] Keluar 
\n''')

from perbarui_data import Perbarui_data
import renovasi as r
import estimasi_pembangunan as es
menu = int(input('Masukkan pilihan Menu = '))

if menu == 1 :
    #Program Estimasi Pembangunan Rumah
    estimasi = es.tampilkan_tipe_pembangunan()
elif menu == 2 :
    # Program Estimasi Renovasi Rumah
    renov = r.main()
elif menu == 3 :
    #Program Pembelian Rumah
    print('Pembelian rumah')
elif menu == 4 :
    #Program Perbarui Data 
    login = Perbarui_data.login_akun()
    print('Perbarui Harga') 
else :
    #Program Selesai
    print('Keluar')