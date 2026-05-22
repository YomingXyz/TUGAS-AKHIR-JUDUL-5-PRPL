class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BSTDasar:
    def __init__(self):
        self.root = None

    def insert_node(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert_node(root.left, key)
        elif key > root.key:
            root.right = self.insert_node(root.right, key)
        return root

    def insert(self, key):
        self.root = self.insert_node(self.root, key)

    def search_node(self, root, key):
        if root is None:
            return False
        if root.key == key:
            return True
        if key < root.key:
            return self.search_node(root.left, key)
        return self.search_node(root.right, key)

    def search(self, key):
        return self.search_node(self.root, key)

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.key, end=" ")
        self.inorder(root.right)

    def preorder(self, root):
        if root is None:
            return
        print(root.key, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)

    def postorder(self, root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.key, end=" ")

    def find_min(self, root):
        if root is None:
            return -1
        current = root
        while current.left is not None:
            current = current.left
        return current.key

    def find_max(self, root):
        if root is None:
            return -1
        current = root
        while current.right is not None:
            current = current.right
        return current.key

    def count_nodes(self, root):
        if root is None:
            return 0
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)

    def sum_nodes(self, root):
        if root is None:
            return 0
        return root.key + self.sum_nodes(root.left) + self.sum_nodes(root.right)


def main():
    bst = BSTDasar()
    pilih = 0
    while pilih != 10:
        print("\n=== Sistem Rekap Transaksi SiToserba ===")
        print("1. Catat Transaksi Baru")
        print("2. Cek Nominal Transaksi")
        print("3. Daftar Transaksi (Inorder / Urut Terkecil-Terbesar)")
        print("4. Tampilkan Preorder")
        print("5. Tampilkan Postorder")
        print("6. Transaksi Terkecil Hari Ini (Min)")
        print("7. Transaksi Terbesar Hari Ini (Max)")
        print("8. Total Pelanggan (Count nodes)")
        print("9. Total Omzet (Sum nodes)")
        print("10. Tutup Kasir (Keluar)")
        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input tidak valid!")
            continue
            
        if pilih == 1:
            try:
                x = int(input("Masukkan nominal belanja (Rp): "))
                bst.insert(x)
                print(f"Transaksi senilai Rp{x} berhasil dicatat.")
            except ValueError:
                print("Input tidak valid!")
        elif pilih == 2:
            try:
                x = int(input("Cari nominal transaksi (Rp): "))
                if bst.search(x):
                    print("Status: Transaksi Ditemukan.")
                else:
                    print("Status: Transaksi Tidak Ditemukan.")
            except ValueError:
                print("Input tidak valid!")
        elif pilih == 3:
            print("Urutan Transaksi: Rp ", end="")
            bst.inorder(bst.root)
            print()
        elif pilih == 4:
            print("Format Preorder: Rp ", end="")
            bst.preorder(bst.root)
            print()
        elif pilih == 5:
            print("Format Postorder: Rp ", end="")
            bst.postorder(bst.root)
            print()
        elif pilih == 6:
            print(f"Transaksi Terkecil: Rp {bst.find_min(bst.root)}")
        elif pilih == 7:
            print(f"Transaksi Terbesar: Rp {bst.find_max(bst.root)}")
        elif pilih == 8:
            print(f"Jumlah Pelanggan: {bst.count_nodes(bst.root)} orang")
        elif pilih == 9:
            print(f"Total Omzet Hari Ini: Rp {bst.sum_nodes(bst.root)}")
        elif pilih == 10:
            print("Kasir ditutup. Program selesai.")
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
