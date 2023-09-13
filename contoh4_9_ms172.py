#fungsi yang mengira kuasa dua
def kuasadua(x):    # x ialah parameter, nama user-defined function ialah kuasadua()
    return x*x

#bahagian utama atur cara
#minta pengguna memasukkan satu nombor
def main():
    nom = int(input("Masukkan satu nombor integer: "))  # nom ialah pembolehubah

    #panggilan fungsi
    nom_kuasa = kuasadua(nom)  
    print(f"Kuasa dua bagi {nom} ialah {nom_kuasa}")

if __name__ == "__main__":
    main()