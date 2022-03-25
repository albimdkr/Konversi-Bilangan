import os

def biner(desimal):
    des = desimal
    Lbagi = []
    Lsisa = []

    if (des < 2):
        Lbagi.append("")
        Lsisa.append(des)
    else:
      while (des >= 2):
        bagi = des // 2
        sisa = des % 2

        Lbagi.append(bagi)
        Lsisa.append(sisa)

        des = bagi

      return [Lbagi, Lsisa]


def octal(desimal, add):
  des = desimal 
  Lbagi = []
  Lsisa = []

  if (des < 8):
    Lbagi.append("")
    Lsisa.append(des)

  else:
      while (des >= 8):
          bagi = des // 8
          sisa = des % 8

          Lbagi.append(bagi)
          Lsisa.append(sisa)

          des = bagi
  for i in range(add):
      Lbagi.append("")
      Lsisa.append("")

  return[Lbagi, Lsisa]

def hexa(desimal, add):
  des = desimal
  Lbagi = []
  Lsisa = []

  if (des < 16):
      Lbagi.append("")

      if (des == 10):
        Lsisa.append("A")
      elif(des == 11):
        Lsisa.append("B")
      elif(des == 12):
        Lsisa.append("C")
      elif(des == 13):
        Lsisa.append("D")
      elif(des == 14):
        Lsisa.append("E")
      elif(des == 15):
        Lsisa.append("F")
      else:
        Lsisa.append(des)
      
  else:

      while (des >= 16):
          bagi = des // 16
          sisa = des % 16

          Lbagi.append(bagi)

          if(sisa == 10):
            Lsisa.append("A")
          elif(sisa == 11):
            Lsisa.append("B")
          elif(sisa == 12):
            Lsisa.append("C")
          elif(sisa == 13):
            Lsisa.append("D")
          elif(sisa == 14):
            Lsisa.append("E")
          elif(sisa == 15):
            Lsisa.append("F")
          else:
              Lsisa.append(sisa)

          des = bagi

  # elemen kosong dalam list
  for i in range(add):
    Lbagi.append("")
    Lsisa.append("")

  return [Lbagi, Lsisa]

def main ():
  pilih ="y"

  while (pilih == "y"):
    os.system("cls")
    print()
    x = int(input("\t\t Masukan Bilangan Desimal yang inngin dikonversi : "))
    print()
    des = x

    print("Binari\t\tOctal\t\tHexa")
    print ("="*110)
    print("{0:>20}\t{0:>20}\t{0:>20}".format(des))

    add_octal = len(biner(des)[0]) - len(octal(des,0)[0])
    add_hexa = len(biner(des)[0]) - len(hexa(des,0)[0])


    for i in range(len(biner(des)[0])):
        # garis bagi
        garisB = "2 ----------- {0}".format(biner(des)[1][i])
        garisO = "8 ----------- {0}".format(octal(des, add_octal)[1][i])
        garisH = "16 ----------- {0}".format(hexa(des, add_hexa)[1][i])
        #hasil bagi
        bagiB = biner(des)[0][i]
        bagiO = octal(des, add_octal)[0][1]
        bagiH = hexa(des, add_hexa)[0][i]

        if(len(octal(des,0)[0]) <= i):
          garisO = ""
          bagiO = ""

        if (len(hexa(des,0)[0]) <= i):
          garisH = ""
          bagiO = ""

        print("\t{0}\t{1}\t{2}".format(garisB, garisO, garisH))
        print("{0:>20}\t{1:>20}\t{2:>20}".format(bagiB, bagiO, bagiH))
        
    # append elemen Binner
    desKeBin = []
    for i in (biner(des)[1]):
      desKeBin.append(i)
    desKeBin.append(biner(des)[0] [ len( biner(des)[0])-1])

    #  append Octal
    octalKeBin = []
    for i in (octal(des,0)[1]):
      desKeBin.append(i)
    octalKeBin.append(octal(des,0)[0][ len(octal(des,0)[0])-1 ])

    # append Hexa
    hexKeBin = []
    for i in (hexa(des,0)[1]):
      hexKeBin.append(i)
    elemen_terakhir = hexa(des,0)[0][ len( hexa(des,0)[0] )-1 ]
    if (elemen_terakhir == 10):
      hexKeBin.append("A")
    elif (elemen_terakhir == 11):
      hexKeBin.append("B")
    elif (elemen_terakhir == 12):
      hexKeBin.append("C")
    elif (elemen_terakhir == 13):
      hexKeBin.append("D")
    elif (elemen_terakhir == 14):
      hexKeBin.append("E")
    elif (elemen_terakhir == 15):
      hexKeBin.append("F")
    else:
      hexKeBin.append(elemen_terakhir)

    # print biner, octal, hexa
    print()   
    print("="*110)
    print("\t Biner :" ,end="")
    for i in range(len(desKeBin)-1, -1, -1):
      print(desKeBin[i],end="")

    print("\t\tOctal : ",end="")
    for i in range(len(octalKeBin)-1, -1, -1):
      print(octalKeBin[i],end="")
  
    print("\t\tHexa : ",end="")
    for i in range(len(hexKeBin)-1, -1, -1):
      print(hexKeBin[i],end="")

    print()
  
    print("-"*110)
    pilih = input("\tIngin mengulang kembali? Iya (y) || Tidak (n) :")
    while (pilih !="y" and pilih != "n" and pilih != "0"):
      pilih = input("\tPilihan anda salah, silahkan input lagi :")

if __name__ == "__main__":
      main()