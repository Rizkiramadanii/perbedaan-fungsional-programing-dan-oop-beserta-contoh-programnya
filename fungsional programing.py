def count_chars(strings):# metode menghitung string
    return sum(len(s) for s in strings if len(s) > 4)# kondisi pengulangan program
strings = ["apple", "banana", "pear", "mango", "kiwi"] # data yang ingin di periksa
print(count_chars(strings))# menampilkan hasil