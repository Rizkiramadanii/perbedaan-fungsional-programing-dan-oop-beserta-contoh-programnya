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
calculator = Calculator()# Membuat objek dari kelas Calculator
print("Hasil penjumlahan: ", calculator.add(5, 3)) # Output: Hasil penjumlahan: 8 # Contoh penggunaan kalkulator
print("Hasil pengurangan: ", calculator.subtract(10, 2)) # Output: Hasil pengurangan: 8 # Contoh penggunaan kalkulator
print("Hasil perkalian: ", calculator.multiply(6, 7)) # Output: Hasil perkalian: 42 # Contoh penggunaan kalkulator
print("Hasil pembagian: ", calculator.divide(25, 5)) # Output: Hasil pembagian: 5.0 # Contoh penggunaan kalkulator