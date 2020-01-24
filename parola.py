def dogru():
    print("Parola Dogru")
def yanlis():
    print("Parola Yanlis")
    
parola = 123456

giris = int(input("Parola Giriniz : "))

if giris == parola:
    dogru()
else:
    yanlis()