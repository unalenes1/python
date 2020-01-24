
def topla(x,y):
    return x+y

def cikar(x,y):
    return x-y

def bol(x,y):
    return x/y

def carp(x,y):
    return x*y


print("seciminizi yapin \n 1-Topla \n 2-Cikar \n 3-bol \n 4-Carp")
print("=========================================================")
secim = int(input(" 1-Topla \n 2-Cikar \n 3-bol \n 4-Carp \nSecim :"))

sayi1 = int(input ("1. Sayiyi Girin : "))
sayi2 = int(input ("2. Sayiyi Girin : "))
    
if secim == 1:
    print(sayi1,"+",sayi2,"=",topla(sayi1,sayi2))

if secim == 2:
    print(sayi1,"-",sayi2,"=",cikar(sayi1,sayi2))

if secim == 3:
    print(sayi1,"/",sayi2,"=",bol(sayi1,sayi2))

if secim == 4:
    print(sayi1,"*",sayi2,"=",carp(sayi1,sayi2))
