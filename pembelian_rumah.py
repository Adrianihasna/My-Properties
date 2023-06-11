def beli():
    Tipe_A = 300000000 # 300 juta
    Tipe_B = 600000000  # 600 juta
    Tipe_C = 1000000000  # 1 milyar

    harga_yang_dicari = int(input("Masukkan harga rumah yang Anda cari (Rupiah): "))

    if harga_yang_dicari <= Tipe_A :
        print("Tipe Rumah : A")
    elif harga_yang_dicari >= Tipe_A and harga_yang_dicari <= Tipe_B :
        print("Tipe Rumah : B")
    elif harga_yang_dicari >= Tipe_B and harga_yang_dicari <= Tipe_C:
        print("Tipe Rumah : C")
    else:
        print("Tipe rumah dengan harga yang anda cari belum tersedia")

    pembelian = input("Apakah Anda ingin melakukan pembelian? (Ya/Tidak): ")
    pembelian.lower()

def hitung_biaya_pajak(harga_rumah):
    pajak_pembelian = harga_rumah * 0.05  # Pajak pembelian 5% dari harga rumah
    biaya_pajak = pajak_pembelian + 5000000  # Tambahan biaya administrasi
    
    return biaya_pajak

def hitung_biaya_total(harga_rumah, tipe_rumah):
    harga_pokok = harga_rumah * 0.8  # Harga pokok 80% dari harga rumah
    biaya_pajak = hitung_biaya_pajak(harga_rumah)
    
    if tipe_rumah == "Apartment":
        biaya_asuransi = harga_rumah * 0.02  # Biaya asuransi 2% dari harga rumah
        biaya_total = harga_pokok + biaya_pajak + biaya_asuransi
    elif tipe_rumah == "Townhouse":
        biaya_perijinan = 10000000  # Biaya perijinan tetap sebesar Rp 10.000.000
        biaya_total = harga_pokok + biaya_pajak + biaya_perijinan
    elif tipe_rumah == "Villa":
        biaya_pengamanan = harga_rumah * 0.015  # Biaya pengamanan 1.5% dari harga rumah
        biaya_total = harga_pokok + biaya_pajak + biaya_pengamanan
    else:
        print("Tipe rumah tidak valid.")
        return None
    
    return biaya_total

def main():
    harga_rumah = float(input("Masukkan harga rumah: "))
    tipe_rumah = input("Masukkan tipe rumah (Apartment/Townhouse/Villa): ")
    
    biaya_total = hitung_biaya_total(harga_rumah, tipe_rumah)
    if biaya_total:
        print("Biaya total pembelian rumah adalah: Rp", biaya_total)

if __name__ == "__main__":
    main()
