#Login
import csv
import pandas as pd
import os

def login_akun() :
    akun =[]
    with open('My-Property\perbarui_data\Akun.csv') as csv_file :
        csv_reader = csv.reader(csv_file, delimiter=';')
        for i in csv_reader:
            akun.append(i)
    label = akun.pop(0)

    username = input('Masukkan Username = ')
    password = input('Masukkan Password = ')

    for i in range(len(akun)) :
        if username == akun[i][0] :
            if password == akun[i][1] :
                print('\nLOGIN BERHASIL')
                pilihan()
            else :
                print('\nPassword Yang Anda Masukkan Salah')
            break
    if username != akun[i][0] :
         print('\nUsername Tidak Tersedia')
    return

#Memilih Program
def pilihan():
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
        print('Nilai Yang Anda Masukkan Salah')
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
    harga =  int(input('Masukkan Harga \t\t= '))
    keterangan = input('Masukkan Keterangan \t= ')

    tambah = '\n{},{},{}'.format(material,harga,keterangan)
    data = open('My-Property\perbarui_data\DATA_MATERIAL.csv','a')
    data.write(tambah)
    data.close()
    print('Data Berhasil Ditambahkan ')

    lagi = input('Tambah Data Lagi (ya/tidak) = ')
    lagi.lower()
    if lagi == 'ya' :
        tambah_data()
    else :
        pilihan()
    return

def hapus_data():
    from tabulate import tabulate
    os.system('cls')

    daftar = pd.read_csv('My-Property\perbarui_data\DATA_MATERIAL.csv')
    print('~'*34,'DATA MATERIAL','~'*34)
    print()
    print('-'*83)
    print(tabulate(daftar,headers = ['Index','     MATERIAL     ', '     HARGA     ', '     KETERANGAN     ' ], tablefmt='grid' )) 
    print('-'*83)
    print()
    try :
        hapus = int(input("Masukkan no indeks yang ingin dihapus = "))
    except ValueError :
        print('Mohon Masukkan Angka Sesuai Indeks')
        hapus_data()
    except KeyError :
        hapus_data()
    else : 
        print()
        daftar.drop(index=hapus,
                    inplace=True)
        daftar.to_csv('My-Property\perbarui_data\DATA_MATERIAL.csv',index= False)
        daftar.reset_index(drop=True,
                    inplace=True)
        print('~'*32,'DAFTAR HARGA BARU','~'*32)
        print()
        print(tabulate(daftar,headers = ['Index','     MATERIAL     ', '     HARGA     ', '     KETERANGAN     ' ], tablefmt='grid' )) 
        

    hapus_lagi = input('\nApakah Anda Ingin Menghapus Data Lagi (ya/tidak) ')
    hapus_lagi.lower()
    if hapus_lagi == 'ya':
        hapus_data()
    else :
        pilihan()
    return

def update_data() :
    from tabulate import tabulate
    os.system('cls')

    daftar = pd.read_csv('My-Property\perbarui_data\DATA_MATERIAL.csv')
    print('~'*34,'DATA MATERIAL','~'*34)
    print()
    print(tabulate(daftar,headers = ['Index','     MATERIAL     ', '     HARGA     ', '     KETERANGAN     ' ], tablefmt='grid' )) 
    print()
    # nama_data = int(input('Masukkan Indeks Nama Material Yang Ingin Diganti = '))
    # harga_baru = int(input('Masukkan Harga Baru = '))
    # daftar[nama_data][1] = daftar[nama_data][1].replace([daftar][1],[harga_baru])
    # print(tabulate(daftar,headers = ['Index','     MATERIAL     ', '     HARGA     ', '     KETERANGAN     ' ], tablefmt='grid' )) 
    
    return
