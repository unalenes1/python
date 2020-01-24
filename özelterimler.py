print("===========================")
print("Harf Harf Ayirmak Ve Aralarina Nokta Koymak : ")
print(*"Enes",sep=".")
print("===========================")
print("Kaç Harf Oldugunu Yazmak : ")
print(len("ENES"))
print("===========================")
print("Kac Tane Metoda Sahip oldugunu Yaziyor \n ======================")
print(dir(""))
print("===========================")
print("Replace() Metodu Ne Ise Yarar : ")
degisken = "enes"
print(degisken.replace("e","E"))
print("===========================")
print("Split() Metodu Ne Ise Yarar")
liste = "Enes Mehmet Veli"
print(liste.split(" ",1))

for i in liste.split():
    print(i)
print("\nHepsinin Ilk Harflerini Alir")
for i in liste.split():
    print (i[0],end= "")
print("\nRsplit() Ornegi ")
print(liste.rsplit(" ",1))

