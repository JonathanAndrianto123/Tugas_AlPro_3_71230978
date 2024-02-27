userinput = input("Masukkan Suhu Anda = ")
try :
    suhu = int(userinput)
    if suhu > 38 :
        print("Anda Demam")
    else :
        print("Anda Tidak Demam")
except :
    print("Input Anda Salah!")