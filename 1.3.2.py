userinput = (input("Masukkan Satu Bilangan = "))
try :
    bil = int(userinput)
    if bil > 0 :
        print("Positif")
    elif bil < 0 :
        print("Negatif")
    elif bil == 0 :
        print("Nol")
except :
    print("Input Anda Salah!")