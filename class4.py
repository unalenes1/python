class point: #Sınıfımızı Oluşturuyoruz
    def __init__(self,x = 0 , y = 0): #Yapıcı Fonksiyonumuzu Oluşturduk
        self.x = x #Gelen x değeri ile fonksiyondaki x değerini eşleştirdik
        self.y = y #Gelen y değeri ile fonksiyondaki y değerini eşleştirdik
    
    def __del__(self): #Bellekten atmak için Kullanılan özel fonksiyonumuzu Çağırıyoruz
        class_name = self.__class__.__name__ 
        print(class_name,"Bellekten Atıldı")
#3 Farklı Point Nesnesi oluşturuyoruz 
pt1 = point()
pt2 = point()
pt3 = point()

#Bu 3 nesnenin id lerini alıp ekrana basıyoruz 
print(id(pt1),id(pt2),id(pt3))
del pt1 #Yazdığımız Fonksiyon sayesinde del kullanıp buidleri boşaltıyoruz
del pt2 #Yazdığımız Fonksiyon sayesinde del kullanıp buidleri boşaltıyoruz
del pt3 #Yazdığımız Fonksiyon sayesinde del kullanıp buidleri boşaltıyoruz
