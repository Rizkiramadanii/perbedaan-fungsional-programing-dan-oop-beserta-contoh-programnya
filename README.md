# perbedaan-fungsional-programing-dan-oop-beserta-contoh-programnya
tugas oop 

pembahasan:
Pemrograman fungsional dan OOP adalah dua cara berbeda untuk menulis kode program. Pemrograman fungsional berfokus pada fungsi sementara OOP berfokus pada objek.

Salah satu perbedaannya adalah bagaimana mereka menangani nilai atau data. Dalam pemrograman fungsional, nilai akan tetap tidak berubah, sedangkan dalam OOP, nilai dapat diubah saat program sedang berjalan.

Perbedaan lainnya adalah cara mereka menangani efek samping. Pemrograman fungsional menghindari efek samping, sedangkan OOP sering menggunakan efek samping.

Pemrograman fungsional juga mendorong komposisi fungsi, yang berarti menggabungkan fungsi dengan fungsi lain untuk membuat fungsi yang lebih kompleks. Dalam OOP, pewarisan dan polimorfisme lebih umum digunakan.

Singkatnya, keduanya memiliki pendekatan yang berbeda untuk menulis kode program, dan masing-masing memiliki kelebihan dan kekurangan tergantung pada situasi dan preferensi programmer. 

contoh program keduanya adalah sebagai berikut:

- fungsional programing:

def count_chars(strings): # metode menghitung string
    return sum(len(s) for s in strings if len(s) > 4) # kondisi pengulangan

strings = ["apple", "banana", "pear", "mango", "kiwi"]
print(count_chars(strings))

program ini akan menghitung jumlah karakter yang ada pada string dalam list jika memenuhi kriteria yakni panjang nya harus lebih dari 4 jadi yang dihitung hanya apple, banana dan mango saja. dan output dari program adalah 16.

- oop:

class Calculator:
    def add(self, x, y): # Metode untuk melakukan penjumlahan
        return x + y
    
    def subtract(self, x, y): # Metode untuk melakukan pengurangan
        return x - y
    
    def multiply(self, x, y): # Metode untuk melakukan perkalian
        return x * y
    
    def divide(self, x, y): # Metode untuk melakukan pembagian
        if y == 0: # Memeriksa apakah pembagi sama dengan 0
            raise ValueError("Pembagian dengan nol tidak valid") # Jika pembagi 0, raise exception
        return x / y

# Membuat objek dari kelas Calculator
calculator = Calculator()

# Contoh penggunaan kalkulator
print("Hasil penjumlahan: ", calculator.add(5, 3)) # Output: Hasil penjumlahan: 8
print("Hasil pengurangan: ", calculator.subtract(10, 2)) # Output: Hasil pengurangan: 8
print("Hasil perkalian: ", calculator.multiply(6, 7)) # Output: Hasil perkalian: 42
print("Hasil pembagian: ", calculator.divide(25, 5)) # Output: Hasil pembagian: 5.0

Program ini memiliki satu kelas yaitu Calculator yang berisi empat metode, yaitu add, subtract, multiply, dan divide. Setiap metode menerima dua argumen yaitu x dan y yang kemudian digunakan untuk melakukan operasi matematika sesuai dengan nama metodenya.

Metode add akan melakukan operasi penjumlahan antara x dan y dan mengembalikan hasilnya.
Metode subtract akan melakukan operasi pengurangan antara x dan y dan mengembalikan hasilnya.
Metode multiply akan melakukan operasi perkalian antara x dan y dan mengembalikan hasilnya.
Metode divide akan melakukan operasi pembagian antara x dan y dan mengembalikan hasilnya. Namun, sebelum melakukan pembagian, metode ini akan memeriksa apakah nilai dari y sama dengan nol. Jika sama dengan nol, maka metode ini akan membangkitkan exception dengan pesan "Pembagian dengan nol tidak valid".
Setelah kelas Calculator didefinisikan, program akan membuat sebuah objek dari kelas tersebut dengan sintaks calculator = Calculator(). Objek ini nantinya akan digunakan untuk melakukan operasi matematika.

Contoh penggunaan kalkulator adalah dengan memanggil metode-metode dari objek calculator dan menyertakan argumen-argumen yang sesuai. Setiap hasil operasi matematika dicetak ke layar menggunakan fungsi print.

Program ini memiliki kelebihan, yaitu jika suatu saat akan ditambahkan fitur-fitur baru pada kalkulator, kita dapat menambahkan metode baru pada kelas Calculator tanpa mengubah kode pada kelas utama. Sehingga memudahkan dalam mengembangkan program yang lebih besar.



