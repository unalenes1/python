class hesap:
    def __init__(self):
        raise yazilmadi("Soyut Sınıf Kurucusu Yok") # raise komutu kullanarak bir hata durumu yayınlanmasını sağlayabiliriz.
    def alan(self):
        raise yazilmadi ("Soyut Sınıf Alan İşlevi Yok")
    def cevre(self):
        raise yazilmadi("Soyut Sınıf Çevre İşlevi Yok")
        
class daire(hesap):
    def __init__(self,aciRad):
        self.yaricap = aciRad
    def alan(self):
        return 3.1428*self.yaricap*self.yaricap
    def cevre(self):
        return 2*3.1428*self.yaricap

class dikdortgen(hesap):
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def alan(self):
        return self.a*self.b
    def cevre(self):
        return 2*(self.a+self.b)
    
def hesaplarbilgi(x):
    assert isinstance(x,hesap)
    print("Alanı",x.alan())
    print("Cevre",x.cevre())
    
    
    
    
hesaplar = dikdortgen(4,5)
hesaplarbilgi(hesaplar)

hesaplar1 = daire(4.12)
hesaplarbilgi(hesaplar1)