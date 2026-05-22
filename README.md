A. PROGRAM REKAP TRANSAKSI HARIAN (SITOSERBA) MENGGUNAKAN BINARY SEARCH TREE (BST)

B. Deskripsi Singkat

Program ini berfungsi sebagai fitur pencatatan dan rekapitulasi nominal transaksi harian kasir, yang sangat cocok diimplementasikan pada sistem manajemen minimarket seperti SiToserba. Program ini memanfaatkan struktur data pohon biner pencarian atau *Binary Search Tree* (BST). Prinsip utama yang berjalan di sini adalah nilai (nominal uang) yang lebih kecil dari akar (*root*) akan diletakkan di cabang sebelah kiri, sedangkan nilai yang lebih besar akan diletakkan di cabang sebelah kanan.

Program dilengkapi dengan fitur utama BST yaitu insert (untuk mencatat nominal belanja baru), search (untuk mengecek transaksi tertentu), inorder (untuk melihat keseluruhan riwayat transaksi yang otomatis terurut dari terkecil ke terbesar), find_min dan find_max (mengecek rekor transaksi), serta kalkulasi count_nodes (menghitung total pelanggan) dan sum_nodes (menghitung total omzet pendapatan). Untuk mencegah terjadinya *crash* saat program berjalan, menu input juga sudah dibungkus dengan validasi try-except sehingga jika pengguna memasukkan selain angka (seperti huruf) pada pilihan menu, program akan tetap berjalan dan memberikan peringatan.

C. Source Code
<img width="878" height="944" alt="Cuplikan layar 2026-05-22 213525" src="https://github.com/user-attachments/assets/03ab2a68-d4a4-44c1-a1ff-47e3c3736a1b" />
<img width="637" height="892" alt="Cuplikan layar 2026-05-22 213536" src="https://github.com/user-attachments/assets/ad5161cb-6598-4241-8b9a-ee80fafbcc6b" />
<img width="1064" height="889" alt="Cuplikan layar 2026-05-22 213547" src="https://github.com/user-attachments/assets/86b34def-ae16-4364-a974-a90269a29a91" />
<img width="911" height="906" alt="Cuplikan layar 2026-05-22 213557" src="https://github.com/user-attachments/assets/026fc486-3f94-4cdf-a008-461957bf29e0" />
<img width="1018" height="511" alt="Cuplikan layar 2026-05-22 213605" src="https://github.com/user-attachments/assets/3d535efb-7a13-46e7-9191-f377993dacb6" />

