def toplam (x,y):
    return x+y
def cikar (x,y):
    return x-y
def bol (x,y):
    return x/y
def carp (x,y):
    return x*y

secim = int(input("Bir Değer Gir : "))

sayi1 = int(input ("1. Sayi Gir:"))
sayi2 = int(input ("2. Sayi Gir : "))

if secim == 1 :
    print(toplam(sayi1,sayi2))
if secim == 2 :
    print(cikar(sayi1,sayi2))
if secim == 3 :
    print(bol(sayi1,sayi2))
if secim == 4 :
    print(carp(sayi1,sayi2))