import requests
from bs4 import BeautifulSoup #Kütüphaneleri ekleme
i=1
while(True):#Kaç sayfa olduğunu bilmediğimiz için true yaptık. If ile status_code 200 değilse döngüden çıkaracağız
	url="http://www.beyazperde.com/filmler/tum-filmleri/kullanici-puani/?page="+str(i)
	sayfa=requests.get(url)
#requests ile url ye bağlanırız.  
	icerik=sayfa.content
#Yazdığımız urlden gelen html şeklindeki veriyi sayfaya kaydettik
	soup=BeautifulSoup(icerik,'html.parser')
#sayfa da bulunan veriyi bs4 teki parser ile parçaladık
	isimlerHepsi=soup.findAll('a',attrs={'class':'no_underline'})
	bilgiler=soup.findAll('ul',attrs={'class':'list_item_p2v tab_col_first'})
	puan=soup.findAll('span',attrs={'class':'note'})				
#isimleri,tarihleri ve puanları almak için findAll diyerek tag ve o taga ait class bilgilerinden istediğimiz alanlara ulaştık
	if(i==200):#Döngü sonsuzda olduğu için sayfadan gelecek cevaba göre döngüyü bitirme yaptık
		break
	else:	
		j=0
		while(j<len(isimlerHepsi)):#Film isimleri ile tarih sayıları eşit olduğu içindöngüde sadece bir tane verinin uzunluğunu kullanmak yetecektir
			print("================================"+str(i)+".SAYFA"+str(j+1)+".FİLM========================")
			print("Film Adı="+isimlerHepsi[j].text.strip())
#strip fonk. ile bpşlukları sildik baştaki ve sondaki
			a=bilgiler[j].div.text.split("(")
#Film süresi ve tarihi aynı yerde olduğu için split yaparak ilk gelen elemanı aldık
			print("Film Vizyon Tarihi="+a[0].strip())
			yonetmen=bilgiler[j].findAll('div',attrs={'class':'oflow_a'})
#bilgiler isimli değişkende bütün ul kısımları almıştık. ul ' lerin içinde bulunan divleri ayırdık
			print("Film Yönetmeni="+yonetmen[1].span.text)
#ayrılan divlerde 2.sırada yönetmen olduğu için yonetmen[1] yazdık
			print("Film Puanı="+puan[j].text.strip())
#puanları tek tek yazdırma kısmı
			j=j+1
	print("=========================")	
	print(str(i)+".SAYFANIN SONU")	
	print("=========================")		
	i=i+1