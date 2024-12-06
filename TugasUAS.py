#Nama: Christian Rafael Abram
#Nim: 24210058
#Dosen Pengampu: Glenn David Maramis, S.Komp, M.Cs
#tugas Uas: Pemrograman
#program yang dibuat:Sistem Inventaris
import csv


class Inventaris:
    def __init__(self):
        self.produk = {}
        self.laporan_penjualan = []

    def tambah_produk(self, nama, jumlah, harga):
        if nama in self.produk:
            self.produk[nama]['jumlah'] += jumlah
        else:
            self.produk[nama] = {'jumlah': jumlah, 'harga': harga}
        print(f"Produk {nama} ditambahkan. Stok sekarang: {self.produk[nama]['jumlah']}")

    def kurangi_produk(self, nama, jumlah):
        if nama in self.produk and self.produk[nama]['jumlah'] >= jumlah:
            self.produk[nama]['jumlah'] -= jumlah
            print(f"Produk {nama} dikurangi. Stok sekarang: {self.produk[nama]['jumlah']}")
            if self.produk[nama]['jumlah'] < 5:
                print(f"Stok {nama} mulai menipis!")
        else:
            print("Gagal mengurangi stok. Cek nama produk dan jumlahnya.")

    def total_nilai_inventaris(self):
        total_nilai = sum(item['jumlah'] * item['harga'] for item in self.produk.values())
        print(f"Total nilai barang di inventaris: {total_nilai}")
        return total_nilai

    def catat_penjualan(self, nama, jumlah):
        if nama in self.produk and self.produk[nama]['jumlah'] >= jumlah:
            self.kurangi_produk(nama, jumlah)
            nilai_penjualan = jumlah * self.produk[nama]['harga']
            self.laporan_penjualan.append({'produk': nama, 'jumlah': jumlah, 'nilai': nilai_penjualan})
            print(f"Penjualan: {jumlah} unit dari {nama}. Nilai penjualan: {nilai_penjualan}")
        else:
            print("Gagal mencatat penjualan. Cek nama produk dan jumlahnya.")

    def ekspor_data(self, nama_file='data_inventaris.csv'):
        with open(nama_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Produk', 'Jumlah', 'Harga'])
            for produk, detail in self.produk.items():
                writer.writerow([produk, detail['jumlah'], detail['harga']])
            print(f"Data inventaris diekspor ke {nama_file}")

def main():
    inventaris = Inventaris()

    while True:
        print("\nMenu Inventaris:")
        print("1. Tambah Produk")
        print("2. Kurangi Stok")
        print("3. Hitung Total Nilai Barang")
        print("4. Catat Penjualan")
        print("5. Ekspor Data")
        print("6. Keluar")

        pilihan = input("Pilih opsi (1-6): ")

        if pilihan == '1':
            nama = input("Masukkan nama produk: ")
            jumlah = int(input("Masukkan jumlah produk: "))
            harga = float(input("Masukkan harga produk: "))
            inventaris.tambah_produk(nama, jumlah, harga)

        elif pilihan == '2':
            nama = input("Masukkan nama produk yang mau dikurangi: ")
            jumlah = int(input("Masukkan jumlah yang mau dikurangi: "))
            inventaris.kurangi_produk(nama, jumlah)

        elif pilihan == '3':
            inventaris.total_nilai_inventaris()

        elif pilihan == '4':
            nama = input("Masukkan nama produk yang terjual: ")
            jumlah = int(input("Masukkan jumlah yang terjual: "))
            inventaris.catat_penjualan(nama, jumlah)

        elif pilihan == '5':
            nama_file = input("Masukkan nama file untuk ekspor (default: data_inventaris.csv): ") or 'data_inventaris.csv'
            inventaris.ekspor_data(nama_file)

        elif pilihan == '6':
            print("Keluar dari sistem. Makasih!")
            break

        else:
            print("Maaf pilihan tidak valid! Coba lagi yah:).")

if __name__ == "__main__":
    main()