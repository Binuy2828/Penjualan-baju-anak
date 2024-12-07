import tkinter as tk
from tkinter import messagebox


class ShoppingCartApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Keranjang Belanja")
        
        # Data keranjang
        self.cart = []
        
        # Elemen GUI
        self.create_widgets()
    
    def create_widgets(self):
        # Label dan Entry untuk menambahkan barang
        tk.Label(self.root, text="Nama Barang").grid(row=0, column=0, padx=10, pady=5)
        self.item_name = tk.Entry(self.root)
        self.item_name.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(self.root, text="Jumlah").grid(row=1, column=0, padx=10, pady=5)
        self.item_qty = tk.Entry(self.root)
        self.item_qty.grid(row=1, column=1, padx=10, pady=5)
        
        tk.Label(self.root, text="Harga").grid(row=2, column=0, padx=10, pady=5)
        self.item_price = tk.Entry(self.root)
        self.item_price.grid(row=2, column=1, padx=10, pady=5)
        
        # Tombol untuk menambahkan barang
        tk.Button(self.root, text="Tambah ke Keranjang", command=self.add_to_cart).grid(row=3, column=0, columnspan=2, pady=10)
        
        # Tampilkan keranjang
        self.cart_list = tk.Listbox(self.root, width=50, height=15)
        self.cart_list.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        
        # Tombol untuk menghitung total
        tk.Button(self.root, text="Hitung Total", command=self.calculate_total).grid(row=5, column=0, columnspan=2, pady=10)
    
    def add_to_cart(self):
        name = self.item_name.get()
        qty = self.item_qty.get()
        price = self.item_price.get()
        
        # Validasi input
        if not name or not qty or not price:
            messagebox.showwarning("Peringatan", "Mohon isi semua data barang!")
            return
        
        try:
            qty = int(qty)
            price = float(price)
        except ValueError:
            messagebox.showerror("Error", "Jumlah dan Harga harus berupa angka!")
            return
        
        # Tambahkan ke keranjang
        self.cart.append({"name": name, "qty": qty, "price": price})
        self.cart_list.insert(tk.END, f"{name} - Jumlah: {qty}, Harga: {price}")
        
        # Reset input
        self.item_name.delete(0, tk.END)
        self.item_qty.delete(0, tk.END)
        self.item_price.delete(0, tk.END)
    
    def calculate_total(self):
        if not self.cart:
            messagebox.showinfo("Info", "Keranjang kosong!")
            return
        
        total = sum(item["qty"] * item["price"] for item in self.cart)
        messagebox.showinfo("Total Harga", f"Total harga semua barang: Rp {total:.2f}")


if _name_ == "_main_":
    root = tk.Tk()
    app = ShoppingCartApp(root)
    root.mainloop()
