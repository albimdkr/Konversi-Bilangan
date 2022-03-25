#Albi Mudakar Nasyabi
#21552011235
#Konversi Bilangan

import os

def biner(desimal):
    #Deklarasi Variabel
    des = desimal
    Lbagi = []
    Lsisa = []

    #kondisi : bilamana kurang dari dua maka ke langkah berikutnnya
    if (des < 2):
        Lbagi.append("")
        Lsisa.append(des)
    else:
      #kondisi : bilamana lebih dari dua sama dengan maka hitung dibagi dan sisa
      while (des >= 2): 
        bagi = des // 2
        sisa = des % 2

        Lbagi.append(bagi)
        Lsisa.append(sisa)

        des = bagi

      return [Lbagi, Lsisa]

def main ():
  pilih ="y"
  while (pilih == "y"):
    os.system("cls")
    print() 
    #Pemberian Nama
    print("\t\t Nama    : Albi Mudakar Nasyabi")
    print("\t\t NPM     : 21552011235")
    print("\t\t MATKUL  : Metode Numerik")
    print()
    print("\t\t KONVERSI BILANGAN DESIMAL KE BINER")
    print("\t\t Soal :") #Soal
    print("\t\t 1. 25689")
    print("\t\t 2. 37896")
    print("\t\t 3. 27001")
    print("="*110)
    #Input Bil Desimal
    x = int(input("\t\t Masukan Bilangan Desimal yang akan dikonversi : ")) 
    des = x

    #looping
    for i in range(len(biner(des)[0])): 
        bagiB = biner(des)[0][i]

    # append elemen Biner
    desKeBin = []
    for i in (biner(des)[1]):
      desKeBin.append(i)
    desKeBin.append(biner(des)[0] [ len( biner(des)[0])-1])

    #output hasil konversi ke biner
    print("\t\t Hasil Konversi Ke Bilangan Biner Adalah       : " ,end="")
    for i in range(len(desKeBin)-1, -1, -1):
      print(desKeBin[i],end="")

    print()
  
    print("="*110)
    #pengulangan program
    pilih = input("\t\t Ingin mengulang kembali? Iya (y) || Tidak (n) :")
    while (pilih !="y" and pilih != "n" and pilih != "0"):
      pilih = input("\t\t Pilihan anda salah, silahkan input lagi :")
    
if __name__ == "__main__":
      main()