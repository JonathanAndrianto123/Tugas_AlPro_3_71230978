a_ = (input("Masukkan bilangan pertama: "))
b_= (input("Masukkan bilangan kedua: "))
c_ = (input("Masukkan bilangan ketiga: "))

try :
    a = int(a_)
    b = int(b_)
    c = int(c_)
    if a > b and a > c:
        print("Terbesar = ", a)
    elif b > a and b > c:
        print("Terbesar = ", b)
    elif c > a and c > b:
        print("Terbesar = ", c)
except :
    print("Input Anda Salah")