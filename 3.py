userinput = input("Masukkan bulan (1-12) : ")
try :
    bulan = int(userinput)
    if bulan == 1 or bulan == 3 or bulan == 5 or bulan == 7 or bulan == 8 or bulan == 10 or bulan == 12 :
        print("Jumlah hari : 31")
    elif bulan == 4 or bulan == 6 or bulan == 9 or bulan == 11 :
        print("Jumlah hari : 30")
    elif bulan == 2 :
        print("Jumlah hari : 29")
except :
    print("Bulan yang diinputkan tidak valid!")