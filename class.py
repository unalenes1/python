#Class Oluşturuyoruz 
class isciler:
    iscisayisi = 0 #iscisayisi değişkenimiizi 0  eşitliyoruz
    def __init__(self,name,salary): #Yapıcı Fonksiyonumuzu Oluşturuyoruz
        self.name = name #Parametredi name ile fonksiyondaki name ile eşleştiriyoruz
        self.salary = salary  #Parametredi Salary ile fonksiyondaki Salary ile eşleştiriyoruz
        isciler.iscisayisi += 1 #İsci Sayimizi her çalıştığında +1 yapıyoruz 
        
    def isciListele(self): #İsciListele adında Fonksiyonumuzu oluşturuyoruz
            print ("Adı : ",self.name,"Maaş",self.salary ) #Nesnemizin içindeki adı ve Maaşı çağırıyoruz 
            
    def isciSayisiK(self): #İşçi Sayımızı ekrana bastırmak için bir fonksiyon oluşturuyoruz
            print("İşçi Sayısı : ",self.iscisayisi) # Nesnemizden isci sayimizi çağırıyoruz ve ekrana bastırıyoruz
            
isci1 = isciler("Ali",4000) #Classımızdan yeni bir nesne oluşturuyoruz ve bu nesnemizin yapıcı fonksiyonundaki parametleri gönderiyoruz. 
print(isci1.isciSayisiK()) #İscisayisiK fonksiyonumuzu Çağırıyoruz
print(isci1.isciListele()) #İsciListele Fonksiyonumuzu Çağırıyoruz

isci = isciler("Enes",5500)#Classımızdan yeni bir nesne oluşturuyoruz ve bu nesnemizin yapıcı fonksiyonundaki parametleri gönderiyoruz. 
print(isci.isciSayisiK()) #İscisayisiK fonksiyonumuzu Çağırıyoruz
print(isci.isciListele()) #İsciListele Fonksiyonumuzu Çağırıyoruz

print(getattr(isci,'salary')) #Maaş Değerimizi Alır
print(hasattr(isci,'yas')) #Yas diye bir değişkenimiz var mı onu kontrol eder 
print(setattr(isci,'yas',8)) #Yas diye bir değişken oluşturur ve ona 8 değerini atar
print(hasattr(isci,'yas'))  #Yas diye bir değişkenimiz var mı onu kontrol eder 
print(delattr(isci,'yas')) #Yas değişkenimizi silmemize yardımcı olur 
print(hasattr(isci,'yas')) #Yas diye bir değişkenimiz var mı onu kontrol eder 