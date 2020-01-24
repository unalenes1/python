#Kalıtım

#Parent Adında Ana Sınıfımızı oluşturuyoruz
class Parent:
    parentCount = 10 #ParentCount değişkenine 10 başlangıç değerini veriyoruz
    def __init__(self): # Yapıcı Fonksiyonumuzu Oluşturuyoruz
        print("Üst sınıf Kurucu Yordamı") 
    def parentMethod(self): #ParentMethod adında bir parametresiz fonksiyon oluşturuyoruz
        print("Parent Method")
    def setAttrS(self,attr): #Parent Count değiştirecek bir setAttrs fonksiyonu oluşturuyoruz
        Parent.parentCount += attr #gelen attr değişkeni kadar parentcount arttırıyoruz
    def getAttrs(self): #ParentCount Değerini ekrana bastırmak için bir fonksiyon oluşturuyoruz
        print("Parent Attr : ", Parent.parentCount)

class Child(Parent): #kalıtım Almış bir Child Sınıfı oluşturuyoruz
    def __init__(self): # Yapıcı fonksiyonunu oluşturuyoruz
        print("Child Kurucu Yordamı")
    def childMethod(self): #Fonksiyon oluşturuyoruz
        print("childMethod")

c = Child() #Child Sınıfıdan c Nesnesini Oluşturuyoruz
c.childMethod() #ChildMethodunu çalıştırıyoruz
c.parentMethod() #Ana Clasımızdaki ParentMethodu Kalıtım Sayesinde Çalıştırıyoruz
c.setAttrS(500) #Ana clasımızdaki setAttrs Methodunu çalıştırıp istediği parametreyi gönderiyoruz
print(c.getAttrs()) #Ana clasımızdaki getAttrs methodu çalıştırıyoruz