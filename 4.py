userinput1 = input("Masukkan sisi 1 = ")
userinput2 = input("Masukkan sisi 2 = ")
userinput3 = input("Masukkan sisi 3 = ")

try : 
    a = int(userinput1)
    b = int(userinput2)
    c = int(userinput3)
    if a == b == c : 
        print("3 sisi sama")
    elif a == b or a == c or b == c :
        print("2 sisi sama")
    else :
        print("Tidak ada sisi yang sama")
except :
    print("Input tidak valid!")