#Login
import csv
import pandas as pd
import os
from tabulate import tabulate

def login_akun() :
    os.system('cls')
    akun =[]
    with open('perbarui_data\\akun.csv') as csv_file :
        csv_reader = csv.reader(csv_file, delimiter=';')
        for i in csv_reader:
            akun.append(i)
    label = akun.pop(0)
    
    i=0
    while i !=3 :
        username = input('Masukkan Username = ')
        password = input('Masukkan Password = ')
        if username == akun[0][0] and password == akun[0][1] :
            print('\nLOGIN BERHASIL')
            pilihan()
            break
        elif username == akun[1][0] and password == akun[1][1] :
            print('\nLOGIN BERHASIL')
            pilihan()
            break
        elif username == akun[2][0] and password == akun[2][1] :
            print('\nLOGIN BERHASIL')
            pilihan()
            break
        elif username == akun[3][0] and password == akun[3][1] :
            print('\nLOGIN BERHASIL')
            pilihan()
            break
        else :
            i+=1
            print('**LOGIN GAGAL**')
    else :
        print('**AKSES DITOLAK**')
    

#Memilih Program
def pilihan():
    os.system('cls')
    print('''

Silahkan Pilih Menu :

[1] Tambah Data
[2] Perbarui Data
[3] Hapus Data
[4] Keluar
    
    ''')
    
    try : 
        pilih = int(input('Masukkan Pilihan = '))
    except ValueError :
        print('\nNilai Yang Anda Masukkan Salah')
        pilihan()
    else:
        if pilih == 1 :
            tambah_data()
        elif pilih == 2 : 
            update_data()
        elif pilih == 3 :
            hapus_data()
        elif pilih == 4 :
            print()
        else : 
            pilihan()
    return


# Perbarui Data
def tambah_data():
    os.system('cls')
    material = input('Masukkan Nama Material \t= ')
    def hargabaru():
        global harga
        try :
            harga =  int(input('Masukkan Harga \t\t= '))
        except ValueError :
            print('\n**Mohon Masukkan Harga Dengan Angka**')
            hargabaru()
    hargabaru()
    keterangan = input('Masukkan Keterangan \t= ')

    tambah = '\n{},{},{}'.format(material,harga,keterangan)
    data = open('perbarui_data\data_material.csv','a')
    data.write(tambah)
    data.close()
    print('Data Berhasil Ditambahkan ')

    lagi = input('Tambah Data Lagi (y/n) = ')
    lagi = lagi.lower()
    if lagi == 'y' :
        tambah_data()
    else :
        pilihan()
    
    return

def hapus_data():
    from tabulate import tabulate
    os.system('cls')

    daftar = pd.read_csv('perbarui_data\data_material.csv')
    print('\n','~'*34,'DATA MATERIAL','~'*34)
    print()
    print(tabulate(daftar,headers = ['Index','     MATERIAL     ', '     HARGA     ', '     KETERANGAN     ' ], tablefmt='grid' )) 
    def hapus_datadata():
        try :
            hapus = int(input("\nMasukkan no indeks yang ingin dihapus = "))
        except ValueError :
            print('\n**Mohon Masukkan Angka Sesuai Index**')
            hapus_datadata()
        else : 
            if hapus in range(len(daftar)):
                daftar.drop(index=hapus,
                            inplace=True)
                daftar.to_csv('perbarui_data\data_material.csv',index= False)
                daftar.reset_index(drop=True,
                            inplace=True)
                print('\n','~'*32,'DATA MATERIAL BARU','~'*32)
                print()
                print(tabulate(daftar,headers = ['Index','     MATERIAL     ', '     HARGA     ', '     KETERANGAN     ' ], tablefmt='grid' )) 
                
                hapus_lagi = input('\nApakah Anda Ingin Menghapus Data Lagi (y/n) =  ')
                hapus_lagi = hapus_lagi.lower()
                if hapus_lagi == 'y':
                    hapus_data()
                else :
                    pilihan()
            else :
                print('\n**Mohon Masukkan Angka Sesuai Index**')
                hapus_lagi = input('\nApakah Anda Ingin Menghapus Data (y/n) = ')
                hapus_lagi = hapus_lagi.lower()
                if hapus_lagi == 'y':
                    hapus_data()
                else :
                    pilihan()
        return
    hapus_datadata()
    return

def update_data():
    os.system('cls')
    daftar = pd.read_csv('perbarui_data\data_material.csv')
    print('\n','~'*34,'DATA MATERIAL','~'*34)
    print()
    print(tabulate(daftar,headers = ['Index','     MATERIAL     ', '     HARGA     ', '     KETERANGAN     ' ], tablefmt='grid' ))
    def ubah():
        try :
            indeks = int(input('\nMasukkan Indeks Material Yang Ingin di Ubah = '))
        except ValueError :
            print('\n**Mohon Masukkan Angka Sesuai Index**')
            ubah()
        else:
            if indeks in range(len(daftar)):
                def update_harga():
                    global harga_lama
                    global harga_baru
                    try : 
                        harga_lama = int(input('Masukkan Harga Lama = '))
                        harga_baru = int(input('Masukkan Harga Baru = '))
                    except ValueError :
                        print('\n**Mohon Masukkan Harga Berupa Angka**')
                    else:
                        daftar.loc[indeks:indeks] = daftar.replace(harga_lama,harga_baru)
                        daftar.to_csv('perbarui_data\data_material.csv',index= False)
                        print('\n','~'*32,'DATA MATERIAL BARU','~'*32)
                        print()
                        print(tabulate(daftar,headers = ['Index','     MATERIAL     ', '     HARGA     ', '     KETERANGAN     ' ], tablefmt='grid' ))
                update_harga()
                update_lagi = input('\nApakah Anda Ingin Memperbarui Data Lagi (y/n) = ')
                update_lagi = update_lagi.lower()
                if update_lagi == 'y' :
                    ubah()
                else :
                    pilihan()

            else: 
                print('\n**Mohon Masukkan Angka Sesuai Index**')
                update_lagi = input('\nApakah Anda Ingin Memperbarui Data (y/n) = ')
                update_lagi = update_lagi.lower()
                if update_lagi == 'y' :
                    ubah()
                else :
                    pilihan()
        return
    ubah()
    return        
