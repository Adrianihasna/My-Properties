import csv
def tambah_data():
    material = input('Masukkan Nama Material \t= ')
    harga =  float(input('Masukkan Harga \t\t= '))
    keterangan = input('Masukkan Keterangan \t= ')
    tambah = '\n{},{},{}'.format(material,harga,keterangan)
    data = open('My-Property\perbarui_data\DATA_MATERIAL.csv','a')
    data.write(tambah)
    data.close()
    return

def hapus_data():
    from tabulate import tabulate
    daftar_harga = []
    with open('My-Property\perbarui_data\DATA_MATERIAL.csv') as daftar :
        daftar = csv.reader(daftar,delimiter=',')
        for i in daftar :
            daftar_harga.append(i)
    daftar_harga.pop(0)
    print('\n\t\t  DAFTAR HARGA MATERIAL ')
    print('-'*62)
    print(tabulate(daftar_harga, headers = ['MATERIAL', 'HARGA', 'KETERANGAN' ], tablefmt='orgtbl'))
    
    # nama = input('Masukkan Nama Material yang ingin dihapus = ')
    # for i in daftar_harga :
    #     if nama == daftar_harga[0] :
    #         print(f'Harga {nama} berhasil dihapus ')
    #     print(i)
    return

def update_data() :
    from tabulate import tabulate
    daftar_harga = []
    with open('My-Property\perbarui_data\DATA_MATERIAL.csv') as daftar :
        daftar = csv.reader(daftar,delimiter=',')
        for i in daftar :
            daftar_harga.append(i)
    daftar_harga.pop(0)
    print('\n\t\t  DAFTAR HARGA MATERIAL ')
    print('-'*62)
    print(tabulate(daftar_harga, headers = ['MATERIAL', 'HARGA', 'KETERANGAN' ], tablefmt='orgtbl'))
    return

tambah_data()