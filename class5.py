#insan adında sınıfımızı oluşturuyoruz
#Soyut sınıflar (interface)üst sınıftaki işlevlerin sadece
#imza yapıları ile tanımlanıp herhangi bir body
#kısmında kodu olmayan işlevlerin olduğu sınıflara denir.
class insan:
    def __init__(self,ad): #yapıcı fonksiyonumuz
        self.ad=ad #ad eşleştirmemiz
        def isim(self):
            raise NotImplementedError ("Üst Soyut Sınıf")
class Ali(insan):
    def isim(self):
        return "Adım Ali"
    
class Ayse(insan):
    def isim(self):
        return "Adım Ayşe"
    
noname = [Ali("ENES"),Ali("Veli"),Ayse("Ayşe")]
for insan in noname:
    print(insan.isim())
    print("--------------------------------")
    print(insan.ad)
    print("--------------------------------")