#Overloading / Aşırı Yükleme
#Vektor  Adında Sınıfımızı Oluşturuyoruz
class Vector:
    def __init__(self,a,b): # Yapıcı Fonksiyonumuzu Oluşturuyoruz 
        self.a = a #a değerlerimizi eşleştiriyoruz
        self.b = b #b değerlerimizi Eşleştiriyoruz
    def __str__(self): #__str__ Sınıfımıza a ya bu cevabı ver diyoruz
         return 'Vector (%d , %d)' %(self.a , self.b)
    def __add__(self,c): #Aşırı Yüklemeye C parametresini gönderiyoruz
         return Vector(self.a+c.a,self.b+c.b)

v1 = Vector(5,20)
v2 = Vector (5,2)
print(v1+v2)