* membuat class Node: sebagai cetak biru untuk membuat kotak penyimpan data nominal transaksi
* membuat fungsi inisialisasi def **init**(self, key): yang pertama kali jalan saat Node baru dibuat
* menyimpan nilai nominal uang yang dimasukkan ke dalam self.key
* menyiapkan penunjuk cabang anak sebelah kiri dengan self.left = None yang awalnya kosong
* menyiapkan penunjuk cabang anak sebelah kanan dengan self.right = None yang awalnya kosong
* membuat class BSTDasar: sebagai kerangka utama untuk struktur pohon keseluruhan
* membuat fungsi inisialisasi awal pohon def **init**(self):
* menentukan akar (*root*) atau data pucuk pohon masih kosong dengan self.root = None
* membuat fungsi def insert_node(self, root, key): untuk mencari posisi yang pas saat menambah transaksi baru
* pengondisian if root is None: untuk mengecek apakah posisi tersebut kosong
* jika kosong, langsung letakkan nilai baru dengan return Node(key)
* pengondisian if key < root.key: jika nominal baru lebih kecil dari node saat ini
* melempar nilai ke cabang kiri secara rekursif menggunakan root.left = self.insert_node(root.left, key)
* pengondisian elif key > root.key: jika nominal baru lebih besar dari node saat ini
* melempar nilai ke cabang kanan secara rekursif menggunakan root.right = self.insert_node(root.right, key)
* mengembalikan struktur pohon yang sudah diperbarui dengan return root
* membuat fungsi pembantu def insert(self, key): agar pemanggilan di menu lebih ringkas
* memulai proses penambahan data dari akar utama dengan self.root = self.insert_node(self.root, key)
* membuat fungsi pencarian inti def search_node(self, root, key):
* mengembalikan False jika cabang sudah ujung dan data tidak ada (if root is None:)
* mengembalikan True jika nominal di node sama persis dengan yang dicari (if root.key == key:)
* menggeser pencarian ke kiri jika nilai dicari lebih kecil, atau ke kanan jika lebih besar menggunakan penelusuran rekursif
* membuat fungsi pembantu pencarian def search(self, key): dari akar pohon
* membuat fungsi penelusuran urut def inorder(self, root):
* menggunakan rekursi self.inorder(root.left) untuk menelusuri nilai terkecil di ujung kiri terlebih dahulu
* mencetak isi data ke layar dengan print(root.key, end=" ")
* melanjutkan penelusuran ke cabang kanan menggunakan self.inorder(root.right)
* membuat fungsi penelusuran preorder (cetak akar, lalu ke kiri, lalu kanan) dan postorder (kiri, kanan, lalu cetak akar)
* membuat fungsi mencari nilai terkecil def find_min(self, root):
* menggunakan perulangan while current.left is not None: untuk terus bergeser ke cabang paling ujung kiri
* mengembalikan nilai di ujung kiri tersebut dengan return current.key
* membuat fungsi find_max dengan logika serupa namun bergeser mentok ke cabang kanan (current.right)
* membuat fungsi hitung pelanggan def count_nodes(self, root):
* menggunakan return 1 + self.count_nodes(root.left) + self.count_nodes(root.right) untuk menghitung total node di seluruh pohon
* membuat fungsi hitung omzet def sum_nodes(self, root):
* menggunakan logika penjumlahan serupa namun menjumlahkan nominal nilai uangnya menggunakan return root.key + ...
* membuat fungsi utama antarmuka def main():
* membuat objek pohon baru dari class BSTDasar dengan bst = BSTDasar()
* menyiapkan variabel pilih = 0 untuk menampung input pilihan menu dari user
* membuat perulangan while pilih != 10: agar menu selalu muncul selama kasir belum ditutup
* mencetak teks pilihan menu 1 sampai 10
* menggunakan blok try untuk menangkap input angka int(input(...)) dari kasir
* menangkap error dengan except ValueError: jika input bukan berupa angka, lalu mencetak peringatan "Input tidak valid!" dan continue untuk mengulang menu
* membuat percabangan bersarang if, elif, else untuk mengeksekusi fitur sesuai nomor pilihan menu
* menu 1 meminta input angka uang dan memanggil fungsi bst.insert(x)
* menu 2 meminta input nominal dan dicari menggunakan bst.search(x)
* menu 3, 4, 5 memanggil fungsi penelusuran seperti bst.inorder(bst.root)
* menu 6 dan 7 mencetak nilai ekstrem menggunakan find_min dan find_max
* menu 8 mencetak total pelanggan memanggil fungsi count_nodes
* menu 9 mencetak total uang memanggil fungsi sum_nodes
* menu 10 mencetak pesan program selesai untuk keluar dari perulangan
* memastikan program bisa dijalankan langsung dari terminal dengan if **name** == "**main**": main()

D. Output Program
<img width="646" height="986" alt="Cuplikan layar 2026-05-22 213340" src="https://github.com/user-attachments/assets/2e800b7e-3eef-494c-997f-5bfd02255cdb" />
<img width="648" height="982" alt="Cuplikan layar 2026-05-22 213349" src="https://github.com/user-attachments/assets/e3aec8f0-c457-4c26-8c9a-1e24d651cf15" />
<img width="697" height="985" alt="Cuplikan layar 2026-05-22 213401" src="https://github.com/user-attachments/assets/c1aaf369-f60d-46a2-83c6-17b4d5f5f765" />
<img width="657" height="449" alt="Cuplikan layar 2026-05-22 213407" src="https://github.com/user-attachments/assets/d1df97bc-8f3b-4046-b986-4c480f145b21" />

Penjelasan Output:
Saat program dijalankan, akan muncul antarmuka menu "Sistem Rekap Transaksi SiToserba". Pertama, kasir menginputkan angka "1" untuk mencatat transaksi baru, lalu memasukkan nominal sebesar 50000. Program merespons dengan menampilkan "Transaksi senilai Rp50000 berhasil dicatat". Kasir kembali memilih menu 1 beberapa kali untuk memasukkan nominal transaksi pembeli berikutnya secara acak, misalnya 30000 dan 70000.
Ketika kasir memilih menu "3" (Daftar Transaksi Inorder), program secara otomatis menampilkan seluruh riwayat nominal uang yang sudah diurutkan dari yang terkecil hingga terbesar (30000 50000 70000) berkat sifat bawaan Binary Search Tree. Selanjutnya, kasir menekan angka "6" dan "7" untuk melihat transaksi terkecil dan terbesar hari itu, di mana program berhasil menampilkan Rp30000 untuk Min dan Rp70000 untuk Max. Pada saat toko akan tutup, kasir memilih menu "8" untuk mengecek total pelanggan dan menu "9" untuk menghitung total omzet. Program secara akurat menjumlahkan total pembeli sebanyak 3 orang dan total omzet sejumlah Rp150000. Setelah selesai, kasir memilih menu "10" dan program ditutup.

E. Link YouTube:
https://youtu.be/P2pSaw9RD0w?si=ZIoNQP0FudrfwxDV
