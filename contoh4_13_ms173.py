"""User-defined function yang memulangkan nombor besar di kiri
dan nombor kecil di kanan"""

def besar_kecil(x,y):   # x dan y ialah parameter, user-defined function ialah besar_kecil()
    if x > y:           # struktur kawalan pilihan / dwipilihan if-else digunakan
        return x, y
    else:
        return y, x
    
def main():
    #bahagian utama atur cara
    #Minta pengguna memasukkan dua nombor
    a = int(input("Masukkan nombor integer yang pertama: "))    
    b = int(input("Masukkan nombor integer yang kedua: "))      

    #panggilan user-defined function
    [besar, kecil] = besar_kecil(a, b)      
    print(f"Nombor {besar} lebih besar daripada {kecil}")

if __name__ == "__main__":
    main()