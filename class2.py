#Geçersiz Kılma Miras ile üst  sınıfa tanımlı bir işlevin alt sınıfta kullanımı sonucunda geçersiz kılınabilir.

class parent:
    def myMethod(self):
        print("Üst Sınıf myMethod")
    def topla(self):
        return "enes" 
        
class child(parent):
    def myMethod(self):
        print("Alt Sınıf myMethod")
        
a=child()
a.myMethod()
a.topla()
