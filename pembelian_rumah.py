def beli():
    Tipe_A = 300000000  # 300 juta
    Tipe_B = 600000000  # 600 juta
    Tipe_C = 1000000000  # 1 milyar

    harga_yang_dicari = int(input("Masukkan harga rumah yang Anda cari (Rupiah): "))

    if harga_yang_dicari <= Tipe_A:
        print("Tipe Rumah : A")
        return "A"
    elif harga_yang_dicari >= Tipe_A and harga_yang_dicari <= Tipe_B :
        print("Tipe Rumah : B")
        return "B"
    elif harga_yang_dicari >= Tipe_B and harga_yang_dicari <= Tipe_C :
        print("Tipe Rumah : C")
        return "C"
    else:
        print("Tipe rumah dengan harga yang anda cari belum tersedia")
        return None

def hitung_biaya_pajak(harga_rumah):
    pajak_pembelian = harga_rumah * 0.05  # Pajak pembelian 5% dari harga rumah
    biaya_pajak = pajak_pembelian + 5000000  # Tambahan biaya administrasi

    return biaya_pajak

def hitung_biaya_total(harga_rumah, tipe_rumah):
    harga_pokok = harga_rumah * 0.8  # Harga pokok 80% dari harga rumah
    biaya_pajak = hitung_biaya_pajak(harga_rumah)

    if tipe_rumah == "A":
        biaya_asuransi = harga_rumah * 0.02  # Biaya asuransi 2% dari harga rumah
        biaya_total = harga_pokok + biaya_pajak + biaya_asuransi
    elif tipe_rumah == "B":
        biaya_perijinan = 10000000  # Biaya perijinan tetap sebesar Rp 10.000.000
        biaya_total = harga_pokok + biaya_pajak + biaya_perijinan
    elif tipe_rumah == "C":
        biaya_pengamanan = harga_rumah * 0.015  # Biaya pengamanan 1.5% dari harga rumah
        biaya_total = harga_pokok + biaya_pajak + biaya_pengamanan
    else:
        print("Tipe rumah tidak valid.")
        return None

    return biaya_total

def pembayaran():
    pilihan_pembayaran = input("Apakah Anda ingin melakukan pembayaran? (ya/tidak): ")
    if pilihan_pembayaran.lower() == "ya":
        return True
    elif pilihan_pembayaran.lower() == "tidak":
        return False
    else:
        print("Pilihan tidak valid. Pembayaran tidak dilakukan.")
        return False

def proses_pembayaran(tipe_rumah, metode_pembayaran):
    nama = input("Masukkan nama: ")
    alamat = input("Masukkan alamat: ")
    nomor_hp = input("Masukkan nomor HP: ")
    print("\n--- Kwitansi ---")
    print("Nama: ", nama)
    print("Alamat: ", alamat)
    print("Nomor HP: ", nomor_hp)
    print("Tipe Rumah: ", tipe_rumah)
    print("Metode Pembayaran: ", metode_pembayaran)

def pilih_metode_pembayaran():
    metode_pembayaran = input("Pilih metode pembayaran (cash/kredit): ")
    if metode_pembayaran.lower() == "cash":
        return "Cash"
    elif metode_pembayaran.lower() == "kredit":
        return "Kredit"
    else:
        print("Metode pembayaran tidak valid.")
        return None

def hitung_jumlah_cicilan(harga_rumah):
    jumlah_cicilan = int(input("Masukkan jumlah cicilan (dalam bulan): "))
    cicilan_per_bulan = harga_rumah / jumlah_cicilan
    return cicilan_per_bulan

def hitung_jangka_waktu(jumlah_cicilan):
    jangka_waktu = int(input("Masukkan jangka waktu pembayaran (dalam bulan): "))
    total_bulan = jumlah_cicilan * jangka_waktu
    return total_bulan

def main():
    print("Selamat datang di Program Pembelian Rumah")
    print("========================================")
    tipe_rumah = beli()
    if tipe_rumah:
        harga_rumah = float(input("Masukkan harga rumah: "))
        if pembayaran():
            metode_pembayaran = pilih_metode_pembayaran()

            if metode_pembayaran == "Cash":
                proses_pembayaran(tipe_rumah, metode_pembayaran)
            elif metode_pembayaran == "Kredit":
                jumlah_cicilan = hitung_jumlah_cicilan(harga_rumah)
                total_bulan = hitung_jangka_waktu(jumlah_cicilan)
                proses_pembayaran(tipe_rumah, metode_pembayaran)
                print("Jumlah Cicilan per Bulan: ", jumlah_cicilan)
                print("Total Bulan Pembayaran: ", total_bulan)
        else:
            print("Pembayaran tidak dilakukan.")
    else:
        print("Pembelian rumah dibatalkan.")

if __name__ == "__main__":
    main()