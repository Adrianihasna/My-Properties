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

from perbarui_data import Login
menu = int(input('Masukkan pilihan Menu = '))

if menu == 1 :
    #Program Estimasi Pembangunan Rumah

    print('Estimasi pembangunan Rumah')
elif menu == 2 :
    # Program Estimasi Renovasi Rumah

    print('Estimasi Renovasi Rumah')
elif menu == 3 :
    #Program Pembelian Rumah

    print('Pembelian rumah')
elif menu == 4 :
    #Program Perbarui Data 
    
    login = Login.login_akun()
    print('Perbarui Harga') 
else :
    #Program Selesai

    print('Keluar')